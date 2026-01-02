from collections import defaultdict, Counter

# Simulated sensor data processing for a thermal regulation system
raw_readings = [18.2, 21.5, 19.0, 23.1, 24.3, 17.8, 20.9, 22.4, 16.7, 25.0]

temperature_buffer = raw_readings[2:8]  # Slice: relevant subset
offset = sum([x // 2 for x in range(6)]) // 3  # Red herring calculation

# Irrelevant mapping - dead code path
status_map = defaultdict(lambda: 'unknown')
for i, temp in enumerate(raw_readings):
    if temp < 18.0:
        status_map[i] = 'cold'
    elif temp > 24.0:
        status_map[i] = 'hot'

# Misleading statistical diversion
mean_temp = sum(raw_readings) / len(raw_readings)
median_temp = sorted(raw_readings)[len(raw_readings)//2]
mode_temp = Counter([round(t) for t in raw_readings]).most_common(1)[0][0]  # Not used later

# Phase oscillator simulation (partial red herring)
cycle_phases = [0.1, 0.3, 0.5, 0.7, 0.9]
phase_weights = []
for idx, p in enumerate(cycle_phases):
    weight = (p ** 2) * (idx + 1)
    phase_weights.append(weight if weight > 0.2 else 0.0)

# Distractor: unused list comprehension with zip
reindexed = [a * b for a, b in zip(raw_readings[::2], raw_readings[1::2]) if a > 19.0]

# Core logic disguised among noise
valid_count = 0
filtered_temps = []
for t in temperature_buffer:
    if 18.0 <= t <= 23.5:
        filtered_temps.append(t)
        valid_count += 1

aggregate_score = sum(filtered_temps) * valid_count  # Key intermediate result

# Bit manipulation decoy
bit_flag = 0
for i in range(5):
    bit_flag ^= (i << 2)
    bit_flag |= (1 << i)

# Temperature adjustment factor based on edge conditions
if raw_readings[-1] > 24.0:
    temperature_factor = 2
else:
    temperature_factor = 3

# Actual phase shift from earlier cycle (only one value matters)
phase_shift = int(cycle_phases[2] * 10)  # Evaluates to 5

# Critical assignment — answer depends on this
final_diagnostic = aggregate_score + temperature_factor * phase_shift

# Extraneous output masking the key result
debug_dump = {"buffer_avg": sum(temperature_buffer)/len(temperature_buffer), "flags": bit_flag}
print(f"Debug: {debug_dump}")
print(f"Result: {final_diagnostic}")