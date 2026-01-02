from collections import defaultdict, Counter

# Simulated sensor data processing with red herrings
def process_sensor_array(raw_readings):
    filtered_data = [x for x in raw_readings if x > 0]
    stats = defaultdict(int)
    
    for val in filtered_data:
        if val % 2 == 0:
            stats['even'] += 1
        else:
            stats['odd'] += 1
        if val > 50:
            stats['high'] += 1

    # Distractor: unused transformation path
    transformed = list(map(lambda x: (x ** 0.5) * 1.5, filtered_data))
    outlier_count = 0
    for t in transformed:
        if t > 40:
            outlier_count += 1  # Dead code path — never used

    # Meaningful but obscured computation
    base_metric = sum(filtered_data) // len(filtered_data) if filtered_data else 0
    adjustment = stats['even'] - stats['odd']
    return base_metric, adjustment

# Legacy system compatibility layer (mostly irrelevant)
def legacy_compatibility_mode(data, mode='v1'):
    checksum = 0
    for item in data:
        checksum ^= item  # Bitwise distraction
    if mode == 'v2':
        return checksum * 2
    return checksum  # Unused return in main flow

# Main diagnostic sequence
sensor_inputs = [12, -5, 67, 34, 89, 0, 23, 44, 56, 78, 91, 13]

# Irrelevant preprocessing chain
preliminary_scan = [x * 2 + 1 for x in sensor_inputs if x % 3 != 0]
duplicate_counter = Counter(preliminary_scan)
redundant_sum = sum([k * v for k, v in duplicate_counter.items() if k < 100])

# Real processing begins here (buried among distractions)
primary_metric, delta_adjust = process_sensor_array(sensor_inputs)

# Fake feedback loop (looks important, does nothing)
feedback_buffer = []
for _ in range(3):
    feedback_buffer.append(primary_metric * 0.1)
    primary_metric += len(feedback_buffer)  # Slight mutation, but ultimately corrected

# Undo spurious mutations
primary_metric -= sum(feedback_buffer) // 10

# Core logic embedded within noise
reference_table = {
    'baseline': 100,
    'tolerance': 5,
    'version': '3.2a'
}

# Multiple layers of conditional logic
if primary_metric > reference_table['baseline'] - reference_table['tolerance']:
    aggregate_score = primary_metric * 2
else:
    aggregate_score = primary_metric * 1.5

# Secondary correction using bit manipulation (distractor-heavy)
temp_flag = 0b1010
flag_mask = 0b1100
masked = temp_flag & flag_mask
shifted = masked << 2
bit_noise = shifted ^ 0b1111  # Computationally irrelevant

# Actual correction factor derived from earlier adjustment
if delta_adjust > 0:
    correction_factor = 17
elif delta_adjust < 0:
    correction_factor = -23
else:
    correction_factor = 5

# Key assignment statement — target of question
final_diagnostic = aggregate_score + correction_factor

# Red herring: unused diagnostics
consistency_check = legacy_compatibility_mode(sensor_inputs)
validation_trace = [final_diagnostic ^ i for i in range(5)]

# Output the target result
print(f"Result: {final_diagnostic}")