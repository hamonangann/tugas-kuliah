import socket
import time

from typing import Tuple


BUFFER_SIZE = 2048
THIS_SERVER_IP = ""
THIS_SERVER_PORT = 12345

ASDOS_SERVER_IP = "34.101.92.60"
ASDOS_SERVER_PORT = 5353

def logic(input: str):
    output_value = {}
    for char in input:
        if char in output_value.keys():
            output_value[char] += 1
        else:
            output_value[char] = 1
    return str(output_value)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sc:
        sc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sc.bind((THIS_SERVER_IP, THIS_SERVER_PORT))

        print("Contoh Socket Server UDP")
        print("Tekan Ctrl/CMD+C untuk menghentikan program")

        while True:
            inbound_message_raw, source_addr = sc.recvfrom(BUFFER_SIZE)
            inbound_message = inbound_message_raw.decode("UTF-8")

            print(f"Menerima input dari {source_addr}: {inbound_message}")

            outgoing_message = logic(inbound_message)
            outgoing_message_raw = outgoing_message.encode("UTF-8")
            sc.sendto(outgoing_message_raw, source_addr)


if __name__ == "__main__":
    main()
