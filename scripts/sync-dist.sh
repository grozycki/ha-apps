#!/usr/bin/env bash
# Copy the files the Supervisor reads for one app into the distribution repo.
#
# Usage: scripts/sync-dist.sh APP DIST_DIR
#
# Only the listed files are copied. Everything else in DIST_DIR/APP is
# removed, so the distribution never holds source code or a Dockerfile.
set -euo pipefail

app="${1:?app slug required}"
dist="${2:?distribution directory required}"

files=(
  config.yaml
  README.md
  DOCS.md
  CHANGELOG.md
  icon.png
  logo.png
  apparmor.txt
  translations
)

if [[ ! -f "${app}/config.yaml" ]]; then
  echo "::error::${app}/config.yaml not found" >&2
  exit 1
fi

if ! grep -qE '^image:' "${app}/config.yaml"; then
  echo "::error::${app}/config.yaml has no image; the distribution needs prebuilt images" >&2
  exit 1
fi

staging="$(mktemp -d)"
trap 'rm -rf "${staging}"' EXIT

for file in "${files[@]}"; do
  if [[ -e "${app}/${file}" ]]; then
    cp -R "${app}/${file}" "${staging}/"
  fi
done

mkdir -p "${dist}/${app}"
rsync -a --delete "${staging}/" "${dist}/${app}/"
echo "Synced ${app}:"
find "${dist}/${app}" -mindepth 1 -maxdepth 1 -printf "  %f\n" | sort
