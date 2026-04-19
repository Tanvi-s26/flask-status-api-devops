\# Flask Status API (DevOps Starter)



This is a simple Flask-based API built to practice DevOps concepts.



\## 🚀 Features

\- Home endpoint

\- Status check endpoint

\- Current time endpoint



\## 📌 Endpoints

\- `/` → Welcome message

\- `/status` → Application status

\- `/time` → Current server time



\## ▶️ Run Locally



```bash

pip install -r requirements.txt

python app.py

---

## 🐳 Run with Docker

```bash
docker build -t flask-status-api .
docker run -p 5000:5000 flask-status-api
