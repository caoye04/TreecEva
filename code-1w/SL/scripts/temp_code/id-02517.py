from collections import defaultdict, Counter
import itertools

# Simulated sensor data ingestion (irrelevant in part)
sensor_nodes = ['temp_01', 'temp_02', 'pressure_a', 'pressure_b', 'flow_x', 'flow_y']
data_stream = [
    (0, 'temp_01', 23.4), (1, 'temp_02', 24.1),
    (2, 'pressure_a', 98.7), (3, 'pressure_b', 99.1),
    (4, 'flow_x', 12.5), (5, 'flow_y', 11.8),
    (6, 'temp_01', 25.0), (7, 'temp_02', 26.3),
    (8, 'pressure_a', 101.2), (9, 'flow_x', 13.0)
]

# Irrelevant preprocessing: group by index parity (distraction)
parity_groups = {k: list(g) for k, g in itertools.groupby(data_stream, key=lambda x: x[0] % 2)}

# Core diagnostic logic setup
def initialize_thresholds(nodes):
    base_map = {}
    for node in nodes:
        if 'temp' in node:
            base_map[node] = (30.0, 'upper')
        elif 'pressure' in node:
            base_map[node] = (105.0, 'upper')
        elif 'flow' in node:
            base_map[node] = (5.0, 'lower')
    return base_map

threshold_map = initialize_thresholds(sensor_nodes)

# Misleading normalization function (never called)
def normalize_readings(stream):
    norm_data = []
    for idx, name, val in stream:
        if 'temp' in name:
            norm_data.append((idx, name, round(val / 100, 3)))
        else:
            norm_data.append((idx, name, val))
    return norm_data

# Decoy statistical summary (unused later)
value_counter = Counter([name for idx, name, val in data_stream])
node_frequency = dict(value_counter)

# Real processing begins here: extract only temperature readings
recent_temps = [(name, val) for idx, name, val in data_stream if 'temp' in name]

# Build aggregate buffer with cumulative sums per node (core data)
aggregate_buffer = defaultdict(float)
for name, val in recent_temps:
    aggregate_buffer[name] += val

# Secondary distraction: unused correlation attempt
correlation_pairs = list(itertools.combinations(['temp_01', 'temp_02'], 2))
dummy_correlations = {}
for a, b in correlation_pairs:
    dummy_correlations[(a,b)] = abs(hash(a) - hash(b)) % 17

# Another red herring: simulate calibration offset (not applied)
calibration_offset = sum([hash(name) % 10 for name in sensor_nodes]) / len(sensor_nodes)
adjusted_offsets = [calibration_offset * 1.5 for _ in range(3)]  # dead code path

# Actual metric processor
def process_metrics(buffer, thresholds):
    score = 0
    for sensor, total in buffer.items():
        limit, direction = thresholds[sensor]
        # Only upper bounds matter for temp sensors
        if direction == 'upper':
            if total > limit:
                score -= int(total)
            else:
                score += int(limit - total)
    # Bit manipulation decoy (looks important but unused in final math)
    magic_key = 0b1101 ^ 0b1011
    mask_result = magic_key & 0b1111
    
    # Final adjustment based on non-obvious condition
    if len(buffer) >= 2 and sum(buffer.values()) > 50.0:
        score = abs(score) + (score ^ 7)  # XOR twist
    return score + 1000

# Critical execution point
final_diagnostic = process_metrics(aggregate_buffer, threshold_map)

# Output required result
print(f"Result: {final_diagnostic}")