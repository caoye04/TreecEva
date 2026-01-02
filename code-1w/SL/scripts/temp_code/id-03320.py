def analyze_pattern(sequence):
    if len(sequence) < 3:
        return False
    peaks = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            peaks += 1
    return peaks >= 2

# Irrelevant helper function (decoy)
def validate_checksum(data_str):
    count = 0
    for char in data_str:
        if char.isdigit():
            count += int(char)
    return count % 7 == 0

# Unused transformation (dead code path)
def transform_legacy_format(raw_list):
    transformed = []
    for item in raw_list:
        if isinstance(item, str):
            transformed.append(len(item) * 2)
        else:
            transformed.append(item ** 0.5)
    return transformed

# Character counting distraction
def count_chars_in_labels(label_dict):
    total = 0
    for key, label in label_dict.items():
        total += len(label.replace('-', '').lower())
    return total  # never used

# Core logic disguised among distractors
def filter_critical_entries(entries, flags):
    result = []
    for i, entry in enumerate(entries):
        if flags[i] and entry > 0 and (entry & 7) != 4:
            result.append(entry)
    # Early return red herring (not taken)
    if len(result) == 0:
        return [-1]
    return result

# Bit manipulation decoy
def encode_signal(value):
    shifted = (value << 3) & 0xFF
    toggled = shifted ^ 0b10101010
    return (toggled >> 2) | (value & 0b11)

# Main processing chain
def compute_baseline(reference_list):
    baseline = 0
    for val in reference_list:
        if val % 2 == 0:
            baseline += val ** 2
        else:
            baseline -= val
    return baseline // len(reference_list)

# Distractor: unused statistical check
def has_outlier_sequence(values):
    if len(values) < 4:
        return False
    avg = sum(values) / len(values)
    return any(abs(v - avg) > 2 * avg for v in values[:3])

# Real work hidden in complexity
def process_readings(data_samples, config_map):
    temp_buffer = []
    scale_factor = config_map['gain']
    offset = config_map.get('offset', 0)
    
    # Irrelevant string processing (distractor)
    labels = ["sensor_A", "sensor_B", "sensor_C"]
    label_hash = 0
    for label in labels:
        label_hash += sum(ord(c) for c in label if c in 'aeiou')
    
    # Meaningful but obscured computation
    for sample in data_samples:
        adjusted = sample * scale_factor + offset
        if adjusted > config_map['threshold']:
            temp_buffer.append(int(adjusted))
    
    # Filter using bitwise condition (critical)
    filtered = [x for x in temp_buffer if (x | 5) != 15]
    
    # Real answer derived here
    aggregate = 0
    for val in filtered:
        if val % 3 == 0:
            aggregate += val // 3
        else:
            aggregate -= val % 4
    
    # Decoy dictionary operation
    stats = {"count": len(filtered), "sum": sum(filtered)}
    stats["ratio"] = stats["sum"] / stats["count"] if stats["count"] > 0 else 0
    
    # Final transformation
    final_score = aggregate * 2
    
    # Critical assignment
    final_diagnostic = final_score + 337
    return final_diagnostic

# Setup with misleading variables
raw_input_data = [0.8, 1.2, 3.1, 4.6, 5.0, 6.3]
decoys = [encode_signal(x) for x in [12, 8, 15]]

# Dictionary operation (required feature)
threshold_map = {
    'threshold': 7.5,
    'gain': 2.5,
    'offset': -1.0,
    'active': True
}

# Set operation distraction
used_ids = {101, 205, 302, 408}
pending_ids = {205, 302, 501}
incomplete = used_ids & pending_ids  # irrelevant intersection

# String method distraction
timestamps = ["2023-12-01T08:00", "2023-12-01T09:15"]
cleaned_times = [t.split('T')[1].replace(':', '') for t in timestamps]

# Actual data feeding into logic
collected_data = [2.0, 4.0, 3.0, 8.0, 12.0, 1.0]

# Flag array for filtering (partially used)
activation_flags = [True, True, False, True, True, True]

# Real signal extraction (buried)
valid_entries = filter_critical_entries(collected_data, activation_flags)

# Baseline computation (semi-relevant)
base = compute_baseline([4, 6, 8, 10])

# Trigger the actual target statement
final_diagnostic = process_readings(collected_data, threshold_map)

# Output the required result
print(f"Result: {final_diagnostic}")