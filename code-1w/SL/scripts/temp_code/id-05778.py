import itertools

# Simulated sensor array diagnostics with embedded logic
sensor_ids = ['S1', 'S2', 'S3', 'S4']
base_readings = [0.88, 0.92, 0.76, 0.94]
status_flags = [True, True, False, True]

calibration_offsets = {s: (i+1) * 0.01 for i, s in enumerate(sensor_ids)}

def analyze_consistency(readings):
    sorted_vals = sorted(readings)
    median = sorted_vals[len(sorted_vals)//2]
    return sum(abs(r - median) < 0.15 for r in readings)

# Irrelevant auxiliary function - decoy
def compute_entropy(data):
    from math import log
    total = sum(data)
    probs = [d/total for d in data if d > 0]
    return -sum(p * log(p) for p in probs)

# Unused transformation path
transformed = list(map(lambda x: round(x * 100), base_readings))
filtered_sensors = [s for s, f in zip(sensor_ids, status_flags) if f]

# Core diagnostic chain
valid_count = len([f for f in status_flags if f])
raw_aggregate = sum(base_readings) / len(base_readings)

# Red herring computation with string methods
id_concat = ''.join(sensor_ids)
flag_summary = id_concat.replace('S', 'Sensor-').split('-')
size_hint = len(flag_summary[0]) if flag_summary else 0  # unused

# Conditional expression with misleading branch
adjustment_factor = 0.1 if all(status_flags) else (0.05 if valid_count >= 3 else -0.1)

# Bit manipulation distraction (unused)
bit_encoded = 0
for i, flag in enumerate(status_flags):
    bit_encoded |= (int(flag) << i)
decoded_check = [(bit_encoded >> i) & 1 for i in range(len(status_flags))]

# Set operations - relevant only in part
active_set = set(filtered_sensors)
all_set = set(sensor_ids)
presence_ratio = len(active_set & all_set) / len(all_set)

# Spurious itertools usage
combinations_test = list(itertools.combinations(sensor_ids, 2))
pair_count = len(combinations_test)

# Diagnostic consistency score (used)
consistency_score = analyze_consistency(base_readings)

# Main calculation chain
normalized_score = consistency_score / len(base_readings)
aggregate_score = raw_aggregate * normalized_score

# Adjustment based on active sensors
if valid_count == 4:
    aggregate_score *= 1.1
elif valid_count == 3:
    aggregate_score *= 1.05
else:
    aggregate_score *= 0.95

# Key assignment - target of query
final_diagnostic = aggregate_score * (1 + adjustment_factor)

# Dead code path
if len(combinations_test) > 10:
    final_diagnostic *= 0.9

# Output result
print(f"Result: {final_diagnostic}")