import sys
import json
from Crypto.Cipher import AES
import base64

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def decrypt(ciphertext, key):
    key = key.encode('utf-8')
    ciphertext = base64.b64decode(ciphertext)
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext)).decode('utf-8')

if len(sys.argv) != 2:
    print("Usage: python decrypt.py '{\"encrypted_message\":\"<ciphertext>\"}'")
    sys.exit(1)

input_json = sys.argv[1]
data = json.loads(input_json)
ciphertext = data.get("encrypted_message")

if not ciphertext:
    print("Invalid input. Please provide a valid encrypted message.")
    sys.exit(1)

key = "thisisaveryshhhh"  # 16 characters
plaintext = decrypt(ciphertext, key)
print("Decrypted message:", plaintext)
