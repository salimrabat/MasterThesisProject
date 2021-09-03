from cryptography.fernet import Fernet

from env_var import s3, bucket_name


def encrypt_and_upload(file_path, file_name, key):
    fernet = Fernet(key)
    try:
        with open(file_path, 'rb') as file:
            word_text = file.read()
            cipher_text = fernet.encrypt(word_text)
        object_name = file_name
        with open(object_name, 'wb+') as encrypted_file:
            encrypted_file.write(cipher_text)
        s3.upload_file(object_name, bucket_name, object_name)
        return True
    except IOError:
        print("File does not exist")
        return False


def download_and_decrypt(object_name, key):
    fernet = Fernet(key)
    try:
        with open(object_name, 'wb') as file:
            s3.download_fileobj(bucket_name, object_name, file)
        with open(object_name, 'rb') as file:
            cipher_text = file.read()

        plain_text = fernet.decrypt(cipher_text)

        with open('decrypted'+object_name, 'wb') as decrypted_file:
            decrypted_file.write(plain_text)
        return True
    except IOError:
        print("File does not exist")
        return False

