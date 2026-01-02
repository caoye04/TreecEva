from itertools import combinations
from collections import defaultdict

# Simulate sensor readings with noise filtering and scoring
def preprocess_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 90]
    baseline = sum(filtered) / len(filtered) if filtered else 0
    
    # Irrelevant intermediate: analyze outlier patterns (not used later)
    outliers = [x for x in raw_readings if abs(x - baseline) > 20]
    outlier_pairs = list(combinations(outliers, 2))  # Dead code path
    
    normalized = [(x - baseline) / baseline for x in filtered]
    return normalized

# Weighted scoring logic
def calculate_confidence(values):
    if not values:
        return 0.5
    variance = sum((v - sum(values)/len(values))**2 for v in values) / len(values)
    return max(0.1, min(1.0, 1 - variance))

# Core evaluation function
def calculate_final_score(results, weights):
    weighted_sum = 0.0
    total_weight = 0.0
    
    # Distractor: track unused category stats
    category_stats = defaultdict(lambda: {'count': 0, 'sum': 0})
    
    for i, (category, result_list) in enumerate(results.items()):
        category_stats[category]['count'] += len(result_list)
        category_stats[category]['sum'] += sum(result_list)
        
        avg_result = sum(result_list) / len(result_list) if result_list else 0
        weight = weights.get(category, 0.1)
        
        # Additional irrelevant transformation
        transformed = [r ** 0.5 for r in result_list if r > 0]
        mean_transformed = sum(transformed) / len(transformed) if transformed else 0
        
        contribution = avg_result * weight * calculate_confidence(result_list)
        weighted_sum += contribution
        total_weight += weight
    
    # Misleading normalization with unused variables
    max_possible = sum(weights.values())
    safety_margin = 0.95
    
    if total_weight == 0:
        return 0
    return int(weighted_sum / total_weight * 100)  # Final score as integer percentage

# Main execution
if __name__ == "__main__":
    raw_sensor_data = {
        'temperature': [85, 76, 92, 67, 70],
        'pressure': [45, 50, 48, 105, 42],
        'humidity': [60, 68, 72, 58, 63],
        'light': [30, 35, 200, 40]  # Contains outlier
    }
    
    processed_results = {}
    for sensor, data in raw_sensor_data.items():
        cleaned = preprocess_readings(data)
        processed_results[sensor] = [abs(c) * 10 + 5 for c in cleaned]  # Scale up for scoring
    
    # Weight configuration (some weights are misleadingly defined but not all used)
    importance_weights = {
        'temperature': 0.3,
        'pressure': 0.25,
        'humidity': 0.35,
        'light': 0.1,
        'motion': 0.05  # Unused sensor
    }
    
    # Red herring computation: simulate calibration drift
    drift_factor = 0
    for i in range(3):
        for j in range(4):
            drift_factor += (i * j) % 3  # Irrelevant accumulation
    
    final_score = calculate_final_score(processed_results, importance_weights)
    
    # Critical output
    print(f"Result: {final_score}")