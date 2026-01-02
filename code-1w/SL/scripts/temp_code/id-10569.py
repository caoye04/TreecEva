from collections import Counter
import math

def calculate_entropy(freq_dict):
    total = sum(freq_dict.values())
    entropy = 0.0
    for count in freq_dict.values():
        probability = count / total
        if probability > 0:
            entropy -= probability * math.log2(probability)
    return entropy

data_stream = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'D', 'C', 'A']
frequency_counts = Counter(data_stream)
redundant_list = [x for x in range(len(data_stream)) if x % 2 == 0]
base_value = len(frequency_counts)
total_entropy = calculate_entropy(frequency_counts)
Result: {total_entropy}