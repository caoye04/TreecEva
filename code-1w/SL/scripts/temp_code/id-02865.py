from collections import defaultdict, Counter

# Simulated sensor data ingestion with noise and redundant fields
data_stream = [
    {'id': 1, 'val': 3, 'type': 'A', 'err': False, 'meta': 'x'},
    {'id': 2, 'val': 5, 'type': 'B', 'err': True,  'meta': 'y'},
    {'id': 3, 'val': 4, 'type': 'A', 'err': False, 'meta': 'x'},
    {'id': 4, 'val': 8, 'type': 'C', 'err': False, 'meta': 'z'},
    {'id': 5, 'val': 2, 'type': 'B', 'err': False, 'meta': 'y'},
    {'id': 6, 'val': 7, 'type': 'A', 'err': False, 'meta': 'x'},
    {'id': 7, 'val': 6, 'type': 'C', 'err': True,  'meta': 'z'},
    {'id': 8, 'val': 1, 'type': 'A', 'err': False, 'meta': 'x'},
]

# Irrelevant aggregation: counts per meta (not used in final logic)
meta_counter = defaultdict(int)
for item in data_stream:
    meta_counter[item['meta']] += 1

# Filter out erroneous readings — relevant step
clean_data = [item for item in data_stream if not item['err']]

# Decoy transformation: convert to higher precision (unused)
decoy_precision_data = [{'val': float(d['val']) * 1.0001, 'type': d['type']} for d in clean_data]

# Group by type for analysis — relevant
 grouped_by_type = defaultdict(list)
for item in clean_data:
    grouped_by_type[item['type']].append(item['val'])

# Compute summary stats — some relevant, some not
summary_stats = {}
total_values_seen = 0  # Red herring counter
for t in grouped_by_type:
    vals = grouped_by_type[t]
    summary_stats[t] = {
        'sum': sum(vals),
        'max': max(vals),
        'min': min(vals),
        'count': len(vals),
        'range': max(vals) - min(vals)
    }
    total_values_seen += len(vals)  # Incremented but unused later

# Spurious bitwise masking operation on type keys (distractor)
type_masks = {}
for typ in grouped_by_type:
    mask_key = 0
    for c in typ:
        mask_key ^= ord(c) << 2
    type_masks[typ] = mask_key & 0xFF  # Truncate to byte

# Simulate checksum from unrelated historical data (dead path)
historical_ids = [1, 3, 6, 8]
historical_checksum = 0
for hid in historical_ids:
    historical_checksum += hid * 11
    historical_checksum &= 0xFFFF

# Critical filtering: only types with count >= 2 are valid
filtered_types = {t: v for t, v in summary_stats.items() if v['count'] >= 2}

# Extract filtered data based on valid types — now we rebuild dataset
filtered_data = []
for item in clean_data:
    if item['type'] in filtered_types:
        filtered_data.append(item['val'])

# Unused frequency map (set operation red herring)
unique_vals_set = set(filtered_data)
complement_vals = {i for i in range(1, 10) if i not in unique_vals_set}  # Distractor

# System key derived from spurious formula involving min and max across all
overall_min = min(summary_stats[t]['min'] for t in filtered_types)
overall_max = max(summary_stats[t]['max'] for t in filtered_types)
system_key = (overall_max ^ overall_min) + len(filtered_types)

# Real processing function with nested logic
def process_signals(data, key):
    # Nested default dictionary for intermediate state tracking (overkill)
    state = defaultdict(lambda: defaultdict(int))
    temp_log = []

    # Bit manipulation decoy
    transformed_key = ((key << 3) & 0xFF) ^ (key >> 2)

    # Artificial segmentation
    segments = []
    segment = []
    for i, v in enumerate(data):
        segment.append(v)
        if (v + i) % 3 == 0 or i == len(data) - 1:
            segments.append(segment[:])
            segment.clear()

    # Count frequencies per segment (unnecessary detail)
    freq_in_segments = Counter()
    for idx, seg in enumerate(segments):
        freq_in_segments[idx] = len(seg)
        for val in seg:
            state['values']['total'] += val
            state['flags'][val % 2] += 1
            temp_log.append(val * transformed_key)  # Logged but unused

    # Core calculation buried in distractions
    base_sum = sum(data)
    adjustment = state['flags'][1] - state['flags'][0]  # diff of odd vs even counts
    penalty = len(segments) * 2

    # Final formula hidden among irrelevant operations
    result = base_sum + (adjustment * key) - penalty

    # Dead conditional: never executed due to logic
    if len(temp_log) > 100:
        fallback = 0
        for x in temp_log:
            fallback ^= int(x)
        result = fallback

    return result

# Execute critical statement
final_diagnostic = process_signals(filtered_data, system_key)
print(f"Target result: {final_diagnostic}")