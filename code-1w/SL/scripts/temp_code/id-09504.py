from collections import defaultdict

# Simulate agricultural yield analysis with noise filtering and efficiency computation
def analyze_crop_health(sensor_readings):
    health_scores = []
    noise_counter = 0
    for reading in sensor_readings:
        if reading < 0 or reading > 100:
            noise_counter += 1
            continue
        if reading >= 80:
            health_scores.append(5)
        elif reading >= 60:
            health_scores.append(4)
        elif reading >= 40:
            health_scores.append(3)
        elif reading >= 20:
            health_scores.append(2)
        else:
            health_scores.append(1)
    return health_scores, noise_counter

def compute_stability_index(health_list):
    if len(health_list) == 0:
        return 0.0
    changes = 0
    for i in range(1, len(health_list)):
        if health_list[i] != health_list[i-1]:
            changes += 1
    return round(1 - (changes / (len(health_list) - 1)) if len(health_list) > 1 else 1, 4)

def calculate_harvest_efficiency(data, min_threshold):
    raw_values = [d["moisture"] * d["sunlight"] + d.get("bonus", 0) for d in data]
    filtered_values = [v for v in raw_values if v >= min_threshold]
    
    # Irrelevant intermediate calculation (distractor)
    avg_raw = sum(raw_values) / len(raw_values) if raw_values else 0
    high_performers = [v for v in filtered_values if v > avg_raw]
    
    # Key logic path
    health_ratings, dropped = analyze_crop_health(filtered_values)
    stability = compute_stability_index(health_ratings)
    base_efficiency = sum(filtered_values) / 10.0 if filtered_values else 0
    
    # Conditional adjustment based on stability
    adjustment_factor = 1.2 if stability > 0.7 else (0.8 if stability < 0.4 else 1.0)
    
    # Dead code branch (distractor)
    if len(filtered_values) > 100:
        outlier_count = 0
        for v in filtered_values:
            if v < 10:
                outlier_count += 1

    final_efficiency = base_efficiency * adjustment_factor
    
    # Additional irrelevant aggregation
    stats = defaultdict(int)
    for r in health_ratings:
        stats[r] += 1
    
    # Final result
    final_yield = int(final_efficiency + stats[5] - stats[1])
    return final_yield

# Input data setup
field_data = [
    {"moisture": 7, "sunlight": 12, "bonus": 3},
    {"moisture": 6, "sunlight": 14},
    {"moisture": 8, "sunlight": 11, "bonus": 5},
    {"moisture": 5, "sunlight": 13},
    {"moisture": 9, "sunlight": 10, "bonus": 2},
    {"moisture": 4, "sunlight": 15},
    {"moisture": 10, "sunlight": 9, "bonus": 4}
]

threshold = 70
final_yield = calculate_harvest_efficiency(field_data, threshold)
print(f"Result: {final_yield}")