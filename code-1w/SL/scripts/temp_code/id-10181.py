from collections import defaultdict, Counter
import itertools

# Simulated sensor data stream (time, id, reading)
sensor_data = [
    (100, 'A7', 0.8), (101, 'B2', 1.2), (102, 'A7', 0.9), (103, 'C5', -0.3),
    (104, 'B2', 1.1), (105, 'D1', 0.0), (106, 'C5', -0.1), (107, 'A7', 0.75)
]

# Irrelevant mapping - red herring
device_powers = {'A7': 2.1, 'B2': 1.8, 'C5': 0.9, 'D1': 3.0}
power_baseline = sum(device_powers.values()) / len(device_powers)  # Unused

# Misleading intermediate aggregation
temporal_bins = defaultdict(list)
for timestamp, dev_id, val in sensor_data:
    temporal_bins[timestamp // 10].append(val)

mean_per_decade = {k: sum(v)/len(v) for k, v in temporal_bins.items()}  # Distractor

# Real processing begins: filter by device type and extract A7 readings
a7_readings = [reading for ts, dev, reading in sensor_data if dev == 'A7']

# Apply decay factor over sequence (simulates signal degradation)
decay_weights = [0.95**i for i in range(len(a7_readings))]
weighted_a7 = sum(reading * weight for reading, weight in zip(a7_readings, decay_weights))
normalized_signal = weighted_a7 / sum(decay_weights)

# Bit manipulation to simulate checksum validation (irrelevant but plausible)
raw_checksum = int.from_bytes(b'health_diag_v2', 'little') & 0xFFFF
mask_offset = (raw_checksum >> 4) ^ 0xAA
valid_checksum = (mask_offset + len(sensor_data)) % 256  # Not actually used

# System status codes (complex lookup table with decoys)
status_interpretation = defaultdict(lambda: 'UNKNOWN')
status_interpretation.update({
    1: 'OPTIMAL', 2: 'STABLE', 3: 'MONITOR', 4: 'WARNING', 5: 'CRITICAL'
})

current_status_code = 2  # STABLE
status_weight_map = {'OPTIMAL': 1.0, 'STABLE': 0.85, 'MONITOR': 0.6, 'WARNING': 0.3, 'CRITICAL': 0.1}
status_influence = status_weight_map.get(status_interpretation[current_status_code], 0.5)

# Secondary data transformation: group by deviation magnitude
abs_deviation = [abs(x) for x in a7_readings]
high_deviation_threshold = 0.8
high_dev_count = sum(1 for x in abs_deviation if x >= high_deviation_threshold)
penalty_factor = high_dev_count * 0.15  # Deduct per high-deviation instance

# Aggregate health score computation (core logic)
base_health = normalized_signal * 100
aggregate_health_score = base_health * status_influence - (penalty_factor * 10)

# System offset from modular arithmetic on data length
data_cycle = len(sensor_data) % 7
timing_phase = (data_cycle * 360) // 7
system_offset = timing_phase - 180  # Shift origin to center

# Final diagnostic fusion (key statement)
final_diagnostic = aggregate_health_score + system_offset

# Decoy output paths
if final_diagnostic > 50:
    shadow_diagnostic = final_diagnostic * 0.9
elif final_diagnostic > 20:
    shadow_diagnostic = final_diagnostic * 0.7
else:
    shadow_diagnostic = final_diagnostic * 0.5  # Dead code path

# Unused list comprehension with itertools (distractor)
all_pairs = [(x,y) for x, y in itertools.combinations_with_replacement([1,2,3], 2) if x != y]
pair_sum_stats = Counter(sum(p) for p in all_pairs)

# Output target result
print(f"Result: {final_diagnostic}")