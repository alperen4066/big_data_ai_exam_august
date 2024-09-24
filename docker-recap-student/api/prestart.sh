#!/bin/sh

# Check if new upgrade operations are detected
if alembic check | grep -q "FAILED: New upgrade operations detected"; then
  # New upgrade operations detected, generate and apply a new migration
  CURRENT_DATE=$(date "+%Y-%m-%d")
  if alembic revision --autogenerate -m "Atomically detected changes on $CURRENT_DATE" && alembic upgrade head; then
    echo "Generated and applied migration for detected changes on $CURRENT_DATE."
  else
    echo "Error generating or applying migration for detected changes on $CURRENT_DATE."
    exit 1
  fi
else
  echo "Existing migrations are up-to-date."
fi

# Continue running other services or commands
exec "$@"
