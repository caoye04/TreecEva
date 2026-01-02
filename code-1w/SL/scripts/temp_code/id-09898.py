def calculate_performance(data):
    # Preprocessing: filter valid entries
    valid_entries = list(filter(lambda x: x['runtime'] > 0 and x['memory'] < 1000, data))
    
    # Irrelevant transformation (distractor)
    temp_offsets = [entry['runtime'] * 0.1 for entry in data]
    offset_sum = sum(temp_offsets)  # Not used later
    
    # Extract execution times and apply weighting via lambda
    weights = map(lambda e: 0.7 if e['optimized'] else 1.0, valid_entries)
    weighted_times = [e['runtime'] * w for e, w in zip(valid_entries, weights)]
    
    # Compute harmonic mean (performance metric)
    if not weighted_times:
        return 0
    
    reciprocal_sum = sum(1 / t for t in weighted_times)
    harmonic_mean = len(weighted_times) / reciprocal_sum
    
    # Simulate adjustment based on memory footprint
    total_memory = sum(e['memory'] for e in valid_entries)
    efficiency_bonus = 100 // (total_memory // 100 + 1)  # Integer division bonus
    
    # Bitwise interference (distractor)
    mask = 0b1101
    masked_result = int(harmonic_mean) & mask  # Unused computation
    
    # Final scoring logic
    base_score = int(harmonic_mean * 10)
    final_score = base_score + efficiency_bonus
    
    return final_score

# Benchmark dataset
benchmark_data = [
    {'runtime': 2.5, 'memory': 300, 'optimized': True},
    {'runtime': 4.0, 'memory': 800, 'optimized': False},
    {'runtime': 1.2, 'memory': 450, 'optimized': True},
    {'runtime': 5.1, 'memory': 1200, 'optimized': False},  # Invalid due to memory
    {'runtime': 3.3, 'memory': 600, 'optimized': True}
]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")