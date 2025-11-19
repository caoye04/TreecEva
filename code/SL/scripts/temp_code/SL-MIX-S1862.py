import re
from collections import defaultdict

def modular_transform(x, mod_base=17):
    return (x * 3 + 7) % mod_base

def extract_frequencies(signal_data):
    pattern = r'freq_(\d+)'
    matches = re.findall(pattern, signal_data)
    return [int(m) for m in matches]

# Audio signal metadata
signal_metadata = "freq_42 amp_15 freq_73 noise_freq_29 freq_18 phase_5 freq_91"

# Extract frequency components using regex
frequencies = extract_frequencies(signal_metadata)

# Apply modular transformation to each frequency
transformed_freqs = [modular_transform(f) for f in frequencies]

# Count occurrences of each transformed frequency
frequency_counter = defaultdict(int)
for freq in transformed_freqs:
    frequency_counter[freq] += 1

# Calculate weighted signal strength using lambda function
weight_function = lambda f, c: (f ** 2) * c + (f % 5)
signal_strengths = [weight_function(freq, count) for freq, count in frequency_counter.items()]

# Apply another modular transformation
final_modulus = 13
processed_signal_strength = sum(signal_strengths) % final_modulus

print(f"Result: {processed_signal_strength}")