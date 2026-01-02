from collections import defaultdict

# Simulated sensor data with noise and redundant readings
data_stream = [
    (1, 'temp', 23.5), (2, 'temp', 24.1), (3, 'hum', 45),
    (4, 'temp', 23.9), (5, 'hum', 47), (6, 'temp', 24.3),
    (7, 'hum', 44), (8, 'temp', 23.7), (9, 'hum', 46)
]

# Misleading auxiliary data that looks relevant but isn't used in final calculation
auxiliary_metrics = {
    'calibration_offset': 0.15,
    'sensor_drift': 0.08,
    'redundancy_factor': 2,
    'baseline_stability': 98.6
}

# Aggregation using defaultdict for cleaner grouping
grouped_data = defaultdict(list)
for sid, stype, value in data_stream:
    grouped_data[stype].append(value)

# Process temperature readings: apply smoothing filter (moving average of window 2)
temp_readings = grouped_data['temp']
smoothed_temps = []
for i in range(len(temp_readings)):
    if i == 0:
        smoothed_temps.append(temp_readings[i])
    else:
        smoothed_temps.append((temp_readings[i-1] + temp_readings[i]) / 2)

# Compute rolling variance as a distraction (not used later)
variance_distractor = 0
if len(smoothed_temps) > 1:
    mean_temp = sum(smoothed_temps) / len(smoothed_temps)
    variance_distractor = sum((t - mean_temp) ** 2 for t in smoothed_temps) / len(smoothed_temps)

# Correct processing path: use only last three smoothed temperature values
relevant_temps = smoothed_temps[-3:]

# Simulate environmental stress factor (unused red herring)
stress_flags = []
for t in relevant_temps:
    if t > 24.0:
        stress_flags.append(True)
    else:
        stress_flags.append(False)

# Actual score computation logic
def calculate_stability_index(values):
    if not values:
        return 0
    return round(max(values) - min(values), 3)

def calculate_final_score(data):
    # Only this function matters for the answer
    stability = calculate_stability_index(data)
    base_score = 100
    penalty = int(stability * 10)
    final = base_score - penalty
    
    # Dead code branch: never executed due to data constraints
    if len(data) < 2:
        adjustment = auxiliary_metrics['baseline_stability']
        final += adjustment
    
    return final

# Key statement
processed_data = relevant_temps
final_score = calculate_final_score(processed_data)

# Output result
print(f"Result: {final_score}")