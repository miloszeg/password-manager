import random
import string

def generate_password(length=12):
    """
    Generate a random password string of the specified length.
    """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    return password
