def analyze_metrics(values, thresholds):
    count_above = 0
    temp_product = 1
    debug_log = []
    for i, val in enumerate(values):
        if val > thresholds[i % len(thresholds)]:
            count_above += 1
            temp_product *= (val % 7)
        else:
            temp_product += i
        debug_log.append(f'Step {i}: {temp_product}')
    
    # Irrelevant aggregation
    weighted_sum = sum(v * (idx + 1) for idx, v in enumerate(values))
    return count_above


def preprocess_dataset(raw_entries):
    cleaned = []
    outlier_flags = []
    shift_offset = 3
    for entry in raw_entries:
        adjusted = [e - shift_offset for e in entry]
        filtered = [x for x in adjusted if x > 0]
        cleaned.append(filtered)
        outlier_flags.append(any(x > 100 for x in adjusted))
    
    # Dead code path - never used
    if len(outlier_flags) > 100:
        shift_offset *= 2
    
    return cleaned


def calculate_final_score(data_chunks):
    scores = []n    total_elements = 0
    zero_count = 0
    
    for chunk in data_chunks:
        chunk_sum = 0
        valid_pairs = []
        
        # Use of zip and enumerate together
        for idx, (a, b) in enumerate(zip(chunk[:-1], chunk[1:])):
            if a < b:
                chunk_sum += (a + b) * (idx + 1)
                valid_pairs.append((a, b))
        
        # Semi-relevant computation
        pair_influence = sum(p[0] * p[1] for p in valid_pairs)
        scores.append(chunk_sum + len(valid_pairs))
        total_elements += len(chunk)
        
        # Distractor: unused tracking
        if chunk_sum == 0:
            zero_count += 1

    # Final logic step: combine scores with offset
    base_result = sum(scores) - total_elements
    adjustment = len(scores) * 2
    final_score = base_result + adjustment
    
    return final_score

# Main execution
raw_data = [
    [5, 8, 6, 9],
    [3, 7, 7, 10],
    [4, 5, 6]
]

thresholds_config = [4, 6, 5]

# Preprocess
processed_data = preprocess_dataset(raw_data)

# Analyze (uses enumerate, returns ignored result)
analysis_result = analyze_metrics([item for sublist in raw_data for item in sublist], thresholds_config)

# Critical statement
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")