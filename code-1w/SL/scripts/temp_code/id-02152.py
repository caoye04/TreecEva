import itertools

def generate_harmonic_series(n):
    return [1 / (i + 1) for i in range(n)]

def calculate_stability_index(fluctuations, threshold):
    filtered = [f for f in fluctuations if f > threshold]
    weighted = list(map(lambda x: x ** 2 * 1.75, filtered))
    base_score = sum(weighted) / len(weighted) if weighted else 0
    
    # Distractor: irrelevant signal processing
    dummy_signal = [x * 0.1 for x in range(len(fluctuations))]
    noise_floor = sum(itertools.accumulate(dummy_signal)) / 1000
    adjusted_score = base_score - noise_floor  # Slight interference

    # Additional distractor variables
    temp_analysis = []
    for i in range(len(fluctuations)):
        if fluctuations[i] > threshold * 2:
            temp_analysis.append(fluctuations[i] * 0.01)
    
    # Real computation path
    correction_factor = 1.0
    if len(filtered) > 5:
        correction_factor *= 1.2
    elif len(filtered) == 3:
        correction_factor *= 0.9
    else:
        correction_factor *= 1.1

    final_index = adjusted_score * correction_factor
    
    # Dead code path (never executed due to data)
    if threshold < 0:
        return -1 * final_index
        extra_analysis = [0] * 10  # unreachable

    return final_index

# Main simulation setup
energy_levels = [0.12, 0.33, 0.41, 0.55, 0.67, 0.49, 0.72, 0.39, 0.51]
delta_t = 0.05
sampling_rate = 100

# Irrelevant transformation
scaled_levels = [level * 1.02 for level in energy_levels]
signal_power = sum([s**2 for s in scaled_levels]) / len(scaled_levels)

# Real input construction
energy_fluctuations = []
for a, b in zip(energy_levels[:-1], energy_levels[1:]):
    diff = abs(b - a)
    energy_fluctuations.append(diff)

# Add minor smoothing (partially relevant)
smoothed = [sum(energy_fluctuations[max(i-1,0):i+2]) / min(i+2, 3) for i in range(len(energy_fluctuations))]
energy_fluctuations = smoothed  # update with smoothed values

# Introduce distractor sequence
sequence_meta = list(itertools.combinations([1,2,3,4], 2))
combination_offset = len(sequence_meta) * 0.001  # unused except in noise

# Key statement
thermal_capacity = calculate_stability_index(energy_fluctuations, threshold=0.45)

# Print result
print(f"Result: {thermal_capacity}")