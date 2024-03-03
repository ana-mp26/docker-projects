from flask import Flask, jsonify
import requests
import time
import numpy as np
from scipy import stats

app = Flask(__name__)

rtt_values = []

@app.route('/measure_round_trip_time')
def measure_round_trip_time():
    global rtt_values
    
    num_requests = 10  # Number of repetitions
    
    rtt_values.clear()  # Clear previous RTT values
    
    for _ in range(num_requests):
        start_time = time.time()
        response = requests.get('http://www.google.com')
        end_time = time.time()
        round_trip_time = end_time - start_time
        rtt_values.append(round_trip_time)
    
    avg_round_trip_time = np.mean(rtt_values)
    std_dev = np.std(rtt_values)
    
    # Calculate the standard error of the mean
    stderr = std_dev / np.sqrt(num_requests)
    
    # Calculate the t-statistic for 90% confidence interval
    t_statistic = stats.t.ppf(0.95, df=num_requests-1)
    
    # Calculate the margin of error
    margin_of_error = t_statistic * stderr
    
    # Calculate the confidence interval
    lower_bound = avg_round_trip_time - margin_of_error
    upper_bound = avg_round_trip_time + margin_of_error
    
    return jsonify({
        'rtt_values': rtt_values,
        'average_round_trip_time': avg_round_trip_time,
        'confidence_interval': (lower_bound, upper_bound)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)

