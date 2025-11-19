import math

# Frequency components and their amplitudes
frequency_spectrum = {'alpha': 4, 'beta': 9, 'gamma': 16, 'delta': 25}

# Weighting function using logarithmic scaling
weight_func = lambda amp: math.log(amp + 1) * 2

# Process each frequency component
weighted_values = {band: weight_func(amp) for band, amp in frequency_spectrum.items()}

# Calculate final response as sum of weighted values raised to power of 1.5
final_response = sum(value ** 1.5 for value in weighted_values.values())

print(f'Result: {round(final_response)}')