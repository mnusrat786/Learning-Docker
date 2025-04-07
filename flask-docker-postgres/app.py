from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database Connection
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    return conn

# Home Route
@app.route('/')
def home():
    return "Flask API with PostgreSQL - Dockerized!"

# Add User
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;", 
                (data['name'], data['email']))
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "User added", "id": user_id}), 201

# Get Users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
