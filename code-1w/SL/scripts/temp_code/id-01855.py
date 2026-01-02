import itertools
import math

# Simulated sensor readings with noise and redundant data
time_stamps = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
raw_signals = [5.2, -3.4, 7.1, -1.8, 9.0, -6.3, 2.2, -8.7, 4.5, -0.9]

# Irrelevant transformation: frequency analysis (dead path)
frequencies = [abs(math.sin(t * 2 * math.pi)) for t in time_stamps]
dummy_spectrum = list(itertools.accumulate(frequencies))

# Core signal processing chain
phases = [math.atan2(signal, 1) for signal in raw_signals]  # phase extraction
magnitude_weights = [math.sqrt(abs(s)) for s in raw_signals]  # weighting factor
weighted_phases = [p * w for p, w in zip(phases, magnitude_weights)]

# Decoy operation: circular pairing with offset (unused)
circular_pairs = list(zip(weighted_phases, weighted_phases[1:] + [weighted_phases[0]]))
rolling_avg = [sum(pair)/2 for pair in circular_pairs]

# Conditional filtering based on dynamic threshold
threshold = sum(magnitude_weights) / len(magnitude_weights)
valid_indices = [
    i for i, weight in enumerate(magnitude_weights)
    if weight > threshold and i % 2 == 0
]

# Extract corresponding phases using valid indices
selected_phases = [weighted_phases[i] for i in valid_indices]

# Red herring: reverse mapping to time (irrelevant)
temporal_mapping = {i: time_stamps[i] for i in range(len(time_stamps))}
phase_time_lookup = {
    weighted_phases[i]: time_stamps[i]
    for i in range(len(weighted_phases))
    if raw_signals[i] > 0
}

# Real computation path begins here
rotated_angles = [
    math.radians(90) - abs(angle) for angle in selected_phases
]

# Normalize angles into [0, π/2] range
normalized_angles = [
    abs(math.cos(angle)) if angle < 0 else math.sin(angle)
    for angle in rotated_angles
]

# Final filter: exclude near-zero contributions
effective_mask = [angle > 0.3 for angle in normalized_angles]
filtered_angles = [
    angle for angle, mask in zip(normalized_angles, effective_mask) if mask
]

# Key statement
filtered_phase_sum = sum(filtered_angles)

# Output result
print(f"Result: {filtered_phase_sum}")