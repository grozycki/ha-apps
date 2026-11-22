#!/usr/bin/env bash
# Print a JSON array of the apps changed between two commits.
#
# Usage: scripts/changed-apps.sh BASE HEAD
#
# An app is a top-level directory with a config.yaml. Any change inside it
# counts. A change to the shared build workflow or scripts selects all apps.
# An empty or all-zero BASE (a new branch) also selects all apps.
set -euo pipefail

base="${1:-}"
head="${2:-HEAD}"

mapfile -t apps < <(find . -mindepth 2 -maxdepth 2 -name config.yaml \
  -not -path './.*' -not -path './_*' | cut -d/ -f2 | sort)

if [[ -z "${base}" || "${base}" =~ ^0+$ ]]; then
  changed=("${apps[@]}")
else
  mapfile -t files < <(git diff --name-only "${base}" "${head}")
  changed=()
  if printf '%s\n' "${files[@]}" | grep -qE '^(\.github/workflows/build(-app)?\.yaml|scripts/)'; then
    changed=("${apps[@]}")
  else
    for app in "${apps[@]}"; do
      if printf '%s\n' "${files[@]}" | grep -q "^${app}/"; then
        changed+=("${app}")
      fi
    done
  fi
fi

if [[ ${#changed[@]} -eq 0 ]]; then
  echo '[]'
else
  jq -nc '$ARGS.positional' --args "${changed[@]}"
fi
