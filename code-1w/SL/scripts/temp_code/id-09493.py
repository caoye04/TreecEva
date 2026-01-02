from itertools import combinations, cycle

# Simulate sensor array signal processing with interference patterns
def generate_harmonic_series(frequency, phase, count):
    return [(frequency * i + phase) % 360 for i in range(1, count + 1)]

def detect_coherence(harmonics):
    coherent_pairs = 0
    for a, b in combinations(harmonics, 2):
        if abs(a - b) < 10 or abs(a - b) > 350:
            coherent_pairs += 1
    return coherent_pairs

def calculate_interference_phase(signals):
    total_phase = 0
    adjustment_factor = 1.5
    for sig in signals:
        base = sum(sig) / len(sig)
        if base > 180:
            base -= 360
        total_phase += base * adjustment_factor
    return round(total_phase, 4)

# Sensor inputs with different harmonic profiles
sensor_a = generate_harmonic_series(23, 15, 8)
sensor_b = generate_harmonic_series(17, 310, 8)
sensor_c = generate_harmonic_series(19, 95, 8)

# Analyze coherence (distractor: not used in final calculation but plausible)
diagnostic_coherence = {
    'a_self': detect_coherence(sensor_a),
    'b_self': detect_coherence(sensor_b),
    'c_self': detect_coherence(sensor_c)
}

# Apply filtering (semi-relevant preprocessing)
filtered_a = [x for x in sensor_a if 10 < x < 350]
filtered_b = [x for x in sensor_b if x > 50]
filtered_c = [x for x in sensor_c if x < 300]

# Construct composite signals with padding to equalize lengths
max_len = max(len(filtered_a), len(filtered_b), len(filtered_c))
cycle_a = [val for val, _ in zip(cycle(filtered_a), range(max_len))]
cycle_b = [val for val, _ in zip(cycle(filtered_b), range(max_len))]
cycle_c = [val for val, _ in zip(cycle(filtered_c), range(max_len))]

composite_signals = [cycle_a, cycle_b, cycle_c]

# Introduce red herring computation: frequency domain approximation
signal_energy = sum(sum(sig)**2 for sig in composite_signals) / 1e4
normalization_constant = len(composite_signals) * max_len
energy_ratio = signal_energy / normalization_constant if normalization_constant else 0

# Key statement
net_phase_shift = calculate_interference_phase(composite_signals)

# Dead code path (distractor)
if energy_ratio > 1:
    net_phase_shift *= 0.9

# Output result
print(f"Result: {net_phase_shift}")