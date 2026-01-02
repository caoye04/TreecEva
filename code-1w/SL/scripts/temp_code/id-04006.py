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

# Simulate character frequency in a coded message fragment
message = 'aabacbeddce'
frequency_map = Counter(message)

# Extra but harmless: analyze unique chars (not used in entropy)
unique_chars = len(frequency_map)

# Core computation
normalized_freq = {k: v / len(message) for k, v in frequency_map.items()}
total_entropy = calculate_entropy(frequency_map)

# Print result as required
print(f"Target result: {total_entropy}")