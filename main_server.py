from fastmcp.server import FastMCP
from tools.postgres_tools import (
    create_user,
    read_users,
    update_user_email,
    delete_user
)

tools = [create_user, read_users, update_user_email, delete_user]
mcp = FastMCP(tools=tools)
app = mcp.app
