# Supabase (Auth + Postgres)

## Auth

- The frontend signs in with Supabase and sends `Authorization: Bearer <access_token>`.
- The backend **verifies** the JWT on every protected request through a single dependency (e.g. `get_current_user`) in `app/services/auth.py`. Never decode a token without verifying its signature or trust unverified claims.
- Verify against the project's public JWKS (`{SUPABASE_URL}/auth/v1/.well-known/jwks.json`, cached) or via `auth.get_user(token)`. Check `exp` and `aud` (`authenticated`).
- Missing/invalid token → 401. User without access to a resource → 403/404.

## Database

- Only the **anon key** exists. There is no service_role key in this backend and none is added without an explicit decision.
- Queries run on behalf of the user: Supabase client with the anon key + the user's JWT, so **RLS** does the filtering. Data security relies on RLS; don't reimplement or bypass it in Python.
- Every new table has RLS enabled with policies. Schema changes are versioned SQL migrations (`supabase/migrations/`), never ad-hoc dashboard edits that aren't reflected in the repo.
- Tests never hit a real Supabase: mock the client or override the dependency.
