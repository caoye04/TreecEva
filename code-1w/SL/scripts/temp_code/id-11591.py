import math

# Simulated sensor data processing with performance evaluation
raw_readings = [0.85, 0.92, 0.78, 0.96, 0.88]
offset_calibration = 0.02

def apply_noise_filter(data, threshold=0.05):
    """Irrelevant filtering function (dead code path)"""
    return [x for x in data if x > threshold]

def deprecated_normalization(arr):
    """Unused legacy function - red herring"""
    max_val = max(arr)
    return [x / max_val for x in arr]

temp_buffer = [x + offset_calibration for x in raw_readings]

# Weighted scoring components
accuracy = sum(temp_buffer) / len(temp_buffer)
consistency = temp_buffer[1] - temp_buffer[-1]
response_time_bias = 0.03

# Fake aggregation metrics (distractors)
phantom_metric_1 = (accuracy ** 2) * 0.7
phantom_metric_2 = math.log(accuracy + 1)

# Real metric preprocessing
metrics = {
    'accuracy': accuracy + response_time_bias,
    'stability': 1 - abs(consistency),
    'latency_penalty': 0.1,
    'reliability': temp_buffer[2]  # mid-point reading
}

# Irrelevant dictionary transformation (distraction)
decoy_map = {i: round(math.sin(v), 3) for i, v in enumerate(temp_buffer)}

# Weight configuration - only this matters
weights = {
    'accuracy': 0.4,
    'stability': 0.3,
    'latency_penalty': -0.2,  # negative impact
    'reliability': 0.1
}

# Unused lambda - misleading functional reference
compute_deviance = lambda x, base: abs(x - base) ** 2

# Core evaluation logic (key path)
def evaluate_performance(met, wgt):
    score = 0.0
    for key in met:
        if key in wgt:
            score += met[key] * wgt[key]
    
    # Artificial complexity: adjustment based on phantom rules
    adjustment_flag = False
    if score > 0.5 and 'latency_penalty' in met:
        phantom_sum = sum([v for k, v in met.items() if 'phantom' not in k])  # real-only
        correction = len([x for x in temp_buffer if x > 0.85]) * 0.01
        score = (score * 0.95) + correction  # minor boost
    
    # Dead recursive branch (never entered)
    def recursive_amplify(val, depth):
        if depth <= 0 or val >= 1.0:
            return val
        return recursive_amplify(val * 1.02, depth - 1)
    
    # This call is never made - decoy logic
    # score = recursive_amplify(score, 3)
    
    return round(score, 6)

# Secondary irrelevant computation
outlier_count = 0
for reading in temp_buffer:
    if reading > 0.95 or reading < 0.80:
        outlier_count += 1

# Dummy normalization map (unused)
normalized_map = dict(map(lambda x: (round(x, 2), round(x * 1.01, 2)), temp_buffer))

# Key execution point
evaluation_trace = True
final_score = evaluate_performance(metrics, weights)

# Final irrelevant bit manipulation (red herring)
status_flag = 0b1010
mask = 0b1100
masked_status = status_flag & mask  # unused result

print(f"Result: {final_score}")