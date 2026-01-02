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

data_stream = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'D', 'D', 'D']
frequency_counter = Counter(data_stream)
baseline = len(data_stream)
normalized_baseline = baseline / 10  # normalization factor (irrelevant to final result)
adjusted_entropy = 0  # distraction variable
flag = True  # control flag for hypothetical branching (not used)
total_entropy = calculate_entropy(frequency_counter)
print(f"Result: {total_entropy}")