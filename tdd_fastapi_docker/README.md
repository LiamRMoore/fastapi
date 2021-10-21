# Overview of structure

This course builds a text summarisation application using FastAPI.

The project source code lies within [/project](/project) and building/running it is 
orchestrated by Docker through the [docker-compose.yml](docker-compose.yml) file.

Currently the app consists of two services; the web server and the database server, 
which are specified by their own distinct docker images.

The [database image](./project/db/Dockerfile) is a simple postgres server which runs a database 
initialisation script on container startup, creating two databases on the server (development and 
testing).

The [web server image](./project/Dockerfile) defines a python environment within which a FastAPI app 
is served by Uvicorn. This anticipates a postgres server running on the docker network. This is guaranteed 
by using an [entrypoint script](./project/entrypoint.sh) which waits for the postgres server process to appear on the network.

The configuration of the database server URL and other parameters of the app are configured via environment variables specified in [docker-compose.yml](./docker-compose.yml).

## app details

- pydantic settings/implicit env checking and dependency injection
- tortoise ORM


