from dataclasses import dataclass
from math import sqrt
from itertools import combinations
from statistics import mean, variance

def normalize_readings(readings):
    if not readings:
        return []
    avg = mean(readings)
    var = variance(readings)
    if var == 0:
        return [0.0] * len(readings)
    std_dev = sqrt(var)
    return [(x - avg) / std_dev for x in readings]

def compute_combinatorial_features(normalized_data):
    features = []
    for combo in combinations(normalized_data, 2):
        product = combo[0] * combo[1]
        features.append(product if product > 0 else 0)
    return features

def calculate_efficiency(filtered_features, threshold=0.5):
    if not filtered_features:
        return 0.0
    positive_count = sum(1 for f in filtered_features if f > threshold)
    return positive_count / len(filtered_features) if len(filtered_features) > 0 else 0

@dataclass
class SensorData:
    sensor_id: str
    raw_readings: list
    processed_features: list = None
    efficiency_score: float = 0.0

# Simulated sensor data
sensor_a_readings = [12.4, 15.6, 13.8, 14.2, 16.0, 11.9, 13.3]
sensor_b_readings = [22.1, 24.5, 23.7, 25.0, 21.8, 24.2, 23.3]

# Process first sensor
normalized_a = normalize_readings(sensor_a_readings)
features_a = compute_combinatorial_features(normalized_a)
filtered_a = [f for f in features_a if f <= max(features_a) * 0.9]
efficiency_a = calculate_efficiency(filtered_a)

# Process second sensor with short-circuit logic
normalized_b = normalize_readings(sensor_b_readings)
features_b = compute_combinatorial_features(normalized_b)
# Conditional assignment using short-circuit
temp_check = len(features_b) > 5 and max(features_b) > 1.0
filtered_b = [f for f in features_b if temp_check and f >= min(features_b) * 0.5] if temp_check else []
efficiency_b = calculate_efficiency(filtered_b, 0.3) if temp_check else 0.0

# Final calculation combining both sensors
combined_efficiencies = [efficiency_a, efficiency_b]
valid_efficiencies = [e for e in combined_efficiencies if e > 0.0]

final_efficiency_score = (
    mean(valid_efficiencies) * 100 
    if valid_efficiencies and len(valid_efficiencies) == 2 
    else sum(valid_efficiencies) * 50
)

print(f"Result: {final_efficiency_score}")