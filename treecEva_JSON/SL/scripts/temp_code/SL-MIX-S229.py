import math
from functools import reduce

def modular_sqrt_sum(values, mod):
    return sum(int(math.sqrt(x)) % mod for x in values if x >= 0)

def process_frequency_bins(base_freq, harmonics):
    bins = [base_freq * h for h in harmonics]
    windowed = [bins[i] * (0.54 - 0.46 * math.cos(2 * math.pi * i / (len(bins) - 1))) for i in range(len(bins))]
    normalized = [int(w) % 1000 for w in windowed]
    return normalized

def aggregate_chunks(data, chunk_size):
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    sums = [reduce(lambda a, b: a + b, chunk, 0) for chunk in chunks]
    return reduce(lambda a, b: a + b, sums, 0)

# Signal processing parameters
harmonic_series = [1, 2, 3, 5, 8, 13, 21]
fundamental_frequency = 440.0

# Process the frequency bins with windowing
processed_bins = process_frequency_bins(fundamental_frequency, harmonic_series)

# Apply modular square root transformation
transformed_values = [modular_sqrt_sum([x], 97) for x in processed_bins]

# Remove zero values and convert to set for uniqueness
unique_signals = frozenset(filter(lambda x: x > 0, transformed_values))

# Convert back to list and sort for divide-and-conquer aggregation
signal_list = sorted(list(unique_signals))

# Perform chunked aggregation using divide and conquer
sync_metric = aggregate_chunks(signal_list, 3)

print(f"Result: {sync_metric}")