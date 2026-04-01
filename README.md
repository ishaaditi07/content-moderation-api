#  AI Content Moderation API

A lightweight, production-ready **content moderation system** built using FastAPI.
This API detects **toxic, profane, and unsafe text** in real-time using modular endpoints.

---

##  Features

* 🔍 Profanity Detection
* ⚠️ Toxicity Analysis
* ✅ Safety Classification
* 🧠 Combined Moderation Endpoint
* ⚡ FastAPI-based high-performance backend
* 🐳 Dockerized for consistent deployment

---

## 🧠 How It Works

The system processes input text and performs:

* **Profanity Check** → detects harmful words
* **Toxicity Check** → identifies aggressive language
* **Safety Decision** → determines if content is safe
* **Moderation Summary** → unified response with explanation

---

## 📡 API Endpoints

### 🔹 Home

```
GET /
```

---

### 🔹 Profanity Detection

```
POST /profanity
```

**Request:**

```json
{
  "text": "You are stupid"
}
```

---

### 🔹 Toxicity Detection

```
POST /toxicity
```

---

### 🔹 Safety Check

```
POST /safe
```

---

### 🔹 Combined Moderation (Recommended)

```
POST /moderate
```

**Request:**

```json
{
  "text": "I hate you idiot"
}
```

**Response:**

```json
{
  "safe": false,
  "profanity": true,
  "toxicity": true,
  "message": "Unsafe content detected"
}
```

---

## ⚙️ Tech Stack

* Python
* FastAPI
* Uvicorn
* Docker

---

## 🖥️ Run Locally

### 1. Install dependencies

```
pip install -r requirements.txt
```

### 2. Run server

```
uvicorn main:app --reload
```

### 3. Open in browser

```
http://127.0.0.1:8000/docs
```

---

## 🐳 Run with Docker

### Build image

```
docker build -t moderation-api .
```

### Run container

```
docker run -p 8000:80 moderation-api
```

---

## 🌍 Deployment

The application can be deployed on cloud platforms like:

* Render
* AWS EC2
* Docker-based environments

## 💼 Use Cases

* Social media moderation
* Chat applications
* Comment filtering systems
* Content safety pipelines

---

##  Future Improvements

* Add ML-based classification models
* Improve keyword detection
* Add logging and monitoring
* Integrate with frontend UI

---

## 👩‍💻 Author

**Isha Aditi**

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
