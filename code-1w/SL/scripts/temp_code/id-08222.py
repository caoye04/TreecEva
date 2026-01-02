def transform_signal(raw):
    """Irrelevant signal transformation (dead-end function)."""
    return [x * 0.95 + 2 for x in raw]


def validate_checksum(data):
    """Misleading validation with no actual use in logic."""
    checksum = sum(data) % 17
    return checksum == 0

# Simulated sensor readings (some are decoys)
sensor_a = [12, 15, 14, 18, 22, 25, 24, 20, 17, 16]
sensor_b = [8, 10, 11, 14, 16, 19, 21, 23, 20, 18]
sensor_c = [50, 45, 40, 35, 30, 25, 20, 15, 10, 5]  # Decoy: descending irrelevant data

# Irrelevant preprocessing path
temp_normalized = [round((x - min(sensor_a)) / (max(sensor_a) - min(sensor_a)), 3) for x in sensor_a]

# Real processing begins here
filtered = [x for x in sensor_b if x > 9]
smoothed = [sum(filtered[i:i+3]) / 3 for i in range(len(filtered) - 2)]

def augment_series(series):
    """Adds positional bias - actually used."""
    return [val + idx * 0.1 for idx, val in enumerate(series)]

augmented = augment_series(smoothed)

# Threshold mapping with red herring entries
threshold_map = {
    'low': 12.0,
    'medium': 14.5,
    'high': 18.0,
    'critical': 25.0,
    'ignore_me': 999  # Distractor key
}

# Data fusion using zip and conditional logic
fused = []
for a, b in zip(augmented, augmented[1:]):
    if a < b:
        fused.append(a * 1.05)
    else:
        fused.append(a * 0.97)

# Conditional expression with slicing to mask intent
processed_data = fused if len(fused) > 4 else fused[::-1]
processed_data = processed_data[:len(processed_data)//2 + 1]  # Truncate to first half + 1

# Spurious counting operation (distractor)
count_high = 0
for x in sensor_c:
    if x > 30:
        count_high += 1  # This is never used

# Core analysis function with nested logic
def analyze_readings(readings, limits):
    alert_level = 0
    history = []
    
    for i, val in enumerate(readings):
        # Bit manipulation decoy
        bit_flag = (i ^ 3) & 1
        
        # Real condition chain
        if val > limits['medium']:
            adjustment = val / (i + 1) if i > 0 else val
            if adjustment > limits['low']:
                alert_level += int(adjustment // 2)
            else:
                alert_level -= 1
        elif val < limits['low']:
            alert_level += 1
            
        # Use of enumerate with conditional expression
        status = 'stable' if val < limits['medium'] else 'elevated'
        history.append({
            'index': i,
            'value': round(val, 2),
            'status': status,
            'flag': bit_flag
        })
    
    # Final computation buried in logic
    base_score = sum(r['value'] for r in history if r['status'] == 'elevated')
    penalty = len([r for r in history if r['flag'] == 1]) * 1.5
    final_index = base_score - penalty
    
    # Critical statement
    final_diagnostic = int(round(final_index * 2.718))
    
    return final_diagnostic

# Dead function call (misdirection)
_ = transform_signal(sensor_c)

# Key execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result as required
print(f"Target result: {final_diagnostic}")