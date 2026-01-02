def process_data(items, limit):
    # Irrelevant tracking variables (distractors)
    total_iterations = 0
    phantom_counter = 0
    
    # Useful intermediate structures
    squared_values = [x ** 2 for x in items if x > 0]
    filtered_items = []
    temp_accum = 0

    # Misleading bitwise manipulation (not used in final logic)
    masked_values = []
    for val in items:
        masked_val = val ^ 7 & 3  # Distractor computation
        masked_values.append(masked_val)
        phantom_counter += 1  # Dead path counter

    # Core logic: filter and transform
    for item in items:
        total_iterations += 1
        if item < limit:
            adjusted = item + (item % 4) * 2
            temp_accum += adjusted
            filtered_items.append(adjusted)
    
    # Lambda-based transformation (required python feature)
    scale_func = lambda x: x * 1.5 if x > 5 else x * 0.8
    scaled_filtered = [int(scale_func(x)) for x in filtered_items]
    
    # Red herring: set operation with no impact
    unique_scaled = set(scaled_filtered)
    set_expansion = [x + 10 for x in unique_scaled if x < 0]  # Unused

    # Actual answer computation
    filtered_sum = sum(scaled_filtered) // (len(scaled_filtered) or 1)  # Avoid zero-division
    
    # More irrelevant computation
    outlier_count = 0
    for x in scaled_filtered:
        if x > 20:
            outlier_count += 1

    final_result = filtered_sum + len(unique_scaled)  # Only filtered_sum matters
    return final_result

# Input setup
data = [3, -1, 4, 7, 2, 8, -5]
threshold = 6
result_placeholder = 0
unused_snapshot = data.copy()

# Execution point of interest
final_result = process_data(data, threshold)

# Output target variable: filtered_sum is computed inside function but not returned directly
# We must infer its value from logic; final_result = filtered_sum + len(unique_scaled)
# So filtered_sum = final_result - len(unique_scaled)

# Recompute filtered_sum explicitly for verification within constraints
squared_values = [x**2 for x in data if x > 0]
filtered_items = []
for item in data:
    if item < threshold:
        adjusted = item + (item % 4) * 2
        filtered_items.append(adjusted)
scale_func = lambda x: x * 1.5 if x > 5 else x * 0.8
scaled_filtered = [int(scale_func(x)) for x in filtered_items]
filtered_sum = sum(scaled_filtered) // len(scaled_filtered)
print(f"Result: {filtered_sum}")