#!/usr/bin/env bash
# Stop: run the test suite before Claude ends its turn.
# Exit 2 makes Claude keep working with the pytest output.
set -uo pipefail

# Avoid loops: if we're already continuing because of this hook, let it stop.
[[ "$(jq -r '.stop_hook_active // false')" == "true" ]] && exit 0

cd "$CLAUDE_PROJECT_DIR" || exit 0
if ! out=$(uv run --quiet pytest -q -x --no-header -p no:warnings 2>&1); then
  echo "Tests are failing; fix them before finishing:" >&2
  echo "$out" | tail -40 >&2
  exit 2
fi
exit 0
