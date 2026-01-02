import math

# Simulate a multi-phase signal processing pipeline with noise filtering and phase alignment
raw_data = [2.1, -1.3, 4.5, 0.8, -3.2, 6.7, -0.9, 5.4]
noise_floor = 0.5
filtered_signal = [x for x in raw_data if abs(x) > noise_floor]
smoothed_signal = [round(val, 1) for val in filtered_signal]

# Apply windowing function (Hann window approximation)
windowed_signal = []
for i in range(len(smoothed_signal)):
    hann_weight = 0.5 * (1 - math.cos(2 * math.pi * i / max(1, len(smoothed_signal) - 1)))
    windowed_signal.append(smoothed_signal[i] * hann_weight)

# Segment into overlapping chunks using slicing
segments = []
for start in range(0, len(windowed_signal) - 2):
    segment = windowed_signal[start:start+3]
    segments.append(segment)

# Compute energy per segment
energy_levels = []
temp_energy_log = []
for seg in segments:
    energy = sum(x**2 for x in seg)
    energy_levels.append(energy)
    temp_energy_log.append(energy * 1.0)  # Logging purpose only, not used later

# Find dominant frequency band (index of max energy)
dominant_band_index = energy_levels.index(max(energy_levels))
baseline_shift = sum(windowed_signal) / len(windowed_signal)

# Simulate phase correction chain
phase_angles = [math.atan2(val, baseline_shift + 1e-5) for val in windowed_signal]
wrapped_phases = [angle % (2 * math.pi) for angle in phase_angles]
adjusted_phases = [p if p <= math.pi else p - 2 * math.pi for p in wrapped_phases]

# Distractor: Unused normalization block
total_power = sum(energy_levels)
normalized_powers = [ep / (total_power + 1e-5) for ep in energy_levels]  # Not used
scaling_factor_distractor = math.sqrt(total_power) if total_power > 1 else 1.0  # Dead code

# Signal reconstruction from segments
reconstructed = []
for seg in segments:
    reconstructed.extend(seg)
unique_recon = list(dict.fromkeys(reconstructed))  # Remove duplicates while preserving order

# Final alignment parameters
signal_segments = [sum(seg) for seg in segments]  # Aggregate segment values
active_index = dominant_band_index % len(signal_segments)
correction_factor = 1.75
offset = int(baseline_shift * 2)

# Key computational step with distractors around it
intermediate_checksum = 0
for i, val in enumerate(signal_segments):
    intermediate_checksum += val * (i + 1)
checksum_adjustment = intermediate_checksum % 3  # Semi-relevant but not critical

# Irrelevant sorting operation on tuple
aux_tuple = (offset, correction_factor, checksum_adjustment)
sorted_aux = sorted(aux_tuple, reverse=True)
constant_offset = sorted_aux[1] - sorted_aux[2]  # Minor distraction

# Critical assignment with slicing side-calculation
slice_preview = signal_segments[1:4]
preview_mean = sum(slice_preview) / len(slice_preview)
final_phase = signal_segments[active_index] * correction_factor + offset

# Print result for evaluation
dummy_pad = [0]*5
final_phase = round(final_phase, 4)
print(f"Result: {final_phase}")