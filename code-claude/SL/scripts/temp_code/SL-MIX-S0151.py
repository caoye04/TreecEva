from collections import Counter

# Analyzing frequency patterns in network traffic data
def analyze_network_packets(packet_data, threshold=15):
    # Initialize counters
    total_packets = len(packet_data)
    filtered_packets = [p for p in packet_data if p > 0]
    
    # Calculate baseline metrics (not directly used in final result)
    baseline_avg = sum(packet_data) / total_packets if total_packets else 0
    variance = sum((p - baseline_avg) ** 2 for p in packet_data) / total_packets
    
    # Process packet frequencies
    packet_counter = Counter(filtered_packets)
    
    # Extract valid samples based on threshold
    valid_samples = []
    excluded_samples = []
    
    for size, count in packet_counter.items():
        # Apply modular arithmetic to determine validity
        if (size % threshold) < threshold // 2:
            valid_samples.extend([size] * count)
        else:
            excluded_samples.extend([size] * count)
    
    # Calculate frequency distribution of valid samples
    frequencies = Counter(valid_samples)
    valid_frequencies = [count for _, count in frequencies.items()]
    valid_frequencies.sort(reverse=True)
    
    # Track some statistics for analysis
    total_valid_samples = len(valid_samples)
    excluded_ratio = len(excluded_samples) / total_packets if total_packets else 0
    
    # Find the majority index using conditional expression
    majority_index = 0 if not valid_frequencies else (1 if len(valid_frequencies) > 1 and 
                                                     valid_frequencies[1] > valid_frequencies[0] // 2 else 0)
    
    # Calculate optimal ratio
    optimal_ratio = valid_frequencies[majority_index] / total_valid_samples
    
    # Calculate alternative metrics (distractors)
    alt_ratio = sum(valid_frequencies) / total_packets if total_packets else 0
    weighted_score = sum(k * v for k, v in zip(range(1, len(valid_frequencies) + 1), valid_frequencies))
    
    print(f"Result: {optimal_ratio}")
    return optimal_ratio

# Test with sample data
packet_sizes = [32, 64, 32, 128, 32, 64, 96, 32, 64, 128, 32, 96, 64, 32, 32, 64, 128, 96]
result = analyze_network_packets(packet_sizes)