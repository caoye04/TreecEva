import math

# Sensor simulation and analysis system
def generate_synthetic_readings():
    readings = []
    for i in range(20):
        val = (i * i) + 5 * i + 4
        if i % 3 == 0:
            val += 10
        elif i % 5 == 0:
            val -= 3
        readings.append(val)
    return readings

# Irrelevant transformation - red herring
def transform_signal(data):
    return [x * 1.5 + 2 for x in data if x % 2 == 0]

# Decoy processing function with misleading intermediate result
def compute_entropy(data):
    total = 0
    for x in data:
        if x > 0:
            total += x * math.log(abs(x))
    return round(total / len(data), 3) if data else 0

# Unused but plausible helper function (dead code path)
def normalize_range(data, low=0, high=100):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [low] * len(data)
    return [low + (x - min_val) * (high - low) / (max_val - min_val) for x in data]

# Real processing chain begins here
def filter_outliers(data, factor=1.5):
    q1 = sorted(data)[len(data)//4]
    q3 = sorted(data)[3*len(data)//4]
    iqr = q3 - q1
    lower_bound = q1 - factor * iqr
    upper_bound = q3 + factor * iqr
    return [x for x in data if lower_bound <= x <= upper_bound]

# Characteristic pattern counting - relevant but subtle
def count_transition_patterns(seq):
    up = down = stable = 0
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            up += 1
        elif seq[i] < seq[i-1]:
            down += 1
        else:
            stable += 1
    return {'up': up, 'down': down, 'stable': stable}

# Lambda-based dynamic thresholding - key concept
threshold_func = lambda x: 2 * x + 10 if x < 50 else 1.8 * x + 12

# Conditional expression based classification
classify_reading = lambda x: 'LOW' if x < 40 else ('HIGH' if x > 80 else 'NORMAL')

# Core processing pipeline
raw_data = generate_synthetic_readings()
decoy_entropy = compute_entropy(raw_data)  # Distraction
filtered_data = filter_outliers(raw_data, factor=2.0)
sorted_data = sorted(filtered_data)

# Tuple unpacking with distractor variables
median_idx = len(sorted_data) // 2
median_value = (sorted_data[median_idx] + sorted_data[~median_idx]) / 2

# Dictionary operations for state tracking
status_log = {
    'init_count': len(raw_data),
    'after_filter': len(filtered_data),
    'median': median_value,
    'mode': 'DIAGNOSTIC'
}

# Destructuring assignment - irrelevant to final answer
up_stats, down_stats, stable_stats = (
    len([x for x in raw_data if x % 3 == 0]),
    len([x for x in raw_data if x % 4 == 0]),
    len([x for x in raw_data if x % 5 == 0])
)

# Transform but do not use (distractor)
unused_enhanced = transform_signal(filtered_data)

# Actual processing that leads to answer
pattern_analysis = count_transition_patterns(filtered_data)
transition_score = pattern_analysis['up'] * 2 - pattern_analysis['down']

# Simulated calibration offset (irrelevant)
calibration_matrix = [[i + j for j in range(3)] for i in range(3)]
offset_correction = sum(calibration_matrix[i][i] for i in range(3))

# Main data transformation
processed_data = []
for val in filtered_data:
    adjusted = val + 5  # baseline adjustment
    if val > 60:
        adjusted += 2
    processed_data.append(adjusted)

# Final diagnostic computation depends only on transition_score and processed_data length
# All above complexity contains distractions
final_diagnostic = 0
for x in processed_data:
    if classify_reading(x) == 'HIGH':
        final_diagnostic += int(threshold_func(x) // 10)
final_diagnostic += transition_score * 3

Result: {final_diagnostic}