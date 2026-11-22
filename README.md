# Home Assistant apps

Source code of my Home Assistant apps. To install them, add the
distribution repository:

[![Open your Home Assistant instance and show the add app repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fgrozycki%2Fhome-assistant-apps)

| App | Description |
| --- | --- |
| [mcp_adb](mcp_adb) | Control Android and Google TV devices over ADB |
| [mcp_memory](mcp_memory) | Local memory for Assist, SQLite FTS5 |
| [mcp_vod_search](mcp_vod_search) | Where to stream a film or series |
| [mcp_web_search](mcp_web_search) | Web search and page reading |

## Development

Each app is a top-level folder. Add user-facing changes to the
`Unreleased` section of its `CHANGELOG.md`. Apps are released one at a
time with **Actions** > **Release app**.
