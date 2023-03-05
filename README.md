# Monitor log between APIs in Microservices

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#architecture">Architecture</a></li>
    <li><a href="#technologies">Technologies</a></li>
    <li><a href="#how-to-run">How to run</a></li>
    <li><a href="#correlation-id">Correlation ID</a></li>
  </ol>
</details>

## About

* "ITSS Linux System and Network Management" Project.
* This is a website builded using Microservice Architecture.
  * A simple website where users can access then like posts which was created by Admin.
  * Admin can CRUD posts.
  * There is no sign in, sign up
* This project solved one of the many problem with Microservice: **How to know which APIs are connect to each other, call each other**.
* By using **Correlation ID** to solve the above problem.
* Statuse: **Finished**. There will be no further update.

## Architecture

Microservice, using 2 diffirent framework `Django` and `Flask`.
* Front-end: `ReactJS`
* Back-end: Python
  * Admin service: `Django`
  * Main service: `Flask`
* Database: MySQL

## Technologies

* NodeJS: v14.21.3
* ReactJS: 18.2.0
* Docker:
```
Client: Docker Engine - Community
 Cloud integration: v1.0.29
 Version:           23.0.1
 API version:       1.42
 Go version:        go1.19.5
 Git commit:        a5ee5b1
 Built:             Thu Feb  9 19:47:01 2023
 OS/Arch:           linux/amd64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          23.0.1
  API version:      1.42 (minimum version 1.12)
  Go version:       go1.19.5
  Git commit:       bc3805a
  Built:            Thu Feb  9 19:47:01 2023
  OS/Arch:          linux/amd64
  Experimental:     false
 containerd:
  Version:          1.6.18
  GitCommit:        2456e983eb9e37e47538f59ea18f2043c9a73640
 runc:
  Version:          1.1.4
  GitCommit:        v1.1.4-0-g5fd4c4d
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0
```
* Everything else is in `requirement.txt` file in each service folder

## How to run

### Admin Service
```
cd admin
docker compose up
```

### Main Service
```
cd main
docker compose up
```

### Log Service
```
cd consumer
docker compose up
```

### ReactJS
```
cd react_crud
npm start
```

## Correlation ID
By adding an ID to every APIs, we shall know which APIs are related to each other.
By adding these few lines of code in both Django and Flask middleware, we can have ID for every APIs called.
```
string correlation_id

def before_request():
  correlation_id = get_correlation_id_from_header()
  if correlation_id == None:
    create_correlation_id()
  append_correlation_id_to_request()
  publish_request_to_message_queue()
  
  return response
```
