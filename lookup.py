import requests
import json

# Set input and output file names
input_file = 'ip.txt'
output_file = 'geolocation_output.txt'

# Set batch size
batch_size = 75

# Open input and output files
with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
    # Read IP addresses from input file
    ip_list = f_in.read().splitlines()
    
    # Process IP addresses in batches
    for i in range(0, len(ip_list), batch_size):
        # Get current batch of IP addresses
        batch = ip_list[i:i+batch_size]
        
        # Get geolocation data for batch of IP addresses
        response = requests.post('http://ip-api.com/batch', json=batch)
        data = json.loads(response.text)
        
        # Write geolocation data to output file
        for j, ip_data in enumerate(data):
            ip = batch[j]
            f_out.write(f'{ip}: {ip_data}\n')
        
        # Print status
        print(f'{i + len(batch)} IPs done')
