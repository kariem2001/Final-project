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
### Make sure you have these on and running
``
apt update -y && apt upgrade -y  \
    && apt install -y iputils-ping \
    && apt install -y telnet \
    && apt install -y nmap
``
### Run with
``
    python3 main.py --env local --debug 
``
\
\
Or you can use
\
``
    gunicorn --bind localhost:8000 --timeout 300 -w 4 -k uvicorn.workers.UvicornWorker app.server:app --reload
``