# encrypt.py | Auth.py

from cryptography.fernet import InvalidToken
from cryptography.fernet import Fernet

class Encrypt:
    def __init__(self, password):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.password = password
    def set_password(self):
        encode = self.fernet.encrypt(self.password.encode())
        return encode
    def get_password(self):
        try:
            decode = self.fernet.decrypt(self.password)
            return decode
        except InvalidToken:
            return 'error: Invalid Token'