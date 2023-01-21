#!/usr/bin/env python

import socket

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from nacl.public import PrivateKey, SealedBox, PublicKey

SERVER_IP = "10.128.0.7"
SERVER_PORT = 6084
BUFFER_SIZE = 2048
BLOCK_SIZE = 32


def generate_asymmetric_key():
    private_key = PrivateKey.generate()
    file_out = open("PrivateKeyClient.pem", "wb")
    file_out.write(bytes(private_key))
    file_out.close()

    public_key = private_key.public_key
    file_out = open("PublicKeyClient.pem", "wb")
    file_out.write(bytes(public_key))
    file_out.close()


def generate_symmetric_key():
    sym_key = get_random_bytes(BLOCK_SIZE)
    file_out = open("SymmetricKeyClient.txt", "wb")
    file_out.write(sym_key)
    file_out.close()


def get_symmetric_object(key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher


def encrypt_with_symmetric(cipher, message):
    result = cipher.encrypt(pad(message.encode(), BLOCK_SIZE))
    return result


def encrypt_with_asymmetric(public_key, message):
    box = SealedBox(PublicKey(public_key))
    result = box.encrypt(message)
    return result


def decrypt_with_symmetric(cipher, message):
    result = unpad(cipher.decrypt(message), BLOCK_SIZE)
    return result


def decrypt_with_asymmetric(private_key, message):
    box = SealedBox(PrivateKey(private_key))
    result = box.decrypt(message)
    return result


def encode_utf8_before_send(message):
    return message.encode("UTF-8")


def decode_utf8_before_print(message):
    return message.decode("UTF-8")


# This method loads the key to the program or generate a new one if freshly started.
def setup(type="fresh"):
    if type == "fresh":
        generate_asymmetric_key()
        generate_symmetric_key()

    symmetric_key = open("SymmetricKeyClient.txt", "rb")
    symmetric_key = symmetric_key.read()
    privkey = open("PrivateKeyClient.pem", "rb")
    privkey = privkey.read()
    pubkey = open("PublicKeyClient.pem", "rb")
    pubkey = pubkey.read()
    symmetric_key_object = get_symmetric_object(symmetric_key)
    return symmetric_key, privkey, pubkey, symmetric_key_object


def connect_symmetric():
    # change this to empty/fresh if you are running it first time
    symmetric_key, privkey, pubkey, symmetric_key_object = setup("fresh")
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect((SERVER_IP, SERVER_PORT))

    # Example of sending "Hello" to server socket
    # sc.send("Hello".encode("UTF-8"))

    # TODO Selesaikan method ini untuk melakukan komunikasi dengan server menggunakan symmetric encryption
    msg = "Halo server!"
    msg_encoded = encode_utf8_before_send(msg)
    sc.send(msg_encoded)

    rep = sc.recv(BUFFER_SIZE)
    rep_decoded = decode_utf8_before_print(rep)
    print(f"Server said: {rep_decoded}")

    key_msg = "Ini Symmetric Keynya:"
    key_encoded = encode_utf8_before_send(key_msg)
    sc.send(key_encoded)

    sc.send(symmetric_key)

    key_rep = sc.recv(BUFFER_SIZE)
    key_rep_decrypted = decrypt_with_symmetric(symmetric_key_object, key_rep)
    print(f"Server said: {key_rep_decrypted}")

    test_msg = "Testing pesan 2006486084"
    test_msg_encrypted = encrypt_with_symmetric(symmetric_key_object, test_msg)
    sc.send(test_msg_encrypted)

    test_rep = sc.recv(BUFFER_SIZE)
    test_rep_decrypted = decrypt_with_symmetric(symmetric_key_object, test_rep)
    print(f"Server said: {test_rep_decrypted}")

    sc.close()


def connect_asymmetric():
    # change this to empty/fresh if you are running it first time
    symmetric_key, privkey, pubkey, symmetric_key_object = setup("rerun")
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect((SERVER_IP, SERVER_PORT))

    # Example of sending "Hello" to server socket
    # sc.send("Hello".encode("UTF-8"))

    # TODO Selesaikan method ini untuk melakukan komunikasi dengan server menggunakan asymmetric encryption
    msg = "Halo Instance Server!"
    msg_encoded = encode_utf8_before_send(msg)
    sc.send(msg_encoded)

    rep = sc.recv(BUFFER_SIZE)
    rep_decoded = decode_utf8_before_print(rep)
    print(f"Server said: {rep_decoded}")

    sc.send(pubkey) # send public key to server
    server_pubkey = sc.recv(BUFFER_SIZE)
    print("Public key server:", server_pubkey)

    key_msg = "Ini Symmetric Keynya:"
    key_encoded = encode_utf8_before_send(key_msg)
    sc.send(key_encoded)

    symmetric_key_encrypted = encrypt_with_asymmetric(server_pubkey, symmetric_key)
    sc.send(symmetric_key_encrypted)

    key_rep = sc.recv(BUFFER_SIZE)
    key_rep_decrypted = decrypt_with_symmetric(symmetric_key_object, key_rep)
    print(f"Server said: {key_rep_decrypted}")

    test_msg = "Testing pesan 2006486084"
    test_msg_encrypted = encrypt_with_symmetric(symmetric_key_object, test_msg)
    sc.send(test_msg_encrypted)

    test_rep = sc.recv(BUFFER_SIZE)
    test_rep_decrypted = decrypt_with_symmetric(symmetric_key_object, test_rep)
    print(f"Server said: {test_rep_decrypted}")

    
    sc.close()


def main():
    print("Starting Client Program.")
    # ganti method connect ke encryption yang sedang dikerjakan
    connect_symmetric()


if __name__ == "__main__":
    main()
