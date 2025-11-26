def calculate_network_efficiency(base_rate, overhead_factor, buffer_size):
    # Relevant calculations
    raw_throughput = base_rate * (1 - overhead_factor)
    buffer_efficiency = min(buffer_size * 0.1, 1.0)
    
    # Distractor variables and computations
    temp_calc = (base_rate % 7) ** 2  # Irrelevant modulo operation
    unused_metric = buffer_size * overhead_factor + temp_calc  # Dead code path
    
    if buffer_size > 50:
        # Misleading conditional path
        adjustment = raw_throughput * 0.15
        dummy_value = adjustment + temp_calc  # Unused result
    else:
        adjustment = raw_throughput * 0.05
    
    # Core logic
    optimized_rate = raw_throughput * buffer_efficiency - adjustment
    efficiency_factor = 1.2 if overhead_factor < 0.3 else 0.8
    
    # More distractors
    alternate_calc = optimized_rate + buffer_size // 10  # Unused integer division
    correction_offset = -5 if base_rate > 200 else 10
    
    # Dead code section
    for i in range(3):
        temp_val = i * correction_offset  # Unused loop result
    
    # Final assignment (critical execution point)
    final_throughput = optimized_rate * efficiency_factor + correction_offset
    
    print(f"Result: {final_throughput}")
    return final_throughput

# Execute with test parameters
base_network_rate = 180
protocol_overhead = 0.25
packet_buffer = 40
result = calculate_network_efficiency(base_network_rate, protocol_overhead, packet_buffer)