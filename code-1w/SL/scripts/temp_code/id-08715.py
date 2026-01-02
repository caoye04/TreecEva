from collections import Counter
import math

def calculate_entropy(freq_map):
    total = sum(freq_map.values())
    entropy = 0.0
    for count in freq_map.values():
        if count > 0:
            probability = count / total
            entropy -= probability * math.log2(probability)
    return round(entropy, 3)

text = "abacabad"
frequency_map = Counter(text)
# Some auxiliary analysis not affecting the main computation
distinct_chars = len(frequency_map)
max_freq = max(frequency_map.values())
min_freq = min(frequency_map.values())

def ignore_this():
    return sum([i**2 for i in range(3)])

result = calculate_entropy(frequency_map)
print(f"Target result: {result}")