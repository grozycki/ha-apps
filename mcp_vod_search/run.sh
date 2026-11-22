#!/usr/bin/with-contenv bashio

COUNTRY="$(bashio::config 'country')"
LANGUAGE="$(bashio::config 'language')"
export COUNTRY LANGUAGE

# Start the MCP server
exec python3 /main.py
