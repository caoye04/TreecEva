from itertools import combinations

# Simulate sensor data with noise and valid readings
def preprocess_sensor_readings(raw_readings):
    cleaned = []
    noise_floor = 5
    for val in raw_readings:
        if val > noise_floor:
            cleaned.append(val - noise_floor)
    return [x for x in cleaned if x % 2 == 1]  # Keep only odd values

# Analyze patterns in sequences
def detect_anomalies(data):
    anomaly_count = 0
    for a, b in combinations(data, 2):
        if (a + b) % 7 == 0:
            anomaly_count += 1
    return anomaly_count

# Misleading function - looks relevant but unused in final path
def legacy_calculate_average(arr):
    total = 0
    count = 0
    for num in arr:
        if num < 0:
            continue
        total += num
        count += 1
    return total / count if count > 0 else 0

# Core logic for score computation
def calculate_final_score(data_list):
    base = 0
    for num in data_list:
        base += num * num  # Sum of squares
    adjustment = detect_anomalies(data_list)
    return base - adjustment  # Final adjustment based on combinatorial anomalies

# Main execution flow
raw_sensor_data = [12, 15, 3, 20, 8, 11, 14, 19]
processed_data = preprocess_sensor_readings(raw_sensor_data)

# Dead code - variables not used later
redundant_stats = {
    'max_val': max(processed_data),
    'min_val': min(processed_data),
    'range': max(processed_data) - min(processed_data)
}
intermediate_sum = sum([x**2 for x in processed_data if x < 10])

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")