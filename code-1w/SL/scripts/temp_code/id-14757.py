from collections import defaultdict
import math

# Simulated sensor data aggregation (irrelevant but plausible)
sensor_readings = [1.2, 3.4, 2.1, 5.6, 4.3, 3.3, 2.7, 3.9]
smoothed_data = [round((a + b) / 2, 1) for a, b in zip(sensor_readings, sensor_readings[1:])]

def analyze_trend(data):
    # Distractor function: computes trend slope but unused later
    n = len(data)
    if n < 2:
        return 0.0
    sum_xy = sum(i * v for i, v in enumerate(data))
    sum_x = sum(range(n))
    sum_y = sum(data)
    sum_x2 = sum(i**2 for i in range(n))
    denominator = n * sum_x2 - sum_x**2
    return (n * sum_xy - sum_x * sum_y) / denominator if denominator != 0 else 0.0

trend_coeff = analyze_trend(smoothed_data)  # Red herring value

# Irrelevant data structure for system logs
event_log = defaultdict(int)
for event in ['init', 'read', 'write', 'read', 'flush', 'read']:
    event_log[event] += 1

# Core logic disguised among distractors
def process_metrics(raw):
    # Apply non-linear transformation (relevant)
    transformed = [math.log(x) ** 2 for x in raw if x > 0]
    
    # Decoy filtering (never actually used)
    filtered_high = [x for x in transformed if x > 2.0]
    filtered_low = [x for x in transformed if x <= 1.5]
    
    # Actual working path
    avg_transformed = sum(transformed) / len(transformed)
    deviation_scores = [abs(t - avg_transformed) for t in transformed]
    return deviation_scores

# Another red-herring function with complex logic
def compute_entropy(data):
    freq = defaultdict(float)
    for d in data:
        freq[round(d, 1)] += 1
    total = len(data)
    return -sum((count / total) * math.log(count / total) for count in freq.values())

entropy_value = compute_entropy(sensor_readings)  # Unused complexity

# Real input pipeline
raw_input_stream = [8, 6, 7, 5, 3, 0, 9]  # Missing zero handled
filtered_stream = [x for x in raw_input_stream if x != 0]  # Remove invalids

# Bit manipulation decoy
bitmask = 0b101010
masked_values = [v ^ bitmask for v in filtered_stream]  # Computed but unused

# String processing distraction
diag_id = "SYS_DIAG_001"
version_code = diag_id.split('_')[-1]
build_number = int(version_code[1:]) if version_code.startswith('0') else 0

# Core metric computation chain
base_threshold = len([c for c in diag_id if c.isdigit()])  # extracts 001 -> 3 digits

metric_data = process_metrics([x + 0.1 for x in filtered_stream])  # Feed real data

# Conditional expression with misleading branches
adjustment_factor = 1.5 if sum(masked_values) % 2 == 0 else 0.8  # Depends on dead code

# Critical branching logic with nested conditions
if len(metric_data) > 5 and base_threshold == 3:
    temp_result = sum(math.sin(x) for x in metric_data[:4])
    if temp_result < 0:
        final_score = int(abs(temp_result) * 1000)
    else:
        interim = max(metric_data) * adjustment_factor  # Uses decoy factor
        final_score = int(interim ** 2)  # Key assignment point
else:
    final_score = -1  # Dead branch (not taken)

# Additional irrelevant output
print(f'Diagnostic: {trend_coeff=}, {entropy_value=}, {build_number=}')
print(f'Metrics shape: {len(metric_data)}')

# Target result output
Result: {final_score}