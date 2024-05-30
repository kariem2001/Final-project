import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

user_agents = [
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36",
    "Mozilla/5.0 (PlayStation; PlayStation 5/2.26) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15",
]

payload = "<mahmoud3x0"

def get_forms(url):
    header = {"User-Agent": user_agents[0]}
    response = requests.get(url, headers=header).content
    soup = BeautifulSoup(response, "html.parser")
    return soup.find_all("form")

def get_form_info(form):
    
    form_info = {}
    form_info["action"] = form.attrs.get("action", "").lower()
    form_info["method"] = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        name_attr = input_tag.attrs.get("name", "")
        id_attr = input_tag.attrs.get("id", "")
        type_attr = input_tag.attrs.get("type", "text")
        inputs.append({"name": name_attr, "id": id_attr, "type": type_attr})

    form_info["inputs"] = inputs
    return form_info


def get_param(url):
    parameter_part = url.split("?")[1]
    parameter_list = parameter_part.split("&")
    return parameter_list

def test_xss(url):
    
    #1 Test on forms parameters for GET & POST Methods
    try:
        forms = get_forms(url)
        i = 0
        for form in forms:
            form_info = get_form_info(form)
            data = {}
            for input_field in form_info["inputs"]:
                if input_field["type"] == "text" or input_field["type"] == "search": #test on text & search forms
                    input_field["value"] = payload
                input_name = input_field.get("name")
                input_value = input_field.get("value")
                if input_name and input_value:
                    data[input_name] = input_value

                    header = {"User-Agent": user_agents[i]}
                    i += 1
                    i %= len(user_agents)
                    endpoint = form_info["action"]
                    target_url = urljoin(url, endpoint)
                    if form_info["method"] == "post":
                        response = requests.post(target_url, data=data, headers=header, allow_redirects=False, timeout=2)
                        if payload in response.text:
                            print(
                                f"XSS Detected at: {target_url} with POST method in {input_field['name']} parameter")
                    else:
                        response = requests.get(target_url, params=data, headers=header, allow_redirects=False, timeout=2)
                        if payload in response.text:
                            print(f"XSS Detected at: {target_url} with GET method in {input_field['name']} parameter")
    except:
        pass


    #2 Test on URL parameters for GET Method
    try:
        i = 0
        for parameter in get_param(url):
            parameter_value = parameter.split("=")[1]
            new_parameter = parameter.replace(parameter_value, payload)
            target_url = url.replace(parameter, new_parameter)
            header = {"User-Agent": user_agents[i]}
            i += 1
            i %= len(user_agents)
            response = requests.get(target_url, allow_redirects=False, headers=header, timeout=2)
            if payload in response.text:
                print(f"XSS Detected at {target_url}")
    except:
        pass
    
    # Make parameter pollution
    try:
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
            if payload in response1.text:
                print(f"XSS Detected with parameter pollution at {target_url1}")
            if payload in response2.text:
                print(f"XSS Detected with parameter pollution at {target_url2}")
    except:
        pass
    
    #3 The payload is injected in path itself as an endpoint
    try:
        i = 0
        for ch in ['/', '#', '~', '../', './', '/.', '/./', ';/', '//', '..;', '..;/', '?',  '%09', '%20', '%5C', '%23', '%00']:
            endpoint = ch + payload
            new_url = url.split("?")[0]
            target_url = urljoin(new_url, endpoint)
            header = {"User-Agent": user_agents[i % len(user_agents)]}
            i += 1
            i %= len(user_agents)
            response = requests.get(target_url, allow_redirects=False, headers=header, timeout=2)
            if payload in response.text:
                print(f"XSS Detected at {target_url}")
    except:
        pass
if __name__ == "__main__":
    url = str(input("URL: "))
    test_xss(url)

# https://xss-game.appspot.com/level1/frame
# http://testphp.vulnweb.com/artists.php
