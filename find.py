from env_var import mongo_client


def find_documents(user, encrypted_keywords):
    db = mongo_client.files_index
    collection = db[user]
    results_intersection = None
    for word in encrypted_keywords:
        if results_intersection is None:
            query_result = collection.find_one({'_id': word})
            if query_result is not None:
                results_intersection = query_result['documents']
            else:
                return []
        else:
            query_result = collection.find_one({'_id': word})
            if query_result is not None:
                results_intersection = [document for document in results_intersection if
                                        document in query_result['documents']]
            else:
                return []
    return results_intersection
