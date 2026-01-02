from collections import defaultdict

# Simulate system benchmark data with noise and metadata
def generate_benchmark_data():
    raw_metrics = [88, 92, 75, 85, 96]
    timestamps = ['t1', 't2', 't3', 't4', 't5']
    metadata_map = defaultdict(lambda: 'unknown')
    for i, t in enumerate(timestamps):
        metadata_map[t] = f'module_{i % 3}'
    
    # Add irrelevant derived values
    squared_offsets = [x**2 for x in range(len(raw_metrics))]
    temp_checksum = sum(squared_offsets) % 100
    
    # Return structured data with red herring fields
    return {
        'metrics': raw_metrics,
        'meta': metadata_map,
        'version': '2.1',
        'temp_checksum': temp_checksum,
        'aux_data': {'scale': 1.0, 'units': 'ms'}
    }

# Helper to compute adaptive weight (not all branches are useful)
def compute_adaptive_weight(index, base=0.1):
    if index < 0:
        return 0.0
    elif index % 3 == 0:
        adjustment = 0.05
    else:
        adjustment = -0.02
    return base + adjustment + (0.01 * (index % 2))

# Core logic buried among distractions
def calculate_performance(data):
    metrics = data['metrics']
    total_weight = 0.0
    weighted_sum = 0.0
    
    # Real computation mixed with side tracking
    running_stats = []
    debug_flags = []
    
    for i, val in enumerate(metrics):
        weight = compute_adaptive_weight(i)
        total_weight += weight
        weighted_sum += val * weight
        
        # Distractor: tracking intermediate states that aren't used
        running_stats.append((val, weight, val * weight))
        if val > 90:
            debug_flags.append(f"high_val@{i}")
        
        # Fake early exit check (never triggers)
        if i == 100:
            return -1  # dead code
    
    # Additional unused transformation
    reversed_stats = running_stats[::-1]
    avg_stat_value = sum([x[0] for x in reversed_stats]) / len(reversed_stats) if reversed_stats else 0
    
    # Actual result calculation
    base_avg = sum(metrics) / len(metrics)
    adjusted_avg = weighted_sum / total_weight if total_weight else 0
    
    # Final score uses adjusted average but adds deterministic offset
    final_offset = len(debug_flags) * 2.5
    final_score = adjusted_avg + final_offset
    
    # More red herrings
    anomaly_detected = False
    for j, (val, w, prod) in enumerate(running_stats):
        if prod > 1000:  # impossible condition
            anomaly_detected = True
            break
    
    return final_score

# Entry point
benchmark_data = generate_benchmark_data()
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")