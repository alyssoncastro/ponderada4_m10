from flask import Flask, request, jsonify
import logging
import requests

app = Flask(__name__)

# Configuração de logging
logging.basicConfig(filename='/logs/eventos.log', level=logging.INFO, format='%(asctime)s %(message)s')

eventos = []

@app.route('/eventos', methods=['POST', 'GET', 'PUT', 'DELETE'])
def handle_eventos():
    try:
        if request.method == 'POST':
            evento = request.json
            eventos.append(evento)
            # Logging
            log_message = f"POST /eventos {evento}"
            logging.info(log_message)
            send_log_to_centralized_system(log_message)
            return jsonify(evento), 201
        elif request.method == 'GET':
            return jsonify(eventos), 200
        elif request.method == 'PUT':
            updated_evento = request.json
            for evento in eventos:
                if evento['id'] == updated_evento['id']:
                    evento.update(updated_evento)
                    # Logging
                    log_message = f"PUT /eventos {updated_evento}"
                    logging.info(log_message)
                    send_log_to_centralized_system(log_message)
                    return jsonify(evento), 200
            return jsonify({'error': 'Evento não encontrado'}), 404
        elif request.method == 'DELETE':
            evento_id = request.json.get('id')
            for evento in eventos:
                if evento['id'] == evento_id:
                    eventos.remove(evento)
                    # Logging
                    log_message = f"DELETE /eventos {evento_id}"
                    logging.info(log_message)
                    send_log_to_centralized_system(log_message)
                    return jsonify({'message': 'Evento deletado'}), 200
            return jsonify({'error': 'Evento não encontrado'}), 404
    except Exception as e:
        logging.error(f"Error in /eventos endpoint: {e}")
        return jsonify({'error': str(e)}), 500

def send_log_to_centralized_system(log_message):
    log_data = {'log': log_message}
    requests.post('http://logs:5002/logs', json=log_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
