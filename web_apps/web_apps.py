import subprocess
import sys
import requests
import os
import socket

class Web_apps:
    def __init__(self, url):
        self.url = url

    def launch_utility(self):
        utilities = {
            "sherlock": "Sherlock is a utility that can be used to find usernames across a number of social media platforms.",
            "host2ip": "Host2ip is a utility that can be used to resolve hostnames to IP addresses.",
            
            "cr3dov3r": "Your best friend in credential reuse attacks.",
            "exit": "Exit the program."
        }

        while True:
            print("Select a utility to launch:")
            for i, (name, description) in enumerate(utilities.items(), 1):
                print(f"{i}. {name} - {description}")

            selection = input("Enter the number of your selection: ")

            try:
                selection = int(selection)
                if selection < 1 or selection > len(utilities):
                    raise ValueError
            except ValueError:
                print("Invalid selection. Please enter a valid number.")
                continue

            utility_name = list(utilities.keys())[selection - 1]
            if utility_name == "exit":
                break
            elif utility_name == "sherlock":
                user_usernames = input("\nEnter a username: ")
               
                subprocess.run(["sherlock",user_usernames])
            elif utility_name == "host2ip":
                hostname = input("Enter the hostname to resolve: ")
                try:
                    ip = socket.gethostbyname(hostname)
                    print(f"{hostname} resolved to {ip}")
                except socket.gaierror:
                    print(f"Could not resolve hostname: {hostname}")
                
              
            elif utility_name == "cr3dov3r":
                path = "Cr3dOv3r/"
                script = "Cr3d0v3r.py"
                user_email = input("\nEnter a email: ").strip()
                os.system(f"python3 {os.path.join(path, script)} {user_email}")


            else:
                print("Invalid selection. Please enter a valid number.")
