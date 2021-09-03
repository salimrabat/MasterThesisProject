from insert import insert
from preprocess import preprocess
from env_var import db
from trapdoor import trapdoor


def build_index(text, key, user, filename):
    words = preprocess(text)
    encrypted_distinct_keywords = []
    collection = db[user]
    for word in words:
        if word == '':
            continue
        encrypted_word = trapdoor(key, word)
        if encrypted_word not in encrypted_distinct_keywords:
            encrypted_distinct_keywords.append(encrypted_word)
            insert(encrypted_word, filename, collection)
    return encrypted_distinct_keywords
