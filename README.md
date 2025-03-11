# Flask Dockerized CRUD API with PostgreSQL
This is a simple Flask API running inside a Docker container with a PostgreSQL database

## Setup Instructions

1️⃣ **Clone the repository:**
```sh
git clone <your-repo-link>
cd flask-docker-postgres
```
2️⃣ Build and run the containers:
```sh
docker-compose up --build
```
3️⃣ Test API Endpoints:

Check if API is running:
```sh
http://localhost:5000/
```
Add a new user:
```sh
curl -X POST http://localhost:5000/users -H "Content-Type: application/json" -d '{"name": "Ali", "email": "ali@example.com"}'
```
Get all users:
```sh
curl -X GET http://localhost:5000/users
```

