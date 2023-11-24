import telnetlib
def get_smtp_commands(mail_server, port=25):

    try:
       
        tn = telnetlib.Telnet(mail_server, port)
          # Wait for the server to send the initial greeting

        tn.write(f"VRFY root\r\n".encode("utf-8"))
        tn.write(b"EHLO\r\n")
        response = tn.read_until(b"501")  # Wait for the server's response

        if b"252" in response:
                # The server has accepted the VRFY command, and it should provide a list of supported commands.
                response = response.decode('utf-8')
                print(response)  # Print the VRFY response, which includes available commands.
        tn.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    mail_server = input("Enter the mail server hostname or IP address: ")
    get_smtp_commands(mail_server, 25)