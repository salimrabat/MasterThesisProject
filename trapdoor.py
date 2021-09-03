from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes


def trapdoor(key: bytes, word: str) -> object:
    digest = hashes.Hash(hashes.SHA256())
    word_bytes = word.encode('utf-8')
    digest.update(word_bytes)
    hashed_word = digest.finalize()
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(hashed_word) + encryptor.finalize()
