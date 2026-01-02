from itertools import combinations
import math

def calculate_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probabilities)

# System signal levels across 4 channels
channel_signals = [8, 12, 5, 15]

# Generate all possible 3-channel combinations and compute their entropy
entropies = []
for combo in combinations(channel_signals, 3):
    entropy = calculate_entropy(combo)
    entropies.append(round(entropy, 4))

# Discard lowest entropy measurement (system noise filter)
del entropies[0]  # Simulate removal of anomalous low-complexity signal

# Final aggregated system entropy
total_entropy = sum(entropies)

print(f"Result: {total_entropy}")