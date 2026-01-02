def analyze_sequence(data):
    temp_result = 0
    auxiliary_sum = 0
    peak_value = float('-inf')
    
    for i in range(len(data)):
        if data[i] > peak_value:
            peak_value = data[i]
        temp_result += data[i] * (i + 1)
        auxiliary_sum += i ** 2  # Irrelevant accumulation

    normalized = temp_result / (len(data) or 1)
    adjustment = 0
    
    # Distractor loop: processes string version but doesn't affect final result
    data_str = ''.join(map(str, data))
    for char in data_str[::2]:  # Every other digit
        if char.isdigit():
            adjustment += int(char) % 3

    return normalized


def validate_stability(measurements):
    if len(measurements) < 3:
        return False
    sorted_vals = sorted(measurements)
    median = sorted_vals[len(sorted_vals) // 2]
    deviation = sum(abs(m - median) for m in measurements) / len(measurements)
    return deviation < 5.0


def evaluate_performance(log_entries, thresholds):
    raw_values = [len(entry.strip()) for entry in log_entries]
    filtered_data = [v for v in raw_values if v >= thresholds['min_length']]
    
    # Real computation path
    base_metric = sum(filtered_data)
    bonus = 0
    
    # Complex distractor: builds a histogram but only uses length
    histogram = {}
    for v in filtered_data:
        rounded = v // 10
        histogram[rounded] = histogram.get(rounded, 0) + 1
    
    # Meaningless recursive helper
    def count_nodes(n):
        if n <= 1:
            return 1
        return count_nodes(n - 2) + count_nodes(n - 1) if n > 5 else n
    
    dummy_tree_size = count_nodes(len(histogram) + 2) if histogram else 0

    # Actual logic continues
    if validate_stability(filtered_data):
        bonus += 15
    
    # Key slicing operation on string representation
    metric_str = str(int(base_metric))
    if len(metric_str) > 2:
        segment = metric_str[-3:-1]  # Extract middle digits
        bonus += int(segment) // 2
    
    final_score = int(analyze_sequence(filtered_data)) + bonus
    
    # Dead code path — never executed due to condition
    if False and dummy_tree_size > 100:
        correction = len([x for x in log_entries if 'ERR' in x])
        final_score -= correction * 5
    
    return final_score

# Input data
logs = [
    "  session_start  ",
    "data_flow_initiated",
    "  processing_complete  ",
    "final_state_verified"
]

thresholds = {"min_length": 10}

result = evaluate_performance(logs, thresholds)
print(f"Target result: {result}")