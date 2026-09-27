# Security

- Never read, print, or commit `.env`. Example values go in `.env.example`.
- Secrets in `Settings` are `SecretStr`; call `.get_secret_value()` only where the secret is sent.
- Never log tokens, `Authorization` headers, or keys.
- CORS with explicit origins; never `"*"` together with credentials.
- Validate all input with Pydantic (max lengths on any text that ends up in a prompt).
- SQL only through the Supabase client or parameterized queries; never string interpolation.
