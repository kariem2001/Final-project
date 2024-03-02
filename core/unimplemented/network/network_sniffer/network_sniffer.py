import subprocess

# Prompt the user to enter the interface and initial filter condition
interface = input("Enter interface (e.g., 'eth0'): ").strip()
filter_condition = input("Enter initial filter condition (e.g., 'port 80'): ").strip()

# Start capturing packets with the initial filter condition
tcpdump_cmd = ['tcpdump', '-i', interface, '-nn', '-l', '-v', '-X', filter_condition]
process = subprocess.Popen(tcpdump_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Counter to track the number of packets captured
packet_counter = 0

# Read the output of tcpdump in real-time
while True:
    # Read a line from tcpdump output
    output = process.stdout.readline().decode().strip()
    
    # Process the captured packet
    if output:
        # Increment the packet counter
        packet_counter += 1
        
        # Implement your packet processing logic here
        print(output)
        
        # Check if it's time to ask the user for input (e.g., after 20 packets)
        if packet_counter % 50 == 0:
            valid_input = False
            while not valid_input:
                # Prompt the user to choose an action (apply, remove, modify filter, or continue without changes)
                user_input = input("Do you want to apply, remove, modify filter, or continue without changes? (apply/remove/modify/continue): ").strip().lower()
                if user_input == 'apply':
                    # Apply the initial filter condition
                    print(f"Applying initial filter: {filter_condition}")
                    valid_input = True
                elif user_input == 'remove':
                    # Remove the filter condition
                    print("Removing filter.")
                    filter_condition = ''  # Empty filter condition
                    valid_input = True
                elif user_input == 'modify':
                    # Modify the filter condition
                    filter_condition = input("Enter new filter condition: ").strip()
                    valid_input = True
                elif user_input == 'continue':
                    valid_input = True
                else:
                    print("Invalid input. Please enter 'apply', 'remove', 'modify', or 'continue'.")

            # Update the tcpdump command with the new filter condition
            tcpdump_cmd = ['tcpdump', '-i', interface, '-nn', '-l', '-v', '-X', filter_condition]
            process.kill()  # Kill the current tcpdump process
            
            # Start a new tcpdump process with the updated filter condition
            process = subprocess.Popen(tcpdump_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Wait for the tcpdump process to finish
process.wait()