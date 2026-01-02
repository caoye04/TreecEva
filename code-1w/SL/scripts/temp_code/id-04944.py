def analyze_pattern(sequence):
    count_a = 0
    count_b = 0
    temp_sum = 0
    for char in sequence:
        if char == 'A':
            count_a += 1
            temp_sum += 2
        elif char == 'B':
            count_b += 1
            temp_sum -= 1
    return count_a > count_b


def validate_entry(record):
    valid_chars = 'ABCD'
    score = 0
    for ch in record:
        if ch in valid_chars:
            score += ord(ch) - ord('A') + 1
    normalized = score / len(record) if record else 0
    return normalized >= 2.5


def calculate_final_score(data, thresholds):
    raw_total = 0
    bonus = 0
    penalty = 0
    intermediate_values = []

    for item in data:
        # Irrelevant transformation (distractor)
        transformed = ''.join([chr(ord(c) + 1) for c in item['seq']])
        
        base_value = len(item['seq']) * item['weight']
        
        # Real computation path
        if analyze_pattern(item['seq']):
            raw_total += base_value
            if validate_entry(item['seq']):
                bonus += item['weight']
        else:
            penalty += 1

        # Semi-relevant tracking (not used in final result)
        intermediate_values.append(base_value * bonus if bonus else base_value)

    # Additional distracting logic
    adjustment_factor = 1.0
    if raw_total > thresholds['limit'] and penalty == 0:
        adjustment_factor = thresholds['boost'] if bonus >= 3 else thresholds['decay']
    else:
        adjustment_factor = thresholds['decay']

    # Core result calculation
    final_score = int((raw_total + bonus) * adjustment_factor - (penalty * 5))
    
    # Dead code path (misleading)
    if False:
        final_score = sum(intermediate_values) // len(intermediate_values)

    return final_score

# Main execution
config = {
    'limit': 20,
    'boost': 1.2,
    'decay': 0.8
}

input_data = [
    {'seq': 'AAAB', 'weight': 3},
    {'seq': 'ABBB', 'weight': 2},
    {'seq': 'AACD', 'weight': 4}
]

# Execution point of interest
final_score = calculate_final_score(input_data, config)
print(f"Result: {final_score}")