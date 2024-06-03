from flask import Flask, jsonify, request, render_template_string
from Crypto.Cipher import AES
import base64
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

def unpad(s):
    logging.debug(f"Unpadding input: {s}")
    result = s[:-ord(s[len(s) - 1:])]
    logging.debug(f"Unpadded result: {result}")
    return result

def decrypt(ciphertext, key):
    logging.debug(f"Starting decryption with key: {key}")
    key = key.encode('utf-8')
    if len(key) not in [16, 24, 32]:
        raise ValueError("Invalid AES key length (must be 16, 24, or 32 bytes)")
    logging.debug(f"Key length is valid: {len(key)} bytes")
    try:
        ciphertext = base64.b64decode(ciphertext)
        logging.debug(f"Base64 decoded ciphertext: {ciphertext}")
    except Exception as e:
        logging.error(f"Error decoding base64 ciphertext: {e}")
        raise ValueError("Invalid base64 ciphertext")
    try:
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = unpad(cipher.decrypt(ciphertext)).decode('utf-8')
        logging.debug(f"Decryption successful: {decrypted}")
        return decrypted
    except Exception as e:
        logging.error(f"Error during decryption: {e}")
        raise ValueError("Decryption failed")

@app.route('/')
def home():
    return "Welcome to Finding Waldo Crypto Challenge!"

@app.route('/message')
def message():
    return jsonify({
        "encrypted_message": "G30tMv+ThtFNhuitft+HAt2IWJ/F+c/9BjyR72tfA8Xkhc+PLny6V7hEy30KYBLnXc/kG30fm/eAWrAGpDB7fQ=="
    })

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt_page():
    decrypted_message = None
    error = None

    if request.method == 'POST':
        encrypted_message = request.form['encrypted_message']
        key = request.form['key']
        logging.debug(f"Received encrypted message: {encrypted_message} and key: {key}")
        try:
            decrypted_message = decrypt(encrypted_message, key)
            logging.debug(f"Decrypted message: {decrypted_message}")
        except Exception as e:
            logging.error(f"Error during decryption: {e}")
            error = str(e)
    
    logging.debug(f"Decrypted message: {decrypted_message}, Error: {error}")
    return render_template_string(DECRYPT_TEMPLATE, decrypted_message=decrypted_message, error=error)

DECRYPT_TEMPLATE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Decrypt Message</title>
  </head>
  <body>
    <div class="container">
      <h1>Decrypt Message</h1>
      <form method="post">
        <div>
          <label for="encrypted_message">Encrypted Message</label>
          <input type="text" id="encrypted_message" name="encrypted_message" required>
        </div>
        <div>
          <label for="key">Decryption Key</label>
          <input type="text" id="key" name="key" required>
        </div>
        <button type="submit">Decrypt</button>
      </form>
      {% if decrypted_message %}
        <h2>Decrypted Message: {{ decrypted_message }}</h2>
      {% elif error %}
        <h2>Error: {{ error }}</h2>
      {% endif %}
    </div>
  </body>
</html>
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
