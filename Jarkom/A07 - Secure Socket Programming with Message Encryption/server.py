#!/usr/bin/env python

import socket
import threading
from typing import Tuple

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from nacl.public import PrivateKey, SealedBox, PublicKey

SERVER_NAME = ""
SERVER_IP = "10.128.0.7"
SERVER_PORT = 6084
BUFFER_SIZE = 2048
BLOCK_SIZE = 32


def generate_asymmetric_key():
    private_key = PrivateKey.generate()
    file_out = open("PrivateKeyServer.pem", "wb")
    file_out.write(bytes(private_key))
    file_out.close()

    public_key = private_key.public_key
    file_out = open("PublicKeyServer.pem", "wb")
    file_out.write(bytes(public_key))
    file_out.close()


def generate_symmetric_key():
    sym_key = get_random_bytes(BLOCK_SIZE)
    file_out = open("SymmetricKeyServer.txt", "wb")
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
    if (type == "fresh"):
        generate_asymmetric_key()
        generate_symmetric_key()

    symmetric_key = open("SymmetricKeyServer.txt", "rb")
    symmetric_key = symmetric_key.read()
    privkey = open("PrivateKeyServer.pem", "rb")
    privkey = privkey.read()
    pubkey = open("PublicKeyServer.pem", "rb")
    pubkey = pubkey.read()
    symmetric_key_object = get_symmetric_object(symmetric_key)
    return symmetric_key, privkey, pubkey, symmetric_key_object


def socket_handler_symmetric(connection: socket.socket, address: Tuple[str, int]):
    print(f"Receive connection from {address}")

    # TODO Selesaikan method ini untuk mengirim pesan dengan symmetric encryption
    input_value_bytes = connection.recv(BUFFER_SIZE)
    input_value = decode_utf8_before_print(input_value_bytes)
    print(f"Client said: {input_value}")

    msg = "Halo juga client!"
    msg_encoded = encode_utf8_before_send(msg)
    connection.send(msg_encoded)

    key_msg_bytes = connection.recv(BUFFER_SIZE)
    key_msg = decode_utf8_before_print(key_msg_bytes)
    print(f"Client said: {key_msg}")

    key = connection.recv(BUFFER_SIZE)
    print(key)

    cipher = get_symmetric_object(key)
    rep = "Symmetric Key Diterima"
    rep_encrypted = encrypt_with_symmetric(cipher, rep)
    connection.send(rep_encrypted)

    test_msg = connection.recv(BUFFER_SIZE)
    test_msg_decrypted = decrypt_with_symmetric(cipher, test_msg)
    print(f"Client said: {test_msg_decrypted}")

    test_rep = "Terima pesan 2006486084"
    test_rep_encrypted = encrypt_with_symmetric(cipher, test_rep)
    connection.send(test_rep_encrypted)
    connection.close()

def socket_handler_asymmetric(connection: socket.socket, address: Tuple[str, int]):
    symmetric_key, privkey, pubkey, symmetric_key_object = setup("fresh")
    
    print(f"Receive connection from {address}")

    # TODO Selesaikan method ini untuk mengirim pesan dengan asymmetric encryption
    input_value_bytes = connection.recv(BUFFER_SIZE)
    input_value = decode_utf8_before_print(input_value_bytes)
    print(f"Client said: {input_value}")

    msg = "Halo juga Instance Client!"
    msg_encoded = encode_utf8_before_send(msg)
    connection.send(msg_encoded)

    client_pubkey = connection.recv(BUFFER_SIZE)
    print("Public key client:", client_pubkey)
    connection.send(pubkey)

    key_msg_bytes = connection.recv(BUFFER_SIZE)
    key_msg = decode_utf8_before_print(key_msg_bytes)
    print(f"Client said: {key_msg}")

    key = connection.recv(BUFFER_SIZE)
    key_decrypted = decrypt_with_asymmetric(privkey, key)

    rep = "Symmetric Key Diterima"
    cipher = get_symmetric_object(key_decrypted)
    rep_encrypted = encrypt_with_symmetric(cipher, rep)
    connection.send(rep_encrypted)

    test_msg = connection.recv(BUFFER_SIZE)
    test_msg_decrypted = decrypt_with_symmetric(cipher, test_msg)
    print(f"Client said: {test_msg_decrypted}")

    test_rep = "Terima pesan 2006486084"
    test_rep_encrypted = encrypt_with_symmetric(cipher, test_rep)
    connection.send(test_rep_encrypted)

    connection.close()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.bind((SERVER_NAME, SERVER_PORT))
        sc.listen(0)

        print("Multithreading Socket Server Program")
        print("Hit Ctrl+C to terminate the program")

        while True:
            connection, address = sc.accept()
            # ganti handler ke tipe socket yang sedang dikerjakan
            thread = threading.Thread(target=socket_handler_asymmetric, args=(connection, address))
            thread.start()


if __name__ == "__main__":
    main()
