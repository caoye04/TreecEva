# Temperature analysis for environmental monitoring
base_temps = {85, 92, 78, 96, 89, 91}
threshold_temp = 90

# Filter temperatures above threshold using set comprehension
high_temps = {temp for temp in base_temps if temp > threshold_temp}

# Calculate average high temperature
if high_temps:
    avg_high = sum(high_temps) // len(high_temps)
else:
    avg_high = 0

# Additional monitoring data (contextual information)
monitoring_stations = 5
sensor_readings = [87, 93, 95, 88, 96]

# Final calculation using dictionary operations
temp_data = {'avg_high': avg_high, 'count_high': len(high_temps)}
result_calculation = temp_data['avg_high'] * temp_data['count_high']
final_result = result_calculation

print(f"Target result: {final_result}")