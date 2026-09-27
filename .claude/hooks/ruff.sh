#!/usr/bin/env bash
# PostToolUse: format and lint the .py file that was just edited.
# Exit 2 feeds the errors back to Claude so it fixes them.
set -uo pipefail

file=$(jq -r '.tool_input.file_path // empty')
[[ "$file" == *.py && -f "$file" ]] || exit 0

cd "$CLAUDE_PROJECT_DIR" || exit 0
uv run --quiet ruff format --quiet "$file"
if ! out=$(uv run --quiet ruff check --fix --quiet "$file" 2>&1); then
  echo "ruff check failed on $file:" >&2
  echo "$out" >&2
  exit 2
fi
exit 0
