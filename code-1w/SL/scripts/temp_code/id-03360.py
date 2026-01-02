from collections import Counter
import math

def calculate_entropy(frequencies):
    total = sum(frequencies)
    probabilities = [freq / total for freq in frequencies]
    entropy = [-p * math.log2(p) if p > 0 else 0 for p in probabilities]
    return sum(entropy)

data_stream = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 1, 1]
counts = Counter(data_stream)
freqs = list(counts.values())

# Compute entropy for each unique symbol group
symbol_entropies = []
for freq in freqs:
    window = [freq] * 2  # artificial expansion for uniform blocks
    entropy = calculate_entropy(window)
    symbol_entropies.append(entropy)

total_entropy = sum(symbol_entropies)

# Irrelevant auxiliary calculation (minimal interference)
dummy_sum = sum([i * 2 for i in range(len(freqs))])

Result: {total_entropy}