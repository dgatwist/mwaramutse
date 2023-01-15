import subprocess
import sys
import requests

class Web_apps:
    def __init__(self, url):
        self.url = url
   
    def input_validation(self):
     
        with open("input-validation.txt", "r") as f:
            
            for payload in f:
                payload = payload.strip()
                try:
                    r = requests.get(self.url + payload)
                    if r.status_code != 404:
                        print(f"Possible input validation vulnerability found with payload: {payload}")
                except requests.exceptions.RequestException as e:
                    print(e)
                    sys.exit(1)

    def output_encoding(self):
        payloads = ["<script>alert(1)</script>", "<img src=x onerror=alert(1)>", "<svg/onload=alert(1)>"]
        for payload in payloads:
            try:
                r = requests.get(self.url, params={'payload': payload})
                if payload in r.text:
                    print(f"Possible output encoding vulnerability found with payload: {payload}")
            except requests.exceptions.RequestException as e:
                print(e)
                sys.exit(1)

    def access_control(self):
        subprocess.run(["arjun", "-u", self.url])
