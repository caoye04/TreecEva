def analyze_network_traffic(packets):
    # Initialize counters
    processed = 0
    filtered = 0
    priority_count = 0
    secondary_count = 0
    
    for packet in packets:
        # Some packets are processed, some filtered out
        if packet % 3 == 0:
            filtered += 1
            continue
        
        processed += 1
        
        # Priority classification based on packet characteristics
        if packet > 15 and packet < 35:
            priority_count += packet % 7
        else:
            secondary_count += packet % 5
        
        # Distractor: this calculation doesn't affect final result
        temp_metric = (packet * 2) - (packet // 2)
    
    # Core logic: calculate final value
    base_value = priority_count * 3 + secondary_count * 2
    adjustment = len([p for p in packets if p % 4 == 0]) - 1
    final_value = base_value - adjustment
    
    # Distractor: unused intermediate calculation
    efficiency_ratio = processed / len(packets) if packets else 0
    
    return final_value

data_packets = [8, 12, 19, 24, 31, 42, 17, 28, 33, 20]
result = analyze_network_traffic(data_packets)
print(f"Result: {result}")