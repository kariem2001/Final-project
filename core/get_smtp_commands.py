import telnetlib
import socket

def is_port_open(host, port):
    try:
        # Create a socket object and attempt to connect to the host and port
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Adjust the timeout as needed
            result = s.connect_ex((host, port))
            return result == 0  # Port is open if the result is 0
    except Exception as e:
        print(f"Error checking port: {e}")
        return False
    
def get_smtp_commands(mail_server, port=25):
    if not is_port_open(mail_server, port):
        print(f"Port {port} is not open.")
        return
    try:
        tn = telnetlib.Telnet(mail_server, port)
        tn.read_until(b"220")  # Wait for the server to send the initial greeting

        tn.write(b"EHLO example.com\r\n") 
        tn.write(b"EHLO\r\n")
         # Send an EHLO (or HELO) command to identify yourself
        response = tn.read_until(b"250 ")  # Wait for the server's response

        if b"250" in response:
            # The server has accepted the EHLO command, and it should provide a list of supported commands.
            response = response.decode('utf-8')
            print(response)  # Print the EHLO response, which includes available commands.

            

        tn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    mail_server = input("Enter the mail server hostname or IP address: ")
    port_input = input("Enter the port number (press Enter for the default port 25): ")

    if port_input.strip():  # Check if the user provided a port number
        try:
            port = int(port_input)
        except ValueError:
            print("Invalid port number. Using the default port 25.")
            port = 25
    else:
        port = 25  # Default to port 25
    get_smtp_commands(mail_server, port)

