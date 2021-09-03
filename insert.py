
def insert(encrypted_word, document_path, collection):
    collection.update_one({'_id': encrypted_word}, {'$addToSet': {'documents': document_path}}, upsert=True)
