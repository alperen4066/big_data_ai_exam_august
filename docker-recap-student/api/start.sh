#!/bin/sh

# Start the FastAPI server with Uvicorn
exec uvicorn --host 0.0.0.0 --port "${API_PORT:-8000}" --log-level info app.main:app
