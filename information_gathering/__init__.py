from .gather import WebCrawler, NetworkScanner, ReverseEngineer, SubdomainEnumeration, DirectoryBruteforcer

class InformationGathering:
    def __init__(self, target_url):
        self.web_crawler = WebCrawler(target_url)
        self.network_scanner = NetworkScanner(target_url)
        self.reverse_engineer = ReverseEngineer(target_url)
        self.subdomain_enumeration = SubdomainEnumeration(target_url)
        self.directory_bruteforcer = DirectoryBruteforcer(target_url)
    def crawl(self):
        self.web_crawler.crawl()
    def scan(self):
        self.network_scanner.scan()
    def analyze(self):
        self.reverse_engineer.analyze()
    def enumerate(self):
        self.subdomain_enumeration.enumerate()
    def bruteforce(self):
        self.directory_bruteforcer.bruteforce()

