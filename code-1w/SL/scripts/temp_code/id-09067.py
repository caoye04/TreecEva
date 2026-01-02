from collections import defaultdict, Counter
from itertools import combinations, cycle

# Simulated sensor network data with noise and redundant channels
def simulate_sensor_network():
    raw_readings = [
        (100, 'temp', 'A'), (105, 'temp', 'B'), (200, 'pressure', 'A'),
        (198, 'pressure', 'C'), (300, 'flow', 'D'), (303, 'flow', 'E'),
        (102, 'temp', 'A'), (201, 'pressure', 'B'), (301, 'flow', 'F')
    ]
    return raw_readings

# Irrelevant helper: generates synthetic timestamps (not used in final result)
def generate_timestamps(n):
    base = 1678886400
    return [base + i * 30 for i in range(n)]

# Misleading function: appears important but is never called
def analyze_trend(data_seq):
    if len(data_seq) < 3:
        return False
    trend = all(data_seq[i] <= data_seq[i+1] for i in range(len(data_seq)-1))
    return 'increasing' if trend else 'fluctuating'

# Decoy data structure: looks like it might be used for calibration
offset_table = {
    'X': lambda x: x + 5,
    'Y': lambda x: x - 3,
    'Z': lambda x: x * 1.1
}

# Main processing pipeline
raw_data = simulate_sensor_network()

# Step 1: Filter by type and aggregate by category (real use)
type_buckets = defaultdict(list)
for value, sensor_type, node_id in raw_data:
    type_buckets[sensor_type].append(value)

# Step 2: Compute baseline stats - some are red herrings
baselines = {}
for stype, values in type_buckets.items():
    baselines[stype] = {
        'mean': sum(values) / len(values),
        'min_val': min(values),
        'max_val': max(values),
        'range': max(values) - min(values),
        'mode': Counter(values).most_common(1)[0][0]  # Real use later
    }

# Distractor block: complex but unused calculation
dynamic_weights = []
for i, (k, v) in enumerate(baselines.items()):
    weight = (v['mean'] * (i + 1)) / (v['range'] + 1)
    dynamic_weights.append(round(weight, 2))

# Unused transformation chain
cyclic_shift = cycle([1, -1, 2])
shifted_bases = []
for val in [baselines[t]['mean'] for t in baselines]:
    shifted = val + next(cyclic_shift)
    shifted_bases.append(shifted)

# Real filtering logic: isolate high-confidence nodes
filtered_data = []
for entry in raw_data:
    value, s_type, node = entry
    mode_val = baselines[s_type]['mode']
    if abs(value - mode_val) <= 3:  # Close to mode
        filtered_data.append((value, s_type, node))

# Another decoy: builds a structure but isn't used
diagnostic_matrix = [[0]*3 for _ in range(3)]
for i, stype in enumerate(baselines):
    diagnostic_matrix[i % 3][i % 3] += int(baselines[stype]['mean'])

# Threshold map based on statistical spread (actual dependency)
threshold_map = {}
for stype in type_buckets:
    spread = baselines[stype]['range']
    threshold_map[stype] = spread * 2 + 1  # Critical for final step

# Core processing function
def process_readings(readings, thresholds):
    result_set = defaultdict(int)
    for val, typ, nid in readings:
        # Bit manipulation as identifier hash (relevant)
        hash_key = len(nid) ^ val & 7  # XOR and bitwise AND
        if val < thresholds[typ]:
            result_set[hash_key] += val % 10  # Use last digit
    # Final aggregation using combinatorics
    total_pairs = 0
    for group in result_set.values():
        # Count unordered pairs within digit groups
        if group > 1:
            total_pairs += group * (group - 1) // 2
    return sum(result_set.values()) + total_pairs

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Print required output
print(f"Target result: {final_diagnostic}")