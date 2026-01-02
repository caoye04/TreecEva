from itertools import compress, cycle

def analyze_performance(metrics, weights):
    weighted_sum = sum(m * w for m, w in zip(metrics, weights))
    norm_factor = sum(weights)
    return weighted_sum / norm_factor if norm_factor else 0

def compute_aggregate(values, limits):
    adjusted = [v * 1.5 if v < limits[0] else v * 0.8 for v in values]
    outlier_mask = [v > limits[1] for v in adjusted]
    filtered = list(compress(adjusted, [not x for x in outlier_mask]))
    return round(sum(filtered) / len(filtered), 4) if filtered else 0

def main():
    raw_data = [85, 90, 78, 92, 88, 76, 95, 89]
    config_weights = [1, 2, 1, 2, 1, 1, 2, 1]
    
    # Irrelevant preprocessing: case conversion simulation (distractor)
    str_versions = [str(x) for x in raw_data]
    reversed_str = [s[::-1] for s in str_versions]
    int_back = [int(s) for s in reversed_str]
    
    # Key transformation chain
    base_average = sum(raw_data) / len(raw_data)
    shifted_data = [x - base_average for x in raw_data]
    abs_shifts = [abs(s) for s in shifted_data]
    max_deviation = max(abs_shifts)
    normalized_devs = [d / max_deviation for d in abs_shifts] if max_deviation else [0]*len(abs_shifts)
    
    # Distractor: unused nested loop with dead logic
    temp_cache = []
    for i in range(2):
        row = []
        for j in range(3):
            dummy = (i + j) ** 2
            if dummy > 5:
                row.append(dummy * 0.1)
        if row:
            temp_cache.append(row)
    
    # Real computation path
    scaled_values = [raw_data[i] * (1 + normalized_devs[i]) for i in range(len(raw_data))]
    
    # Another distractor: enumeration without impact
    indexed_pairs = list(enumerate(zip(raw_data, scaled_values)))
    for idx, (orig, scaled) in indexed_pairs:
        if idx % 3 == 0:
            _ = f"Processing record {idx}"

    # Threshold logic with slicing distraction
    sorted_scaled = sorted(scaled_values)
    mid_slice = sorted_scaled[2:-2]  # Middle portion, not used later
    
    # Critical thresholds
    thresholds = [80, 100]
    
    # Key statement
    final_score = compute_aggregate(scaled_values, thresholds)
    
    # Print required result
    print(f"Target result: {final_score}")
    
    # Unused itertools example (distractor)
    cycled_weights = list(zip(scaled_values, cycle(config_weights)))
    weighted_total = sum(val * wt for val, wt in cycled_weights[:len(scaled_values)])
    
    return final_score

if __name__ == "__main__":
    main()