#!/bin/bash

# Get the directory where this script lives
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd)"

# Activate virtual environment
source "$SCRIPT_DIR/env/bin/activate"

# Set Flask environment variables
export FLASK_APP="$SCRIPT_DIR/app.py"
export FLASK_ENV=development

# Start Flask in the background
flask run &

# Give Flask a moment to start
sleep 2

# Open the app in the default browser
open http://127.0.0.1:5000

# Wait for Flask to exit so Ctrl+C still stops it
wait

