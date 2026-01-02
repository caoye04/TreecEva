from collections import defaultdict, Counter

# Simulate sensor data with noise and redundancy
def preprocess_sensor_data(raw_data):
    filtered_data = []
    noise_counter = 0
    for val in raw_data:
        if isinstance(val, str) and val.isdigit():
            val = int(val)
        if isinstance(val, int) and 0 <= val <= 100:
            filtered_data.append(val)
        else:
            noise_counter += 1
    # Misleading normalization (not used later)
    normalized = [x / 100.0 for x in filtered_data]
    return filtered_data

# Analyze frequency patterns in cleaned data
def analyze_pattern(data):
    freq = Counter(data)
    mode_val = freq.most_common(1)[0][1] if freq else 0
    unique_count = len(freq)
    # Red herring computation
    entropy_approx = 0
    total = sum(freq.values())
    for count in freq.values():
        if count > 0 and total > 0:
            p = count / total
            entropy_approx -= p * p  # Not real entropy, just distraction
    return unique_count

# Core scoring logic with weighted contributions
def calculate_final_score(data, weights):
    base_sum = sum(data)
    adjusted_sum = 0
    weight_factor = 1.0
    
    for i, val in enumerate(data):
        cycle_mod = (i % 3) + 1
        intermediate = val * weights[i % len(weights)]
        adjusted_sum += intermediate * cycle_mod
        weight_factor *= (weights[i % len(weights)] + 1) / 2  # Unused accumulation
    
    # Key branching logic based on pattern insight
    pattern_complexity = analyze_pattern(data)
    bonus = 0
    if pattern_complexity > 5:
        bonus = 10
    elif pattern_complexity == 4:
        bonus = 7
    else:
        bonus = 3
    
    # Final composition
    penalty = len([x for x in data if x < 10]) * 2
    final_score = int((adjusted_sum / len(data)) + bonus - penalty)
    return final_score

# Simulated input with mixed types and irrelevant entries
raw_input = [12, '15', 23, 'invalid', 45, 12, 67, None, 23, 89, 12, 23, 34, 45, 56, '78', 12, 23]
weights = [0.8, 1.2, 1.0, 0.9]

cleaned = preprocess_sensor_data(raw_input)
final_score = calculate_final_score(cleaned, weights)
print(f"Result: {final_score}")