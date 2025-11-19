import math
from functools import reduce

def hamming_window(n, N):
    return 0.54 - 0.46 * math.cos(2 * math.pi * n / (N - 1))

def process_signal_samples():
    N = 10
    samples = [1.0] * N  # Unit amplitude samples
    
    # Apply windowing function using map and lambda
    window_values = list(map(lambda n: hamming_window(n, N), range(N)))
    windowed_samples = list(map(lambda pair: pair[0] * pair[1], zip(samples, window_values)))
    
    # Compute energy contributions using list comprehension
    energy_contributions = [s**2 for s in windowed_samples]
    
    # Find maximum energy contribution
    max_energy = reduce(lambda a, b: a if a > b else b, energy_contributions)
    
    # Count significant contributions using filter and lambda
    threshold = max_energy / 2.0
    significant_contributions = len(list(filter(lambda e: e > threshold, energy_contributions)))
    
    return significant_contributions

# Execute the signal processing pipeline
significant_contributions = process_signal_samples()
print(f"Result: {significant_contributions}")