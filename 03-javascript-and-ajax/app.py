import random
import json
from flask import Flask, render_template, Response
app = Flask(__name__)

def read_sensors():
    """Returns an array of 3 random values between 0 and 1"""
    return [ f'{random.random():.4f}' for i in range(3) ]

@app.route('/')
def index():
    data = read_sensors()
    return render_template('index.html', data=data)

@app.route('/v2')
def index_async():
    return render_template('index-async.html', data=read_sensors())

@app.route('/data')
def get_data():
    data = read_sensors()
    return Response(json.dumps(data), mimetype='application/json')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
