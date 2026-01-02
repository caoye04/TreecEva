import itertools

def process_metrics(stream):
    base_multiplier = 2.5
    temp_buffer = []
    cumulative_shift = 0
    trigger_threshold = 88
    efficiency_score = 0
    
    # Preprocess: filter valid entries and apply conditional transformation
    filtered_data = [x for x in stream if x > 0]
    adjusted_values = list(map(lambda x: x * base_multiplier if x % 2 == 0 else x * 1.1, filtered_data))
    
    # Simulate sliding window analysis with itertools
    window_pairs = list(itertools.pairwise(adjusted_values))
    
    for a, b in window_pairs:
        if a < b:
            cumulative_shift += (b - a) * 0.5
        elif a > b:
            cumulative_shift -= (a - b) * 0.3

    # Secondary tracking: irrelevant to final result but adds cognitive load
    peak_count = sum(1 for val in adjusted_values if val > trigger_threshold)
    stability_factor = len(window_pairs) / (cumulative_shift + 1) if cumulative_shift != -1 else 0

    # Core logic: compute efficiency score using only specific elements
    relevant_subset = [v for i, v in enumerate(adjusted_values) if i % 3 == 0]
    efficiency_score = sum(relevant_subset) + cumulative_shift

    # Dead code path - never executed but looks plausible
    if False:
        backup_metric = peak_count * stability_factor
        efficiency_score = max(efficiency_score, backup_metric)

    final_output = efficiency_score
    print(f"Result: {final_output}")
    return final_output

# Input data
raw_input = [10, -5, 12, 15, 8, 0, 14, 11, 16]
data_stream = raw_input.copy()

result = process_metrics(data_stream)