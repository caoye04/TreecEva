def analyze_pattern(data, base):
    adjustment_factor = 0.85
    temp_result = 0
    cumulative = [0] * len(data)
    
    for i in range(len(data)):
        if i == 0:
            cumulative[i] = data[i]
        else:
            cumulative[i] = cumulative[i-1] + data[i]
    
    # Irrelevant transformation (distractor)
    transformed = [x * adjustment_factor for x in data if x > 5]
    ignored_sum = sum(transformed)  # Not used later
    
    slice_window = cumulative[1:-1]  # Use of slicing - relevant
    if len(slice_window) == 0:
        slice_window = [0]
    
    avg_middle = sum(slice_window) / len(slice_window)
    
    # Secondary loop with early break (semi-relevant)
    trend = 0
    for val in data:
        if val > base:
            trend += 1
            if trend > 2:
                break  # Early exit pattern
    
    # Dead code path (distractor)
    if base < 0:
        dummy = [i ** 2 for i in range(10)]
        temp_result += sum(dummy)

    # Core logic: compute threshold_score
    volatility_index = max(data) - min(data)
    stability_score = avg_middle * (1 + trend / 10)
    threshold_score = int(stability_score - volatility_index * 0.5)

    return threshold_score

# Main execution
metrics = [12, 7, 9, 15, 6, 11]
baseline = 8
interim = [x ** 2 for x in metrics if x % 2 == 0]  # Unused computation
auxiliary_total = sum(interim)  # Distractor variable

threshold_score = analyze_pattern(metrics, baseline)
print(f"Result: {threshold_score}")