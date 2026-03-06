# 🚀 MCP Server

A standardized Model Context Protocol (MCP) server that enables AI agents (like Claude) to securely interact with your local tools and data.

---

## Overview

This server implements the Model Context Protocol to expose local Python functions as executable tools for LLMs. It supports two primary deployment patterns:

* **Local:** Communication via Standard Input/Output (`stdio`).
* **Remote:** Communication via Server-Sent Events (`SSE`) or HTTP.

---

## Quickstart (Modern Workflow)

Recommended for Windows, macOS, and Linux users using the **`uv`** package manager.

### 1. Prerequisites

* **Install `uv`**:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```


* **Node.js**: Required for the [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector).

### 2. Initialization

```bash
# Create project
mkdir my-mcp-server && cd my-mcp-server

# Initialize environment
uv init
uv add fastmcp
```

### 3. Development & Testing

1. **Code your server**: Add your tools to `main.py` using the `@mcp.tool()` decorator.
2. **Launch Developer Mode**:
```bash
uv run fastmcp dev main.py
```


*This command starts the server with hot-reload and automatically opens the browser-based Inspector.*

### 4. Deployment to Claude Desktop

To link this server to your Claude Desktop app automatically:

```bash
uv run fastmcp install main.py
```

---

## 🐧 Manual Workflow (Debian/Ubuntu Linux)

Use this method if you prefer manual virtual environment management or face restricted environment policies (PEP 668).

### 1. System Setup

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-venv python3-pip -y
```

### 2. Environment Configuration

```bash
# Create and enter repo
mkdir mcp-dev && cd mcp-dev

# Initialize virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install fastmcp
```

### 3. Server Implementation

Create `server.py`:

```python
from fastmcp import FastMCP

mcp = FastMCP("Local Dev Server")

@mcp.tool()
def calculate_sum(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

if __name__ == "__main__":
    mcp.run()

```

### 4. Testing via MCP Inspector

Since Claude Desktop is not available on Linux, use the official Inspector to test your tools:

```bash
npx @modelcontextprotocol/inspector python3 server.py
```

> **Note:** Access the UI at `http://localhost:6274` to manually trigger and debug your tools.

---

## Command Reference

| Action | `uv` (Recommended) | `pip` (Manual) |
| --- | --- | --- |
| **Install Package** | `uv add fastmcp` | `pip install fastmcp` |
| **Test / Debug** | `uv run fastmcp dev main.py` | `npx @modelcontextprotocol/inspector python3 server.py` |
| **Run (Stdio)** | `uv run fastmcp run main.py` | `python3 server.py` |
| **Check Version** | `uv run fastmcp version` | `fastmcp version` |

---

## 🔒 Security

* **Local Execution:** Tools run with the permissions of the local user.
* **Sandboxing:** It is recommended to run MCP servers in isolated environments when handling sensitive data.

---