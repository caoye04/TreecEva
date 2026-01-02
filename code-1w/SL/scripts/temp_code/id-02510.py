from collections import defaultdict
from itertools import combinations

# Simulate wave interference in a multi-path signal transmission system
def simulate_signal_propagation(paths, frequency, time):
    phase_contributions = []
    attenuation_log = defaultdict(float)
    temp_buffer = []

    for i, (distance, velocity) in enumerate(paths):
        # Physical propagation delay
        delay = distance / (3e8)  # Speed of light
        doppler_shift = frequency * (velocity / 3e8)
        raw_phase = 2 * 3.14159 * (frequency + doppler_shift) * (time - delay)
        
        # Unrelated logging for system diagnostics (distractor)
        attenuation_log[f'path_{i}'] += 0.001 * distance
        
        # Actual relevant computation
        wrapped_phase = raw_phase % (2 * 3.14159)
        phase_contributions.append(wrapped_phase)
        
        # Dead code path - never used (distractor)
        if len(temp_buffer) > 100:
            temp_buffer.clear()

    return phase_contributions

# Analyze constructive/destructive interference
def calculate_interference(phases, amplitudes):
    weighted_sum = 0.0
    total_energy = 0.0
    cross_terms = []

    # Compute vector sum in complex plane (real component only)
    for i, (phase, amp) in enumerate(zip(phases, amplitudes)):
        weighted_sum += amp * 3.14159 * (phase / (2 * 3.14159))  # Projection on real axis
        total_energy += amp ** 2

    # Spurious combination analysis (distractor - not used in result)
    for combo in combinations(range(len(phases)), 2):
        cross_terms.append(abs(phases[combo[0]] - phases[combo[1]]))

    # Final net effect: normalized phase shift
    normalization_factor = sum(amplitudes) or 1
    net_phase_shift = weighted_sum / normalization_factor

    # Additional irrelevant transformation (distractor)
    if net_phase_shift > 3.14159:
        net_phase_shift -= 2 * 3.14159
    elif net_phase_shift < -3.14159:
        net_phase_shift += 2 * 3.14159

    return net_phase_shift

# System configuration
time_step = 1.2e-6
operating_frequency = 2.4e9
transmission_paths = [
    (1500, 25),
    (1620, 30),
    (1480, 20),
    (1550, 35)
]

# Signal characteristics
amplitude_weights = [0.8, 1.0, 0.7, 0.9]

# Execute simulation
phases_measured = simulate_signal_propagation(transmission_paths, operating_frequency, time_step)

# Critical computation point
net_phase_shift = calculate_interference(phases_measured, amplitude_weights)

# Auxiliary diagnostic output (distractor)
diagnostic_snapshot = {"timestamp": 1625094888, "status": "nominal"}

print(f"Result: {net_phase_shift}")