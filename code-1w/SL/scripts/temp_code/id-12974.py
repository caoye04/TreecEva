def analyze_metrics(data):
    base_values = [x * 0.85 for x in data if x > 10]
    offset = sum(base_values) / len(base_values) if base_values else 0
    
    # Distractor: irrelevant transformation on strings
    labels = ['item_' + str(i) for i in range(len(data))]
    labeled_map = {lbl: val for lbl, val in zip(labels, data)}
    key_list = list(labeled_map.keys())
    mid_index = len(key_list) // 2
    pivot_label = key_list[mid_index] if mid_index >= 0 else ''
    
    # Semi-relevant: preprocessing step that affects later normalization
    adjusted = []
    for val in data:
        if val < 5:
            adjusted.append(val * 1.2)
        elif val > 20:
            adjusted.append(val * 0.9)
        else:
            adjusted.append(val)
    
    # Dummy counters and side calculations
    high_count = sum(1 for x in adjusted if x > 15)
    low_count = sum(1 for x in adjusted if x < 8)
    balance_factor = (high_count - low_count) * 0.3 if high_count != low_count else 1.0
    
    # String-based filtering mask (some distraction here)
    status_flags = ['high' if x > 15 else 'low' for x in adjusted]
    valid_flags = [f for f in status_flags if f == 'high']
    flag_ratio = len(valid_flags) / len(status_flags) if status_flags else 0
    
    return adjusted, balance_factor, offset


def normalize_sequence(seq, factor):
    mean_val = sum(seq) / len(seq)
    normalized = [(x - mean_val) * factor for x in seq]
    # Extra operation with no impact
    squared_devs = [(x - mean_val)**2 for x in seq]
    variance = sum(squared_devs) / len(squared_devs) if squared_devs else 0
    return normalized


def calculate_performance(raw_input):
    # Initial filtering and distractor variables
    filtered_data = [x for x in raw_input if x % 2 == 1]  # keep only odd numbers
    temp_sum = sum(filtered_data)
    size_tag = f"size_{len(filtered_data)}"
    
    # Core analysis
    processed, bf, off = analyze_metrics(filtered_data)
    
    # Apply normalization using balance factor
    scaled_data = normalize_sequence(processed, bf)
    
    # More distractions: string manipulation unrelated to final score
    tag_parts = size_tag.split('_')
    tag_num = int(tag_parts[1]) if len(tag_parts) > 1 and tag_parts[1].isdigit() else 0
    tag_suffix = ''.join([c for c in size_tag if c.isalpha()])
    
    # Actual scoring logic
    magnitude_score = sum(abs(x) for x in scaled_data)
    spread_bonus = max(scaled_data) - min(scaled_data) if scaled_data else 0
    
    # Final computation
    intermediate = magnitude_score * 0.7 + spread_bonus * 1.5
    penalty = abs(off) * 0.2
    final_score = intermediate - penalty
    
    # This print is required per instructions
    print(f"Result: {final_score}")
    
    return final_score

# Main execution
benchmark_data = [12, 15, 3, 22, 7, 19, 4, 11, 14, 17, 6, 25]
calculate_performance(benchmark_data)