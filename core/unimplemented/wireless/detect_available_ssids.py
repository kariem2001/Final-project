import subprocess

def scan_wifi():
    result = subprocess.run(["netsh", "wlan", "show", "network"], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    scan_wifi()
