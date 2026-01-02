from math import log2

def calculate_entropy(freq_dict):
    total = sum(freq_dict.values())
    probabilities = {k: v / total for k, v in freq_dict.items()}
    entropy = 0.0
    for p in probabilities.values():
        if p > 0:
            entropy -= p * log2(p)
    return entropy

# Simulate character frequency in a restricted cipher alphabet
cipher_stream = ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'B']
frequency_map = {}
for char in cipher_stream:
    frequency_map[char] = frequency_map.get(char, 0) + 1

# Irrelevant auxiliary variable (minor distraction)
redundant_sum = sum(frequency_map.values()) + len(frequency_map)

# Core computation
shannon_lambda = lambda x: log2(x) if x > 1 else 0
apply_noise = shannon_lambda(2)

total_entropy = calculate_entropy(frequency_map)
print(f"Result: {total_entropy}")