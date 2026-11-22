# MCP Memory

## How it works

The app runs an MCP server with the SSE transport on port `8000`:

```text
http://<home-assistant-host>:8000/sse
```

Add it in Home Assistant with the **Model Context Protocol** integration and
expose it to your Assist pipeline.

Memories are stored in SQLite under `/data/memory_db`, so they survive
restarts and updates and are included in backups.

## Tools

- `remember_fact`: store a fact for a pipeline, or for all pipelines
- `search_memory`: full-text search
- `list_all_memories`, `update_memory`, `delete_memory`

Every tool takes the ID of the Assist pipeline, so each pipeline keeps its own
memories. Facts saved as global are visible to all pipelines.

## Options

This app has no options.
