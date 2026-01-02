from collections import defaultdict

def calculate_network_load(log):
    frequency = defaultdict(int)
    for entry in log:
        frequency[entry['node']] += 1
    
    base_load = 0
    for count in frequency.values():
        if count > 2:
            base_load += count * 3
        else:
            base_load += count * 2
    
    checksum = 0
    for i, val in enumerate(frequency.values()):
        checksum += (i + 1) * val  # Irrelevant computation
    
    return base_load

# Simulated transmission data
data_log = [
    {'node': 'A', 'signal': 'OK'},
    {'node': 'B', 'signal': 'OK'},
    {'node': 'A', 'signal': 'RETRY'},
    {'node': 'C', 'signal': 'OK'},
    {'node': 'A', 'signal': 'OK'},
    {'node': 'B', 'signal': 'ERROR'},
    {'node': 'C', 'signal': 'OK'},
    {'node': 'D', 'signal': 'OK'},
    {'node': 'C', 'signal': 'OK'}
]

initial_offset = 5  # Unused variable (minor distraction)
temp_result = sum(len(data_log) % 3 for _ in range(2))  # Slight interference

total_load = calculate_network_load(data_log)
print(f"Result: {total_load}")