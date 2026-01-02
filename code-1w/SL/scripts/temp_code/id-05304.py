from collections import defaultdict

# Simulate sensor data processing with noise filtering and thresholding
def preprocess_data(raw_values):
    filtered = [x for x in raw_values if x > 0]  # Remove non-positive values
    smoothed = []
    for i in range(1, len(filtered) - 1):
        avg = (filtered[i-1] + filtered[i] + filtered[i+1]) / 3
        smoothed.append(int(avg))
    return smoothed

# Analyze trend direction based on moving differences
def detect_trend(values):
    if len(values) < 3:
        return 0
    trend_sum = 0
    for i in range(1, len(values)):
        diff = values[i] - values[i-1]
        trend_sum += (1 if diff > 0 else -1 if diff < 0 else 0)
    return 1 if trend_sum >= 0 else -1

# Main scoring logic with multiple validation layers
def calculate_final_score(sensor_data, limits):
    # Irrelevant preprocessing: normalize to percentage (not used in final logic)
    max_val = max(sensor_data)
    percentages = [round(x / max_val * 100, 2) for x in sensor_data]  # Distractor

    # Relevant computation: count how many exceed dynamic thresholds
    threshold_map = defaultdict(int)
    for limit in limits:
        threshold_map[limit] = sum(1 for x in sensor_data if x > limit)

    base_count = threshold_map[limits[0]]
    bonus_factor = 2 if detect_trend(sensor_data) == 1 else 1

    # Additional distractor: simulate calibration offset (unused)
    calibration_shift = sum([i * 0.1 for i, x in enumerate(sensor_data) if i % 3 == 0])  # Dead computation
    adjustment_magnitude = len([x for x in sensor_data if x % 2 == 0])  # Semi-relevant?

    # Core scoring formula
    raw_score = base_count * bonus_factor
    penalty = 0
    if adjustment_magnitude > 3:
        penalty = 5
    
    # Final adjustment based on sorted position median
    sorted_data = sorted(sensor_data)
    median_index = len(sorted_data) // 2
    median_value = sorted_data[median_index]
    if median_value > 50:
        raw_score += 3

    final_score = raw_score - penalty

    # Red herring: unused state tracking
    log_entry = {
        'size': len(sensor_data),
        'peak': max_val,
        'calibration': round(calibration_shift, 2)
    }

    return final_score

# Input data
sensor_readings = [12, 45, 67, -5, 89, 23, 77, 56, 90, 11, 67]
threshold_levels = [50, 75, 25]

# Execute main logic
processed = preprocess_data(sensor_readings)
final_score = calculate_final_score(processed, threshold_levels)
print(f"Result: {final_score}")