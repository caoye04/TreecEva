import math

# Irrelevant helper function (decoy)
def normalize(data):
    return [x / sum(data) for x in data]

# Unused transformation (dead code path)
def transform_metric(x, method='log'):
    if method == 'log':
        return math.log(x + 1)
    elif method == 'sqrt':
        return math.sqrt(x)
    return x

# Simulated sensor readings (distraction data)
sensor_readings = [145, 203, 98, 117, 256]
calibration_offset = 12
adjusted_readings = [r - calibration_offset for r in sensor_readings]

# Core performance metrics (relevant data)
response_time_ms = 240
error_rate = 0.04
throughput_bps = 15200
availability = 0.997

# Distractor calculations (irrelevant metrics)
latency_jitter = 18.3
packet_loss_ratio = 0.002
retransmission_count = 3
estimated_bandwidth = throughput_bps * (1 - packet_loss_ratio)

# Weight configuration (partially relevant)
weights = {
    'speed': 0.35,
    'accuracy': 0.40,
    'capacity': 0.20,
    'reliability': 0.05  # Downweighted but still used
}

# Metric preprocessing with lambda and conditional expression (core concept)
preprocess = lambda x, limit: x if x > 0 else 1
safe_log = lambda x: math.log(x) if x > 0 else 0

# Composite metric construction with red herrings
raw_speed = 1000 / preprocess(response_time_ms, 1)
scaled_accuracy = (1 - error_rate) * 100
normalized_throughput = min(throughput_bps / 1000, 20)  # Capped at 20

# Fake fusion using bitwise distraction (misleading intermediate)
temp_fusion = (int(scaled_accuracy) << 2) ^ int(raw_speed)
decoy_hash = (temp_fusion & 0xFF) | (int(normalized_throughput) << 8)

# Real metric set (only some components are actually used later)
metric_set = {
    'speed_val': raw_speed,
    'acc_val': scaled_accuracy,
    'cap_val': normalized_throughput,
    'rel_val': availability * 100,
    'jitter': latency_jitter,  # unused field
    'retrans': retransmission_count  # unused field
}

# Auxiliary computation (distractor)
avg_sensor = sum(adjusted_readings) / len(adjusted_readings)
sensor_variance = sum((x - avg_sensor) ** 2 for x in adjusted_readings) / len(adjusted_readings)

# Conditional logic with nesting and multiple concepts
def evaluate_reliability(availability, retransmissions):
    if availability > 0.98:
        if retransmissions < 5:
            return 95
        else:
            return 70
    else:
        return 50

# Main evaluation function with complex dependencies
def evaluate_performance(metrics, w):
    base_speed = metrics['speed_val']
    base_acc = metrics['acc_val']
    base_cap = metrics['cap_val']
    
    # Introduce conditional expression (required feature)
    penalty = 10 if metrics['acc_val'] < 90 else 0
    
    # Hidden dependency on reliability via availability
    rel_score = evaluate_reliability(metrics['rel_val']/100, 2)  # Fixed retrans=2
    
    # Critical calculation chain (8-12 steps)
    s1 = base_speed * w['speed']
    s2 = base_acc * w['accuracy']
    s3 = base_cap * w['capacity']
    s4 = rel_score * w['reliability']
    
    # Accumulation with rounding distraction
    total = s1 + s2 + s3 + s4
    rounded_total = round(total * 2) / 2  # Half-point precision
    
    # Final adjustment based on accuracy threshold (key logic)
    final = rounded_total - penalty
    
    # Dead branch (red herring)
    if decoy_hash > 1000:  # Never executed due to prior masking
        final += 5
    
    return final

# Execution point of interest
final_score = evaluate_performance(metric_set, weights)

# Print result as required
print(f"Target result: {final_score}")