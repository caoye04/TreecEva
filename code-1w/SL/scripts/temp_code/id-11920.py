def analyze_pattern(sequence):
    count_vowels = 0
    temp_sum = 0
    for char in sequence:
        if char in 'aeiou':
            count_vowels += 1
        temp_sum += ord(char) % 7
    return count_vowels


def validate_range(value, min_val, max_val):
    if value < min_val:
        return min_val
    elif value > max_val:
        return max_val
    return value


def process_metrics(data, config):
    baseline = 10
    adjustment = 0
    total_weight = 0.0
    outlier_count = 0
    intermediate_results = []
    
    for item in data:
        # Irrelevant vowel analysis (distractor)
        vowels_in_key = analyze_pattern(item['key'])
        
        raw_value = item['value']
        weight = len(item['key'])
        
        # Real computation path
        if raw_value < config['min']:
            adjustment -= 2
        elif raw_value > config['max']:
            outlier_count += 1  # tracked but not used directly
        else:
            total_weight += weight * raw_value
        
        intermediate_results.append(raw_value * weight)
    
    # Secondary distraction: string manipulation with no impact
    status_tag = "valid" if outlier_count == 0 else "flagged"
    status_code = ''.join([chr(ord(c)+1) for c in status_tag]).upper()
    
    # Core logic depends only on total_weight and baseline
    aggregated = sum(intermediate_results) // len(intermediate_results) if intermediate_results else 0
    final_score = baseline + adjustment + (aggregated // 10)
    
    # Early termination red herring (never reached due to logic flow)
    if len(status_code) > 10:
        return -1
        
    return final_score

# Input setup
data_set = [
    {'key': 'alpha', 'value': 15},
    {'key': 'beta', 'value': 8},
    {'key': 'gamma', 'value': 23},
    {'key': 'delta', 'value': 12}
]

tuning_params = {
    'min': 10,
    'max': 20
}

result = process_metrics(data_set, tuning_params)
print(f"Target result: {result}")