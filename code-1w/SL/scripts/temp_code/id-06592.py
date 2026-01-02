def analyze_data_stream(data_packets):
    base_threshold = 42
    temp_buffer = []
    cumulative_xor = 0
    validation_sum = 0
    
    for packet in data_packets:
        raw_segment = packet.strip().split(':')
        id_tag = raw_segment[0]
        payload = int(raw_segment[1])
        
        # Irrelevant checksum (distractor)
        checksum = sum([ord(c) for c in id_tag]) % 256
        
        if len(id_tag) % 2 == 0:
            adjusted_payload = payload ^ base_threshold
        else:
            adjusted_payload = payload + (base_threshold & 7)
        
        temp_buffer.append(adjusted_payload)
        
        # Semi-relevant transformation
        if adjusted_payload > 50:
            validation_sum += adjusted_payload >> 2

    # Distractor: unused filtering
    filtered_temp = [x for x in temp_buffer if x % 3 != 0]
    
    # Core logic: compute weighted contribution
    weighted_contributions = [
        (i + 1) * val for i, val in enumerate(temp_buffer) if val < 100
    ]
    
    aggregate_total = sum(weighted_contributions)
    
    # Secondary distractor: dead path with misleading name
    if base_threshold > 100:
        aggregate_total *= 2  # Never executed

    return aggregate_total


def calculate_performance_metric(config_id, data_source):
    scaling_factor = 1.75
    offset_bias = -10
    intermediate_result = 0
    
    # Simulate parsing from string-based input
    parsed_data = [
        f"A{chr(65+i)}:{(i*13)+25}" for i in range(len(data_source))
    ]
    
    # Call helper function with side-effect-free processing
    raw_metric = analyze_data_stream(parsed_data)
    
    # Real computation path
    if config_id.startswith('X'):
        intermediate_result = raw_metric * scaling_factor
    elif config_id.startswith('Y'):
        intermediate_result = raw_metric + scaling_factor
    else:
        intermediate_result = raw_metric + 20  # Triggered for 'Z'
    
    # Final adjustment with bitwise mix
    final_score = int((intermediate_result + offset_bias) & ~1)  # Clear LSB
    
    # Print required output
    print(f"Result: {final_score}")
    
    return final_score

# Main execution
input_sequence = ['alpha', 'beta', 'gamma', 'delta']
final_score = calculate_performance_metric('Z99', input_sequence)