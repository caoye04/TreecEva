def analyze_signal(samples, threshold=0.75):
    filtered = [s for s in samples if abs(s) > threshold]
    power = sum([x ** 2 for x in filtered]) / len(filtered) if filtered else 0
    return power

# Irrelevant helper (distractor)
def smooth_data(data):
    return [sum(data[max(0, i-1):i+2]) / min(3, i+2) for i in range(len(data))]

# Unused function (dead code path)
def legacy_calibrate(x):
    return (x * 0.987) + 1.2

# Sensor simulation constants (mix of relevant and irrelevant)
base_frequency = 440
harmonic_series = [base_frequency * (i+1) for i in range(8)]
noise_floor = [0.01, -0.02, 0.015, -0.008]
dummy_offsets = {f'chan_{i}': i * 0.003 for i in range(1, 10)}

# Primary data structures with slicing and dictionary ops
sensor_readings = {
    'A1': [0.1, 0.3, 0.8, 1.2, 0.9, 0.4, 0.2],
    'B2': [0.2, 0.1, 0.05, 0.01, 0.03],
    'C3': [0.9, 1.1, 1.3, 0.95]
}

# Extract and slice only relevant sensor
raw_sequence = sensor_readings['A1'][1:6]  # Take middle segment

# Signal processing chain
normalized = [x / max(raw_sequence) for x in raw_sequence]
calibration_sequence = [round(x, 3) for x in normalized]

# Bit manipulation red herring (irrelevant to final result)
bit_flags = 0b101010
shifted_mask = (bit_flags << 3) & 0b11111111
inverted = ~shifted_mask & 0xFF

# Set operations as distractors
active_sensors = set(sensor_readings.keys())
excluded_sensors = {'B2', 'D4'}
valid_sensors = active_sensors - excluded_sensors

# Simulated diagnostic codes (mostly unused)
diagnostics = {
    'baseline': 1842,
    'tolerance': 0.05,
    'version': 'v2.3',
    'flags': [1, 0, 1],
    'history': [1842, 1845, 1838]
}

# Decoy calculation with combinatorics distraction
from math import comb
possible_pairs = sum(comb(len(seq), 2) for seq in sensor_readings.values() if len(seq) >= 2)

# Real logic buried among distractions
def evaluate_stability(seq):
    if len(seq) < 3:
        return 0
    peaks = 0
    for i in range(1, len(seq)-1):
        if seq[i-1] < seq[i] > seq[i+1]:
            peaks += 1
    return peaks

def integrate_phase(signal):
    accumulated = 0
    for i, val in enumerate(signal):
        accumulated += val * (i % 2 == 0)  # Only even indices
    return round(accumulated, 3)

def process_metrics(seq, meta):
    # Key computation hidden in multi-step process
    stability = evaluate_stability(seq)
    phase_integral = integrate_phase(seq)
    reference = meta['baseline']
    
    # Red herring: complex-looking but unused transformation
    dummy_transform = [((x * 1000) ** 2) % 97 for x in seq]
    shuffle_probe = dummy_transform[::2]  # Slicing distractor
    
    # Actual answer computation
    score_component = stability * 100
    adjustment = int(phase_integral * 50)
    final_value = reference - score_component + adjustment
    
    # More decoys
    stats_summary = {
        'count': len(seq),
        'unique': len(set(seq)),
        'mid_range': (max(seq) + min(seq)) / 2
    }
    
    # This variable is critical
    final_diagnostic = final_value
    
    # Dead code assignment (misleading)
    final_diagnostic = final_diagnostic  # No-op reassignment
    
    return final_diagnostic

# Execution flow with misleading intermediate prints
interim_power = analyze_signal(noise_floor + calibration_sequence)

# Critical statement
final_diagnostic = process_metrics(calibration_sequence, diagnostics)

print(f"Result: {final_diagnostic}")