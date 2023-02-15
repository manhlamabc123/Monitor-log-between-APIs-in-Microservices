#!/bin/bash

cd admin
docker compose down
cd ..
cd main
docker compose down
cd ..
cd consumer
docker compose down