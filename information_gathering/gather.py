import subprocess

import os
class WebCrawler:
    
    def __init__(self, starting_url):
        self.starting_url = starting_url

    def crawl(self):
        print("\033[1;32;40m Crawl\033[m")
        subprocess.run(["photon", "-u", self.starting_url])
       

        result_dir = self.starting_url

        if os.path.exists(result_dir):
            # Get the list of files in the directory
            files = os.listdir(result_dir)
            for file in files:
                print("\033[1;32;40m Reading contents of \033[m",file)
               
                # Open each file and read its contents
                with open(os.path.join(result_dir, file), 'r') as f:
                    contents = f.read()
                    # Print the contents of the file
                    print(contents)
        else:
            print(f"{result_dir} not found.")





class NetworkScanner:
    def __init__(self, target_host):
        self.target_host = target_host

    def scan(self):
        print("\033[1;32;40m Port Scan \033[m")
        subprocess.run(["nmap", self.target_host])

class ReverseEngineer:
    def __init__(self, target_url):
        self.target_url = target_url

    def analyze(self):
        print("\033[1;32;40m Source Code Scan \033[m")
        tool_name = "nikto"
        url="http://"+self.target_url
        subprocess.run([tool_name, "-h",url])

class SubdomainEnumeration:
    def __init__(self, target_host):
        self.target_host = target_host
        
    def enumerate(self):
        print("\033[1;32;40m Subdomain Enumeration \033[m")
        subprocess.run(["nmap", "-sn","--script","hostmap-crtsh", self.target_host])
            
class DirectoryBruteforcer:
    def __init__(self, target_url):
        self.target_url = target_url
    
    def bruteforce(self):
        print("\033[1;32;40m Directory Bruteforcing \033[m")
        subprocess.run(["feroxbuster", "-u", self.target_url])
