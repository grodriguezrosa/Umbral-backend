# LLMs via AI Gateway

- Every LLM call goes through the AI Gateway using `AI_GATEWAY_API_KEY`. Don't call providers (OpenAI, Anthropic, etc.) directly or add their keys.
- AI features are built last; the key is currently optional (`SecretStr | None`). Don't start AI work unless asked. When it starts, make the key required in `Settings` again.
- Wrap access in a single service (`app/services/llm.py`); routers never build gateway requests.
- Model IDs live in config or centralized constants, not scattered through the code. Don't invent model IDs; check the gateway's current docs.
- Always set an explicit timeout. Use streaming (`StreamingResponse` / SSE) for long responses.
- User input goes in the user message, never concatenated into the system prompt.
- Don't log full prompts or responses containing user data; log model, latency, and token counts.
- Tests never call the real gateway: mock the service.
- **Jev** will be integrated here later; until it's documented in CLAUDE.md, don't assume its API.
