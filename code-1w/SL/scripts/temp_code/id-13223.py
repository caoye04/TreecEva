def analyze_pattern(sequence, threshold):
    if len(sequence) < threshold:
        return sum([x ** 2 for x in sequence if x % 2 == 0])
    else:
        return sum([x for x in sequence if x > 0])


def transform_data(input_str, mode='hex'):
    # Irrelevant transformation branch
    if mode == 'hex':
        hex_vals = [ord(c) % 16 for c in input_str]
        return [h + 5 for h in hex_vals]
    elif mode == 'oct':
        return [ord(c) % 8 for c in input_str]  # Dead code path
    else:
        return []

# Misleading preprocessing
raw_signal = [3, -1, 4, 1, 5, 9, 2, 6]
decoy_signal = [x * 2 + 1 for x in raw_signal if x < 5]
filtered_signal = [x for x in raw_signal if x >= 2]

# Unused intermediate calculations
offset_correction = sum(decoy_signal) // len(decoy_signal) if decoy_signal else 0
normalization_factor = max(filtered_signal) / min(filtered_signal)

# String-based red herring
diagnostic_tag = 'SYS_DIAG_2077v2'
version_code = diagnostic_tag.split('_')[-1].rstrip('v')
revision_number = int(version_code) if version_code.isdigit() else 2

# Key slicing operation (relevant)
segment_a = filtered_signal[1:4]  # [4, 1, 5]
segment_b = filtered_signal[-3:]  # [5, 9, 2]

# Distractor: unused tuple unpacking
primary, secondary, tertiary = segment_a[0], segment_a[1], segment_a[2]

# Composite list with irrelevant transformations
hybrid_chain = []
for i in range(len(segment_a)):
    val = segment_a[i] * 3 - segment_b[i] % 4
    hybrid_chain.append(val)

# Decoy dictionary with misleading keys
status_map = {
    'init': 101,
    'pending': 205,
    'active': 888,  # looks important but unused
    'final': 999   # red herring
}

# Simulated processing chain (only some parts matter)
processing_chain = []
for x in hybrid_chain:
    if x > 10:
        processing_chain.append(x // 2)
    else:
        processing_chain.append(x * 2)

# Conditional manipulation using string method result
if 'v' in diagnostic_tag.lower():
    processing_chain = [p + revision_number for p in processing_chain]

# Validation key derived from string slicing
validation_key = int(diagnostic_tag[10:14])  # 2077

# Function that appears complex but has deterministic flow
def aggregate_metrics(chain, key):
    base_score = sum(chain)
    adjustment = key % 100
    
    # Bitwise distraction
    flag_mask = 0b1101
    control_flag = (adjustment ^ flag_mask) & 0b1111
    
    # Real computation buried in noise
    if control_flag > 10:
        temp_result = base_score * 1.5
    else:
        temp_result = base_score * 1.2
    
    # Final logic step involving average and floor
    avg_val = sum(segment_a) / len(segment_a)
    final_offset = int(avg_val)  # 3
    
    # Actual answer calculation
    result = int(temp_result - final_offset * 4)
    
    # Dead code — never reached
    if result < 0:
        fallback = status_map['init']
        return fallback
    
    return result

# Critical execution point
final_diagnostic = aggregate_metrics(processing_chain, validation_key)
print(f"Result: {final_diagnostic}")