from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_conn():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'postgres-service'),
        database='feedback',
        user='postgres',
        password=os.environ.get('DB_PASSWORD', 'password')
    )

@app.route('/api/message', methods=['POST'])
def save_message():
    data = request.get_json()
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO messages (text) VALUES (%s)", (data['message'],))
    conn.commit()
    cur.close()
    conn.close()
    return '', 201

@app.route('/api/messages', methods=['GET'])
def get_messages():
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, text FROM messages")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": row[0], "text": row[1]} for row in rows])

@app.route('/api/message/<int:msg_id>', methods=['DELETE'])
def delete_message(msg_id):
    conn = get_db_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM messages WHERE id = %s", (msg_id,))
    conn.commit()
    cur.close()
    conn.close()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
