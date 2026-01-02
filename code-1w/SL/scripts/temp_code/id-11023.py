from collections import defaultdict

# Simulate sensor readings over time with some noise
timestamps = [100, 105, 110, 115, 120, 125, 130]
raw_readings = [23.5, 24.1, 23.9, 0.0, 24.2, 24.0, 23.8]  # Zero indicates sensor dropout

calibration_factor = 1.02
offset_compensation = 0.5
adjusted_readings = []
valid_count = 0

drop_counter = 0
spike_threshold = 5.0
prev_value = raw_readings[0]

for val in raw_readings:
    if val == 0.0:
        drop_counter += 1
        continue
    
    diff = abs(val - prev_value)
    if diff > spike_threshold:
        prev_value = val
        continue
    
    corrected = (val * calibration_factor) + offset_compensation
    adjusted_readings.append(corrected)
    valid_count += 1
    prev_value = val

# Track usage cycles
cycles = [(100, 105), (110, 120), (125, 130)]
active_periods = sum(end - start for start, end in cycles)

# Compute output metrics
total_output = 0
for i, reading in enumerate(adjusted_readings):
    hour_slot = timestamps[i] // 10
    multiplier = 1.0
    if hour_slot == 11:
        multiplier = 1.1
    elif hour_slot == 12:
        multiplier = 1.15
    total_output += reading * multiplier

# Distractor: irrelevant aggregation
daily_summary = defaultdict(int)
for ts, val in zip(timestamps, raw_readings):
    daily_summary[ts // 100] += 1

# Distractor: unused helper
def smooth(data, factor=0.8):
    result = [data[0]]
    for i in range(1, len(data)):
        result.append(result[-1] * factor + data[i] * (1 - factor))
    return result

# Distractor: dead code path
if len(raw_readings) > 100:
    efficiency_score = -1
else:
    efficiency_score = total_output / active_periods if active_periods else 0

# Final result
print(f"Result: {efficiency_score}")