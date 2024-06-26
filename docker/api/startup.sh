#!/bin/bash


# Get the absolute path of the script
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[1]}" )" && pwd )"

# Construct the absolute path to the .env file
ENV_FILE_PATH="$SCRIPT_DIR/.env"

# Check if the .env file exists
if [ -f "$ENV_FILE_PATH" ]; then
    echo " Sourcing $ENV_FILE_PATH"
    # Source (execute) the .env file
    source "$ENV_FILE_PATH"
    # Alternatively, you can use the following line, which is equivalent:
    # . "$ENV_FILE_PATH"
else
    echo "Error: $ENV_FILE_PATH not found."
    exit 1
fi


dockerize -wait tcp://db:3306 -timeout 20s
alembic upgrade head && gunicorn --bind $APP_HOST:8000 --timeout 300 -w 4 -k uvicorn.workers.UvicornWorker app.server:app --reload