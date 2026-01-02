from collections import Counter
import math

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        if count > 0:
            probability = count / total
            entropy -= probability * math.log2(probability)
    return entropy

data_stream = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C', 'A']
frequency_map = Counter(data_stream)
redundant_sum = sum([x**2 for x in range(3)])  # distractor
normalization_factor = len(data_stream)

# Key computation
adjusted_counts = {k: v + 0.1 for k, v in frequency_map.items()}
renormalized_total = sum(adjusted_counts.values())
total_entropy = calculate_entropy(frequency_map)

total_entropy = round(total_entropy, 4)
print(f"Result: {total_entropy}")