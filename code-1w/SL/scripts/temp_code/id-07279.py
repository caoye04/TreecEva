from collections import defaultdict
from itertools import combinations

# Simulate sensor data with some noise and redundancy
def generate_sensor_readings():
    raw_readings = [15, 22, 18, 24, 30, 12, 25, 20]
    filtered = [x for x in raw_readings if x > 14]
    adjusted = [x * 0.9 for x in filtered]
    return adjusted

# Process data through multiple stages with intermediate diagnostics
def process_diagnostics(data):
    stats = defaultdict(int)
    temp_sum = 0
    count_above_20 = 0
    
    for val in data:
        temp_sum += val
        if val > 20:
            count_above_20 += 1
        
    stats['avg'] = temp_sum / len(data)
    stats['high_count'] = count_above_20
    
    # Irrelevant diagnostic computation (distractor)
    pair_sums = []
    for pair in combinations(data, 2):
        pair_sums.append(pair[0] + pair[1])
    stats['max_pair'] = max(pair_sums) if pair_sums else 0
    
    return stats

# Core scoring logic depending on processed thresholds
def calculate_final_score(metrics):
    base = metrics['avg'] * 10
    bonus = 5 if metrics['high_count'] > 2 else 0
    penalty = 3 if metrics.get('outlier_count', 0) > 1 else 0  # Unused key
    return int(base + bonus - penalty)

# Main execution flow
if __name__ == '__main__':
    # Step 1: Acquire and clean sensor data
    sensor_data = generate_sensor_readings()
    
    # Step 2: Extract statistical features
    processed_data = process_diagnostics(sensor_data)
    
    # Step 3: Compute final score (this is the key statement)
    final_score = calculate_final_score(processed_data)
    
    # Distractor variables - not used in final result
    normalized_data = [round(x / processed_data['avg'], 2) for x in sensor_data]
    outlier_flags = [True if x < 5 or x > 50 else False for x in normalized_data]
    
    # Output target result
    print(f"Result: {final_score}")