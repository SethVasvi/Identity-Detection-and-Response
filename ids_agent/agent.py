import os
import time
import json
import psutil
import requests

def capture_traffic():
    # Capture network traffic
    connections = psutil.net_connections(kind='inet')
    traffic_data = []
    for conn in connections:
        if conn.status == psutil.CONN_ESTABLISHED:
            traffic_data.append({
                "local_ip": conn.laddr.ip,
                "local_port": conn.laddr.port,
                "remote_ip": conn.raddr.ip if conn.raddr else None,
                "remote_port": conn.raddr.port if conn.raddr else None,
                "status": conn.status
            })
    return traffic_data

def send_data(data):
    url = "http://localhost:5000/api/traffic"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)
    return response

while True:
    data = capture_traffic()
    response = send_data(data)
    print(f"Data sent: {response.status_code}")
    time.sleep(60)  # Wait for 60 seconds before sending the next data
