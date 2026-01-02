from itertools import cycle

# Simulate time-series sensor readings over a monitoring period
data_stream = [12, 15, 23, 18, 25, 30, 20, 19, 22, 24, 29, 31, 27, 26]
window_size = 3
temperature_bias = 1.25
offset_correction = sum(data_stream[:4]) // 4 - 20

# Apply bias correction to raw data (semi-relevant)
bias_applied = [round(x + temperature_bias) for x in data_stream]

# Misleading pre-processing: irrelevant frequency analysis
signal_cycle = cycle([1, -1, 0])
frequency_marker = [next(signal_cycle) * x for x in data_stream[:6]]
spurious_total = sum(frequency_marker)

# Core logic: compute rolling average over window
rolling_avg = []
for i in range(len(bias_applied) - window_size + 1):
    segment = bias_applied[i:i + window_size]
    avg = sum(segment) / window_size
    rolling_avg.append(avg)

# Secondary adjustment based on system baseline
baseline = 22.5
adjusted_peaks = [val for val in rolling_avg if val > baseline]

# Distractor: unused conditional expression for hypothetical fail-safe
safety_engaged = len(adjusted_peaks) > 5 else False

# Track duration above threshold (not used in final result)
exceedance_duration = sum(1 for x in adjusted_peaks if x > baseline)

# Final load evaluation
peak_load = max(rolling_avg, default=0)

# Unrelated cleanup operation (dead code path, but syntactically present)
if offset_correction < 0:
    data_stream.reverse()

print(f"Result: {peak_load}")