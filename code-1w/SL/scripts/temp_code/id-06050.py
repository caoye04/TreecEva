from collections import defaultdict, Counter

# Simulated sensor data stream over time
sensor_ids = ['S1', 'S2', 'S3', 'S4']
time_stamps = list(range(100, 200, 3))
raw_readings = [t * 1.5 + (t % 7) * 0.3 for t in time_stamps]

# Irrelevant mapping: color codes (distractor)
color_priority = {'red': 3, 'yellow': 2, 'green': 1}
status_colors = [color_priority['green']] * len(time_stamps)

# Real processing begins
reading_map = defaultdict(list)
for i, sid in enumerate(sensor_ids):
    start_idx = i * 10
    for j in range(start_idx, start_idx + 10):
        if j < len(raw_readings):
            adjusted = raw_readings[j] + (i * 0.1) - ((j + i) % 4) * 0.05
            reading_map[sid].append(round(adjusted, 3))

# Extract and slice relevant window
window_data = reading_map['S2'][5:15]  # Only S2 matters here

# Decoy aggregation (never used later)
decoy_aggregate = sum([len(reading_map[s]) for s in reading_map]) * 0.7

# Signal filtering and transformation
filtered = [val for val in window_data if val > 155 and val < 165]
squared_residuals = [(x - 160) ** 2 for x in filtered]
mean_square = sum(squared_residuals) / len(squared_residuals) if squared_residuals else 0

# Bit manipulation red herring
event_flag = 0b101010
shifted_flag = (event_flag << 3) | 0b111
checksum = shifted_flag ^ 0b1101111

# Control flow with misleading branches
system_engaged = False
phase_shift = 2
if len(filtered) > 3:
    phase_shift = 5
    temp_cache = {i: filtered[i]**0.5 for i in range(len(filtered))}
    if sum(temp_cache.values()) > 20:
        system_engaged = True
        phase_shift = 8  # Overwritten in next block
        for k in temp_cache:
            temp_cache[k] *= phase_shift
else:
    backup_state = [x * 2 for x in filtered]

# More irrelevant logic
redundant_counter = Counter()
for val in raw_readings:
    redundant_counter[int(val // 10)] += 1

# Critical path disguised among decoys
baseline = [round(158 + i * 0.4, 2) for i in range(10)]
overlap = [b for b in baseline if any(abs(b - f) < 0.5 for f in filtered)]

# Conditional expression with side effect simulation
phase_offset = phase_shift if system_engaged else -3

# Data structure cross-reference distraction
data_matrix = [[i + j * 2 for j in range(5)] for i in range(6)]
reference_lookup = defaultdict(int)
for row in data_matrix:
    for elem in row[::2]:
        reference_lookup[elem] += 1

# Real computation chain
aggregate_metrics = []
for i, val in enumerate(overlap):
    metric = int((val - 158) * 10)
    if i % 2 == 0:
        metric = abs(metric - 4)
    else:
        metric = metric + (i % 3)
    aggregate_metrics.append(metric)

# Dead code path
if False:
    fallback_metrics = [m * 2 for m in aggregate_metrics]
    aggregate_metrics = fallback_metrics

# Key statement containing answer
dummy_var = aggregate_metrics.copy()
final_diagnostic = aggregate_metrics[-1] + phase_offset if system_engaged else 0

print(f"Result: {final_diagnostic}")