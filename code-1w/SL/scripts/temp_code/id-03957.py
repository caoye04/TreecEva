from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline with performance evaluation

def analyze_readings(data_stream):
    readings = [x for x in data_stream if x > 0]
    normalized = [r / sum(readings) for r in readings]
    entropy = -sum(p * math.log(p) for p in normalized if p > 0)
    return entropy

def compute_health_index(values):
    # Irrelevant health metric computation (decoy)
    avg = sum(values) / len(values)
    variance = sum((v - avg) ** 2 for v in values) / len(values)
    return math.exp(-variance)

def extract_features(records):
    # Real feature extraction with distractions
    features = defaultdict(float)
    temp_buffer = []
    
    for i, (idx, val) in enumerate(zip(range(len(records)), records)):
        if idx % 2 == 0:
            features['even_sum'] += val
        else:
            features['odd_prod'] *= (val + 1)  # starts at 1.0 by default
        
        temp_buffer.append(val ** 0.5)
    
    # Distractor: unused transformation
    squared_chain = [temp_buffer[i]**2 for i in range(len(temp_buffer)) if i % 3 == 0]
    reversed_chain = squared_chain[::-1]
    
    features['buffer_entropy'] = analyze_readings(temp_buffer)
    return dict(features)

def calculate_risk_profile(entries):
    # Dead code path - never actually used
    risk = 0
    for e in entries:
        if e < 0:
            risk += 1
    return risk

def evaluate_performance(metrics, weights):
    score = 0.0
    components = ['even_sum', 'buffer_entropy', 'odd_prod']
    
    # Key logic hidden among irrelevant operations
    decoy_value = 0
    for k in ['timing_jitter', 'phase_drift', 'gain_skew']:
        decoy_value ^= hash(k) % 100  # Red herring
    
    intermediate_results = []
    for i, (key, weight) in enumerate(zip(components, weights)):
        raw_val = metrics.get(key, 0)
        if key == 'odd_prod':
            # Only consider last digit due to overflow protection
            adjusted = abs(raw_val) % 10
        elif key == 'even_sum':
            adjusted = raw_val * 1.5
        elif key == 'buffer_entropy':
            adjusted = raw_val * 2.0
        else:
            adjusted = 0
        intermediate_results.append(adjusted * weight)
    
    # Actual accumulation happens here
    total = sum(intermediate_results)
    penalty = 0
    
    # Misleading conditional block (never triggers due to data constraints)
    if metrics.get('anomaly_count', 10) > 5 and metrics.get('fault_flag', True):
        penalty = total * 0.1
    
    final = total - penalty
    
    # Decoy assignment
    summary_stats = Counter({'processed': len(weights), 'errors': 0})
    summary_stats['score_snapshot'] = final  # Not used further
    
    return final

# Simulated input data (deterministic)
data_log = [4, 8, 2, 6, 3, 9]

# Weight configuration (critical)
weights_config = [0.4, 0.3, 0.7]  # Applied to [even_sum, buffer_entropy, odd_prod]

# Extract meaningful features
extracted_metrics = extract_features(data_log)

# Inject irrelevant variables
dummy_analysis = compute_health_index(data_log)
security_token = ''.join(chr((ord('a') + i) % 26 + ord('a')) for i in range(10))
system_uptime = 1247 % 97

# Evaluate performance - KEY EXECUTION POINT
final_score = evaluate_performance(extracted_metrics, weights_config)

# Output result
print(f"Result: {final_score}")