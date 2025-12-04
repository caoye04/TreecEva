from collections import defaultdict

def calculate_weighted_sum(data_points, weights):
    # This is a distractor function that won't be used meaningfully
    weighted_sum = 0
    for i, point in enumerate(data_points):
        weighted_sum += point * weights[i % len(weights)]
    return weighted_sum

# Main computation starts here
input_sequence = [8, 15, 22, 5, 19, 12, 25, 3]
processing_factors = [2, 4, 1, 3]

# Initial processing - this part is relevant
processed_values = []
for i, num in enumerate(input_sequence):
    factor = processing_factors[i % len(processing_factors)]
    processed = (num * factor) // 2 if num % 2 == 0 else (num + factor) * 3
    processed_values.append(processed)

# Create frequency map using defaultdict - relevant computation
frequency_map = defaultdict(int)
for value in processed_values:
    frequency_map[value] += 1

# Distractor computation that looks important but isn't
redundant_calc = sum(input_sequence) * len(processing_factors)
temp_buffer = [x ^ 7 for x in input_sequence[:4]]  # Unused bitwise operations

# Core logic - finding the most frequent processed value
most_frequent_value = None
max_count = 0
for value, count in frequency_map.items():
    if count > max_count:
        max_count = count
        most_frequent_value = value

# More distractor operations
misleading_adjustment = (most_frequent_value >> 2) + 10
unused_ratio = len(input_sequence) / len(processing_factors)

# Final computation - this is what matters
processed_value = most_frequent_value
adjustment_factor = (processed_values[3] + processed_values[6]) // 4
final_output = processed_value + adjustment_factor

# Print the result
print(f"Result: {final_output}")