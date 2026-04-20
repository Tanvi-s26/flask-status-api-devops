# Flask Status API - DevOps Project

This project is a simple Flask-based API built to understand core DevOps concepts.

---

## 🚀 Features
- REST API with Flask
- Docker containerization
- CI pipeline using GitHub Actions

---

## 📌 Endpoints
- `/` → Welcome message  
- `/status` → Application status  
- `/time` → Current server time  

---

## 🐳 Run with Docker

```bash
docker build -t flask-status-api .
docker run -p 5000:5000 flask-status-api

---

## ⚙️ CI/CD Pipeline

This project uses GitHub Actions to:
- Automatically install dependencies
- Run the application
- Build Docker image on every push

---

