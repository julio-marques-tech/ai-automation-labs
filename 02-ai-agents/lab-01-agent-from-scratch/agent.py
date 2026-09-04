"""Lab 01 - a minimal agent with one custom tool, built directly with the
Claude Agent SDK (no n8n, no framework hiding the loop).

Watching the printed message stream shows the agent's reasoning loop:
it decides on its own whether the question needs the calculator tool.
"""

import ast
import asyncio
import operator

from claude_agent_sdk import (
    ClaudeAgentOptions,
    ClaudeSDKClient,
    create_sdk_mcp_server,
    tool,
)

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def safe_eval(expr: str) -> float:
    """Evaluates simple arithmetic (+ - * / and unary -) without using
    eval(), so the tool can't execute arbitrary code."""

    def _eval(node):
        if isinstance(node, ast.BinOp):
            return _OPS[type(node.op)](_eval(node.left), _eval(node.right))
        if isinstance(node, ast.UnaryOp):
            return _OPS[type(node.op)](_eval(node.operand))
        if isinstance(node, ast.Constant):
            return node.value
        raise ValueError(f"Unsupported expression: {expr}")

    return _eval(ast.parse(expr, mode="eval").body)


@tool("calculate", "Evaluate a simple arithmetic expression", {"expression": str})
async def calculate(args: dict) -> dict:
    result = safe_eval(args["expression"])
    return {"content": [{"type": "text", "text": str(result)}]}


calculator_server = create_sdk_mcp_server(
    name="calculator",
    version="1.0.0",
    tools=[calculate],
)

options = ClaudeAgentOptions(
    mcp_servers={"calculator": calculator_server},
    allowed_tools=["mcp__calculator__calculate"],
)


async def main():
    async with ClaudeSDKClient(options=options) as client:
        # No instructions about the tool at all - purely a hard enough
        # calculation to see whether the model chooses the tool on its own.
        await client.query(
            "Quanto e (48372 * 9184 - 773102) / 641, arredondado a 3 casas decimais?"
        )
        async for message in client.receive_response():
            print(message)


if __name__ == "__main__":
    asyncio.run(main())
