from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Replace with your Pushover API token and user key
PUSHOVER_TOKEN = 'aom2u6d973uwhxd8shchojhmioek2c'
PUSHOVER_USER_KEY = 'ux76y4hy4fs9oscfec3t64yshgrdhn'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    payload = {
        'token': PUSHOVER_TOKEN,
        'user': PUSHOVER_USER_KEY,
        'message': message
    }
    response = requests.post('https://api.pushover.net/1/messages.json', data=payload)
    return f'Status: {response.status_code}, Response: {response.text}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
