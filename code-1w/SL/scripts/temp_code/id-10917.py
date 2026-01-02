import math

# Simulated sensor readings with noise and calibration offsets
data_stream = [127, -95, 203, 44, -150, 89, 301, -416, 73, 22, -88, 134, 502, -307, 91]
noise_floor = 100
signal_threshold = 200
calibration_factor = 0.87
offset_adjustment = 15

# Irrelevant statistical placeholders (distractors)
mean_value = sum(data_stream) / len(data_stream)
variance_proxy = sum((x - mean_value) ** 2 for x in data_stream)
entropy_approx = 0.0
for x in data_stream:
    if x != 0:
        entropy_approx += abs(x) * math.log(abs(x))
entropy_approx /= len(data_stream)

# Signal processing pipeline: real target logic begins
raw_signals = [abs(x) for x in data_stream]  # Convert to magnitude
adjusted_signals = [calibration_factor * sig + offset_adjustment for sig in raw_signals]

# Identify high-energy signals above threshold
high_energy_mask = [sig > signal_threshold for sig in adjusted_signals]
energy_indices = [i for i, flag in enumerate(high_energy_mask) if flag]

# Apply dynamic windowing based on first and last burst
if len(energy_indices) > 1:
    first_burst = energy_indices[0]
    last_burst = energy_indices[-1]
    window_start = max(0, first_burst - 2)
    window_end = min(len(data_stream), last_burst + 3)
else:
    window_start = 0
    window_end = len(data_stream)

# Extract working segment within dynamic window
temporal_window = adjusted_signals[window_start:window_end]

# Decoy transformation: frequency-domain mimicry (irrelevant)
freq_dct_approx = []
for k in range(len(temporal_window)):
    acc = 0
    for n, x in enumerate(temporal_window):
        acc += x * math.cos((math.pi / len(temporal_window)) * k * (n + 0.5))
    freq_dct_approx.append(acc)

# Real filtering logic: focus on odd-positioned samples in window that exceed noise floor
candidate_positions = list(range(1, len(temporal_window), 2))  # Odd indices
strong_candidates = [
    temporal_window[pos] for pos in candidate_positions
    if temporal_window[pos] > noise_floor
]

# Secondary filter: reject values ending in digits 3 or 7 (arbitrary interference rule)
filtered_data = [
    val for val in strong_candidates
    if int(round(val)) % 10 not in {3, 7}
]

# Final computation — TARGET STATEMENT
filtered_sum = sum(filtered_data)

# Dead code path: misleading alternative aggregation (never used)
if filtered_sum < 0:
    backup_result = math.prod([x for x in filtered_data if x > 0])
    filtered_sum = int(backup_result % 1000)

# Output result
print(f"Result: {filtered_sum}")