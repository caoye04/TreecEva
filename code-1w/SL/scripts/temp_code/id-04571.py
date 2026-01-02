import itertools

def analyze_pattern(sequence):
    # Irrelevant helper function – never called in execution path
    return [x ** 2 for x in sequence if x % 3 == 0]

def precompute_weights(data):
    # Dead code path – computed but never used
    weights = {}
    for i, val in enumerate(data):
        weights[i] = (val * 0.85) ** 0.5 if i % 2 else val / 1.2
    return weights

def transform_stream(stream):
    # Distractor transformation – modifies data but result unused
    shifted = [(x >> 2) + 1 for x in stream]
    normalized = [round(x / max(shifted), 3) for x in shifted]
    return normalized

def filter_outliers(arr, limit=50):
    # This function is called but its output ignored – red herring
    return [x for x in arr if abs(x) < limit]

def calculate_entropy(metrics, thresh):
    entropy = 0.0
    count = 0
    
    # Real logic begins: process valid segments
    for k, group in itertools.groupby(metrics, key=lambda x: x > thresh):
        if k:  # Only consider groups above threshold
            group_list = list(group)
            size = len(group_list)
            if size >= 2:
                # Compute weighted variation
                variation = sum((group_list[i] - group_list[i-1]) ** 2 for i in range(1, size))
                entropy += variation * 0.75
            else:
                entropy -= 1.5  # Small penalty for isolated values
            count += 1
    
    # Additional adjustment based on distribution
    flat_data = [item for sublist in [metrics[i:i+2] for i in range(0, len(metrics), 3)] if len(sublist) == 2]
    if flat_data:
        coherence = sum(a * b for a, b in flat_data) / len(flat_data)
        entropy += coherence * 0.1
    
    return round(entropy, 6)

# Main execution block
if __name__ == '__main__':
    # Input signal data (simulated sensor readings)
    raw_readings = [12, 15, 15, 13, 4, 6, 20, 22, 22, 22, 8, 10, 30, 31]
    
    # Irrelevant preprocessing – results not used downstream
    cleaned = [x for x in raw_readings if x > 5]
    filtered = filter_outliers(cleaned, limit=25)
    _ = transform_stream(raw_readings)
    
    # Critical variables
    baseline = 18
    adjustment_factor = 0.9
    dynamic_offset = sum(1 for x in raw_readings if x > baseline) * 2
    threshold = baseline - dynamic_offset + 1  # threshold = 18 - 6 + 1 = 13
    
    # Decoy dictionary operations – look important but irrelevant
    flow_stats = {
        'peak': max(raw_readings),
        'density': len(raw_readings) / (max(raw_readings) - min(raw_readings)),
        'shift': adjustment_factor * dynamic_offset
    }
    flow_stats['adjacent_pairs'] = sum(1 for a, b in zip(raw_readings, raw_readings[1:]) if a == b)
    flow_stats['streaks'] = len([k for k, _ in itertools.groupby(raw_readings)])
    
    # Core data for actual computation
    flow_metrics = [x - 1 for x in raw_readings]  # Shift all down by 1 -> [11,14,...,30]
    
    # Misleading intermediate calculation (unused)
    aggregate_score = 0
    for i, val in enumerate(flow_metrics):
        if val % 4 == 0:
            aggregate_score += val // 4
    
    # Key statement
    final_flux = calculate_entropy(flow_metrics, threshold)
    
    # Print result as required
    print(f"Result: {final_flux}")