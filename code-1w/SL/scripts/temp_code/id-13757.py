import itertools

def analyze_pattern(sequence):
    count = 0
    trend_values = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            count += 1
            trend_values.append(1)
        elif sequence[i] < sequence[i-1]:
            count -= 1
            trend_values.append(-1)
        else:
            trend_values.append(0)
    return count

def filter_outliers(data, threshold=2):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= threshold * std_dev]
    outlier_count = len(data) - len(filtered)
    temp_analysis = {"mean": mean_val, "std": std_dev, "outliers_removed": outlier_count}
    return filtered

def calculate_final_score(data_dict):
    base_score = 0
    adjustment_factor = 0.0
    total_entries = 0
    
    # Extract sequences using dictionary operations
    raw_sequences = data_dict.get('sequences', [])
    metadata_log = data_dict.get('metadata', {})
    
    processed_sequences = []
    for seq in raw_sequences:
        filtered_seq = filter_outliers(seq)
        processed_sequences.append(filtered_seq)
    
    # Use itertools to generate sliding window pairs
    flat_data = list(itertools.chain.from_iterable(processed_sequences))
    window_pairs = list(itertools.pairwise(flat_data))  # pairwise from itertools
    
    # Dummy computation - irrelevant to final score but adds cognitive load
    pair_trends = []
    for a, b in window_pairs:
        if a < b:
            pair_trends.append('up')
        elif a > b:
            pair_trends.append('down')
        else:
            pair_trends.append('stable')
    
    # Actual scoring logic
    direction_counter = analyze_pattern(flat_data)
    base_score += direction_counter * 10
    
    # Additional rule: penalize if any original sequence had length > 5
    penalty_trigger = any(len(seq) > 5 for seq in raw_sequences)
    if penalty_trigger:
        base_score -= 15
    
    # Irrelevant aggregation
    avg_value = sum(flat_data) / len(flat_data) if flat_data else 0
    max_jump = max(abs(b - a) for a, b in window_pairs) if window_pairs else 0
    
    # Final adjustment based on metadata
    version_flag = metadata_log.get('version', 'A')
    if version_flag == 'B':
        adjustment_factor = 1.1
    else:
        adjustment_factor = 1.0
    
    # Dead code - never used
    debug_snapshot = {
        'timestamp': '2024-01-01',
        'mode': 'diagnostic',
        'checksum': sum(flat_data[:3]) if len(flat_data) >= 3 else 0
    }
    
    # Compute final score
    final_score = int(base_score * adjustment_factor)
    return final_score

# Input data structure
input_data = {
    'sequences': [
        [3, 6, 9],
        [2, 4, 8, 7],
        [5, 5, 5, 5, 5, 5]  # This will trigger penalty
    ],
    'metadata': {
        'version': 'A',
        'author': 'system'
    }
}

# Process data
intermediate_results = {}
processed_data = {}
processed_data['raw_input'] = input_data['sequences']
processed_data['valid'] = True

# Call main function
final_score = calculate_final_score(input_data)
print(f"Result: {final_score}")