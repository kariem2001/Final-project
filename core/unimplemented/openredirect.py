import requests
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode


def replace_param(url, param_name, new_value):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    if param_name in query_params:
        query_params[param_name] = new_value
        updated_query = urlencode(query_params, doseq=True)
        updated_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path,
                                 parsed_url.params, updated_query, parsed_url.fragment))
        return updated_url
    else:
        return url


def replace_params(url):
    params_to_replace = ['path', 'link', 'next', 'ret', 'page',
                         'r2', 'url', 'page', 'toredirect', 'forward', 'redirect']
    new_value = 'http://google.com'
    updated_url = url
    for param_name in params_to_replace:
        updated_url = replace_param(updated_url, param_name, new_value)
    return updated_url


def check_redirects(url):
    redirects = []
    final_url = None

    try:
        response = requests.get(url, allow_redirects=False)
        status_code = response.status_code
        final_url = response.url

        while response.is_redirect:
            new_location = response.headers['Location']
            redirects.append((status_code, response.url))
            response = requests.get(new_location, allow_redirects=False)
            status_code = response.status_code

        # Append the final destination
        redirects.append((status_code, response.url))

    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

    return redirects, final_url


def main():
    url = input("Enter the URL to check redirects: ")

    updated_url = replace_params(url)

    redirects, final_url = check_redirects(updated_url)

    url1 = updated_url  # Initialize url1 with the updated URL

    print("\nChain of redirects:")
    for status_code, redirect_url in redirects:
        print(f"Status Code: {status_code}, URL: {redirect_url}")
        if status_code == 200:
            url1 = redirect_url  # Update url1 only if status code is 200
            print(f"url: {url1}")

    print("\nFinal Destination URL:", url1)
    if url1 != updated_url:
        print("has openredirect vuln")
    else:
        print("has not openredirect vuln")


if __name__ == "__main__":
    main()
