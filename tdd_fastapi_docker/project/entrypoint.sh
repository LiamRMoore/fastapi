#!/bin/sh
# wait for postgresql process

echo "Waiting for postgres..."

while ! nc -z web-db 5432; do
    sleep 0.1
done

echo "PostgreSQL started"

# anything given as commands to this script (such as appended to the entrypoint cmd via docker's CMD 
# directive) are executed after the postgres server has been launched
exec "$@"