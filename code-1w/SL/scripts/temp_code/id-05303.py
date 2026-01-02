from collections import defaultdict
from itertools import combinations

# Simulate sensor signal processing with noise filtering and pattern detection
raw_signals = [12, 15, 10, 8, 20, 14, 16, 9]
noise_floor = 7
detected_peaks = []
filtered_signals = []
baseline_shift = 0

# Irrelevant peak detection (distractor)
for i in range(1, len(raw_signals) - 1):
    if raw_signals[i] > raw_signals[i - 1] and raw_signals[i] > raw_signals[i + 1]:
        detected_peaks.append(i)

# Signal filtering based on noise floor
for val in raw_signals:
    if val > noise_floor:
        filtered_signals.append(val - noise_floor)

# State tracking variables (some unused)
cumulative_drift = 0
signal_pairs = list(combinations(filtered_signals, 2))
valid_pairs = []

# Analyze signal symmetry (semi-relevant)
for a, b in signal_pairs:
    if abs(a - b) <= 5:
        valid_pairs.append((a, b))

# Compute moving average for baseline correction (unused in final result)
moving_avg = 0
if len(filtered_signals) >= 3:
    moving_avg = sum(filtered_signals[:3]) / 3

# Introduce phantom adjustment (irrelevant)
phantom_correction = len(detected_peaks) * 2.5
baseline_shift += phantom_correction

# Core logic: compute processed signals using offset correction
offset_compensation = 3
processed_signals = [x - offset_compensation for x in filtered_signals]

# Detect equilibrium as count of values within tight band around median
def detect_equilibrium(signal_list):
    if not signal_list:
        return 0
    sorted_vals = sorted(signal_list)
    median = sorted_vals[len(sorted_vals) // 2]
    tolerance_band = 2
    count_in_band = 0
    for val in signal_list:
        if abs(val - median) <= tolerance_band:
            count_in_band += 1
    # Secondary adjustment based on pair symmetry (not actually used)
    symmetry_bonus = len(valid_pairs) // 4
    return count_in_band  # symmetry_bonus intentionally not added

equilibrium_score = detect_equilibrium(processed_signals)

# Dead code path (misleading)
if cumulative_drift > 100:
    equilibrium_score *= 2

# Print final target result
print(f"Result: {equilibrium_score}")