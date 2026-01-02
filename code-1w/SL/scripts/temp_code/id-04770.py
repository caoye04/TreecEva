def calculate_entropy(freq_map):
    import math
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        if count > 0:
            probability = count / total
            entropy -= probability * math.log2(probability)
    return entropy

# Problem setup: analyze character frequency in a diagnostic string
input_data = "aabbbbcccddee"
frequency_map = {}
for char in input_data:
    frequency_map[char] = frequency_map.get(char, 0) + 1

# Use set operations to identify unique even-count characters
char_counts = list(frequency_map.values())
even_count_chars = set(char for char, cnt in frequency_map.items() if cnt % 2 == 0)
odd_count_chars = set(frequency_map.keys()) - even_count_chars

# Perform modular arithmetic on length-related properties
data_length = len(input_data)
mod_offset = data_length % 3
adjusted_counts = [cnt + mod_offset for cnt in char_counts]

# Compute entropy based on original frequencies
scaling_factor = 1.0
if len(even_count_chars) > len(odd_count_chars):
    scaling_factor = 0.5

intermediate_sum = 0
for i, cnt in enumerate(adjusted_counts):
    intermediate_sum += cnt * (i + 1)

# Key computation step
normalizer = sum(char_counts)
scaled_entropy_component = 0.0
if normalizer > 0:
    scaled_entropy_component = intermediate_sum / normalizer

# Final entropy calculation from frequency map
total_entropy = calculate_entropy(frequency_map)

# Print final result as required
print(f"Result: {total_entropy}")