def analyze_frequency(data, base):
    freq_map = {}
    for item in data:
        freq_map[item] = freq_map.get(item, 0) + 1
    adjusted = {k: v * base for k, v in freq_map.items()}
    return adjusted


def normalize_values(raw):
    total = sum(raw.values())
    if total == 0:
        return raw
    return {k: round(v / total, 4) for k, v in raw.items()}


def filter_outliers(scores, limit=3):
    sorted_vals = sorted(scores)
    cutoff = sorted_vals[-limit] if len(sorted_vals) >= limit else sorted_vals[0]
    return [s for s in scores if s >= cutoff]


def process_segments(segments, thresholds):
    temp_results = []
    noise_floor = 0.05
    aggregate = 0
    
    for i, seg in enumerate(segments):
        segment_total = sum(seg)
        if segment_total < noise_floor:
            continue
            
        # Simulate signal correction
        corrected = [abs(x - 0.1) for x in seg]
        valid_points = [c for c in corrected if c > 0.05]
        
        # Irrelevant sorting (distractor)
        valid_points.sort(reverse=True)
        
        # Dummy transformation chain
        transformed = [v**2 for v in valid_points]
        mean_val = sum(transformed) / len(transformed) if transformed else 0
        
        # Weighting by index (relevant)
        weight = thresholds[i % len(thresholds)]
        temp_results.append(mean_val * weight * (i + 1))

    # Secondary processing path (partially irrelevant)
    if len(temp_results) > 1:
        diff_chain = [temp_results[j+1] - temp_results[j] for j in range(len(temp_results)-1)]
        abs_diffs = [abs(d) for d in diff_chain]
        median_diff = sorted(abs_diffs)[len(abs_diffs)//2] if abs_diffs else 0
        aggregate += median_diff * 0.1  # Minor contribution

    primary_sum = sum(temp_results)
    
    # Final adjustment using auxiliary function
    dummy_data = [10, 20, 30]
    fake_freq = analyze_frequency(dummy_data, 2)
    norm_freq = normalize_values(fake_freq)
    # The above two calls are dead code — no impact on output
    
    outlier_filtered = filter_outliers([int(primary_sum * 100)])
    cleaned_sum = sum(outlier_filtered) / 100.0 if outlier_filtered else primary_sum
    
    final_score = int(round(cleaned_sum * 10)) * 1.5
    
    Result: final_score
    return final_score

# Input data
segments_input = [
    [0.12, 0.15, 0.08],
    [0.21, 0.19, 0.23],
    [0.07, 0.11, 0.13],
    [0.25, 0.27, 0.24]
]
thresholds_input = [1.2, 0.8, 1.5]

# Execution entry point
final_score = process_segments(segments_input, thresholds_input)
print(f"Result: {final_score}")