import math

# Simulate sensor data with noise and calibration offsets
data_stream = [104, 98, 112, 95, 108, 115, 93, 107]
noise_floor = 5
baseline_offset = 90

# Irrelevant statistical placeholders (distractors)
mean_deviation = 0
max_fluctuation = 0
running_variance = 0

# Calibration map for sensor segments (dictionary operation)
sensor_calibration = {
    'segment_A': 1.05,
    'segment_B': 0.98,
    'segment_C': 1.02,
    'segment_D': 1.01
}

calibration_factor = sensor_calibration['segment_A'] * sensor_calibration['segment_C']

# Apply baseline correction and noise filtering
corrected_readings = []
for raw_value in data_stream:
    corrected = (raw_value - baseline_offset) * calibration_factor
    if corrected > noise_floor:
        corrected_readings.append(corrected)

# Compute moving average over window of 2 (semi-relevant processing)
moving_averages = []
for i in range(len(corrected_readings) - 1):
    avg = (corrected_readings[i] + corrected_readings[i + 1]) / 2
    moving_averages.append(avg)

# Secondary transformation with dead code branch (distractor)
transformed_values = []
scaling_curve = []
for x in moving_averages:
    transformed = math.log(x) ** 2
    transformed_values.append(transformed)
    
    # Dead code path: never accessed due to loop logic
    if x < 0:
        scaling_curve.append(0)

# Auxiliary computation that looks important but isn't used
aggregate_magnitude = sum([math.sqrt(v) for v in corrected_readings[:3]])

# Prepare data structure for final processing
processed_data = {
    'readings': transformed_values,
    'count': len(transformed_values),
    'aux_data': {'magnitude': aggregate_magnitude, 'calibration': calibration_factor}
}

# Simulate scoring model
threshold_reference = 6.5
penalty_rate = 0.15
base_score = 100

# Function uses dictionary lookup and conditional weighting
def calculate_final_score(data):
    score = base_score
    readings = data['readings']
    
    # Loop with nested conditionals (2-3 level nesting)
    for i, val in enumerate(readings):
        if val > threshold_reference:
            bonus = (val - threshold_reference) * 1.2
            score += bonus
        else:
            # Apply increasing penalty based on index
            if i % 3 == 0:
                score -= penalty_rate * (threshold_reference - val)
    
    # Red herring adjustment (never triggered in this data)
    if data['count'] > 20:
        score *= 0.95
    
    return score

# Critical execution point
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")