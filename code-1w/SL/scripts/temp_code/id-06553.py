from collections import defaultdict, Counter

# Simulate sensor data segments with noise and metadata
def generate_signal_segments():
    raw_signals = [
        [1, 1, 2, 2, 2, 3],
        [4, 4, 5, 5, 5, 5],
        [1, 2, 2, 3, 3, 3],
        [6, 6, 6, 6, 7, 8]
    ]
    metadata_tags = ['A', 'B', 'C', 'D']
    labeled_segments = {}
    for i, sig in enumerate(raw_signals):
        labeled_segments[metadata_tags[i]] = sorted(sig)
    return labeled_segments

# Auxiliary function to compute moving average (not used in final logic)
def smooth_signal(signal, window=2):
    smoothed = []
    for i in range(len(signal) - window + 1):
        avg = sum(signal[i:i+window]) / window
        smoothed.append(round(avg, 2))
    return smoothed

# Heuristic to estimate signal stability (distractor computation)
def estimate_stability(segment):
    counts = Counter(segment)
    mode_freq = max(counts.values())
    total = len(segment)
    stability_score = mode_freq / total
    return stability_score > 0.5

# Main processing function with relevant logic
def process_segments(data, limit):
    aggregated = defaultdict(int)
    temp_buffer = []
    
    for key, values in data.items():
        # Irrelevant smoothing applied but result not stored meaningfully
        _ = [smooth_signal(values) for _ in range(1)]  # Dead repetition
        
        segment_sum = sum(x for x in values if x >= 3)  # Only values >=3 contribute
        filtered_count = len([x for x in values if x < limit])
        
        # Track per-segment stats (only one will be used later)
        segment_stats = {
            'sum_high': segment_sum,
            'count_low': filtered_count,
            'stability': estimate_stability(values)
        }
        
        # Only sum_high is actually accumulated
        aggregated[key] += segment_stats['sum_high']
        
        # Red herring: buffer unused accumulation
        temp_buffer.append(sum(values) // len(values) if values else 0)
    
    # Linear search for qualifying keys (overcomplicated)
    valid_keys = []
    for k in aggregated.keys():
        if k in ['A', 'C', 'D']:
            valid_keys.append(k)
    
    # Final tally from selected segments
    intermediate_total = 0
    for vk in valid_keys:
        intermediate_total += aggregated[vk]
    
    # Additional irrelevant transformation
    offset = len(temp_buffer) * 2
    dummy_shift = offset >> 1
    
    # Final result calculation (only depends on logic above)
    final_tally = intermediate_total - dummy_shift  # dummy_shift = 4
    return final_tally

# Execution flow
if __name__ == '__main__':
    collected_data = generate_signal_segments()
    base_threshold = 3
    adjustment_factor = 1
    threshold = base_threshold - adjustment_factor
    
    # Distractor variables
    shadow_copy = {k: v[:] for k, v in collected_data.items()}
    normalized = {k: [x / max(v) for x in v] for k, v in collected_data.items()}
    summary_stats = Counter()
    for seg in collected_data.values():
        summary_stats.update(seg)
    
    # Key statement
    final_tally = process_segments(collected_data, threshold)
    
    # Print result as required
    print(f"Result: {final_tally}")