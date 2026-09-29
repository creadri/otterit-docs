#!/usr/bin/env bash
set -euo pipefail

# The ~/.claude volume is created root-owned; hand it to the container user so
# Claude Code can persist its config and credentials across rebuilds.
sudo chown -R "$(id -u):$(id -g)" "$HOME/.claude" || true

npm install -g @anthropic-ai/claude-code

python3 -m pip install --upgrade pip

echo "node    $(node --version)"
echo "npm     $(npm --version)"
echo "python  $(python3 --version)"
echo "claude  $(claude --version)"
