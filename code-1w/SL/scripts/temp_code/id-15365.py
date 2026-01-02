def analyze_system_metrics(data_points):
    cumulative_score = 0
    for point in data_points:
        if point > 50:
            cumulative_score += point * 0.1
    return cumulative_score

# Simulate sensor readings over time
data_stream = [45, 67, 89, 23, 78, 91, 34]
raw_total = sum(data_stream)
anomaly_threshold = 30

# Identify anomalous readings
anomalies = {x for x in data_stream if x < anomaly_threshold}
corrected_data = [x for x in data_stream if x >= anomaly_threshold]

# Calculate base efficiency using corrected data
base_efficiency = sum(corrected_data) / len(corrected_data)

# Track historical peaks
peak_readings = []
for val in data_stream:
    if val > 85:
        peak_readings.append(val)

# Efficiency set used in final calculation
efficiency_set = {int(base_efficiency), len(peak_readings), len(anomalies)}

# Irrelevant signal processing block (distractor)
signal_power = 0
for i in range(len(data_stream)):
    if i % 2 == 0:
        signal_power += data_stream[i] ** 0.5

# Degradation model with fixed parameters
degradation_factor = 1.75
temp_bias = 0.05 * len(anomalies)  # Minor adjustment not affecting final logic

# Core capacity computation function
def calculate_remaining_capacity(efficiencies, factor):
    initial = max(efficiencies)
    adjustment = min(efficiencies) * factor
    dropoff = len(efficiencies) ** 1.5
    result = initial - adjustment - dropoff
    return int(result)

# Execute main calculation
final_capacity = calculate_remaining_capacity(efficiency_set, degradation_factor)

# Print result as required
print(f"Result: {final_capacity}")