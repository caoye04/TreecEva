from itertools import compress, cycle

def analyze_performance(raw_data, threshold=50):
    # Preprocess: filter values above threshold and map to binary indicators
    filtered_mask = [x > threshold for x in raw_data]
    filtered_values = list(compress(raw_data, filtered_mask))
    
    # Distractor: create a cycling pattern that isn't used later
    pattern_cycle = list(zip(filtered_values, cycle([1, -1])))
    signed_seq = [val * sign for val, sign in pattern_cycle]  # unused

    # Transform: apply logarithmic scaling (only relevant for positive values)
    import math
    safe_log = lambda x: math.log(x) if x > 0 else 0
    logged_values = [safe_log(x) for x in filtered_values]
    
    # Normalize between 0 and 100
    if logged_values:
        min_val = min(logged_values)
        max_val = max(logged_values)
        range_val = max_val - min_val or 1
        normalized = [99 * (x - min_val) / range_val + 1 for x in logged_values]
    else:
        normalized = []
    
    # Introduce red herring computation on strings
    status_codes = ['OK', 'ERR', 'WARN']
    code_freq = {code: len(raw_data) % 3 for code in status_codes}  # irrelevant
    summary_tag = ''.join([code[0] for code in status_codes])  # unused

    return normalized


def calculate_adjusted_average(values):
    if not values:
        return 0.0
    
    # Apply exponential weighting to emphasize recent elements
    n = len(values)
    weights = [i+1 for i in range(n)]  # linear weights
    weighted_sum = sum(val * weight for val, weight in zip(values, weights))
    total_weight = sum(weights)
    arithmetic_mean = sum(values) / len(values)
    weighted_avg = weighted_sum / total_weight
    
    # Adjustment factor based on variance (distraction with intermediate calc)
    variance = sum((x - arithmetic_mean) ** 2 for x in values) / len(values) if values else 0
    adjustment = math.sqrt(variance) / 10 if variance > 1 else 0  # minor penalty
    adjusted_average = weighted_avg - adjustment
    
    return adjusted_average

# Main execution
sensor_readings = [45, 67, 89, 12, 55, 91, 34, 78, 66, 23, 50, 72]

dummy_offset = sum(x ** 0.5 for x in sensor_readings if x % 3 == 0)  # irrelevant calculation

processed_values = analyze_performance(sensor_readings, threshold=44)

# Additional distraction: simulate checksum
checksum = 0
for i, v in enumerate(processed_values):
    checksum ^= int(v)  # bitwise XOR accumulation, not used later
temp_result = [x for x in processed_values if x > 50]  # semi-relevant filtering

final_score = calculate_adjusted_average(processed_values)

print(f"Result: {final_score}")