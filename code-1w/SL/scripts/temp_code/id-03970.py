def analyze_pattern(seq):
    counts = {c: seq.count(c) for c in set(seq)}
    freq_list = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    return freq_list[0][1] if freq_list else 0

# Simulate sensor data segments with noise filtering
def filter_noisy_readings(readings):
    filtered = [r for r in readings if 10 <= r <= 100]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    adjusted = [abs(r - baseline) * 0.9 for r in filtered]
    return adjusted

def process_segments(data, importance):
    segment_scores = {}
    temp_buffer = []
    
    for i, (seg_name, values) in enumerate(zip(data.keys(), data.values())):
        clean_vals = filter_noisy_readings(values)
        raw_total = sum(clean_vals)
        
        # Distractor: pattern analysis not used in final score
        pattern_strength = analyze_pattern([int(v) % 10 for v in clean_vals])
        offset_adjustment = len(clean_vals) % 4
        
        normalized = raw_total / (len(clean_vals) + 1e-5)
        weighted_score = normalized * importance.get(seg_name, 1.0)
        
        # Store intermediate result
        segment_scores[seg_name] = weighted_score + offset_adjustment
        
        # Dead code path - never accessed but looks relevant
        if False:
            temp_buffer.append((seg_name, pattern_strength))

    # Final aggregation
    final_score = sum(segment_scores.values())
    outlier_check = max(segment_scores.values()) > 200
    
    # Irrelevant transformation
    status_flags = {k: 'high' if v > 100 else 'low' for k, v in segment_scores.items()}
    
    return int(final_score)

# Input data
segment_data = {
    'sensor_A': [15, 20, 105, 25, -5, 30],
    'sensor_B': [50, 12, 88, 95, 102, 45],
    'sensor_C': [70, 80, 75, 110, 65, 60]
}

weights = {
    'sensor_A': 1.2,
    'sensor_B': 0.9,
    'sensor_C': 1.4
}

# Trigger computation
final_score = process_segments(segment_data, weights)
print(f"Result: {final_score}")