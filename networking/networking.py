import subprocess
import os

class Networking:
    def __init__(self, url):
        self.url = url

    def brute_force(self):
        login_page = input("Enter the login page URL: ")
        path = input("Enter the path of the login page( Example /login/index.php:username=^USER^&password=^PASS^:F=incorrect login): ")
        username = input("Enter the username (default is admin): ") or "admin"
        use_password_generator = input("Do you want to generate a password list? (yes/no): ")
        if use_password_generator.lower() == "yes":
            subprocess.run(["cupp", "-i","-q"])
            cupp_file_name = input("Enter the file name generated: ")
            password_list = cupp_file_name
       
        else:
            password_list = "rockyou.txt"

        subprocess.run(["hydra", "-l", username, "-P", password_list, login_page, "-v", "http-post-form", f"{path}"])


    def sql_injection(self):
        url = input("Please enter a URL: ")
        subprocess.run(["sqlmap", "-u", url, "--wizard"])


    def xss(self):
        url = input("Enter the URL: ")
        subprocess.run(["xsstrike", "-u", url])

        
    def get_xss_results(self):
        output = subprocess.check_output(["xsstrike", "-u", self.url])
        return output.decode()

