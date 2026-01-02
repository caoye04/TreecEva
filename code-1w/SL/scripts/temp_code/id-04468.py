def analyze_metrics(values, threshold=10):
    count = 0
    temp_sum = 0
    for i, val in enumerate(values):
        if val > threshold:
            count += 1
            temp_sum += val
    return temp_sum if count > 0 else 0


def validate_sequence(seq):
    valid = True
    for x in seq:
        if x < 0:
            valid = False
    return valid


def calculate_performance(data):
    adjusted = []
    offset = len(data) // 2
    
    for idx, item in enumerate(data):
        transformed = (item ** 2) + offset
        if idx % 2 == 0:
            transformed -= 3
        adjusted.append(transformed)
    
    # Irrelevant tracking variables (distractors)
    total_iterations = 0
    peak_value = float('-inf')
    for x in adjusted:
        total_iterations += 1
        if x > peak_value:
            peak_value = x
    
    # Semi-relevant filtering
    filtered = [x for x in adjusted if x % 4 == 0]
    
    helper_sum = sum(filtered)
    
    # Additional distraction: unused intermediate calculation
    average_filtered = helper_sum / len(filtered) if filtered else 0
    outlier_count = 0
    for f in filtered:
        if f > 50:
            outlier_count += 1
    
    # Core logic path
    base_score = helper_sum // 3 if helper_sum > 0 else 0
    bonus = 5 if len(filtered) >= 3 else 0
    penalty = 2 * (len(data) - len(filtered))
    
    final_score = base_score + bonus - penalty
    
    # Print required at end
    print(f"Result: {final_score}")
    
    return final_score

# Main execution
raw_input = [4, 7, 2, 8, 5]

# Preprocessing distraction
processed_data = []
for index, value in enumerate(zip(raw_input[:-1], raw_input[1:])):
    diff = value[1] - value[0]
    processed_data.append(abs(diff))

# Actual benchmark data
benchmark_data = [3, 4, 6, 8, 2]

# Validate data (not actually used later — red herring)
is_valid = validate_sequence(benchmark_data)

# Analyze metrics (side computation)
analysis_result = analyze_metrics(benchmark_data, threshold=5)

# Key statement
final_score = calculate_performance(benchmark_data)