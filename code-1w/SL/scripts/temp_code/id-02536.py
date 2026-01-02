from collections import defaultdict

# Simulate sensor data with noise and valid readings
def preprocess_sensor_data(raw_data):
    processed = []
    noise_count = 0
    for val in raw_data:
        if abs(val) > 100:  # Assume values beyond this are noise
            noise_count += 1
            continue
        if val % 2 == 0:
            processed.append(val * 0.95)
        else:
            processed.append(val * 1.05)
    return processed, noise_count

def analyze_trends(values):
    trend_info = defaultdict(int)
    increases = 0
    decreases = 0
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            increases += 1
            trend_info['up'] += 1
        elif values[i] < values[i-1]:
            decreases += 1
            trend_info['down'] += 1
        else:
            trend_info['stable'] += 1
    net_trend = increases - decreases
    return net_trend, trend_info

def apply_threshold_filter(items, threshold_map):
    # Misleading function that appears important but only used partially
    filtered = []
    debug_stats = {'above': 0, 'below': 0}
    for item in items:
        if item > threshold_map.get('high', 50):
            filtered.append(item * 0.8)
            debug_stats['above'] += 1
        elif item < threshold_map.get('low', 10):
            filtered.append(item * 1.1)
            debug_stats['below'] += 1
        else:
            filtered.append(item)
    return filtered

def calculate_final_score(data, thresholds):
    # Main logic with embedded distractions
    adjusted_data, dropped = preprocess_sensor_data(data)
    
    # Dummy tracking variables (distractors)
    total_adjustments = 0
    peak_value = float('-inf')
    for x in adjusted_data:
        if x > peak_value:
            peak_value = x
        total_adjustments += 1

    # Analyze trend significance
    net_change, trends = analyze_trends(adjusted_data)
    
    # Irrelevant aggregation (distractor)
    cumulative_sum = 0
    for val in adjusted_data:
        cumulative_sum += val ** 0.5 if val > 0 else 0

    # Filter based on thresholds (semi-relevant)
    refined_data = apply_threshold_filter(adjusted_data, thresholds)
    
    # Core scoring logic (depends on net_change and refined average)
    base_score = sum(refined_data) / len(refined_data) if refined_data else 0
    modifier = 1.0
    if net_change > 5:
        modifier = 1.3
    elif net_change < -5:
        modifier = 0.7
    else:
        modifier = 1.0 + (net_change * 0.02)
    
    # Introduce a red herring calculation
    outlier_ratio = dropped / len(data) if data else 0
    stability_penalty = trends['stable'] * 0.01  # Not actually used
    
    final_score = base_score * modifier
    
    # Additional misleading adjustment path (dead code)
    if final_score > 1000:
        final_score *= 0.9
    elif final_score < 0:
        final_score = abs(final_score)

    return int(final_score)  # Final deterministic integer result

# Input data and configuration
sensor_readings = [120, -5, 18, 22, 25, 27, 30, 33, 200, -15, 45, 50, 52]
config_thresholds = {'low': 15, 'high': 40}

# Execute main computation
final_score = calculate_final_score(sensor_readings, config_thresholds)
print(f"Result: {final_score}")