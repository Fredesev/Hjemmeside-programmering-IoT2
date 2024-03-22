from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, send_file

app = Flask(__name__)

def generate_flow_data():
    # Simulere antal liter vand per time
    hours = np.arange(1, 25)
    water_flow = np.random.randint(0, 5, size=24)  # Tilfældige værdier
    
    # Generer bar diagrammet
    plt.figure(figsize=(10, 6))
    plt.bar(hours, water_flow, color='pink')  # Pink farve
    plt.xlabel('Hour')
    plt.ylabel('Water Flow (Liters)')
    plt.title('Water Flow Data')
    
    # Gem diagrammet som en BytesIO-objekt
    flow_data = BytesIO()
    plt.savefig(flow_data, format='png')
    flow_data.seek(0)
    
    plt.close()  # Luk plot for at frigive ressourcer

    return flow_data

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/flowdata')
def flowdata():
    flow_data = generate_flow_data()
    return send_file(flow_data, mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)


