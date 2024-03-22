from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, send_file
from get_flow_IoT2_data import get_flow_data
from random import randint
import sqlite3
from datetime import datetime

app = Flask(__name__)

def log_flow_data():
    while True:
        query = """INSERT INTO flow (datetime, gps, humidity) VALUES(?, ?, ?)"""
        data = (datetime.now(), randint(0, 30), randint(0, 100))

        try:
            conn = sqlite3.connect("database/sensor_data.db")
            cur = conn.cursor()
            cur.execute(query, data)  # Tilføj data til query
            conn.commit()
        except sqlite3.Error as sql_e:
            print(f"sqlite error occured: {sql_e}")
            conn.rollback()
        except Exception as e:
            print(f"Error occured: {e}")
        finally: 
            conn.close()

def generate_flow_data():
    timestamp, gps, hum = get_flow_data()

    # Simulere antal liter vand per time
    hours = np.arange(1, 25)
    water_flow = np.random.randint(0, 5, size=24)  # Tilfældige værdier
    
    # Generer bar diagrammet
    plt.figure(figsize=(10, 6))
    plt.bar(hours, water_flow)
    plt.xlabel('Hour')
    plt.ylabel('Water Flow (liters)')
    plt.title('Water Flow Over 24 Hours')  # Rettelse af stavefejl
    plt.xticks(np.arange(1, 25))
    plt.grid(True)

    # Markér hver gang der er løbet 1 liter vand igennem
    for hour, flow in zip(hours, water_flow):
        if flow == 1:
            plt.text(hour, flow, '1L', ha='center', va='bottom')

    # Gem diagrammet som en bytestream
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    return buf

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/flowdata')
def flowdata():
    flow_data = generate_flow_data()
    return send_file(flow_data, mimetype='image/png')

if __name__ == "__main__":
    log_flow_data()  # Log flow data
    app.run(debug=True)

