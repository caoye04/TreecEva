from collections import defaultdict, Counter

def analyze_patterns(sequence):
    freq_map = defaultdict(int)
    for item in sequence:
        freq_map[item] += 1
    return freq_map

def extract_features(data):
    feature_vector = []
    temp_sum = 0
    
    for i, val in enumerate(data):
        if i % 2 == 0 and val > 3:
            temp_sum += val ** 2
        else:
            temp_sum -= val
    
    # Distractor: complex but unused calculation
    entropy_approx = 0
    counts = Counter(data)
    total = len(data)
    for count in counts.values():
        prob = count / total
        if prob > 0:
            entropy_approx -= prob * (prob ** 0.5)  # Not real entropy, just noise

    feature_vector.append(temp_sum)
    return feature_vector

def filter_outliers(values):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    threshold = mean_val + 1.5 * std_dev
    return [v for v in values if v <= threshold]

def calculate_final_score(dataset):
    cleaned = filter_outliers(dataset)
    features = extract_features(cleaned)
    pattern_freq = analyze_patterns(cleaned)
    
    base_score = features[0]
    bonus = 0
    
    # Logic chain with interdependencies
    for k, v in pattern_freq.items():
        if v >= 2 and k % 2 == 1:
            bonus += k * v

    adjustment = 0
    sorted_vals = sorted(cleaned)
    if len(sorted_vals) > 2:
        mid_val = sorted_vals[len(sorted_vals) // 2]
        adjustment = (mid_val & 7) ^ 3  # Bitwise distraction with partial relevance

    # Final computation
    final_score = base_score + bonus - adjustment
    
    # Irrelevant tracking variables
    debug_log = []
    for x in cleaned:
        if x > 10:
            debug_log.append(f"High: {x}")
    
    return final_score

# Main execution
raw_input = [5, 2, 8, 3, 9, 2, 7, 4, 6, 3, 11, 3]
processed_data = [x + 1 for x in raw_input if x % 2 == 1]
intermediate_checksum = sum(x * (x % 4) for x in raw_input)  # Dead computation
normalization_factor = max(processed_data) / 10.0  # Unused normalization

final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")