from flask import Flask, jsonify, request, render_template_string, make_response
from Crypto.Cipher import AES
import base64
import logging

app = Flask(__name__)

# Setup logging
logging.basicConfig(level=logging.DEBUG)

def unpad(s):
    padding_len = s[-1]
    app.logger.debug(f"Padding length: {padding_len}")
    if padding_len < 1 or padding_len > 16:
        raise ValueError("Invalid padding length")
    return s[:-padding_len]

def decrypt(ciphertext, key):
    key = key.encode('utf-8')
    if len(key) not in [16, 24, 32]:
        raise ValueError("Invalid AES key length")
    ciphertext = base64.b64decode(ciphertext)
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    app.logger.debug(f"Decrypted bytes before unpadding: {decrypted}")
    unpadded = unpad(decrypted)
    app.logger.debug(f"Unpadded bytes: {unpadded}")
    return unpadded.decode('utf-8')

@app.route('/')
def home():
    return "Welcome to Finding Waldo Crypto Challenge!\n He has hidden a secret message and key for you to decrypt. Good luck!"
    

@app.route('/message')
def message():
    return jsonify({
         "encrypted_message": "You found Waldo's secret message, G30tMv+ThtFNhuitft+HAj2FRg1sqtz7QtcaBzQNUHryhC2UCsFKE2LYfNpD8yiL"
    })


@app.route('/key')
def index():
  admin_cookie = request.cookies.get('WaldoesCookie')
  if admin_cookie == 'true':
    return 'thisisaveryshhhh'
  elif admin_cookie is None:
    resp = make_response("Sorry, but Waldo wants cookies in exchange for his key.")
    resp.set_cookie('WaldoesCookie', 'false')
    return resp
  else:
    return 'Sorry, but Waldo wants cookies in exchange for his key.'

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt_page():
    encrypted_message = ''
    key = ''
    decrypted_message = ''
    error = ''
    
    if request.method == 'POST':
        encrypted_message = request.form['encrypted_message']
        key = request.form['key']
        app.logger.debug(f"Received encrypted_message: {encrypted_message}")
        app.logger.debug(f"Received key: {key}")
        try:
            if len(key) not in [16, 24, 32]:
                raise ValueError("Invalid AES key length (must be 16, 24, or 32 bytes)")
            decrypted_message = decrypt(encrypted_message, key)
            app.logger.debug(f"Decrypted message from Waldo: {decrypted_message}")
            print("done")  # Print "done" to console
        except Exception as e:
            error = str(e)
            app.logger.error(f"Error during decryption: {error}")
    
    return render_template_string(DECRYPT_TEMPLATE, decrypted_message=decrypted_message, error=error, encrypted_message=encrypted_message, key=key)

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
          <input type="text" id="encrypted_message" name="encrypted_message" required value="{{ encrypted_message }}">
        </div>
        <div>
          <label for="key">Decryption Key</label>
          <input type="text" id="key" name="key" required value="{{ key }}">
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
    app.run(host='0.0.0.0', port=8000)
