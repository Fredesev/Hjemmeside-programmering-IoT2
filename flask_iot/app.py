from flask import Flask, render_template, send_file
from get_flow_IoT2_data import generate_flow_data  # Opdater importen til generate_flow_data
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/flowdata')
def flowdata():
    # Generer flowdata 
    flow_data = generate_flow_data()

    # Returner flowdata som en fil og angiv MIME-typen som 'image/png'
    return send_file(flow_data, mimetype='image/png')

@app.route('/gpsdata')
def gpsdata():
    # Generer tilfældige GPS-koordinater
    lat = random.uniform(-90, 90)
    lng = random.uniform(-180, 180)

    # Send GPS-data til gpsdata.html
    return render_template('gpsdata.html', lat=lat, lng=lng)

@app.route('/battery')
def battery():
    # Generer tilfældigt batteriniveau (dummy data)
    battery_level = random.randint(0, 100)

    # Send batteridata til batteriopladning.html
    return render_template('batteriopladning.html', battery_level=battery_level)

if __name__ == "__main__":
    app.run(debug=True)





