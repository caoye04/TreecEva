from itertools import combinations, cycle

# Simulated sensor array data with calibration offsets
data_stream = [1.7, -2.3, 4.1, 0.5, -1.2, 3.6, -0.8]
reference_phases = [0.25, -1.1, 0.9, 2.2]
calibration_map = {i: val ** 2 for i, val in enumerate(reference_phases)}

# Irrelevant pre-computed statistics (distractor)
extreme_values = [max(data_stream), min(data_stream), sum(data_stream) / len(data_stream)]
summary_stats = {"peak": extreme_values[0], "trough": extreme_values[1], "mean": extreme_values[2]}

# Buffer setup for signal processing (mixed relevant/irrelevant)
signal_buffer = []
for idx, point in enumerate(data_stream):
    if idx % 2 == 0:
        shifted = point + reference_phases[idx % len(reference_phases)]
        signal_buffer.append(shifted * 0.9)
    else:
        # Unused branch - dead code path (distractor)
        normalized = (point + 1.0) / 2.5
        signal_buffer.append(normalized * 0.1)  # Not used later

# Active processing path begins here
active_signals = [x for x in data_stream if x > 0]
modulation_cycle = cycle([1, -1, 1])
modulated = [val * next(modulation_cycle) for val in active_signals]

# Complex transformation using combinatorics
pairwise_interactions = list(combinations(modulated, 2))
interaction_energy = [abs(a * b) for a, b in pairwise_interactions]
total_energy = sum(interaction_energy)

# Baseline derived from control sequence (red herring variables included)
control_sequence = [calibration_map[i] for i in range(len(reference_phases)) if i % 2 == 0]
baseline_offset = sum(control_sequence) * 0.3  # Used later

# Dummy transformation chain (distractor)
dummy_buffer = []
for x in interaction_energy:
    temp = x ** 0.5
    if temp < 5:
        dummy_buffer.append(temp + 0.1)
# Unused result (misleading intermediate)
final_diagnostic = sum(dummy_buffer) if dummy_buffer else 0

# Core compression algorithm (key logic)
compression_factor = len(active_signals) / (len(data_stream) + 1e-8)
raw_compression = total_energy * compression_factor
compressed_result = raw_compression

# Final computation with critical statement
filtered_magnitude = abs(compressed_result - baseline_offset)

# Output required variable
print(f"Result: {filtered_magnitude}")