import sqlite3

def save_data_to_db(data):
    conn = sqlite3.connect('idr.db')
    c = conn.cursor()
    for entry in data:
        c.execute("INSERT INTO traffic (local_ip, local_port, remote_ip, remote_port, status) VALUES (?, ?, ?, ?, ?)",
                  (entry['local_ip'], entry['local_port'], entry['remote_ip'], entry['remote_port'], entry['status']))
    conn.commit()
    conn.close()

@app.route('/api/traffic', methods=['POST'])
def receive_traffic():
    data = request.json
    print("Data received:", data)
    save_data_to_db(data)
    socketio.emit('update', {'traffic': data})  # Emit data to WebSocket clients
    return jsonify({"status": "success"}), 200
