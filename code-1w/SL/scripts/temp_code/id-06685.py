def normalize_string(s):
    return s.lower().replace(' ', '').replace('-', '')

# Simulate processing of sensor data with metadata tagging
data_entries = [
    {'raw': 'Temp-23C', 'type': 'sensor', 'seq': 1},
    {'raw': 'HUMID 45PCT', 'type': 'sensor', 'seq': 2},
    {'raw': 'PRESSURE 1013', 'type': 'sensor', 'seq': 3},
    {'raw': 'ERROR-NULL', 'type': 'error', 'seq': 4}
]

stats_tracker = {
    'valid_count': 0,
    'total_chars': 0,
    'normalized_sum': 0,
    'skipped': 0
}

processed_data = []
buffer_cache = []

for entry in data_entries:
    if entry['type'] != 'sensor':
        stats_tracker['skipped'] += 1
        continue

    clean_text = normalize_string(entry['raw'])
    
    # Extract numeric value using basic string analysis
    num_str = ''
    for char in clean_text:
        if char.isdigit():
            num_str += char
    
    if num_str:
        numeric_value = int(num_str)
        category_key = 'temp' if 'temp' in clean_text else 'other'
        offset_correction = 5 if category_key == 'temp' else 0
        adjusted_value = numeric_value + offset_correction
        
        processed_data.append({
            'seq': entry['seq'],
            'value': numeric_value,
            'corrected': adjusted_value,
            'tag': category_key
        })
        
        stats_tracker['valid_count'] += 1
        stats_tracker['total_chars'] += len(clean_text)
        stats_tracker['normalized_sum'] += adjusted_value
    
    # Misleading accumulation - looks important but unused later
    buffer_cache.append(len(clean_text) * entry['seq'])

# Dead code path - simulates alternative logic but never called
def legacy_compatibility_mode(data):
    return sum(len(d['raw']) for d in data if 'C' in d['raw'])

# Auxiliary calculation that seems relevant but is only partially used
total_processed = stats_tracker['valid_count']
avg_length = stats_tracker['total_chars'] / total_processed if total_processed else 0
dummy_anchor = sum(buffer_cache) // len(buffer_cache) if buffer_cache else 0

# Real computation begins here — semantic weighting by tag type
tag_weights = {'temp': 3, 'other': 2}
weighted_sum = 0
weight_total = 0

for record in processed_data:
    w = tag_weights[record['tag']]
    weighted_sum += record['corrected'] * w
    weight_total += w

mean_weighted = weighted_sum / weight_total if weight_total else 0

# Secondary adjustment based on sequence continuity
seq_values = [r['seq'] for r in processed_data]
seq_gap_penalty = 0
for i in range(1, len(seq_values)):
    if seq_values[i] - seq_values[i-1] > 1:
        seq_gap_penalty += 1

# Final scoring with red herring variables included to increase cognitive load
drift_compensation = stats_tracker['skipped'] * 2.5
fudge_factor = avg_length // 5  # Looks sophisticated but minor impact

final_score = int(mean_weighted + fudge_factor - seq_gap_penalty + 0.5)  # Rounded integer

# Irrelevant formatting operation — distractor
display_label = f"Score: {final_score}".ljust(20, '.')

# Critical execution point
final_score = calculate_final_score(processed_data)

print(f"Result: {final_score}")

def calculate_final_score(data):
    base = 0
    count = 0
    for item in data:
        # Recompute corrected values consistently
        tag_mult = 3 if item['tag'] == 'temp' else 2
        base += item['corrected'] * tag_mult
        count += tag_mult
    raw_mean = base / count if count else 0
    gap_count = sum(1 for i in range(1, len(data)) if data[i]['seq'] - data[i-1]['seq'] > 1)
    return int(raw_mean - gap_count + 1)