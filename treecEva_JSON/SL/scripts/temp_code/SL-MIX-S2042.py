import math
from collections import namedtuple
from statistics import variance

def compute_entropy_metric(freq_data):
    if not freq_data:
        return 0
    total = sum(freq_data)
    probabilities = [f/total for f in freq_data]
    entropy_terms = [-p * math.log2(p) for p in probabilities if p > 0]
    return sum(entropy_terms)

def gcd_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = math.gcd(result, num)
    return result

def lcm_of_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = abs(result * num) // math.gcd(result, num)
    return result

# Signal processing pipeline
SignalProfile = namedtuple('SignalProfile', ['frequencies', 'amplitudes'])

with open('temp_signal.txt', 'w') as f:
    f.write('5,10,15,20\n2,4,6,8')

processed_signals = []

with open('temp_signal.txt', 'r') as f:
    for line in f:
        values = list(map(int, line.strip().split(',')))
        if len(values) % 2 == 0:
            mid = len(values) // 2
            freqs, amps = values[:mid], values[mid:]
            profile = SignalProfile(freqs, amps)
            processed_signals.append(profile)

# Compute metrics
frequency_sets = [list(signal.frequencies) for signal in processed_signals]
all_frequencies = [freq for freq_set in frequency_sets for freq in freq_set]

base_entropy = compute_entropy_metric(all_frequencies)
exponent_factor = math.exp(0.1 * len(processed_signals))
gcd_value = gcd_of_list(all_frequencies)
lcm_value = lcm_of_list([10, 15, 20])

variance_component = variance(all_frequencies) if len(all_frequencies) > 1 else 0

# Final acoustic index calculation
acoustic_index = (
    (base_entropy * exponent_factor) + 
    (math.log(lcm_value) / math.log(gcd_value)) - 
    (variance_component ** 0.5)
) * 100

print(f"Result: {int(acoustic_index)}")

# Clean up
import os
os.remove('temp_signal.txt')