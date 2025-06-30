## Project Overview

This project is a proof of concept Flask API that extracts a secret code from DynamoDB and serves it over HTTP.

## Development Steps

1. **Repo setup**

   - Forked the repository
   - Initialized project structure under `/app`
2. **Backend API**

   - Used Flask with two routes:
     - `/secret`: Fetches `secret_code` from AWS DynamoDB
     - `/health`: Healthcheck endpoint with DockerHub and GitHub links
   - Wrapped routes using `Blueprint` for better modularity
3. **Dockerization**

   - Created `Dockerfile` with Python 3.10 base
   - Configured `docker-compose.yml`
4. **Testing**

   - Created unit tests using `pytest` for `/health`, and mocked `/secret` to avoid real AWS calls during testing
5. **Travis CI**

   - Configured .travis.yml to install dependencies, run tests, build the Docker image, and push it to Docker Hub on each push to master

## Tools Used

- Python 3.10
- Flask
- Boto3
- pytest
- Docker
- Travis CI
