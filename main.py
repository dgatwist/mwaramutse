import argparse
import platform
import sys
from random import choice
from rich.columns import Columns
from rich.text import Text
from information_gathering import WebCrawler, NetworkScanner, ReverseEngineer, SubdomainEnumeration, DirectoryBruteforcer
from networking import Networking
from obfuscation import Encoder, Compressor, Encryptor, PayloadGenerator
from passwords import Passwords
from web_apps import Web_apps



# Menu
TERMS = """
I shall not use mwaramutse to:
(i) upload or otherwise transmit, display or distribute any
content that infringes any trademark, trade secret, copyright
or other proprietary or intellectual property rights of any
person; (ii) upload or otherwise transmit any material that contains
software viruses or any other computer code, files or programs
designed to interrupt, destroy or limit the functionality of any
computer software or hardware or telecommunications equipment;
"""

                                                                                      

BANNER4 = r"""




 ██████   ██████ █████   ███   █████   █████████   ███████████     █████████   ██████   ██████ █████  █████ ███████████  █████████  ██████████
░░██████ ██████ ░░███   ░███  ░░███   ███░░░░░███ ░░███░░░░░███   ███░░░░░███ ░░██████ ██████ ░░███  ░░███ ░█░░░███░░░█ ███░░░░░███░░███░░░░░█
 ░███░█████░███  ░███   ░███   ░███  ░███    ░███  ░███    ░███  ░███    ░███  ░███░█████░███  ░███   ░███ ░   ░███  ░ ░███    ░░░  ░███  █ ░ 
 ░███░░███ ░███  ░███   ░███   ░███  ░███████████  ░██████████   ░███████████  ░███░░███ ░███  ░███   ░███     ░███    ░░█████████  ░██████   
 ░███ ░░░  ░███  ░░███  █████  ███   ░███░░░░░███  ░███░░░░░███  ░███░░░░░███  ░███ ░░░  ░███  ░███   ░███     ░███     ░░░░░░░░███ ░███░░█   
 ░███      ░███   ░░░█████░█████░    ░███    ░███  ░███    ░███  ░███    ░███  ░███      ░███  ░███   ░███     ░███     ███    ░███ ░███ ░   █
 █████     █████    ░░███ ░░███      █████   █████ █████   █████ █████   █████ █████     █████ ░░████████      █████   ░░█████████  ██████████
░░░░░     ░░░░░      ░░░   ░░░      ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░     ░░░░░   ░░░░░░░░      ░░░░░     ░░░░░░░░░  ░░░░░░░░░░ 
                                                                                                                                              
                                                                                                                                              
                                                                                                                                              
                                                                     
                                                                     
                                                                     
"""

def main():
    # Display terms and conditions
    print(BANNER4)
    print(TERMS)
    # Ask user to accept terms and conditions
    accept_terms = input("Do you accept the terms and conditions? (yes/no): ")
    if accept_terms != "yes":
        sys.exit("Terms and conditions not accepted.")
    
    # Get target url or ip from user
    target_url = input("Enter the target URL or IP: ")
    if not target_url:
        sys.exit("Invalid target URL or IP.")

    # Show menu and ask user to select a module
    modules = ["1. Information Gathering", "2. Networking", "3. Obfuscation", "4. Passwords", "5. Web Applications", "5. All"]
    selected_module = input(Text("Select a module:") + "\n" + "\n".join(modules) + "\n")
    if selected_module == "6":
        # Run all modules
        information_gathering = WebCrawler(target_url)
        information_gathering.crawl()
        
        information_gathering = NetworkScanner(target_url)
        information_gathering.scan()
       
        information_gathering = ReverseEngineer(target_url)
        information_gathering.analyze()
        
        information_gathering = SubdomainEnumeration(target_url)
        information_gathering.enumerate()
        
        information_gathering = DirectoryBruteforcer(target_url)
        information_gathering.bruteforce()


        networking = Networking(target_url)
        networking.brute_force()
        networking.sql_injection()
        networking.xss()
        
        obfuscation = PayloadGenerator()
        payload=obfuscation.generate_payload()

        obfuscation = Encoder(payload)
        obfuscation.base64_encode()
       
        encryption_key = input("Enter an encryption key: ")
        obfuscation = Encryptor(payload, encryption_key)
        obfuscation.aes_encrypt()
        obfuscation = Compressor(payload)
        obfuscation.deflate()

        passwords = Passwords(target_url)
        passwords.generate_dictionary()
        passwords.dictionary_attack()
        passwords.rule_based_attack()

        web_apps = Web_apps(target_url)
        #web_apps.input_validation()
        web_apps.output_encoding()
        web_apps.access_control()
        
    elif selected_module == "1":
        
        information_gathering = WebCrawler(target_url)
        information_gathering.crawl()
        
        information_gathering = NetworkScanner(target_url)
        information_gathering.scan()
       
        information_gathering = ReverseEngineer(target_url)
        information_gathering.analyze()
        
        information_gathering = SubdomainEnumeration(target_url)
        information_gathering.enumerate()
        
        information_gathering = DirectoryBruteforcer(target_url)
        information_gathering.bruteforce()
    elif selected_module == "2":
        networking = Networking(target_url)
        networking.brute_force()
        networking.sql_injection()
        networking.xss()
        
    elif selected_module == "3":
      
        
        obfuscation = PayloadGenerator()
        payload=obfuscation.generate_payload()

        obfuscation = Encoder(payload)
        obfuscation.base64_encode()
       
        encryption_key = input("Enter an encryption key: ")
        obfuscation = Encryptor(payload, encryption_key)
        obfuscation.aes_encrypt()
        obfuscation = Compressor(payload)
        obfuscation.deflate()
        
    elif selected_module == "4":
        
        passwords = Passwords(target_url)
        passwords.generate_dictionary()
        passwords.dictionary_attack()
        passwords.rule_based_attack()
        
    elif selected_module == "5":
        web_apps = Web_apps(target_url)
        #web_apps.input_validation()
        web_apps.output_encoding()
        web_apps.access_control()
    else:
        sys.exit("Invalid choice.")

if __name__ == "__main__":
    main()
