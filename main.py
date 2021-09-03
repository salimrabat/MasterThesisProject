
from build_index import build_index
from preprocess import preprocess
from find import find_documents
from getkeys import get_keys
from trapdoor import trapdoor
from upload_and_download import encrypt_and_upload, download_and_decrypt


def test():
    print("Welcome to searchable encryption:")
    print("Specify your username to login:")
    username = input()
    keyword_key, file_key, user_exists = get_keys(username)
    done = False

    if user_exists:
        print("Existing user and keys fetched")
    else:
        print("User created and keys generated")
    while not done:
        while user_exists:
            print("What do you want to do? Write the number of your choice:\n1. Upload a file\n2. Search in files\n"
                  "0. exit")
            choice = int(input())
            if choice == 1:
                print("Write the filename with its full path:")
                file_path = input()
                with open(file_path, 'r') as file:
                    text = file.read()
                file_path_split = file_path.split('/')
                file_name = file_path_split[len(file_path_split) - 1]
                encrypted_keywords = build_index(text, keyword_key, username, file_name)
                if encrypt_and_upload(file_path, file_name, file_key):
                    print('File uploaded!')
            elif choice == 2:
                print("Write the keyword that you want to search for:\n")
                keywords = input()
                clean_keywords = preprocess(keywords)
                encrypted_keywords = [trapdoor(keyword_key, word) for word in clean_keywords]
                result = find_documents(username, encrypted_keywords)
                for x in result:
                    if download_and_decrypt(x, file_key):
                        print('File downloaded')
            elif choice == 0:
                print("Thanks for using searchable encryption! Bye!")
                done = True
                break
            else:
                print("Choice not supported, write valid choice number!\n")
        while not user_exists:
            print("What do you want to do? Write the number of your choice:\n1. Upload a file\n0. exit")
            choice = int(input())
            if choice == 1:
                print("Write the filename with its full path:")
                file_path = input()
                with open(file_path, 'r') as file:
                    text = file.read()
                file_path_split = file_path.split('/')
                file_name = file_path_split[len(file_path_split)-1]
                encrypted_keywords = build_index(text, keyword_key, username, file_name)
                user_exists = True
                if encrypt_and_upload(file_path, file_name, file_key):
                    print('File uploaded!')
            elif choice == 0:
                print("Thanks for using searchable encryption! Bye!")
                done = True
                break
            else:
                print("Choice not supported, write valid choice number!\n")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
