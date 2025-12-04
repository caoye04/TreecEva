# Analysis of weather temperature anomalies

temperature_readings = [-2.5, 1.8, 0.5, 3.2, -1.7, 4.6, -0.3, 2.9, -1.5, 5.1]
baseline = 0.8
threshold = 1.5

# Preprocessing data
processed_readings = [round(temp - baseline, 1) for temp in temperature_readings]
max_temp = max(processed_readings)
min_temp = min(processed_readings)

# Some additional calculations that aren't directly relevant
temperature_range = max_temp - min_temp
average_deviation = sum(abs(temp) for temp in processed_readings) / len(processed_readings)

# Filter data points based on specific criteria
filtered_data = []
for i, temp in enumerate(processed_readings):
    # We're interested in readings that exceed the threshold (positive or negative)
    if abs(temp) > threshold:
        # Apply a weighting based on position in the sequence
        position_weight = (i + 1) / len(processed_readings)
        # Calculate weighted value
        weighted_value = temp * position_weight
        filtered_data.append(weighted_value)
    elif i % 3 == 0:  # Every third reading gets special handling
        # These values don't meet our primary criteria but we track them separately
        special_case = temp * 0.5

# Extract a slice of the filtered data for analysis
analysis_segment = filtered_data[1:] if len(filtered_data) > 1 else filtered_data

# Calculate the sum of filtered values
filtered_data_sum = sum(filtered_data)

# Generate a summary report
print(f"Temperature anomaly analysis:")
print(f"Range: {temperature_range}")
print(f"Average deviation: {average_deviation:.2f}")
print(f"Result: {filtered_data_sum}")