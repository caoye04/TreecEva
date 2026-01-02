def calculate_performance(data):
    # Preprocessing phase with distractor computations
    temp_offsets = [d % 7 for d in data]
    magnitude_factor = sum(d ** 0.5 for d in data if d > 10)
    adjustment = len([x for x in temp_offsets if x > 4]) * 1.5
    
    # Core logic embedded within noise
    filtered = [x for x in data if x % 2 == 1]  # Only odd values contribute
    base_score = sum(filtered) / len(filtered) if filtered else 0
    
    # Distractor: irrelevant statistical measures
    peak = max(data)
    spread = min(data) * 0.1
    entropy_proxy = 0
    for i in range(len(data)):
        if i % 3 == 0:
            entropy_proxy += (data[i] + adjustment) / (i + 1)

    # Conditional scaling based on string-derived threshold
    mode_flag = 'high' if sum(temp_offsets) > 10 else 'low'
    scale = 2.5 if 'h' in mode_flag else 1.0
    
    # Actual performance calculation with dependency on prior steps
    deviation_penalty = sum(abs(base_score - x) for x in filtered) / len(filtered)
    final_score = (base_score * scale) - deviation_penalty
    
    # Red herring: unused transformation chain
    transformed = ''.join([chr(97 + (d % 26)) for d in data])
    checksum = sum(ord(c) - 96 for c in transformed if c in 'aeiou')
    
    return final_score

# Input data with semantic meaning (simulated sensor readings)
data_sequence = [12, 15, 22, 19, 8, 33, 14, 27]
offset_correction = sum(x * 2 for x in data_sequence if x < 15)  # Irrelevant precomputation
benchmark_data = [x + (x % 4) for x in data_sequence]  # Modified input
intermediate_stats = {"count": len(benchmark_data), "floor": min(benchmark_data)}

# Key execution point
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")