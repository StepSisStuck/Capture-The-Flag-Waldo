from Crypto.Cipher import AES
import base64


def pad(s):
    block_size = 16
    padding_len = block_size - len(s) % block_size
    padding = bytes([padding_len] * padding_len)
    return s + padding

def encrypt(plaintext, key):
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode('utf-8'))
    encrypted = cipher.encrypt(padded_plaintext)
    return base64.b64encode(encrypted).decode('utf-8')

key = "thisisaveryshhhh"  # 16 characters
plaintext = "CTF{42.3601,-71.0589}"
encrypted_message = encrypt(plaintext, key)
print(f"Encrypted message: {encrypted_message}")
