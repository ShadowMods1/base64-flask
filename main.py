from flask import Flask, request, render_template
import base64

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/decode', methods=['POST'])
def decode():
    encoded_str = request.form['encoded']
    try:
        # Decode the base64 encoded string
        decoded_bytes = base64.b64decode(encoded_str)
        decoded_text = decoded_bytes.decode('utf-8')
    except Exception as e:
        decoded_text = f"Error: {e}"

    return render_template('index.html', decoded_text=decoded_text)

@app.route('/encode', methods=['POST'])
def encode():
    text = request.form['text']
    try:
        # Encode the text to base64
        encoded_bytes = base64.b64encode(text.encode('utf-8'))
        encoded_str = encoded_bytes.decode('utf-8')
    except Exception as e:
        encoded_str = f"Error: {e}"

    return render_template('index.html', encoded_text=encoded_str)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
