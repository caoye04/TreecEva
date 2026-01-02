from itertools import combinations

def analyze_pattern(sequence):
    count = 0
    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if (sequence[i] + sequence[j]) % 3 == 0:
                count += 1
    return count

def preprocess_input(raw_values):
    normalized = [x % 7 for x in raw_values if x > 0]
    filtered = [x for x in normalized if x != 3]
    expanded = []
    for val in filtered:
        expanded.extend([val, val * 2])
    return list(set(expanded))

def calculate_final_score(data_chunk):
    temp_result = 0
    for a, b in combinations(data_chunk, 2):
        temp_result += a * b
    
    # Distractor: complex but unused calculation
    checksum = sum([x ** 2 for x in data_chunk])
    checksum -= len(data_chunk)
    dummy_tracker = {i: checksum % (i+1) for i in range(1, 5)}
    
    adjustment_factor = len(data_chunk) % 4
    if adjustment_factor == 0:
        adjustment_factor = 2
    
    final_value = temp_result // adjustment_factor
    
    # Irrelevant state tracking
    log_entries = 0
    for item in data_chunk:
        if item > 5:
            log_entries += 1
    return final_value

# Main execution
raw_input_data = [12, -5, 8, 0, 14, 21, 7, 3]
intermediate_state = preprocess_input(raw_input_data)
processed_data = sorted(intermediate_state)

# Key analysis on sub-patterns (distractor with partial reuse)
pattern_intensity = analyze_pattern(processed_data)
duplicate_risk_score = len(processed_data) - len(set(processed_data))

# Critical statement
final_score = calculate_final_score(processed_data)

Result: {final_score}