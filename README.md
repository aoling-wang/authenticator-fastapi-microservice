# FastAPI Authenticator Microservice

### A lightweight, containerized authentication service designed to be integrated into small to mid-sized applications.

> **Portfolio Project · Python · Pydantic · FastAPI · UV · bcrypt · SQLAlchemy · Authentication · Microservices · Docker**

---

## Overview

**FastAPI Authenticator Microservice** is a lightweight authentication service built with **Python and FastAPI**, designed to provide a reusable authentication layer for small to mid-sized applications. With how fast the modern user landscape and cybersecurity practices evolved, a key concern is how microservices can be updated and connected to applications without interrupting user experience or application uptime. 

<p align="center">
  <img width="295" height="300" alt="image" src="https://github.com/user-attachments/assets/590fc6be-49cf-43d3-9c7d-53d354d2f4c5" />
  <img width="295" height="300" alt="image" src="https://github.com/user-attachments/assets/9d451413-99a1-4c59-a24a-0e092df9fd87" />
  <img width="315" height="300" alt="image" src="https://github.com/user-attachments/assets/19d13829-1751-4384-b3f9-c2b112e4dfdb" />
</p>

Inspired by components in React JS, this project combats on a common challenge in modern application development: **how can authentication logic be developed independently from the applications that depend on it?**

Rather than tightly coupling authentication directly to an application's codebase, this project separates authentication into its own service. This allows the service to be developed, tested, containerized, and updated independently while keeping the integration point relatively simple.

### Key Design Idea

> **Create a developer-friendly authenticator microservice that can be attached to any application at multiple points to replace multiple authenticator services that may sit through a application.**

The service currently uses **SQLite** for local development, but the database layer is structured so that it can be adapted to other relational databases such as PostgreSQL or MySQL.

---

## Architecture Flow

My main intention for this project was to explore options for separating the authenticator feature from main applications services in python. Similar to the way a AuthGuard works in NestJS, this feature was design to be a standalone authenticator that would verify identity and provide a predictable output (e.g. True or False) and could be call upon at any point of the user experience to start or extend tokens and sessions.

```text
Client Application → FastAPI Authenticator → Validation → Password Verification → Database
```

Future iterations could receive passkeys as input and return valid cookies/sessions and JWTs as output.

### Database Configuration

The project currently uses **SQLite** to keep local development lightweight and simple.

The database layer can be adapted for a different relational database depending on the application environment.

Potential production configurations include:

* PostgreSQL
* MySQL
* Managed cloud databases

When changing the database implementation, update both the **database configuration** and the relevant **unit tests** so that the test environment reflects the new connection and behavior.

---

## What I Learned

* **FastAPI** — building a lightweight Python REST API
* **Authentication fundamentals** — separating credential handling from application logic
* **Password security** — hashing passwords with bcrypt rather than storing plaintext credentials
* **Pydantic** — validating incoming request data
* **SQLAlchemy** — using an ORM to interact with the database
* **Database design** — comparing SQLite, PostgreSQL, and MySQL for different use cases
* **Microservice architecture** — designing authentication as an independently deployable service

---

## The Stack

| Technology     | Purpose                              |
| -------------- | ------------------------------------ |
| **Python**     | Application language                 |
| **uv**         | Dependency and project management    |
| **FastAPI**    | REST API framework                   |
| **Uvicorn**    | ASGI server runtime                  |
| **Pydantic**   | Request validation and data modeling |
| **bcrypt**     | Password hashing                     |
| **SQLAlchemy** | Database ORM                         |
| **SQLite**     | Lightweight development database     |
| **Docker**     | Application containerization         |

---

## Project Setup

### 1. Check Your Python Version

```bash
python --version
```

Python 3.x is required.

### 2. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 3. Install Dependencies

Using `uv`:

```bash
uv sync
```

### 4. Run the Application

```bash
uv run uvicorn app.main:app --reload
```

The API will be available locally through the address provided by Uvicorn.

FastAPI's interactive API documentation can also be used to explore and test the available endpoints.

---

## Docker

Build the Docker image:

```bash
docker build -t fastapi-authenticator .
```

Run the container:

```bash
docker run -p 8000:8000 fastapi-authenticator
```

The authenticator can then run as an independent service alongside the application that consumes it.

---

## Next Steps

### Database Integration

Connect the service to a production-oriented database such as PostgreSQL and improve configuration for different deployment environments.

### Authentication Expansion

Add additional authentication capabilities such as:

* JWT-based authentication
* Refresh tokens
* Session management
* Email verification
* Password reset workflows

### Testing

Expand automated testing to cover:

* Registration
* Login
* Invalid credentials
* Duplicate users

### Deployment

Deploy the containerized service to a cloud environment and explore the transition from:

**Local Development → Docker → CI → Container Registry → Cloud Deployment**

### Application Integration

Create a small frontend or backend application that consumes the authenticator as an independent service.

---

**Project Goal:** Explore how authentication can be designed as a **modular, independently deployable service** while practicing Python backend development, secure credential handling, database abstraction, and Docker-based deployment.

