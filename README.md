# OpexPanda Deployment Project

## About
Simple Flask web app containerized using Docker for OpexPanda.

## Problem Statement
Manual deployments were error-prone and time-consuming.
This project standardizes the deployment process using Docker containers.

## My Role (DevOps Intern)
- Understood project requirements with senior team
- Set up Docker environment on local machine
- Created Dockerfile for containerization
- Tested local deployment and documented the process

## How to Run
docker build -t opexpanda-app .
docker run -p 5000:5000 opexpanda-app

## Tech Stack
- Python Flask
- Docker
- Git & GitHub
- Ubuntu (Linux)

## Status
🟡 Work In Progress — Week 4 of 8

## Next Steps
- Add CI/CD pipeline
- Implement automated testing