from collections import defaultdict, Counter
import math

# Simulated sensor readings and diagnostic flags
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8, 24.4, 26.2, 23.7]
pressure_readings = [101.3, 102.1, 100.8, 103.5, 101.9, 102.7, 104.0, 101.2]
humidity_readings = [45, 47, 50, 44, 48, 52, 46, 49]

# Irrelevant transformation: normalize to z-score (unused later)
def z_score_normalize(data):
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    return [(x - mean) / std_dev for x in data]

# Misleading preprocessing path (dead end)
def analyze_trend(sequence):
    trend = []
    for i in range(1, len(sequence)):
        trend.append(1 if sequence[i] > sequence[i-1] else 0)
    return trend

# Unused function: creates decoy logic
def compute_entropy(labels):
    counts = Counter(labels)
    total = len(labels)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Core evaluation metric computation
def calculate_stability_metric(readings):
    avg = sum(readings) / len(readings)
    variation = sum(abs(x - avg) for x in readings)
    return round(avg - variation * 0.1, 4)

# Complex scoring logic with distractors
def generate_diagnostic_profile(temp, pressure, humidity):
    profile = defaultdict(dict)
    
    # Real metric used later
    profile['thermal']['stability'] = calculate_stability_metric(temp)
    
    # Distractor metrics (not used in final score)
    profile['pressure']['trend_complexity'] = len(analyze_trend(pressure))
    profile['humidity']['diversity_index'] = compute_entropy([h // 5 for h in humidity])
    
    # Fake correlation matrix (irrelevant)
    correlation_matrix = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(len(temp)):
        correlation_matrix[0][1] += abs(temp[i] - pressure[i] * 0.1)
        correlation_matrix[1][2] += abs(humidity[i] - temp[i] * 0.2)
    
    # Dummy normalization
    norm_factor = sum(sum(row) for row in correlation_matrix) or 1
    profile['system']['noise_ratio'] = round(correlation_matrix[0][1] / norm_factor, 4)
    
    return profile

# Metric combination engine
def fuse_metrics(metrics_dict):
    fused = 1.0
    weights = {'stability': 0.6, 'noise_ratio': 0.1, 'phantom': 0.3}  # Only 'stability' actually exists
    
    if 'stability' in metrics_dict['thermal']:
        fused += weights['stability'] * metrics_dict['thermal']['stability']
    
    # These keys don't exist, so no effect
    if 'noise_ratio' in metrics_dict['system']:
        fused += weights['noise_ratio'] * metrics_dict['system']['noise_ratio']
    
    return fused

# Main evaluation function
def evaluate_performance(metric_set, data_map):
    # Red herring: set operations with no impact
    critical_keys = {'temp', 'pressure', 'humidity'}
    available_keys = set(data_map.keys())
    missing = critical_keys - available_keys
    
    if missing:
        return -999  # Never triggered
    
    # Actual work begins here
    raw_profile = generate_diagnostic_profile(
        data_map['temp'],
        data_map['pressure'],
        data_map['humidity']
    )
    
    # This is the only path that contributes
    intermediate = fuse_metrics(raw_profile)
    
    # Additional meaningless transformation
    adjustment_factor = len([x for x in temperature_readings if x > 24])
    phantom_offset = sum(1 for x in pressure_readings if x > 102) - adjustment_factor
    
    # Final computation chain
    base_score = intermediate * 100
    volatility_penalty = math.floor(base_score * 0.02)  # Small deduction
    final = base_score - volatility_penalty + abs(phantom_offset)  # offset is 0
    
    # Dead code branch (never reached due to structure)
    for k in ['A', 'B', 'C']:
        if k == 'Z':
            final ^= 255  # Bitwise red herring
    
    return int(final)

# Execution block
if __name__ == '__main__':
    # Define actual input data
    benchmark_data = {
        'temp': temperature_readings,
        'pressure': pressure_readings,
        'humidity': humidity_readings
    }
    
    # Placeholder set (distractor)
    metric_set = {'latency', 'throughput', 'stability', 'jitter', 'consistency'}
    
    # Key assignment statement
    final_score = evaluate_performance(metric_set, benchmark_data)
    
    # Output result as required
    print(f"Result: {final_score}")