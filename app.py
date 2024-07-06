from flask import Flask, request, render_template, redirect, url_for, flash
import os
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Necessary for flashing messages

# Fetch Pushover API token and user key from environment variables
PUSHOVER_TOKEN = os.getenv('PUSHOVER_TOKEN')
PUSHOVER_USER_KEY = os.getenv('PUSHOVER_USER_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    message = request.form['message']
    url = request.form.get('url', '')  # Fetching optional URL parameter
    payload = {
        'token': PUSHOVER_TOKEN,
        'user': PUSHOVER_USER_KEY,
        'message': message,
        'url': url
    }
    try:
        response = requests.post('https://api.pushover.net/1/messages.json', data=payload)
        if response.status_code == 200:
            flash('Message sent successfully!')
        else:
            flash(f'Failed to send message. Status: {response.status_code}, Response: {response.text}')
    except requests.exceptions.RequestException as e:
        flash(f'Error: {e}')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)