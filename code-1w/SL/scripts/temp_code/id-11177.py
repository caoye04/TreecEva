from collections import defaultdict
import math

def analyze_readings(sensor_data):
    temp_stats = defaultdict(float)
    total_samples = 0
    valid_count = 0

    for idx, reading in enumerate(sensor_data):
        if reading < 0:
            continue
        temp_stats['sum'] += reading
        temp_stats['squared_sum'] += reading ** 2
        valid_count += 1
        total_samples += 1

    if valid_count == 0:
        return {'mean': 0, 'stdev': 0}

    mean_val = temp_stats['sum'] / valid_count
    variance = (temp_stats['squared_sum'] / valid_count) - (mean_val ** 2)
    stdev_val = math.sqrt(max(variance, 0))

    return {'mean': mean_val, 'stdev': stdev_val}

def preprocess_data(raw_input):
    cleaned = []
    outlier_threshold = 30
    temp_buffer = []

    for val in raw_input:
        if val > outlier_threshold:
            temp_buffer.append(val * 0.1)
        else:
            cleaned.append(val)

    adjustment_factor = sum(temp_buffer) if temp_buffer else 0.0
    adjusted_cleaned = [x + adjustment_factor * 0.01 for x in cleaned]

    return adjusted_cleaned

def calculate_final_score(data_chunk):
    score = 0
    penalty = 0
    bonus_tracker = []

    summary = defaultdict(int)
    for i, item in enumerate(data_chunk):
        if i % 2 == 0:
            score += int(math.log1p(item) * 10)
            summary['even_contrib'] += 1
        else:
            base_penalty = item // 10
            penalty += base_penalty
            summary['odd_penalties'] += base_penalty

        # Dummy tracking for distraction
        transform = lambda x: (x ** 0.5) * 2
        bonus_tracker.append(transform(item))

    net_score = score - penalty + len(bonus_tracker) // 5
    return int(net_score)

# Simulated sensor readings
raw_sensor_readings = [12, 45, 8, 3, 99, 7, 22, 15, 60, 4]

# Step 1: Preprocess the raw data
temp_offset = sum(x for x in raw_sensor_readings if x > 50) * 0.05
processed_data = preprocess_data(raw_sensor_readings)

# Add dummy transformation (irrelevant to final result)
dummy_matrix = [[i * j for j in range(3)] for i in range(len(processed_data))]
matrix_trace = sum(dummy_matrix[i][i] for i in range(min(len(dummy_matrix), 3))) if dummy_matrix else 0

# Step 2: Analyze statistics (semi-relevant, but not used directly)
stats = analyze_readings(processed_data)

# Step 3: Calculate final score
calibration_constant = 1.0
final_score = calculate_final_score(processed_data)

# Misleading computation (dead path)
if matrix_trace > 100:
    final_score *= 2

# Output result
print(f"Result: {final_score}")