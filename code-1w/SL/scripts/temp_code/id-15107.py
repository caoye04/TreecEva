from itertools import compress

# Simulate sensor readings and reliability weights
sensor_readings = [68, 72, 74, 80, 65]
reliability = [True, True, False, True, False]
weights = [0.9, 1.0, 0.8, 1.1, 0.7]

# Apply weighting only to reliable sensors
calibrated_readings = list(compress(sensor_readings, reliability))
weight_mask = list(compress(weights, reliability))

# Compute weighted scores using list comprehension
weighted_scores = [calibrated_readings[i] * weight_mask[i] for i in range(len(calibrated_readings))]

# Determine if any sensor exceeds critical threshold after calibration
dummy_var = sum(1 for x in weighted_scores if x < 0)  # Irrelevant computation (minimal distraction)
threshold_flag = any(weighted_scores[i] > 75 for i in range(len(weighted_scores)))

Result: threshold_flag