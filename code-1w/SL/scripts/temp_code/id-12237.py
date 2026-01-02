def transform_signal(raw_values, factor):
    """Apply non-linear transformation to sensor signal (distractor)"""
    return [round((x ** 0.5) * factor + 2.5, 2) for x in raw_values if x > 0]


def validate_checksum(data_str):
    """Compute ASCII checksum for data integrity (irrelevant)"""
    return sum(ord(c) for c in data_str) % 256


def decode_sequence(seq):
    """Decode bit-packed sequence (dead path)"""
    decoded = []
    for s in seq:
        val = 0
        for ch in s:
            val = (val << 1) | (1 if ch == '1' else 0)
        decoded.append(val)
    return decoded

# Simulated sensor inputs (some irrelevant)
sensor_a_readings = [16, 25, 36, 49, 64]
sensor_b_readings = [10, -5, 0, 15, 20]  # Contains negative and zero (filtered out)
sensor_c_readings = [81, 100, 121]
dummy_labels = ['A', 'B', 'C', 'D', 'E']

# Irrelevant transformation (distractor call)
transformed = transform_signal(sensor_a_readings, 1.75)

# Data preprocessing block
filtered_b = [x for x in sensor_b_readings if x > 0]  # Remove non-positive
normalized = [round(x ** 0.5, 3) for x in filtered_b]  # sqrt normalization

# Threshold logic with dictionary mapping
threshold_map = {
    'low': 2.0,
    'medium': 3.0,
    'high': 4.0
}

status_flags = []
for val in normalized:
    if val < threshold_map['low']:
        status_flags.append('NOMINAL')
    elif val < threshold_map['medium']:
        status_flags.append('CAUTION')
    else:
        status_flags.append('ALERT')

# Tuple-based packing of results (mixed relevance)
data_packed = list(zip(filtered_b, normalized, status_flags))

# Core analysis function (key relevant logic)
def analyze_readings(data_list, limits):
    """Analyze normalized readings against thresholds to compute diagnostic score."""
    score = 0
    alert_count = 0
    
    for original, norm, flag in data_list:
        # Scoring logic: each ALERT adds exponentially
        if flag == 'ALERT':
            score += int(norm) ** 2
            alert_count += 1
        elif flag == 'CAUTION':
            score += int(norm) * 2
        else:
            score += 1
    
    # Recursive adjustment based on alert count
    def adjust_score(n):
        if n <= 1:
            return n
        return n + adjust_score(n - 1)
    
    bonus = adjust_score(alert_count) if alert_count > 0 else 0
    final_score = score + bonus
    
    # String-based mode check (uses string method)
    mode = 'STABLE' if final_score < 20 else 'VOLATILE'
    modifier = 0.9 if mode.startswith('VO') else 1.1
    
    # Final adjusted diagnostic value
    return int(final_score * modifier)

# Processed data used in final call
processed_data = data_packed

# Misleading checksum validation (red herring)
checksum = validate_checksum('sensor_b_data_block_01')
if checksum > 100:
    dummy_labels.append('CHECK_PASSED')

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")