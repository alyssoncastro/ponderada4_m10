from flask import Flask, request, jsonify

app = Flask(__name__)

logs = []

@app.route('/logs', methods=['POST'])
def add_log():
    log = request.json
    logs.append(log)
    return jsonify(log), 201

@app.route('/logs', methods=['GET'])
def get_logs():
    return jsonify(logs), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
