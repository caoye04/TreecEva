def analyze_pattern(seq, threshold):
    count = 0
    for i in range(len(seq)):
        if seq[i] % 2 == 0:
            count += 1
            if count > threshold:
                break
    return count * 2


def validate_entry(record):
    if not record.get('active'):
        return False
    if record['value'] < 0:
        return False
    return True

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    import math
    freq = {}
    total = len(data)
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = 0.0
    for f in freq.values():
        p = f / total
        entropy -= p * math.log2(p)
    return round(entropy, 4)

# Unused transformation chain
def transform_chain(x):
    x = (x ** 2 + 3) % 7
    x = (x * 5 - 1) // 2
    return x

# Distractor variables
temp_offset = 17
scaling_factor = 0.91
buffer_pool = [0] * 15

# Real computation begins
raw_data = [3, 7, 2, 8, 4, 6, 9, 1]
filter_mask = [x > 5 for x in raw_data]
selected_indices = [i for i, valid in enumerate(filter_mask) if valid]

# Simulate data records with metadata
records = [
    {'id': idx, 'value': val, 'active': (idx % 2 == 0), 'tag': f't{idx%3}'}
    for idx, val in enumerate(raw_data)
]

# Filter valid records using validate_entry (some are inactive or invalid)
valid_records = [r for r in records if validate_entry(r)]

# Extract values from valid records
extracted_values = [r['value'] for r in valid_records]

# Weight mapping by tag group
weight_map = {'t0': 1.1, 't1': 0.8, 't2': 1.5}
weights = [weight_map[r['tag']] for r in valid_records]

# Apply sliding window sum of size 2 (irrelevant intermediate)
window_sums = [extracted_values[i] + extracted_values[i+1] 
               for i in range(len(extracted_values)-1)]

# Key data used in final calculation
data = []
for i, val in enumerate(extracted_values):
    # Compute contribution with index modulation
    mod_val = val * (i + 1) * weights[i]
    data.append(mod_val)

# Another decoy: bit manipulation chain (unused)
current_state = 0b1101
current_state ^= 0b1010
current_state |= (current_state << 2)
current_state &= 0xFF

# Dictionary aggregation by transformed keys
tag_grouped = {}
for r in valid_records:
    tag = r['tag']
    if tag not in tag_grouped:
        tag_grouped[tag] = []
    tag_grouped[tag].append(r['value'])

avg_groups = {k: sum(v)/len(v) for k, v in tag_grouped.items()}

# Secondary distraction: string processing on ids
id_strings = [str(r['id']) for r in valid_records]
joined_ids = ''.join(id_strings)
split_parts = joined_ids.split('2')

# Real processing function
def process_results(values, wts):
    total_weighted = 0.0
    total_norm = 0.0
    for i, (v, w) in enumerate(zip(values, wts)):
        adjusted = v * w
        penalty = abs(i - len(values)//2) * 0.1
        total_weighted += adjusted - penalty
        total_norm += w
    base_score = total_weighted / (total_norm + 1e-8)
    
    # Additional correction based on pattern analysis
    pattern_hint = analyze_pattern(raw_data, 3)
    correction_factor = 0.5 if pattern_hint > 8 else 1.2
    
    # Final nonlinear scaling
    final_raw = base_score * correction_factor
    
    # Red herring: unused rounding variants
    rnd_floor = int(final_raw)
    rnd_ceil = int(-(-final_raw // 1))
    
    return int(round(final_raw))

# Execute main logic
dummy_entropy = calculate_entropy([1,2,2,3,3,3])

final_score = process_results(data, weights)
print(f"Result: {final_score}")