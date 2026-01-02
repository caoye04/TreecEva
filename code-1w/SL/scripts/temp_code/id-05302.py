def analyze_temperatures(raw_readings):
    adjusted = [temp * 1.8 + 32 for temp in raw_readings if temp > -273.15]
    valid_count = len(adjusted)
    sum_fahrenheit = sum(adjusted)
    average_f = sum_fahrenheit / valid_count if valid_count else 0
    
    # Irrelevant computation - distractor (not used later)
    outlier_count = sum(1 for t in raw_readings if abs(t) > 100)
    temp_variance = sum((t - average_f)**2 for t in adjusted) / valid_count if valid_count else 0
    
    return average_f, valid_count

# Data transformation pipeline
def transform_entries(entries_list):
    indexed = list(enumerate(entries_list))
    paired = list(zip([e[1] * 2 for e in indexed], [e[0] + 1 for e in indexed]))
    processed = [x * y for x, y in paired if y % 2 == 1]
    
    # Dead code path - misleading
    if len(processed) > 100:
        processed = [p // 10 for p in processed]
    
    return processed

# Core scoring logic
def calculate_final_score(data_points):
    base_func = lambda x: x ** 2 if x > 0 else abs(x)
    scores = [base_func(val) for val in data_points]
    
    # Conditional accumulation with nesting
    total = 0
    for i, s in enumerate(scores):
        if i % 3 == 0:
            total += s
        elif i % 5 == 0:
            total -= s // 2
    
    # Extra distraction variables
    peak_score = max(scores) if scores else 0
    decay_factor = 0.95 ** len(scores)
    adjusted_total = total * decay_factor  # Not used
    
    return int(total)

# Main execution flow
sensor_data = [-40, 0, 25, -80, 50, 100, -5, 10]
scaled_data = [x + 273.15 for x in sensor_data]

# First processing stage
mean_temp, count = analyze_temperatures(scaled_data)
intermediate_values = [mean_temp * 10, count * 5, 999]  # 999 is red herring

# Second processing stage
raw_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
processed_data = transform_entries(raw_sequence)

# Final scoring stage
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")