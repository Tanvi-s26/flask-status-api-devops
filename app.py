from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to DevOps Project 🚀")

@app.route('/status')
def status():
    return jsonify(status="Application is running ✅")

@app.route('/time')
def time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return jsonify(time=current_time)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)