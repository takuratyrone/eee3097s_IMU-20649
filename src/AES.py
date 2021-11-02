from base64 import b64encode, b64decode 
import hashlib 
from Cryptodome.Cipher import AES 
import os 
from Cryptodome.Random import get_random_bytes
from huffman import*
import time
from test import* 

def encrypt(plain_text, password):
    # generate a random salt
    salt = get_random_bytes(AES.block_size)
    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt( password.encode(), salt=salt, n=2**14, 
        r=8, p=1, dklen=32)
    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)
    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8')) 
    return {
        'cipher_text': b64encode(cipher_text).decode('utf-8'), 
        'salt': b64encode(salt).decode('utf-8'), 
        'nonce': b64encode(cipher_config.nonce).decode('utf-8'), 
        'tag': b64encode(tag).decode('utf-8')
    }

def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    salt = b64decode(enc_dict['salt']) 
    cipher_text = b64decode(enc_dict['cipher_text']) 
    nonce = b64decode(enc_dict['nonce']) 
    tag = b64decode(enc_dict['tag'])
    
    # generate the private key from the password and salt
    private_key = hashlib.scrypt( password.encode(), salt=salt, n=2**14, 
        r=8, p=1, dklen=32)
    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag) 
    return decrypted

def encrypt_file(filename): 
    global encrypted, f, password
    password = input("Password: ")
    f = open("data_encrypted", "w")
    f1 = open("data_decrypted", "w")
    print("Starting Encryption...")
    start_enc = time.time()
    encrypted = encrypt(filename, password)
    end_enc = time.time()
    print("Encryption Complete...")
    process() #CPU and RAM usage after encryption
    print(f"ENCRYPTION: {(end_enc-start_enc):.6f} seconds")
    f.write(str(encrypted))

    print("Starting Decryption...")
    start_dec = time.time()
    decrypted = decrypt(encrypted, password)
    end_dec = time.time()
    print(f"DECRYPTION: {(end_dec-start_dec):.6f} seconds")
    f1.write(str(decrypted))
    str_decrypted = str(decrypted.decode('utf-8'))
    print("Decryption Complete...")
    process()   #CPU and RAM usage after decryption
    return str_decrypted

def decrypt_file(filename):
    # Let us decrypt using our original password
    f2 = open(filename, "r")
    read = f2.read()
    decrypted = decrypt(read, password) 
    print(bytes.decode(decrypted))

