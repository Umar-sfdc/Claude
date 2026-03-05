# How to create own MCP Server

There are two types of Server

- Local Server (own)
- Remote Server (on internet)

## Basic Setup

- Install uv
- Create a folder with your require project name.
- Open this folder into vscode.
- Open terminal
- Execute the command `uv init`.
- Then execute this command `uv add fastmcp`
- Check if it's install or not `fastmcp version`
- Creat a basic server
- Test the server - `uv run fastmcp dev main.py`
- Run the server -  `uv run fastmcp run main.py`
- Add the server to Claude Desktop - `uv run fastmcp install claude-desktop main.py`
