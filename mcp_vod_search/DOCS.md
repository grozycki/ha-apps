# MCP VOD Search

## How it works

The app runs an MCP server with the SSE transport on port `8101`:

```text
http://<home-assistant-host>:8101/sse
```

Add it in Home Assistant with the **Model Context Protocol** integration and
expose it to your Assist pipeline. Data comes from JustWatch.

## Tools

- `get_streaming_providers`: where a title can be watched
- `get_show_episodes`: seasons and episodes of a series
- `get_popular_releases`: popular titles, optionally for given providers

## Options

| Option | Default | Description |
| --- | --- | --- |
| `country` | `UK` | Country code used for availability, for example `PL` |
| `language` | `en` | Language of titles and descriptions, for example `pl` |
