
from cryptography.fernet import Fernet
import os

class Encoder:
    def __init__(self):
        key_path = os.path.join(os.getcwd(), 'filekey.key')
        key_exists = os.path.isfile(key_path)
        if not key_exists:
            # key generation
            key = Fernet.generate_key()

            # string the key in a file
            with open('filekey.key', 'wb') as filekey:
                filekey.write(key)
        else:
            # opening the key
            with open('filekey.key', 'rb') as filekey:
                key = filekey.read()

            # using the generated key
        self.fernet = Fernet(key)



    def encode(self,path):
        # opening the original file to encrypt
        with open(path, 'rb') as file:
            original = file.read()

        # encrypting the file
        encrypted = self.fernet.encrypt(original)

        # opening the file in write mode and 
        # writing the encrypted data
        with open(path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decode(self,path):
        # opening the encrypted file
        with open(path, 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = self.fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open(path, 'wb') as dec_file:
            dec_file.write(decrypted)
