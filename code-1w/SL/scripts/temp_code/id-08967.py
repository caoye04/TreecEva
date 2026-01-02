def calculate_weighted_sum(data):
    weights = [i ** 0.5 for i in range(1, len(data) + 1)]
    weighted_values = [a * b for a, b in zip(data, weights)]
    return sum(weighted_values)

# Simulate sensor readings with noise filtering
data_points = [12, 15, 10, 18, 22, 14]

# Irrelevant transformation (distractor)
ascii_shift = sum(ord(c) for c in 'dummy') % 5
offset_data = [x + ascii_shift for x in data_points]

# Filtering and processing relevant data
filtered_data = list(filter(lambda x: x > 13, data_points))
expanded_data = [(i, val) for i, val in enumerate(filtered_data)]
processed_data = [val ** 2 for i, val in expanded_data if i % 2 == 0]

# Red herring computation (dead path)
temp_result = 0
for i in range(3):
    temp_result += i * 100  # Unused later

# Key computational chain
baseline = sum(processed_data) // len(processed_data)
adjusted_data = [x - baseline for x in processed_data]

# Final output calculation
final_output = calculate_weighted_sum(processed_data)

# Print result for evaluation
print(f"Result: {final_output}")