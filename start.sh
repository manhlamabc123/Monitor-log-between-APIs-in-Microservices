#!/bin/bash

cd admin
docker compose up -d
cd ..
cd main
docker compose up -d
cd ..
cd consumer
docker compose up -d
cd ..
cd react-crud
npm start &