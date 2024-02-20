# PENTEST SERVERSIDE

## For Docker use
``
    docker-compose -p pentest-severside-image -f .\docker-compose.yml build
``
###
``
    docker-compose -p pentest-severside-image -f .\docker-compose.yml up
``
## For local use
``
    python3 main.py --env local --debug
    gunicorn --bind localhost:8000 --timeout 300 -w 4 -k uvicorn.workers.UvicornWorker app.server:app --reload
``