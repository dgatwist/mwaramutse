import subprocess

class Passwords:
    def __init__(self, url):
        self.url = url
        
    def generate_dictionary(self):
        print("\033[1;32;40m Generation of dictionary \033[m")
        print("Select a dictionary generation tool:")
        print("1. CUPP")
        print("2. Crunch")
        choice = input()

        if choice == "1":
            subprocess.run(["cupp", "-i", "-q"])
        elif choice == "2":
            length = input("Enter the length of characters:")
            charset = input("Enter the charset to use:")
            output_file = input("Enter the output file name:")
            subprocess.run(["crunch", length, length, charset, "-o", output_file])
        else:
            print("Invalid choice")
            return None
        

    def dictionary_attack(self):
    
            print("\033[1;32;40m Dictionary attack using hydra \033[m")
            url=input("Enter the url of the login page: ")
            login_path = input("Enter the login path (e.g. /login/index.php:username=^USER^&password=^PASS^:F=incorrect): ")
            username = input("Enter the username to use (default is admin): ") or "admin"
            passwordfile= input("Enter the dictionnary file you want to use e.g: password.txt ( Default is rockyou.txt):") or "rockyou.txt"
            subprocess.run(["hydra", "-l", username, "-P", passwordfile, url, "-V", "http-post-form", f"{login_path}"])

    def rule_based_attack(self):
        print("\033[1;32;40m Rule based attack using medusa \033[m")
        host=input("Enter the target host name or IP: ")
        module=input("Enter the name of the module e.g; http, ftp: ")
        username = input("Enter the username to use (default is admin): ") or "admin"
        passwordfile= input("Enter the dictionnary file you want to use e.g: password.txt (default is rockyou.txt):") or "rockyou.txt"
    	
        subprocess.run(["medusa", "-h", host, "-u", username, "-P", passwordfile, "-M", module])
