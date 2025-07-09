from fastapi import FastAPI
from typing import Callable, List
from pydantic import BaseModel

class ToolInput(BaseModel):
    name: str
    args: dict

class FastMCP:
    def __init__(self, tools: List[Callable]):
        self.tools = {tool.name: tool for tool in tools}  # tool.name is correct for LangChain tools
        self.app = FastAPI()
        self._add_routes()

    def _add_routes(self):
        @self.app.get("/")
        def read_root():
            return {"status": "MCP is running"}

        @self.app.post("/query")
        def run_tool(input: ToolInput):
            print("📨 Received tool input:", input)
            tool = self.tools.get(input.name)
            if not tool:
                print(f"❌ Tool '{input.name}' not found. Available tools: {list(self.tools.keys())}")
                return {"error": f"Tool '{input.name}' not found"}

            try:
                result = tool.invoke(input.args)
                print("✅ Tool result:", result)
                return {"result": result}
            except Exception as e:
                print("❌ Tool execution error:", str(e))
                return {"error": str(e)}
