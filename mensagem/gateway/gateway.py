from flask import Flask, request, jsonify
import requests
import logging

app = Flask(__name__)

# Configuração de logging
logging.basicConfig(filename='/logs/gateway.log', level=logging.INFO, format='%(asctime)s %(message)s')

@app.route('/eventos', methods=['POST', 'GET', 'PUT', 'DELETE'])
def eventos():
    try:
        if request.method == 'POST':
            response = requests.post('http://eventos:5001/eventos', json=request.json)
        elif request.method == 'GET':
            response = requests.get('http://eventos:5001/eventos')
        elif request.method == 'PUT':
            response = requests.put('http://eventos:5001/eventos', json=request.json)
        elif request.method == 'DELETE':
            response = requests.delete('http://eventos:5001/eventos', json=request.json)
        else:
            response = jsonify({'error': 'Método não permitido'}), 405

        # Logging
        log_message = f"{request.method} /eventos {response.status_code}"
        logging.info(log_message)
        send_log_to_centralized_system(log_message)
        return response.json()
    except Exception as e:
        logging.error(f"Error in /eventos endpoint: {e}")
        return jsonify({'error': str(e)}), 500

def send_log_to_centralized_system(log_message):
    log_data = {'log': log_message}
    requests.post('http://logs:5002/logs', json=log_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
