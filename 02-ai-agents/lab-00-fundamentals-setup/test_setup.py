"""Smoke test: confirms the Claude Agent SDK works via the authenticated
`claude` CLI, with no separate ANTHROPIC_API_KEY needed."""

import asyncio

from claude_agent_sdk import query


async def main():
    async for message in query(prompt="Diz ola numa frase curta"):
        print(message)


if __name__ == "__main__":
    asyncio.run(main())
