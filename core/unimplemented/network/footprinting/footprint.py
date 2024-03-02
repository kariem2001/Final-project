import re
import random
import urllib.request
from urllib.error import HTTPError

url2 = input("Enter the URL: ")
a_tag = "<address>"  # Adjust the regular expression pattern as needed
file_text = open("result.txt", 'a')


while True:  # Use a while loop with break statements for better control flow
    try:
        if not re.match(r'^https?://', url2):
            raise ValueError("Invalid URL format. Please include the scheme (e.g., http://)")
        
        http_r = urllib.request.urlopen(url2)
        content = http_r.read().decode('utf-8')  # Decode content here

        # Print request attributes
        
        print("----------------------------------")
        print("-------------REQUEST-------------:")
        print("----------------------------------")
        print(f"\nMethod: GET")  # Or replace GET with the actual HTTP method you used
        print(f"\nURL: {url2}")

        # Print response headers
        print("\nHEADERS:")
        print("----------------------------------")
        for header, value in http_r.headers.items():
            print(f"\n{header}: {value}")
        print("\n----------------------------------\n")

        if http_r.getcode() == 404:
            file_text.write(f"--------------\n{url2}--------------\n")
            file_text.write(content)
            matches = re.finditer(a_tag, content)
            for match in matches:
                print("Coding is not good")
                print(match.group())  # Print matched content
            break  # Break out of the loop since 404 is found

        elif http_r.getcode() == 200:
            print("\n----------------------------------\n")
            print("Web page is using a custom Error page")
            print("\n----------------------------------\n")
            server_header = http_r.headers.get('Server')
            if server_header:
               print("\n----------------------------------\n")
               print(f"The server is: {server_header}")
               print("\n----------------------------------\n")
            else:
                print("\n----------------------------------\n")
                print("Server information not available")
                print("\n----------------------------------\n")
            break  # Break out of the loop since 200 is found
    except HTTPError as e:
        print(f"HTTP Error {e.code}: {e.reason}")
        break  # Break out of the loop on error

file_text.close()  # Close the file after writing to it