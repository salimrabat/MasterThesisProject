import os
from cryptography.fernet import Fernet


def keygen():
    keyword_key = os.urandom(32)
    key = Fernet.generate_key()
    return keyword_key, key
