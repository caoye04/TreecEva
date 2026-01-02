def calculate_network_load():
    packet_sizes = [128, 256, 512, 64, 1024, 32, 896, 192]
    threshold = 200
    
    # Filter packets above threshold
    filtered_data = [size for size in packet_sizes if size > threshold]
    
    # Apply efficiency factor (simulates compression)
    efficiency_factor = 0.9
    adjusted_data = [int(size * efficiency_factor) for size in filtered_data]
    
    # Slice to only consider first three large packets
    sample_slice = adjusted_data[:3]
    
    # Calculate total effective load
    total_load = sum(filtered_data)
    
    # Irrelevant metadata (minimal distraction)
    metadata = {'version': '1.2', 'protocol': 'TCP'}
    temp_var = len(metadata['version'])
    
    print(f"Result: {total_load}")

calculate_network_load()