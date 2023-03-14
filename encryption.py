import base64
import hashlib
from cryptography.fernet import Fernet

def generate_key(password):
    """
    Generate a 256-bit key from a given password string.
    """
    encoded_password = password.encode('utf-8')
    salt = hashlib.sha256(encoded_password).digest()
    key = hashlib.pbkdf2_hmac('sha256', encoded_password, salt, 100000)
    return base64.urlsafe_b64encode(key)

def encrypt_password(password, key):
    """
    Encrypt a password string using a given encryption key.
    """
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode('utf-8'))
    return encrypted_password.decode('utf-8')

def decrypt_password(encrypted_password, key):
    """
    Decrypt an encrypted password string using a given encryption key.
    """
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password.encode('utf-8'))
    return decrypted_password.decode('utf-8')
