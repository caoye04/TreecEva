from itertools import combinations
import math

# Simulate sensor array readings with noise filtering
def analyze_sensor_readings(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    sorted_readings = sorted(filtered, reverse=True)
    top_quartile = sorted_readings[:len(sorted_readings)//4]
    avg_top = sum(top_quartile) / len(top_quartile) if top_quartile else 0
    
    # Misleading intermediate: entropy-like calculation (not used later)
    entropy_proxy = 0.0
    for val in filtered:
        p = val / sum(filtered) if sum(filtered) != 0 else 0
        if p > 0:
            entropy_proxy -= p * math.log(p)
    
    return avg_top, entropy_proxy

# Weight normalization and scoring
def normalize_and_weight(values, weights):
    total_weight = sum(weights)
    normalized = [w / total_weight for w in weights]
    
    # Apply weights to values
    weighted_sum = sum(v * nw for v, nw in zip(values, normalized))
    
    # Distractor: generate unused combinations
    combo_products = []
    for combo in combinations(normalized, 2):
        combo_products.append(combo[0] * combo[1])
    
    return weighted_sum, normalized

# Threshold logic based on system health
def calculate_threshold(weights):
    base = sum(w ** 2 for w in weights)
    adjustment = math.sin(len(weights)) * 0.1
    return int(base * 100 + adjustment)  # deterministic integer output

# Main execution
if __name__ == "__main__":
    # Sensor data from 8 zones
    raw_data = [15, 88, 92, 5, 67, 95, 103, 44, 76, 81, -5, 90]
    avg_top_sensors, _ = analyze_sensor_readings(raw_data)
    
    # System component priorities (misaligned length on purpose)
    components = ['power', 'thermal', 'network', 'storage']
    priorities = [0.4, 0.3, 0.2, 0.1]
    
    # Normalize and compute composite metric
    composite_score, normalized_weights = normalize_and_weight(
        [avg_top_sensors, 85, 70, 90], 
        priorities
    )
    
    # Irrelevant slicing operation (distraction)
    window_slice = normalized_weights[1:3]
    temp_avg = sum(window_slice) / len(window_slice)
    
    # Key computation point
    threshold_score = calculate_threshold(normalized_weights)
    
    # Unused conditional branch (dead code path)
    if temp_avg > 0.5:
        threshold_score *= 2
    
    # Final result output
    print(f"Result: {threshold_score}")