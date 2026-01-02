def analyze_component(values, threshold=10):
    count = 0
    temp_sum = 0
    for i, val in enumerate(values):
        if val > threshold:
            count += 1
            temp_sum += val
    return count, temp_sum


def validate_sequence(seq):
    valid = True
    for a, b in zip(seq, seq[1:]):
        if abs(a - b) > 5:
            valid = False
    return valid

benchmark_data = [8, 12, 15, 3, 20, 7, 14]

# Irrelevant pre-processing (distractor)
duplicate_check = [x for x in benchmark_data if benchmark_data.count(x) > 1]
unique_flag = len(duplicate_check) == 0

# Semi-relevant transformation (partial distractor)
normalized = [x * 1.1 for x in benchmark_data if x > 5]
offset_correction = sum([0.5 for _ in range(3)])  # Red herring computation

# Core logic with conditional expressions and nesting
def calculate_performance(data):
    size_factor = 2 if len(data) >= 5 else 1
    base_score = 0
    adjustment = 0
    
    # First analysis branch
    high_count, total = analyze_component(data, 10)
    
    # Second parallel check (not used in final path but looks important)
    sequence_valid = validate_sequence(data)
    
    # Accumulation with distraction
    temp_result = 0
    for idx, num in enumerate(data):
        if num % 2 == 0 and idx % 2 == 1:
            temp_result += num

    # Conditional logic chain with red herring variables
    if high_count > 2:
        base_score = total * size_factor
        # Distracting nested condition
        if temp_result > 10:
            adjustment = 5  # Never actually applied due to override below
        else:
            adjustment = -3
    else:
        base_score = sum(data) / 2
        adjustment = 10

    # Final override that negates prior logic
    adjustment = len(data) - high_count  # Key reset

    final_value = base_score + adjustment
    
    # Unused dead-end function call structure
    def unused_helper():
        return sum([x**2 for x in data]) / len(data)
    
    return int(final_value)

# Execution point of interest
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")