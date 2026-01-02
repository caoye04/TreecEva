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
    
    # Distractor: analyze trend but not used in final result
    stable_periods = 0
    for t in trend:
        if t == 0:
            stable_periods += 1

    return sum(sequence)


def validate_string_format(s):
    # Uses string method - required feature
    if s.startswith('DATA') and s.endswith('END'):
        cleaned = s[4:-3].strip()
        parts = cleaned.split('|')
        return len(parts) == 4 and all(p.isdigit() for p in parts)
    return False


def calculate_final_score(raw_data, limits):
    # Complex processing with lists and conditionals
    processed = []
    temp_sum = 0
    
    for item in raw_data:
        if isinstance(item, str):
            # String preprocessing - partially irrelevant
            if validate_string_format(item):
                nums = [int(x) for x in item[4:-3].split('|')]
                temp_sum += sum(nums)
        elif isinstance(item, list):
            processed.extend(item)
    
    # Core logic begins here
    base_total = sum(processed)
    adjustment_factor = 0.0
    
    # Multiple conditions with red herring variables
    above_limit_count = 0
    adjusted_values = []
    for val in processed:
        if val > limits['max']:
            above_limit_count += 1
        adjusted_values.append(val * 0.9 if val % 2 == 0 else val * 1.1)
    
    # Real computation path
    adjusted_total = sum(adjusted_values)
    if len(processed) > 5:
        adjustment_factor = 1.2
    else:
        adjustment_factor = 0.8
    
    # Secondary distractor: complex but unused recursion
    def recursive_sum(n):
        return n + recursive_sum(n-1) if n > 0 else 0
    
    unused_computation = recursive_sum(10)  # Dead-end computation
    
    # Final score calculation - this is what matters
    raw_score = base_total * adjustment_factor
    penalty = above_limit_count * 5
    final_score = int(raw_score - penalty + 10)  # deterministic integer result
    
    # Print required output format
    print(f"Target result: {final_score}")
    return final_score

# Main execution
raw_input_data = [
    "DATA|15|20|8|42|END",
    [12, 18, 25, 30, 14, 19],
    "INVALID|1|2|3|END",
    [7, 11]
]

thresholds = {'max': 20}

# Key statement
final_score = calculate_final_score(raw_input_data, thresholds)