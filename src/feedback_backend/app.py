from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database connection using hardcoded defaults and environment overrides

def get_db_conn():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database='feedback',
        user='postgres',
        password=os.environ.get('DB_PASSWORD', 'db-78n9n')
    )

# Initialize the database schema at startup

def init_db():
    conn = get_db_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id SERIAL PRIMARY KEY,
                    text TEXT NOT NULL
                );
            """)

@app.route('/api/message', methods=['POST'])
def save_message():
    data = request.get_json()
    conn = get_db_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO messages (text) VALUES (%s)",
                (data['message'],)
            )
    return '', 201

@app.route('/api/messages', methods=['GET'])
def get_messages():
    conn = get_db_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id, text FROM messages")
            rows = cur.fetchall()
    return jsonify([{"id": r[0], "text": r[1]} for r in rows])

@app.route('/api/message/<int:msg_id>', methods=['DELETE'])
def delete_message(msg_id):
    conn = get_db_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM messages WHERE id = %s", (msg_id,))
    return '', 204

@app.route('/api/scoring', methods=['POST'])
def save_message():
    data = request.get_json()
    conn = get_db_conn()
    with conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO messages (text) VALUES (%s)",
                (data['message'],)
            )
    return '', 201

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
