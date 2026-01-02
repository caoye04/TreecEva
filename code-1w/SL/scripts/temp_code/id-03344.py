import itertools

def analyze_pattern(sequence):
    count = 0
    trend = []
    for i in range(1, len(sequence)):
        if sequence[i] > sequence[i-1]:
            trend.append(1)
        elif sequence[i] < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    
    # Irrelevant computation: counts oscillations but not used later
    oscillations = 0
    for j in range(1, len(trend)):
        if trend[j] != trend[j-1] and trend[j-1] != 0:
            oscillations += 1

    return trend

def filter_outliers(data, threshold=2.5):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = variance ** 0.5
    
    # Dead code path - never executed due to fixed condition
    if False:
        cleaned = [x for x in data if abs(x - mean_val) / std_dev <= threshold]
    else:
        cleaned = [x for x in data if x >= mean_val - std_dev]
    
    # Extra transformation with slicing that isn't used
    temp_slice = cleaned[::2]
    temp_sum = sum(temp_slice)
    
    return cleaned

def compute_final_score(data_list):
    base = sum(data_list) * 0.8
    
    # Use of dictionary to map indices (semi-relevant)
    index_map = {i: val for i, val in enumerate(data_list)}
    bonus = 0
    
    # Conditional logic with nested structure
    if len(data_list) > 5:
        sorted_vals = sorted(data_list)
        mid_index = len(sorted_vals) // 2
        median_val = (sorted_vals[mid_index] + sorted_vals[~mid_index]) / 2
        
        if median_val > 50:
            # Use of itertools.chain to flatten a constructed list
            extended_seq = list(itertools.chain([base], data_list, [median_val]))
            adjustment = sum(extended_seq[i] for i in range(len(extended_seq)) if i % 3 == 0) * 0.1
            bonus = adjustment
        else:
            bonus = 10
    else:
        bonus = 5
    
    score = base + bonus
    
    # Multiple assignments – one is distracting
    final_score, temp_score = score * 1.05, score * 0.95
    
    return final_score

# Main execution flow
raw_input = [45, 67, 23, 89, 56, 77, 34, 68]
processed_trend = analyze_pattern(raw_input)
processed_data = filter_outliers(raw_input, threshold=2.2)
intermediate_flag = len(processed_data) % 2 == 1

# Key statement
final_score = compute_final_score(processed_data)

print(f"Result: {final_score}")