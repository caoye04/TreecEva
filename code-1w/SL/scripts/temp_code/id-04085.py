import itertools

def analyze_pattern(sequence):
    if not sequence:
        return 0
    
    # Irrelevant transformation (distractor)
    normalized = [x / max(sequence) for x in sequence if x > 0]
    smoothed = [sum(normalized[i:i+3]) / 3 for i in range(len(normalized) - 2)]
    
    # Semi-relevant preprocessing
    filtered = list(filter(lambda x: x > 0.5, normalized))
    
    # Real logic begins: count oscillations above threshold
    peaks = 0
    for i in range(1, len(filtered) - 1):
        if filtered[i] > filtered[i-1] and filtered[i] > filtered[i+1]:
            peaks += 1
    
    return peaks

def calculate_performance(base, data):
    offset = base * 0.1
    adjusted_data = [val - offset for val in data]
    
    # Distractor: unused intermediate calculation
    squared_sums = sum(x ** 2 for x in adjusted_data)
    temp_result = squared_sums ** 0.5
    
    # Conditional expression used (required feature)
    status = 'optimal' if temp_result < 100 else 'suboptimal'
    
    # Use of string method (required feature)
    log_entry = f"Performance: {status}, Peak Count: {len([x for x in adjusted_data if x > 0])}"
    word_count = len(log_entry.upper().split())
    
    # Real contribution to result
    valid_readings = [x for x in adjusted_data if x > 5]
    
    # Simulate dependency on pattern analysis (calls helper)
    dummy_sequence = [1, 3, 2, 5, 4, 6]
    pattern_weight = analyze_pattern(dummy_sequence)
    
    # Final score computation
    base_score = sum(valid_readings)
    final_score = int(base_score + pattern_weight * word_count // 2)
    
    return final_score

# Main execution
baseline = 15
readings = [20, 3, 8, 12, 5, 18, 7, 9]

# Key statement
final_score = calculate_performance(baseline, readings)
print(f"Result: {final_score}")