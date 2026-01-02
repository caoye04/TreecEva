from itertools import combinations

# Simulate sensor readings and security key generation
temperature_reads = [21, 26, 19, 34, 28]
humidity_reads = [45, 53, 38, 60]

# Calculate derived signal values using pairwise combinations
signal_pairs = list(combinations(temperature_reads, 2))
derived_signals = [(a + b) % 29 for a, b in signal_pairs]

# Generate diagnostic checksum (irrelevant distractor)
diagnostic_checksum = sum(humidity_reads) * 0.5

# Critical security logic
base_key = 17
offset = 5
secure_keys = [((key + offset) | base_key) & 31 for key in derived_signals]

# Key computation step
energy_threshold = max(secure_keys) ^ (1 << 3)

# Output result as required
print(f"Target result: {energy_threshold}")