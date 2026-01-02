from collections import defaultdict
from itertools import cycle

# Simulate sensor benchmark results with metadata
def generate_sensor_data():
    data = [
        {'sensor': 'A', 'reads': [12, 15, 14, 13], 'calibrated': True},
        {'sensor': 'B', 'reads': [9, 11, 10], 'calibrated': False},
        {'sensor': 'C', 'reads': [16, 16, 17, 15, 14], 'calibrated': True}
    ]
    return data

# Misleading auxiliary function (not used in final calculation)
def compute_avg_smooth(data_list):
    total = 0
    count = 0
    for val in data_list:
        if val > 10:
            total += val // 2  # Distorted computation
            count += 1
    return total / count if count else 0

# Helper to adjust readings based on calibration status
def adjust_readings(sensor_dict):
    readings = sensor_dict['reads']
    is_calib = sensor_dict['calibrated']
    
    if is_calib:
        return sum(readings) / len(readings)  # Simple mean
    else:
        # Apply arbitrary correction factor (not actually used)
        corrected = [r * 1.1 for r in readings]
        return sum(corrected) / len(corrected)

# Main performance calculator
def calculate_performance(results):
    scores = defaultdict(float)
    temp_aggregates = []  # Unused tracking variable (distractor)
    adjustment_cycle = cycle([0.9, 1.0, 1.1])  # Cycling iterator (partially used)

    for entry in results:
        sensor_id = entry['sensor']
        base_avg = sum(entry['reads']) / len(entry['reads'])
        
        # Irrelevant intermediate calculation
        variance_proxy = 0
        for r in entry['reads']:
            variance_proxy += (r - base_avg) ** 2
        std_approx = variance_proxy ** 0.5
        
        # Only calibration status matters for adjustment
        if entry['calibrated']:
            adjusted_avg = base_avg * 1.05
        else:
            adjusted_avg = base_avg * 0.95
        
        # Use the cycling iterator to add noise-like behavior (only one use)
        noise_factor = next(adjustment_cycle)
        final_adjusted = adjusted_avg * noise_factor
        
        scores[sensor_id] = final_adjusted
        temp_aggregates.append(std_approx)  # Stored but not used later
    
    # Compute composite score using only specific logic
    raw_total = sum(scores.values())
    penalty = 0
    
    # Additional red herring: complex condition that never triggers
    extreme_values = list(filter(lambda x: x > 100, scores.values()))
    if extreme_values:
        penalty = sum(extreme_values) * 0.1
    
    # Actual result computation
    composite = raw_total - penalty
    normalized = int(composite * 100) / 100  # Round to two decimals
    
    # Final transformation
    return int(normalized + 5)  # Deterministic shift

# Execution flow
if __name__ == "__main__":
    benchmark_results = generate_sensor_data()
    
    # Dummy preprocessing (no effect)
    processed = []
    for item in benchmark_results:
        item['timestamp'] = "2023-01-01"  # Added metadata (unused)
        processed.append(item)
    
    # Key execution point
    final_score = calculate_performance(benchmark_results)
    
    # Output result as required
    print(f"Result: {final_score}")