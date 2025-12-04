from collections import Counter

def analyze_network_packets():
    packet_sizes = [512, 1024, 768, 512, 1024, 512, 768, 1024, 512, 1536]
    packet_counter = Counter(packet_sizes)
    
    # Main processing calculations
    total_bytes = sum(packet_sizes)
    avg_packet_size = total_bytes // len(packet_sizes)
    
    # Some intermediate calculations (distractors)
    size_variance = max(packet_sizes) - min(packet_sizes)
    common_size_count = packet_counter.most_common(1)[0][1]
    
    # Processing steps with some irrelevant operations
    processed_total = total_bytes - (avg_packet_size * 2)
    adjustment_factor = common_size_count * 10
    modulus_base = 256
    
    # Key calculation - this determines the final output
    result_modulus = (processed_total + adjustment_factor) % modulus_base
    
    # More distractor operations that don't affect the result
    temp_buffer = [size for size in packet_sizes if size > 800]
    unused_metric = len(temp_buffer) * size_variance
    
    final_output = result_modulus
    print(f"Result: {final_output}")
    return final_output

# Execute the function
final_result = analyze_network_packets()