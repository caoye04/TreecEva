from collections import Counter
import math

def calculate_entropy(frequencies):
    total = sum(frequencies)
    probabilities = [freq / total for freq in frequencies]
    return sum(-p * math.log2(p) for p in probabilities if p > 0)

data_stream = ['A', 'B', 'A', 'C', 'B', 'A', 'D']
char_counts = Counter(data_stream)

frequencies_per_char = list(char_counts.values())
entropy_per_char = calculate_entropy(frequencies_per_char)

# Simulate multiple windows of data
window_sizes = [1, 2, 3]
entropies = []
for w in window_sizes:
    segments = [data_stream[i:i+w] for i in range(0, len(data_stream), w) if data_stream[i:i+w]]
    segment_counts = [Counter(segment) for segment in segments]
    segment_frequencies = [sum(counts.values()) for counts in segment_counts]
    if segment_frequencies:
        entropies.append(calculate_entropy(segment_frequencies))

entropies.append(entropy_per_char)
total_entropy = sum(entropies)
print(f"Result: {total_entropy}")