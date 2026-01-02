from collections import Counter

# Simulate signal processing: analyze frequency peaks in a sampled waveform
data_stream = [1, 2, 2, 3, 3, 3, 4, 4, 2, 2, 1, 5, 5, 5, 5, 3, 3, 3, 3]

# Count occurrences of each signal level
counts = Counter(data_stream)

# Normalize counts to frequencies
sample_size = len(data_stream)
base_frequencies = {key: count / sample_size for key, count in counts.items()}

# Identify the highest frequency component
peak_frequency = max(base_frequencies.values())

# Irrelevant auxiliary variable (minimal distraction)
total_energy = sum(x**2 for x in data_stream)

print(f"Result: {peak_frequency}")