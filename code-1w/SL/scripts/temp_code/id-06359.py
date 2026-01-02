def transform_sequence(seq, factor):
    """Irrelevant transformation function (dead code path)"""
    return [x * factor + 2 for x in seq if x % 2 == 0]


def accumulate_segments(data, limit):
    """Another decoy function that is never called"""
    total = 0
    segments = []
    for val in data:
        if total + val < limit:
            total += val
        else:
            segments.append(total)
            total = val
    if total > 0:
        segments.append(total)
    return segments

# Simulated sensor array metadata (mostly irrelevant)
sensor_labels = ['S1', 'S2', 'S3', 'S4', 'S5']
installation_date = '2023-07-15'
firmware_version = 'v2.1.8'

# Raw diagnostic readings from system modules (mixed relevant/irrelevant)
raw_readings = [127, 255, 192, 64, 31, 15, 8, 111, 240, 168]

# Noise filter mask using string-based bit tagging (distractor)
bit_flags = '11011010'
mask_filter = [i for i, b in enumerate(bit_flags) if b == '1']
filtered_noise = [raw_readings[i] for i in range(len(raw_readings)) if i % 8 in mask_filter]

# Core processing begins here — actual relevant logic
threshold_map = {
    'low': 64,
    'medium': 128,
    'high': 192
}

scaling_factor = 1.75
adjusted_readings = [round(x * scaling_factor) for x in raw_readings]

# Bit manipulation layer: XOR with position index (partial relevance)
positionally_adjusted = []
for idx, val in enumerate(adjusted_readings):
    transformed = val ^ idx  # XOR with index to obscure pattern
    positionally_adjusted.append(transformed)

# Conditional filtering based on dynamic criteria
processed_data = []
count_high_severity = 0
warning_codes = []

for num in positionally_adjusted:
    # Determine severity level
    if num >= threshold_map['high']:
        severity = 'CRITICAL'
        count_high_severity += 1
        warning_codes.append(num % 11)
    elif num >= threshold_map['medium']:
        severity = 'HIGH'
    elif num >= threshold_map['low']:
        severity = 'MODERATE'
    else:
        severity = 'LOW'
    
    # Only collect CRITICAL and MODERATE
    if severity in ['CRITICAL', 'MODERATE']:
        processed_data.append(num)

# Additional distraction: fake checksum calculation (never used)
temp_checksum = 0
for x in warning_codes:
    temp_checksum = (temp_checksum + x) * 3 % 17

# Decoy list comprehension for statistical summary (unused)
stat_summary = [sum(processed_data), len(processed_data), sum(processed_data) / len(processed_data) if processed_data else 0]

# Real analysis function — key logic
def analyze_readings(data_list, limits):
    base_score = 0
    adjustment = 0
    for item in data_list:
        if item > limits['medium']:
            base_score += item // 10
        else:
            base_score -= item % 7
        
        # String method used for digit analysis (required feature)
        binary_rep = bin(item)[2:]  # Remove '0b' prefix
        ones_count = binary_rep.count('1')
        zeros_count = binary_rep.count('0')
        if ones_count > zeros_count:
            adjustment += 3
        else:
            adjustment -= 2
    
    # Final computation combining arithmetic and bit logic
    final_score = base_score * 2 + adjustment
    return final_score

# Execution point of interest
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")