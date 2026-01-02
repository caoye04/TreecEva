from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings
def load_sensor_metadata():
    return {
        'sensors': [f'sensor_{i}' for i in range(15)],
        'calibration': {f's_{i}': (i % 3) for i in range(15)},
        'threshold': 7.2
    }

def legacy_filter(data, limit=5):
    # Obsolete function - not used in main logic
    return [x for x in data if x > limit]

def generate_checksum(sequence):
    # Unused checksum generator - distraction
    return sum(x ^ (x << 1) for x in sequence) % 1000

def apply_mask(values, mask_type='xor'):
    if mask_type == 'xor':
        return [v ^ (v & 7) for v in values]
    elif mask_type == 'add':
        return [v + (v % 4) for v in values]
    return values

def recursive_reduce(seq, depth=0):
    if len(seq) <= 1 or depth >= 3:
        return seq[0] if seq else 0
    mid = len(seq) // 2
    new_seq = [seq[i] - seq[i+1] for i in range(0, mid*2-1, 2)]
    return recursive_reduce(new_seq, depth + 1)

def count_transitions(data):
    transitions = 0
    for i in range(1, len(data)):
        if (data[i-1] < 0) != (data[i] < 0):
            transitions += 1
    return transitions

def analyze_pattern(data_list):
    # Core analysis function
    stats = defaultdict(int)
    for val in data_list:
        if val > 0:
            stats['positive'] += 1
        elif val < 0:
            stats['negative'] += 1
        if val % 2 == 1:
            stats['odd_count'] += 1

    sorted_vals = sorted(data_list, key=lambda x: -abs(x))
    top_quartile = sorted_vals[:len(sorted_vals)//4]
    
    # Real computation path
    base_score = sum(abs(x) for x in top_quartile)
    penalty = stats['odd_count'] * 2
    adjustment = abs(stats['positive'] - stats['negative'])
    
    # Irrelevant intermediate calculations (distractors)
    _ = [x * 1.5 for x in data_list if x % 4 == 0]
    _temp_sum = sum(x**2 for x in data_list[:5])  # unused
    _useless_map = dict(map(lambda x: (x, x*3), range(3)))
    
    return base_score - penalty + adjustment

# Main execution flow
sensor_meta = load_sensor_metadata()
data_stream = [i * (-1)**i * (i % 11) for i in range(1, 21)]  # alternating pattern

# Apply transformation chain
masked_data = apply_mask(data_stream, 'xor')
filtered_data = [x for x in masked_data if abs(x) > 2]  # relevant filter
extended_data = filtered_data + [x - 1 for x in filtered_data[:3]]
sliced_data = extended_data[1::2]  # take every second element

# Dead code path - never called
if False:
    alt_result = legacy_filter(sliced_data)
    verify = generate_checksum(alt_result)

# Transform via slicing and mapping
transformed_data = sliced_data[::-1]  # reverse

# Introduce more distractions
freq_count = Counter(transformed_data)
duplicate_correction = sum(v - 1 for v in freq_count.values() if v > 1)

# Critical statement
final_diagnostic = analyze_pattern(transformed_data)

# Additional noise
_debug_info = {
    'size': len(transformed_data),
    'range': max(transformed_data) - min(transformed_data),
    'zeros': transformed_data.count(0)
}
other_metric = recursive_reduce(transformed_data[:8])

# Print result
print(f"Result: {final_diagnostic}")