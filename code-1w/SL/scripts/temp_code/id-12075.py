import itertools

def analyze_metrics(data, threshold=5.0):
    high_performers = []
    temp_sum = 0
    count = 0
    
    for i, val in enumerate(data):
        if val > threshold:
            high_performers.append(val * 0.85)
        else:
            high_performers.append(val * 0.3)
        
    # Irrelevant aggregation
    dummy_avg = sum(high_performers) / len(high_performers) if high_performers else 0
    
    return [x for x in high_performers if x > 4.0]

def filter_outliers(sequence):
    if not sequence:
        return []
    mean_val = sum(sequence) / len(sequence)
    deviation = [abs(x - mean_val) for x in sequence]
    median_dev = sorted(deviation)[len(deviation)//2]
    # Dead code path - never used
    if median_dev < 1.0:
        scale_factor = 2.0
    else:
        scale_factor = 1.0
    return [x for x, d in zip(sequence, deviation) if d <= 2 * median_dev]

def calculate_performance(logs):
    processed = []
    base_offset = 10
    scaling_factor = 0.9
    
    for record in logs:
        # Simulate transformation chain
        transformed = [x ** 0.5 for x in record if x > 0]
        filtered = [x for x in transformed if x.is_integer()]
        scaled = [x * scaling_factor for x in filtered]
        processed.extend(scaled)
    
    # Secondary processing with distractor variables
    total_entries = len(processed)
    null_count = 0
    for v in processed:
        if v == 0:
            null_count += 1
    
    # Actual computation path
    trimmed_data = processed[:10] if len(processed) > 10 else processed
    analyzed = analyze_metrics(trimmed_data, threshold=3.5)
    cleaned = filter_outliers(analyzed)
    
    # Final score calculation (depends only on specific path)
    adjustment = len(cleaned) * 0.5
    raw_total = sum(cleaned)
    final_score = int(raw_total + adjustment + base_offset)  # Key assignment
    
    # Unused debugging artifacts
    debug_snapshot = {"size": total_entries, "adjusted": adjustment, "raw": raw_total}
    temp_result_cache = []
    for _ in itertools.repeat(None, 3):
        temp_result_cache.append("cached")
    
    return final_score

# Input data generation
sequence_pool = [4, 9, 16, 25, 36]
expanded_grid = list(itertools.product(sequence_pool, repeat=2))
benchmark_data = [[a + b for a, b in expanded_grid[i:i+3]] for i in range(0, len(expanded_grid), 3)][:5]

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")