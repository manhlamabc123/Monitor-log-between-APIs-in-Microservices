#!/bin/bash

cd main
docker compose up -d &
cd ..
cd admin
docker compose up -d &
cd ..
cd consumer
docker compose up -d &
cd ..
cd react-crud
npm start