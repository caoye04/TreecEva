def analyze_trends(data, threshold=5):
    trend_flags = {}
    for i, value in enumerate(data):
        if value > threshold:
            trend_flags[i] = True
        else:
            trend_flags[i] = False
    return trend_flags

# Irrelevant function - dead code path
def calculate_network_latency(packets):
    total_delay = 0
    for pkt in packets:
        if pkt % 2 == 0:
            total_delay += pkt * 0.5
    return total_delay

# Decoy data
network_packets = [12, 34, 56, 78, 90]
latency_result = calculate_network_latency(network_packets)  # Unused

# Main computation setup
raw_readings = [3, 7, 9, 2, 8, 6]
base_offset = sum([x for x in raw_readings if x % 2 == 1]) - 4  # 3 + 7 + 9 - 4 = 15

# Bit manipulation red herring
bitmask = 0b10101
shifted_mask = (bitmask << 3) & 0b11111
obfuscated_value = shifted_mask ^ 0b11001  # Irrelevant result

# Conditional branching with distractors
status_map = {k: ('high' if v > 6 else 'low') for k, v in enumerate(raw_readings)}
alert_count = len([v for v in status_map.values() if v == 'high'])  # 3 values > 6

# Set operations as per requirement
unique_categories = set(['A', 'B', 'C', 'B', 'D'])
discount_codes = set(['X10', 'B', 'Y20', 'C'])
overlaps = unique_categories & discount_codes  # {'B', 'C'} -> size 2, irrelevant

# Dictionary and zip usage (required)
timestamps = [100, 101, 102, 103, 104, 105]
named_metrics = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6']
metric_index = dict(zip(named_metrics, timestamps))

readings_with_id = list(enumerate(raw_readings))
indexed_data = {idx: val for idx, val in readings_with_id}

# Simulated intermediate transformation (misleading)
transformed = []
for idx, val in indexed_data.items():
    if idx % 2 == 0:
        transformed.append(val * 2)
    else:
        transformed.append(val + 1)

aggregate = sum(transformed) // len(transformed)  # average-like, but unused

# Core logic buried among distractions
scaling_factor = 1
if alert_count >= 3:
    scaling_factor *= 2
if len(raw_readings) > 5:
    scaling_factor *= 3  # Now 6

adjusted_values = [v * scaling_factor for v in raw_readings]

# Use of enumerate and complex filtering
filtered_contributions = [
    adjusted_values[i] for i, v in enumerate(raw_readings)
    if status_map[i] == 'high' or (i > 0 and raw_readings[i-1] < 5)
]

# Another decoy: string processing (allowed via suggestion)
token_sequence = "split-this-sequence-now"
split_parts = token_sequence.split('-')
joined_back = ''.join([p[0] for p in split_parts])  # 'stsn', unused

# Critical function with multiple concepts
def aggregate_performance(metrics, offset):
    temp_results = []
    for key, val in metric_index.items():
        pos = named_metrics.index(key)
        if pos < len(metrics):
            computed = metrics[pos] + val + offset
            if computed % 2 == 0:
                temp_results.append(computed * 0.5)
            else:
                temp_results.append(computed * 1.1)
    # Mix of float and int arithmetic
    return int(sum(temp_results) - min(temp_results))

# Execution point of interest
final_score = aggregate_performance(raw_readings, base_offset)

print(f"Target result: {final_score}")