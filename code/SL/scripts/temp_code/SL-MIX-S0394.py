import math
from collections import defaultdict

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def calculate_harmonic_index(freq):
    if freq <= 0:
        return 0
    return int(math.log(freq) * 10) + 1

# Signal frequency data from deep space observations
signal_frequencies = [23, 45, 67, 89, 101, 113, 131, 157, 179, 191]

# Initialize data structures
harmonic_map = defaultdict(set)
frequency_sets = []

# Process each frequency to build harmonic mappings
for freq in signal_frequencies:
    index = calculate_harmonic_index(freq)
    if is_prime(index):
        harmonic_map[index].add(freq)
        
# Apply set operations to identify unique signatures
base_set = frozenset(signal_frequencies)
for idx, freq_set in harmonic_map.items():
    if idx % 2 == 1:  # Odd indices
        intersected = base_set & freq_set
        frequency_sets.append(intersected)
    else:  # Even indices
        unioned = base_set | freq_set
        frequency_sets.append(unioned)
        
# Count unique signatures using lambda function
signature_counter = lambda sets: sum(len(s) for s in sets)
final_signature_count = signature_counter(frequency_sets)

print(f"Result: {final_signature_count}")