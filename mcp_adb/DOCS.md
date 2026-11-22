# MCP Android Debug Bridge

## How it works

The app runs an MCP server with the SSE transport on port `8555`:

```text
http://<home-assistant-host>:8555/sse
```

Add it in Home Assistant with the **Model Context Protocol** integration and
expose it to your Assist pipeline.

The app uses the host network and finds Android devices on your network with
mDNS. The ADB key is kept in `/data/.android`, so it survives restarts and
updates and is included in backups.

## Tools

- Devices: `list_discovered_devices`, `pair_device`
- Apps: `list_installed_apps`, `get_current_app`, `launch_app` (with an
  optional deep link), `stop_app`, `trigger_global_search`
- Remote control: D-pad, select, back, home, power, volume, play, stop, next,
  previous
- Screen: `get_screen_texts`
- Resources: navigation guides for selected apps

## Pairing

Turn on wireless debugging on the device, then ask Assist to pair it with the
pairing code shown on the device.

## Options

| Option | Default | Description |
| --- | --- | --- |
| `device_ip` | `127.0.0.1` | Device address. The server currently finds devices with mDNS and does not read this option. |
| `port` | `5555` | ADB port. The server currently does not read this option. |

## Why it needs host networking

mDNS discovery and ADB connections to devices on your local network need the
host network.
