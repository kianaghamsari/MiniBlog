# MiniBlog API

MiniBlog is a minimal yet professional Django REST API project built to demonstrate core backend development skills, clean architecture, and real-world development workflow.

This project is designed for learning purposes and technical interviews.

---

## Tech Stack

- Python
- Django & Django REST Framework
- JWT Authentication (SimpleJWT)
- Docker & Docker Compose
- Git & GitHub (Issues, Branches, PRs)

---

## Features

- User registration and authentication using JWT
- Modular `accounts` and `blog` apps
- CRUD operations for blog posts
- Comment system for posts
- Permission control:
  - Only authenticated users can create posts or comments
  - Only post owners can update or delete their posts
- Dockerized development environment

---

## Project Structure

```

MiniBlog/
├── accounts/        # Authentication & user management
├── blog/            # Posts, comments, permissions
├── config/          # Project settings
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── manage.py

````

---

## Authentication

JWT-based authentication is implemented using `djangorestframework-simplejwt`.

### Auth Endpoints
- `POST /api/auth/users/register/` — Register new user
- `POST /api/auth/login/` — Obtain access & refresh tokens
- `POST /api/auth/refresh/` — Refresh access token

---

## Blog Endpoints

### Posts
- `GET /api/posts/`
- `POST /api/posts/`
- `PUT /api/posts/{id}/`
- `DELETE /api/posts/{id}/`

### Comments
- `GET /api/comments/`
- `POST /api/comments/`
- `PUT /api/comments/{id}/`
- `DELETE /api/comments/{id}/`


---

## Redis Caching

In this project, **Redis** is used as a caching layer to improve API performance and reduce database load.

The main use case is caching the **posts list endpoint**, which is a read-heavy endpoint and does not change frequently.

**How it works:**

* On the first request to `GET /api/posts/`, data is fetched from the database and stored in Redis.
* Subsequent requests are served directly from Redis for 5 minutes.
* Whenever a post is created, updated, or deleted, the cache is invalidated to ensure data consistency.

**Benefits:**

* Reduced number of database queries
* Faster response times for read operations
* Better scalability for high-traffic scenarios

Redis is integrated using **django-redis** and is fully containerized via Docker.




---

## Run Project with Docker

Make sure Docker is installed, then run:

```bash
docker compose up --build
````

The project will be available at:

```
http://127.0.0.1:8000/
```

---

## Development Notes

* Authentication logic is separated into the `accounts` app
* Permissions are handled using custom DRF permission classes
* Git workflow follows best practices (Issues, feature branches, Pull Requests)
* Docker is used to ensure consistent development environment

---

## Purpose

This project was built to:

* Practice Django REST Framework concepts
* Demonstrate backend development skills
* Serve as a portfolio project for job applications

