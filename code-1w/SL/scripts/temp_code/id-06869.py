import math

# Simulated sensor data processing with performance evaluation
raw_readings = [145, 203, 178, 99, 212, 167, 155]
offset_correction = 5

def apply_noise_filter(data, threshold=100):
    """Applies a filter to remove low-amplitude noise (distractor function)"""
    return [x for x in data if x > threshold]

def calculate_checksum(sequence):
    """Calculates XOR checksum of a sequence (irrelevant but plausible)"""
    checksum = 0
    for val in sequence:
        checksum ^= val
    return checksum

def generate_metrics(readings):
    """Generates various performance metrics from sensor readings"""
    corrected = [r - offset_correction for r in readings]
    squared_errors = [(x - 150)**2 for x in corrected]  # deviation from ideal baseline
    mse = sum(squared_errors) / len(squared_errors)
    rmse = math.sqrt(mse)
    
    # Irrelevant transformations
    log_vals = [math.log(x) for x in corrected if x > 0]
    avg_log = sum(log_vals) / len(log_vals) if log_vals else 0
    
    # Decoy metric set
    decoy_set = set([int(math.ceil(x)) for x in log_vals])
    
    # Key metric: count of readings within acceptable range [150, 170] after correction
    valid_range_count = len([x for x in corrected if 150 <= x <= 170])
    
    # Another red herring: frequency analysis
    freq_map = {}
    for val in corrected:
        freq_map[val] = freq_map.get(val, 0) + 1
    unique_count = len(freq_map)
    
    # Return a mix of relevant and irrelevant metrics
    return {
        'rmse': rmse,
        'valid_count': valid_range_count,
        'unique_count': unique_count,
        'decoy_set': decoy_set,
        'avg_log': avg_log
    }

def evaluate_performance(metrics):
    """Evaluates system performance based on key metric"""
    # Only valid_count is actually used in final score
    base_score = metrics['valid_count'] * 100
    penalty = 0
    
    # Distractor logic - looks important but unused
    if metrics['rmse'] > 500:
        penalty += 20
    if len(metrics['decoy_set']) > 10:
        penalty += 10
    if metrics['unique_count'] < 5:
        penalty += 15
    
    # Final score depends only on valid_count
    return base_score - penalty  # penalty is always 0 due to data

# Main execution flow
filtered_data = apply_noise_filter(raw_readings)
corrupted_checksum = calculate_checksum(filtered_data)  # unused result

# Primary data transformation
performance_metrics = generate_metrics(filtered_data)

# Critical statement: evaluation based on metrics
final_score = evaluate_performance(performance_metrics)

# Print result as required
print(f"Target result: {final_score}")