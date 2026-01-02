import math

# Simulated sensor readings from a distributed network
timestamps = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
signal_amplitudes = [3.2, -1.4, 4.8, -2.2, 0.9, -3.1, 5.5, -0.8, 2.7, -4.0]
frequencies = [50.1, 49.8, 50.3, 49.9, 50.0, 50.2, 49.7, 50.4, 49.6, 50.5]

# Irrelevant transformation - red herring
adjusted_timestamps = [ts * 1.001 for ts in timestamps]
decoy_signal = [abs(math.sin(amp)) for amp in signal_amplitudes]

# Phase calculation with noise filtering
raw_phases = []
for i, (amp, freq) in enumerate(zip(signal_amplitudes, frequencies)):
    phase = (amp * freq) % (2 * math.pi)
    if abs(amp) > 1.0:
        raw_phases.append(phase)

# Misleading intermediate aggregation
total_decoy = 0
for p in raw_phases:
    total_decoy += math.cos(p)  # Unused computation

decoys_set = set([int(p) for p in raw_phases])
distinct_int_phases = len(decoys_set)  # Distractor variable

# Frequency band classification
valid_bands = set()
for f in frequencies:
    if 49.7 <= f <= 50.3:
        valid_bands.add(round(f, 1))

# Main processing path: extract phases corresponding to stable frequency windows
stable_indices = []
for i, f in enumerate(frequencies):
    if round(f, 1) in valid_bands and timestamps[i] % 2 == 1:
        stable_indices.append(i)

# Apply index filter to amplitudes (secondary relevance)
active_amplitudes = []
for idx in stable_indices:
    if idx < len(signal_amplitudes):
        active_amplitudes.append(signal_amplitudes[idx])

# Compute derived phase values from active signals
derived_phases = []
for j, amp in enumerate(active_amplitudes):
    if j % 2 == 0:
        derived_phases.append(math.atan2(amp, frequencies[stable_indices[j]]) * 2)
    else:
        derived_phases.append(abs(amp) ** 0.5)

# Filter phases above threshold - key execution point
threshold_phase = math.pi / 3
filtered_phases = []
for phase_val in derived_phases:
    if phase_val > threshold_phase:
        filtered_phases.append(phase_val)

# Critical assignment - target of question
filtered_phase_sum = sum(filtered_phases)

# Dead code path - never executed
if False:
    backup_calc = math.log(sum(signal_amplitudes))
    filtered_phase_sum = backup_calc

# Print final result
print(f"Result: {filtered_phase_sum}")