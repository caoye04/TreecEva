import math

temperature_readings = [23.5, 24.1, 22.8, 31.2, 24.0, 23.9, 24.2, 50.1]
valid_range = (frozenset(range(20, 30)), frozenset(range(30, 40)))
sensor_weights = {0: 1.2, 1: 1.0, 2: 1.1, 3: 0.9, 4: 1.0, 5: 1.0, 6: 1.0, 7: 0.8}

# Stage 1: Filter out obviously invalid readings
filtered_readings = [temp for temp in temperature_readings if any(int(temp) in r for r in valid_range)]

# Stage 2: Calculate weighted mean of filtered readings
weighted_sum = sum(temp * sensor_weights[i] for i, temp in enumerate(temperature_readings) if temp in filtered_readings)
weight_total = sum(sensor_weights[i] for i, temp in enumerate(temperature_readings) if temp in filtered_readings)
mean_temp = weighted_sum / weight_total if weight_total != 0 else 0

# Stage 3: Identify outliers using modified z-score with lambda
median_temp = sorted(filtered_readings)[len(filtered_readings)//2]
mad = lambda data, med: sorted([abs(x - med) for x in data])[len(data)//2]
deviations = [abs(temp - median_temp) for temp in filtered_readings]
scale_factor = 1.4826  # For normally distributed data
modified_z_scores = [(0.6745 * (temp - median_temp)) / (scale_factor * mad(filtered_readings, median_temp)) for temp in filtered_readings]

# Stage 4: Apply boolean logic to determine anomalies
is_anomaly = [abs(z) > 2.0 and temp > mean_temp + 3.0 for z, temp in zip(modified_z_scores, filtered_readings)]
anomaly_indices = [i for i, anomaly in enumerate(is_anomaly) if anomaly]

# Stage 5: Compute final anomaly score
anomaly_temps = [filtered_readings[i] for i in anomaly_indices]
anomaly_weights = [sensor_weights[i] for i in anomaly_indices]
final_anomaly_score = round(sum(temp * weight for temp, weight in zip(anomaly_temps, anomaly_weights)) / len(anomaly_temps) if anomaly_temps else 0, 2)

print(f"Result: {final_anomaly_score}")