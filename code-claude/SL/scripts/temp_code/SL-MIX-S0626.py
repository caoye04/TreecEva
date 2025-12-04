# Network device inventory comparison function
# Identifies devices present in only one of two network segments

def analyze_network_segments(segment_a, segment_b):
    # Convert input lists to sets for set operations
    network_devices_a = set(segment_a)
    network_devices_b = set(segment_b)
    
    # Count devices in both segments
    common_devices = len(network_devices_a.intersection(network_devices_b))
    
    # Find devices unique to either segment A or segment B (but not both)
    unique_elements = len(network_devices_a.symmetric_difference(network_devices_b))
    
    # Calculate total unique device count across both segments
    total_devices = len(network_devices_a.union(network_devices_b))
    
    return unique_elements

# Network segment device IDs
segment_a_devices = [101, 103, 105, 107, 109, 111]
segment_b_devices = [102, 104, 106, 108, 109, 111]

# Analyze network segments
result = analyze_network_segments(segment_a_devices, segment_b_devices)
print(f"Result: {result}")