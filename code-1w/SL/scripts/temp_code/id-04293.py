from collections import defaultdict
from itertools import cycle

# Simulate sensor data stream with timestamps and readings
data_stream = [
    (100, 23.5), (101, 24.1), (102, 23.9), (103, 25.0), (104, 24.5),
    (105, 26.0), (106, 25.8), (107, 26.2), (108, 27.0), (109, 26.8)
]

# Misleading auxiliary data (distractor)
baseline_readings = [22.0, 23.1, 24.0, 25.2, 26.1]
offset_map = {i: val for i, val in enumerate(baseline_readings)}

# Buffer to hold processed chunks
stream_buffer = []
for ts, val in data_stream:
    adjusted_val = round(val + 0.5, 1)  # Artificial adjustment (not used later)
    normalized = val - 20.0  # Normalize to base
    stream_buffer.append((ts, normalized))

# Dead code path - never executed due to fixed condition (distractor)
current_mode = 'A'
if current_mode == 'DEBUG':
    debug_log = []
    for item in stream_buffer:
        debug_log.append(f"Debug: {item}")

# Frequency counter for time deltas (semi-relevant)
time_diffs = []
for i in range(1, len(data_stream)):
    time_diffs.append(data_stream[i][0] - data_stream[i-1][0])

freq_count = defaultdict(int)
for diff in time_diffs:
    freq_count[diff] += 1

# Core processing function with lambda and itertools
smoothing_window = cycle([0.25, 0.5, 0.25])  # For weighted smoothing


def process_data(buffer):
    cumulative_score = 0
    weights = [next(smoothing_window) for _ in range(len(buffer))][:3]  # Only use first 3

    # Extract values and apply weighted sum on first three entries
    values = [entry[1] for entry in buffer]
    if len(values) >= 3:
        weighted_sum = sum(v * w for v, w in zip(values[:3], weights))
    else:
        weighted_sum = sum(values) * 0.5

    # Secondary calculation: count how many exceed threshold
    threshold_count = 0
    for v in values:
        if v > 4.0:  # Above normalized base
            threshold_count += 1

    # Tertiary distractor computation (no impact)
    temp_aggr = 0
    for i, v in enumerate(values):
        temp_aggr += v * (i % 2 + 1)
    avg_temp = temp_aggr / len(values) if values else 0

    # Final logic: combine weighted sum and count with modular arithmetic
    intermediate = int(weighted_sum * 10)  # Scale up
    mod_step = (intermediate + threshold_count) % 7
    final_modifier = pow(mod_step, 2, 10)  # Square mod 10

    result = intermediate + final_modifier - 5
    return result

# Key execution point
final_output = process_data(stream_buffer)
print(f"Result: {final_output}")