from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_socketio import SocketIO, emit
import sqlite3
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'admin' and password == 'password':
        return redirect(url_for('dashboard'))
    else:
        return 'Invalid credentials', 401

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/traffic', methods=['POST'])
def receive_traffic():
    data = request.json
    print("Data received:", data)
    save_data_to_db(data)
    socketio.emit('update', {'traffic': data})  # Emit data to WebSocket clients
    return jsonify({"status": "success"}), 200

def save_data_to_db(data):
    conn = sqlite3.connect('idr.db')
    c = conn.cursor()
    for entry in data:
        c.execute("INSERT INTO traffic (local_ip, local_port, remote_ip, remote_port, status) VALUES (?, ?, ?, ?, ?)",
                  (entry['local_ip'], entry['local_port'], entry['remote_ip'], entry['remote_port'], entry['status']))
    conn.commit()
    conn.close()

@app.route('/export/pdf')
def export_pdf():
    # Implement PDF export logic
    pass

@app.route('/export/csv')
def export_csv():
    # Implement CSV export logic
    pass

@app.route('/filter', methods=['POST'])
def filter_data():
    date_range = request.form.get('date_range')
    threat_type = request.form.get('threat_type')
    # Implement filter logic
    return jsonify({"status": "success"})

if __name__ == '__main__':
    socketio.run(app, debug=True)

