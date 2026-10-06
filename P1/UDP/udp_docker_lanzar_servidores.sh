#!/bin/bash

docker run -d --name hola1 --network pruebas -v "$(pwd)":/app python:3.7 python -u /app/udp_servidor6_broadcast.py

docker run -d --name hola2 --network pruebas -v "$(pwd)":/app python:3.7 python -u /app/udp_servidor6_broadcast.py

docker run -d --name hola3 --network pruebas -v "$(pwd)":/app python:3.7 python -u /app/udp_servidor6_broadcast.py