# INSTRUCTIONS.md

This file explains how a cloning user can run, test, and use the repository.

---

## Prerequisites

- Python 3.10+
- Docker
- Docker Compose
- AWS credentials (in `.env`)

---

## Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/<your-user>/devops-challenge.git
cd devops-challenge
```

### 2. Set Up Environment Variables

Create a `.env` file in the root of the project with your AWS credentials:

```env
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
```

### 3. Run the Application

Use Docker Compose to build and start the app:

```bash
docker-compose up --build
```

You can then access:
`http://127.0.0.1:5000/health` → returns status and links
`http://127.0.0.1:5000/secret` → returns the secret code from DynamoDB

### 4. Run Unit Tests

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run tests using pytest:

```bash
pytest test/
```

The tests will:

* Verify `/health` response
* Mock AWS and test `/secret` without making real AWS calls

### 5. Continuous Integration (Travis CI)

**When you push to the `master` branch:**

* Travis installs Python dependencies
* Runs all tests
* Builds and pushes the Docker image to Docker Hub

**Required environment variables in Travis:**

* `DOCKER_USERNAME`
* `DOCKER_PASSWORD`

These should be defined in your Travis CI settings.
