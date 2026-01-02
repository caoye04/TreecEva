from collections import Counter

def calculate_network_capacity(masks):
    capacity = 0
    for mask in masks:
        prefix_length = int(mask.split('/')[1])
        host_bits = 32 - prefix_length
        # Usable addresses = 2^host_bits - 2 (subtract network and broadcast)
        usable_addresses = (2 ** host_bits) - 2 if host_bits > 1 else 1
        capacity += usable_addresses
    return capacity

def analyze_traffic_patterns(log_lines):
    # Dummy function to simulate unrelated analysis
    freq = Counter()
    for line in log_lines:
        ip = line.split()[0]
        if ':' not in ip:  # IPv4 only
            freq[ip] += 1
    return freq

def main():
    subnet_masks = ['192.168.1.0/24', '10.0.0.0/28', '172.16.0.0/16']
    total_capacity = 0
    temp_result = [len(mask) for mask in subnet_masks]  # Irrelevant computation
    
    total_capacity = calculate_network_capacity(subnet_masks)
    
    # Additional unrelated check
    valid = all('/' in mask for mask in subnet_masks)
    return total_capacity

result = main()
print(f"Result: {result}")