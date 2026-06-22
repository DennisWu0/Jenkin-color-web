# Jenkin-color-web (Flask + PostgreSQL + Docker Compose)

A simple end-to-end containerized web application that demonstrates a basic CI/CD-style architecture using Flask, PostgreSQL, and Docker Compose.

This project is designed for learning DevOps fundamentals such as containerization, service orchestration, and environment-based configuration.


## 📌 Architecture Overview

This demo consists of:

- **Web Service**: Flask application (Python)
- **Database**: PostgreSQL
- **Container Orchestration**: Docker Compose
- **Initialization Script**: SQL seed data for DB setup

The Flask app reads data from PostgreSQL and dynamically renders a webpage based on database content.


## ⚙️ Tech Stack

- Python 3.11
- Flask
- PostgreSQL 15
- Docker
- Docker Compose


## 🐳 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/DennisWu0/Jenkin-color-web.git
cd Jenkin-color-web
```

### 2. Start services

```bash
docker compose up --build
```
### 3. Open in browser

```bash
http://localhost:5000
```
