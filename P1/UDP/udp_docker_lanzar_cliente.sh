#!/bin/bash

docker run --rm -it --name hola_cliente --network pruebas -v "$(pwd)":/app python:3.7 python /app/udp_cliente6_broadcast.py