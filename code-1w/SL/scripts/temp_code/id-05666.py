from collections import defaultdict

# Simulate physiological monitoring data over time
time_series_data = [
    {'stress_level': 80, 'heart_rate_variability': 45},
    {'stress_level': 60, 'heart_rate_variability': 55},
    {'stress_level': 90, 'heart_rate_variability': 40}
]

# Irrelevant accumulator for minor distraction (intervention level 5)
data_summary = defaultdict(int)
for entry in time_series_data:
    data_summary['total_entries'] += 1

# Primary computation: assess autonomic nervous system state
baseline_correction = 5
stress_level = time_series_data[2]['stress_level']
hrv_list = [entry['heart_rate_variability'] for entry in time_series_data]
heart_rate_variability = sum(hrv_list) / len(hrv_list)

# Key logical operation combining arithmetic and boolean logic
calibration_offset = 2.5
adjusted_hrv = heart_rate_variability - calibration_offset

# Critical statement: dual-condition physiological threshold detection
drowsiness_index = stress_level * 0.3 + adjusted_hrv * 0.7
temperature_reading = 36.8  # Irrelevant sensor reading (minor distractor)
threshold_flag = stress_level > 75 and heart_rate_variability < 50

# Output required result
print(f"Result: {threshold_flag}")