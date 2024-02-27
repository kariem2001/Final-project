import socket

def banner(ip, port):
    s = socket.socket()
    s.settimeout(10)  # Increase the timeout to 10 seconds
    try:
        s.connect((ip, int(port)))
        print(str(s.recv(2048)))
    except TimeoutError:
        print("Connection timed out. Please check the server or try again later.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        s.close()

def main(): 
    ip = input("Please enter the IP: ")
    port = input("Please enter the port: ")
    banner(ip, port)

if __name__ == "__main__":
    main()