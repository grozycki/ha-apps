# MCP Web Search

## How it works

The app runs an MCP server with the SSE transport on port `8405`:

```text
http://<home-assistant-host>:8405/sse
```

Add it in Home Assistant with the **Model Context Protocol** integration and
expose it to your Assist pipeline.

## Tools

- `search_web`: search DuckDuckGo and return the top results
- `read_page`: download a page and return its main text

## Options

This app has no options.
