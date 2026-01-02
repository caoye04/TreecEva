from math import log2

def calculate_entropy(frequencies):
    total = sum(frequencies)
    probabilities = [freq / total for freq in frequencies if freq > 0]
    entropy = [-p * log2(p) for p in probabilities]
    return sum(entropy)

data_streams = [
    [4, 1, 1, 2, 6],
    [3, 3, 3, 3],
    [5, 0, 5]
]

# Compute entropy for each data stream
temp_results = []
for idx, stream in enumerate(data_streams):
    entropy = calculate_entropy(stream)
    temp_results.append((idx, entropy))

# Extract only the entropy values using zip and list comprehension
indices, entropy_values = zip(*temp_results)

# Final aggregation step
total_entropy = sum(entropy_values)
print(f"Result: {total_entropy}")