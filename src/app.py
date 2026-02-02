from flask import Flask, jsonify
import datetime
import socket
app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'hostname': socket.gethostname(),
        'message': 'You are doing great! <3<3'
        })

@app.route('/api/v1/healthz')

def health():
    return jsonify({'status':'up'}), 200


@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})

if __name__ == '__main__':
    app.run(host="0.0.0.0")

# '/api/v1/details'
# '/api/v1/healthz'
