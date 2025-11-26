def analyze_network_traffic(packet_data):
    # Initialize base metrics
    packet_sizes = [1500, 512, 1024, 768, 2048, 256, 1536, 384]
    
    # Calculate relevant statistics (distractor)
    total_packets = len(packet_sizes)
    max_packet = max(packet_sizes)
    min_packet = min(packet_sizes)
    
    # Core processing with slicing and list comprehension
    selected_packets = packet_sizes[2:6]
    processed_sizes = [size * 0.8 for size in selected_packets]
    
    # Calculate average with some intermediate steps
    size_sum = sum(processed_sizes)
    temp_avg = size_sum / len(processed_sizes)
    
    # Distractor operations that don't affect final result
    dummy_calc = (max_packet + min_packet) * 1.5
    formatted_ratio = round(dummy_calc / 1000, 2)
    
    # Key calculation path
    processed_result = round(size_sum - temp_avg * 2, 1)
    adjustment_factor = 1.25
    
    # Final computation that uses the target variable
    final_calculation = processed_result * adjustment_factor
    
    print(f"Target result: {processed_result}")
    return processed_result

# Execute the analysis
analyze_network_traffic([])