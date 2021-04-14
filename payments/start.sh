#!/bin/sh
# start.sh

set -e

until PGPASSWORD=$DB_PASS psql -h "$DB_HOST" -U "postgres" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
