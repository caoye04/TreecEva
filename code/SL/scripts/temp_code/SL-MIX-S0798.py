from collections import Counter

def calculate_sensor_baseline(readings):
    # Misleading baseline calculation (distractor)
    temp_sum = sum(readings) * 2.5
    adjusted_sum = temp_sum - len(readings) * 10
    return adjusted_sum / 3.0

def filter_anomalies(data_points):
    # Dead code path - never called
    threshold = 150
    filtered = [x for x in data_points if x < threshold]
    return sum(filtered) * 0.75

def process_sensor_data(sensor_readings):
    # Relevant processing logic
    reading_counts = Counter(sensor_readings)
    
    # Distractor variables
    dummy_calc = (reading_counts.most_common(1)[0][0] * 7) % 13
    redundant_value = dummy_calc + 25
    
    # Key logic chain
    unique_readings = len(reading_counts)
    total_readings = len(sensor_readings)
    mode_frequency = reading_counts.most_common(1)[0][1]
    
    # Complex calculation with multiple steps
    base_value = (unique_readings * 15) + (mode_frequency * 8)
    adjustment = (total_readings % 7) * 3
    intermediate = base_value - adjustment
    
    # Final transformation
    final_result = (intermediate // 2) + (intermediate % 4)
    
    # More distractors
    unused_var = final_result * 2 + redundant_value
    misleading_temp = unused_var - dummy_calc
    
    return final_result

# Main execution
sensor_readings = [45, 67, 45, 89, 67, 23, 45, 67, 89, 45, 12, 67, 45]

# Irrelevant calculations
baseline_dummy = calculate_sensor_baseline(sensor_readings)
threshold_check = baseline_dummy > 100

# Core execution
final_output = process_sensor_data(sensor_readings)

# Print result
print(f"Result: {final_output}")