#!/bin/bash
# Start the local server for the mitzvot HTML files

set -euo pipefail

# Ensure we run from the script directory
cd "$(dirname "$0")/../.."

echo "Starting local server on http://localhost:8000"
python3 Archive/server/serve.py
