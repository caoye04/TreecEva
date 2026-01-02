import itertools

def analyze_pattern(seq):
    counts = {}
    for k, g in itertools.groupby(seq):
        counts[k] = counts.get(k, 0) + len(list(g))
    return counts

def normalize_weights(w):
    total = sum(w)
    return [x / total for x in w]

def filter_outliers(data, threshold=3.0):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    return [x for x in data if abs(x - mean_val) / std_dev <= threshold]

def process_segments(segments, weight_map):
    segment_values = []
    temp_results = []
    
    for i, seg in enumerate(segments):
        raw_sum = sum(seg)
        weight = weight_map.get(i, 1.0)
        adjusted = raw_sum * weight
        temp_results.append(adjusted)
        
        # Simulate auxiliary analysis (not used later)
        pattern_stats = analyze_pattern(seg)
        zero_count = pattern_stats.get(0, 0)
        spike_count = sum(1 for x in pattern_stats.keys() if x > 5)
        
    # Secondary processing with filtering (distractor path)
    filtered_temps = filter_outliers(temp_results)
    normalized_temps = normalize_weights(filtered_temps)  # Not actually used
    
    # Core logic: weighted harmonic mean of non-zero adjusted sums
    non_zero = [v for v in temp_results if v != 0]
    if not non_zero:
        return 0
    
    harmonic_components = [len(non_zero) / sum(1/v for v in non_zero)]
    smoothing_factor = 0.85
    instability_penalty = abs(len(temp_results) - len(filtered_temps)) * 0.1
    
    # Final computation
    base_score = harmonic_components[0]
    final_score = int(base_score * smoothing_factor - instability_penalty)
    
    # Irrelevant tracking variables
    cumulative_drift = sum(abs(temp_results[i] - temp_results[i-1]) for i in range(1, len(temp_results))) if len(temp_results) > 1 else 0
    peak_segment = max(temp_results)
    
    return final_score

# Input data
segment_data = [
    [1, 2, 0, 0, 3],
    [4, 0, 1, 0, 2],
    [0, 0, 0, 5],
    [2, 2, 2, 0, 0, 1]
]

weights = {0: 1.2, 1: 0.9, 2: 1.5, 3: 0.7}

# Execution point
final_score = process_segments(segment_data, weights)
print(f"Result: {final_score}")