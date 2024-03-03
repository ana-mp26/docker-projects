from flask import Flask, jsonify, render_template
import requests
import time
import numpy as np
from scipy import stats

app = Flask(__name__)

@app.route('/')
def index():
    measurements = []
    for i in range(100):
        start_time = time.time()
        response = requests.get('http://flask_app_1:5000/')
        rtt = time.time() - start_time
        measurements.append(rtt)
    avg_rtt = np.mean(measurements)
    std_err = np.std(measurements) / np.sqrt(100)
    confidence_interval = stats.t.interval(0.90, len(measurements)-1, loc=avg_rtt, scale=std_err)
    
    response_data = {
        "response_from_app_1": response.text,
        "measurements": measurements,
        "average_rtt": avg_rtt,
        "confidence_interval": confidence_interval
    }
    
    return jsonify(response_data)

# Route to serve HTML page with chart
@app.route('/chart')
def chart():
    return render_template('chart.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)

