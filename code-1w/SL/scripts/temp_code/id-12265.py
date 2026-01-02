from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings and distractions
def process_sensor_array(raw_data):
    temp_buffer = []
    error_flags = []
    diagnostic_log = defaultdict(int)
    
    for index, reading in enumerate(raw_data):
        if reading < 0:
            diagnostic_log['negative_readings'] += 1
            continue
        
        shifted = reading >> 2
        if shifted % 3 == 0:
            temp_buffer.append(shifted * 1.5)
        elif shifted % 3 == 1:
            error_flags.append(index)
            temp_buffer.append(shifted ** 0.5)
        else:
            temp_buffer.append(shifted + (index & 3))
    
    return temp_buffer, diagnostic_log

# Legacy system compatibility layer (distractor)
def legacy_calibrate(x):
    return (x << 1) ^ 0xFF

# Irrelevant statistical summary (dead path)
def compute_distribution_metrics(data):
    count = len(data)
    mean = sum(data) / count if count else 0
    variance = sum((x - mean) ** 2 for x in data) / count if count else 0
    mode = Counter(data).most_common(1)[0][0] if data else 0
    return {'mean': round(mean, 4), 'variance': round(variance, 4), 'mode': mode}

# Main diagnostic workflow
raw_input_stream = [24, 18, -5, 36, 42, 15, 27, 33, 12, 6]

# Step 1: Process raw sensor array
filtered_values, logs = process_sensor_array(raw_input_stream)

# Step 2: Apply phantom correction (irrelevant)
phantom_adjustments = []
for val in filtered_values:
    if val > 20:
        phantom_adjustments.append(legacy_calibrate(int(val)))

# Step 3: Compute active diagnostics
active_thresholds = [x for x in filtered_values if x < 15]
running_total = 0
for i, val in enumerate(filtered_values):
    if i % 2 == 0:
        running_total += int(val) // (i + 1) if i > 0 else int(val)
    else:
        running_total -= int(val) % 7

diagnostic_sum = sum(int(x) for x in active_thresholds)

# Step 4: Hidden bit manipulation chain (critical path)
bit_accumulator = 0
for val in [12, 6, 3]:
    bit_accumulator ^= (val << 2) | (val & 3)

scaling_factor = len(active_thresholds) or 1
correction_factor = (bit_accumulator % 100) / scaling_factor

# Step 5: Aggregate from multiple sources (mixing relevant and irrelevant)
aggregate_score = 0
if logs.get('negative_readings'):
    aggregate_score += 50
else:
    aggregate_score += len(filtered_values) * 3

# Dead logic branch — never executed due to data
if any(x > 1000 for x in phantom_adjustments):
    aggregate_score *= 2

# Critical assignment point
final_diagnostic = aggregate_score + correction_factor

# Distraction: unused complex structure
snapshot = {
    'raw_count': len(raw_input_stream),
    'processed_count': len(filtered_values),
    'error_rate': len(logs) / len(raw_input_stream),
    'phantom_total': sum(phantom_adjustments),
    'debug_trace': compute_distribution_metrics(filtered_values)
}

print(f"Result: {final_diagnostic}")