from collections import defaultdict

# Simulate sensor data aggregation and anomaly detection
def collect_diagnostics(raw_readings):
    stats = defaultdict(int)
    anomalies = []
    temp_sum = 0
    reading_count = len(raw_readings)

    for val in raw_readings:
        if val < 0:
            stats['negative'] += 1
        elif val % 7 == 0:
            stats['divisible_by_7'] += 1
        if 100 < val < 200:
            temp_sum += val

    avg_temp_region = temp_sum / (stats['divisible_by_7'] + 1)
    return stats, avg_temp_region

def apply_calibration(readings, base_offset):
    calibrated = [((x ^ 3) + base_offset) % 105 for x in readings]
    outlier_count = sum(1 for c in calibrated if c > 100)
    # Misleading normalization
    normalized = [c / 1.5 for c in calibrated]
    return calibrated, outlier_count

def evaluate_performance(metrics, thresh):
    score = 0
    penalty = 0
    
    # Complex scoring logic with red herrings
    if metrics['divisible_by_7'] > thresh:
        score += 15
    if metrics['negative'] == 0:
        score += 10
    
    # Irrelevant transformation
    dummy_calc = sum([i * i for i in range(1, 6)])  # 1-5 squared sum, unused later
    
    # Additional decoy logic
    temp_cache = {}
    for k in metrics:
        temp_cache[k + '_sq'] = metrics[k] ** 2
    
    # Real influence: hidden rule based on XOR pattern in original data
    hidden_flag = (thresh ^ metrics['divisible_by_7']) & 1
    if hidden_flag:
        score += 7
    
    return score

# Main execution flow
if __name__ == '__main__':
    sensor_log = [14, 23, 49, 55, 63, 71, 84, 97, 105, 113]
    offset = 12
    
    # Step 1: Apply fake calibration with side effects
    calibrated_readings, outliers = apply_calibration(sensor_log, offset)
    
    # Step 2: Collect real diagnostics (used in final score)
    diagnostic_stats, average_midrange = collect_diagnostics(calibrated_readings)
    
    # Step 3: Compute auxiliary metric (distractor)
    aux_values = [x for x in calibrated_readings if x % 5 == 0]
    aux_sum = sum(aux_values)  # Not used later
    
    # Step 4: Determine threshold from irrelevant heuristic
    threshold = len(aux_values) + 2  # Based on multiples of 5
    
    # Step 5: Evaluate performance using actual logic chain
    final_score = evaluate_performance(diagnostic_stats, threshold)
    
    # Output target result
    print(f"Result: {final_score}")