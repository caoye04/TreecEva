def analyze_readings(sensor_readings):
    filtered = [x for x in sensor_readings if x > 20 and x < 80]
    normalized = [(x - 20) / 60 for x in filtered]
    return normalized

sensor_data = [15, 25, 30, 45, 55, 60, 75, 85, 90]

# Misleading transformation (not used in final path)
transformed_data = [x * 1.5 + 10 for x in sensor_data]
dropped_count = len(sensor_data) - len([x for x in transformed_data if 30 < x < 100])

# Actual processing path
processed_data = analyze_readings(sensor_data)

# Auxiliary computation with side distraction
averages = []
for i, val in enumerate(processed_data):
    rolling_avg = sum(processed_data[:i+1]) / (i+1)
    averages.append(rolling_avg)

# Red herring: unused helper function
def compute_entropy(data):
    from math import log
    total = 0
    for x in data:
        if x > 0:
            total -= x * log(x)
    return total

# State tracking with irrelevant metric
change_points = 0
for i in range(1, len(processed_data)):
    if abs(processed_data[i] - processed_data[i-1]) > 0.2:
        change_points += 1

# Main scoring logic
scaling_factor = 100
offset = 10

adjusted_values = [val * scaling_factor for val in processed_data]

# Final aggregation
base_score = sum(adjusted_values)
penalty = len(sensor_data) * 2

# Secondary red herring: unused tuple unpacking
stats_summary = (len(processed_data), base_score, penalty)
item_count, _, _ = stats_summary

# Final score calculation
final_score = base_score - penalty + offset
Result: {final_score}