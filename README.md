# Rate-Limiting-with-FastAPI
This project demonstrates how to build a rate limiter that restricts the number of requests a client can make to an endpoint within a given time window.
It uses a decorator to wrap FastAPI routes and control access dynamically, ensuring fair API usage and preventing abuse.

# Features

- Built with FastAPI and Python decorators

- Simple and lightweight — no external cache or DB

- Per-endpoint independent rate limiting

- Adjustable limits (max_calls, time_frame)

- Easily extendable to IP-based or Redis-based rate limiting

# Result
<img width="600" height="300" alt="image" src="https://github.com/user-attachments/assets/c43eb3d5-0684-4a19-8f7a-df9941ced89c" />

# Installation and set up
```
# 1. Clone the repository
git clone https://github.com/Oudarja/Rate-Limiting-with-FastAPI.git

# 2. Python version 3.9.13
 
# 3. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

# 4. Install dependencies
pip install fastapi uvicorn
```

# Run the Application
```
uvicorn main:app --reload

Server will start at:

http://127.0.0.1:8000
```
