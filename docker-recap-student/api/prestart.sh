#!/bin/sh

# Wait for the database to be ready
echo "Checking database connection..."
until mysql -h"${MYSQL_HOST}" -u"${MYSQL_USER}" -p"${MYSQL_PASSWORD}" -e "USE ${MYSQL_DATABASE};" >/dev/null 2>&1; do
  echo "Waiting for the database connection..."
  sleep 2
done

# Apply migrations to ensure the database is up-to-date
if alembic upgrade head; then
  echo "Database migrations applied successfully."
else
  echo "Error applying database migrations."
  exit 1
fi

# Continue running other services or commands
exec "$@"
