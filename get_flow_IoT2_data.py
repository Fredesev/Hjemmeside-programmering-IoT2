import base64
from io import BytesIO
import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, render_template, send_file
from get_flow_IoT2_data import get_flow_data

app = Flask(__name__)

def generate_flow_data():
    # Hent data fra databasen
    timestamps, gps, hum = get_flow_data(number_of_rows=10)  # Antaget værdi for number_of_rows

    # Brug timestamps til at generere timer
    hours = [timestamp.hour for timestamp in timestamps]

    # Generer bar diagrammet
    plt.figure(figsize=(10, 6))
    plt.bar(hours, hum)  # Brug humidity data i stedet for vandflow data
    plt.xlabel('Hour')
    plt.ylabel('Humidity')
    plt.title('Humidity Over 24 Hours')
    plt.xticks(np.arange(1, 25))
    plt.grid(True)

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
    app.run(debug=True)





            
      