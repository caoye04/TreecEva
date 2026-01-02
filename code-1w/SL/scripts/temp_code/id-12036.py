from collections import Counter
import math

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    probabilities = [count / total for count in freq_map.values()]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 3)

data_stream = 'aabbcddddeeeee'
frequency_map = Counter(data_stream)

# Irrelevant auxiliary variable (minor distraction)
redundant_copy = data_stream[::-1]

# Key computation step
total_entropy = calculate_entropy(frequency_map)

Result: total_entropy