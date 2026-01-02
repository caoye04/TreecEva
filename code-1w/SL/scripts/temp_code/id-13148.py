def calculate_final_score(data):
    # Irrelevant transformation (distractor)
    normalized = [round(x * 0.9 + 5, 2) for x in data if x > 10]
    
    # Semi-relevant filtering with side computation
    filtered = [x for x in data if x % 2 == 1]
    temp_sum = sum([x ** 2 for x in filtered if x < 50])  # Unused later

    # Core logic: sum odd numbers divisible by 3, then apply transform
    core_values = list(filter(lambda x: x % 3 == 0 and x % 2 == 1, data))
    base_score = sum(core_values)
    
    # Additional processing with red herring variables
    adjustment_factor = len([x for x in data if x < 0])  # Always zero in input
    offset = 10 if any(x > 100 for x in data) else 5  # Not triggered
    
    # Actual score calculation
    raw_score = base_score * 3 - 7
    final_score = raw_score + offset
    
    return final_score

# Simulated sensor readings (clean data)
data_points = [15, 22, 9, 45, 60, 33, 7, 18, 99, 104]

# Preprocessing step with distraction
processed_data = []
for val in data_points:
    if val >= 0:
        processed_data.append(val)
    else:
        processed_data.append(0)  # Dead code path (no negatives)

# Distractor: unused statistical summary
mean_val = sum(processed_data) / len(processed_data)
variance_proxy = sum((x - mean_val) ** 2 for x in processed_data) / len(processed_data)

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")