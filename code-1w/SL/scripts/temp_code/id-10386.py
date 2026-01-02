from collections import Counter
import math
from functools import reduce

# Simulate character frequency analysis for a coded message fragment
def calculate_entropy(freq_map):
    total_chars = sum(freq_map.values())
    probabilities = map(lambda x: x / total_chars, freq_map.values())
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 4)

# Observed character counts from intercepted communication
raw_message = "aabbbccccddddd"
frequency_map = Counter(raw_message)

# Auxiliary calculation: total pairs (irrelevant but plausible)
total_pairs = sum([i for i in range(len(raw_message)) if i % 3 == 0])

# Main computation
reduced_freq = dict(filter(lambda item: item[1] > 2, frequency_map.items()))
total_entropy = calculate_entropy(frequency_map)

# Print final result as required
print(f"Target result: {total_entropy}")