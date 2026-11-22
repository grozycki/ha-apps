# Home Assistant apps: source

Source code of the Home Assistant apps published in
[grozycki/home-assistant-apps](https://github.com/grozycki/home-assistant-apps).

**To install an app, add the distribution repository, not this one:**

[![Open your Home Assistant instance and show the add app repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fgrozycki%2Fhome-assistant-apps)

| App | Description |
| --- | --- |
| [mcp_adb](mcp_adb) | Control Android and Google TV devices over ADB |
| [mcp_memory](mcp_memory) | Local memory for Assist, SQLite FTS5 |
| [mcp_vod_search](mcp_vod_search) | Where to stream a film or series |
| [mcp_web_search](mcp_web_search) | Web search and page reading |

## Repositories

| Repository | Visibility | Content |
| --- | --- | --- |
| `grozycki/ha-apps` | public | this repository: code, CI, release tags |
| `grozycki/home-assistant-apps` | public | distribution: what the Supervisor reads |
| `grozycki/ha-apps-specs` | private | OpenSpec specifications, one folder per app |

Every app is a top-level folder with a `config.yaml`. Images are built in CI
and published to `ghcr.io/grozycki/<app>`; nothing is built on users' devices.

## Working on an app

Commit as often as you like. Commits do not reach users: the distribution
repository changes only when an app is released.

Add every user-facing change to the `## [Unreleased]` section of the app's
`CHANGELOG.md`. Pull requests and pushes to `main` run the linters and test
builds of the apps they change, without pushing images.

To try an app on a real device, copy its folder to `/addons` (shown as
`local_apps`) and comment out `image:` in `config.yaml`, so the Supervisor
builds it instead of pulling.

## Releasing one app

Run **Actions** > **Release app** on `main` with the app folder and the new
version. The workflow:

1. checks that the version is higher and `Unreleased` is not empty;
2. sets `version`, moves `Unreleased` under the new version, commits and tags
   `<app>-v<version>`;
3. builds and pushes the images for every architecture, refusing to overwrite
   an existing version;
4. creates the GitHub release from the changelog;
5. only then copies the app's `config.yaml`, docs, changelog, icons,
   translations and AppArmor profile into the distribution repository.

Pushing a tag `<app>-v<version>` by hand runs steps 3 to 5; the version in
`config.yaml` and a changelog section must already match it.

### One-time setup

- A GitHub App with **Contents: read and write** on
  `grozycki/home-assistant-apps` only, installed on that repository.
- In this repository: variable `DIST_APP_CLIENT_ID` and secret
  `DIST_APP_PRIVATE_KEY`. Optional variables `DIST_REPOSITORY` and
  `DIST_BRANCH` (set `DIST_BRANCH=next` to try a release without reaching
  users).
- After the first release of an app, make its three packages public on
  ghcr.io: `<app>`, `amd64-<app>` and `aarch64-<app>`.
