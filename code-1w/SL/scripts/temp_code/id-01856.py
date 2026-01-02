from itertools import combinations

# Simulate sensor data with noise and valid readings
def preprocess_sensor_readings(raw_readings):
    cleaned = [x for x in raw_readings if x >= 0]
    sorted_readings = sorted(cleaned, reverse=True)
    top_five = sorted_readings[:5]
    
    # Distractor: calculate average but not used later
    avg = sum(top_five) / len(top_five) if top_five else 0
    adjusted = [x * 0.9 for x in top_five]
    
    return adjusted

# Analyze patterns in adjusted sensor values
def detect_anomalies(data):
    pairs = list(combinations(data, 2))
    anomaly_count = 0
    for a, b in pairs:
        if abs(a - b) > 15:
            anomaly_count += 1
    # Irrelevant computation
    squared_sums = [a**2 + b**2 for a, b in pairs]
    total_ss = sum(squared_sums)
    return anomaly_count  # Only count matters

# Core scoring logic
def compute_final_score(data):
    base = sum(data)
    penalty = detect_anomalies(data) * 2
    bonus = 5 if len(data) >= 4 else 0
    intermediate_result = base - penalty + bonus
    
    # Extra distraction: unused transformation
    transformed = [round(x ** 0.5, 2) for x in data]
    temp_sum = sum(transformed)
    
    scaling_factor = 1.1 if temp_sum > 10 else 1.0  # Not actually applied
    
    return int(base - penalty + bonus)  # Final score uses simplified version

# Main execution flow
raw_sensor_data = [23, -5, 34, 12, 45, 8, 45, -1, 34]
processed_data = preprocess_sensor_readings(raw_sensor_data)

# Additional red herring variables
buffer_cache = {i: processed_data.count(i) for i in set(processed_data)}
data_stats = {
    'max': max(processed_data),
    'min': min(processed_data),
    'range': max(processed_data) - min(processed_data)
}

# Secondary irrelevant calculation chain
redundant_calc = 0
for val in processed_data:
    if val > 20:
        redundant_calc += val // 3

# Key statement
final_score = compute_final_score(processed_data)

# Print result as required
print(f"Result: {final_score}")