from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation (distractor: some values are irrelevant)
def collect_telemetry():
    raw_streams = [
        [1.2, 3.5, 2.1, 4.4, 5.0],
        [0.8, 2.9, 1.7, 3.8, 4.6],
        [1.5, 3.1, 2.5, 5.1, 6.2]
    ]
    aggregated = []
    for stream in raw_streams:
        offset = 0.3  # red herring: not used in final logic
        adjusted = [x + 0.1 for x in stream]
        aggregated.extend(adjusted)
    return aggregated

# Irrelevant preprocessing path (dead code)
def legacy_normalize(data):
    mean_val = sum(data) / len(data)
    return [x / mean_val for x in data]

# Real preprocessing with subtle filtering
def preprocess_readings(telemetry):
    filtered = [x for x in telemetry if x > 2.0]  # key filter
    smoothed = [x * 0.95 for x in filtered]
    return sorted(smoothed, reverse=True)

# Misleading diagnostic using outdated method
def deprecated_analysis(signal):
    stats = defaultdict(float)
    stats['peak'] = max(signal)
    stats['noise_floor'] = min(signal) if signal else 0
    stats['distortion'] = stats['peak'] - stats['noise_floor']
    return stats  # never actually used

# Core metric computation with distractor variables
def compute_envelope(signal):
    envelope = 0.0
    harmonics = []
    for i, val in enumerate(signal):
        if i % 2 == 0:
            envelope += math.sin(val)  # real contribution
        else:
            harmonics.append(math.cos(val))  # distraction
    envelope *= 1.5
    return envelope

# Threshold-based classification with tuple unpacking
def classify_risk(envelope_value, risk_map):
    level, code = None, None
    for threshold, (lvl, cd) in sorted(risk_map.items(), reverse=True):
        if envelope_value >= threshold:
            level, code = lvl, cd
            break
    return level, code  # unused return components act as distractors

def evaluate_stability(metrics, config):
    stability_score = 0
    weights = config.get('weights', [1, 0.5, 0.25])
    decay = config.get('decay', 0.9)  # misleading parameter
    
    # Complex but partially irrelevant transformation
    transformed = []
    for i, m in enumerate(metrics):
        if i < 3:
            transformed.append(m * (weights[i] if i < len(weights) else 0.1))
    
    # Actual stability logic
    if len(transformed) > 0 and transformed[0] > 1.0:
        stability_score = int(sum(transformed) * 100)
    else:
        stability_score = -1
        
    # Dead branch with decoy calculation
    if False:  # never executed
        backup = sum(math.tan(x) for x in metrics if x < 5)
        stability_score = int(backup % 100)
        
    return stability_score

# Main processing pipeline with multiple concepts
def process_metrics(data, thresholds):
    # Step 1: Preprocess signal
    processed_signal = preprocess_readings(data)
    
    # Step 2: Compute physical envelope (critical path)
    envelope = compute_envelope(processed_signal)
    
    # Step 3: Classify risk level (uses tuple unpacking but only one part matters)
    risk_level, _ = classify_risk(envelope, thresholds)
    
    # Step 4: Prepare auxiliary metrics (mostly distractions)
    aux_metrics = [
        sum(processed_signal) / len(processed_signal),
        len([x for x in processed_signal if x > 3.0]),
        envelope * 0.1
    ]
    
    # Step 5: Configuration with default nesting (red herring structure)
    eval_config = {
        'mode': 'advanced',
        'params': {
            'iterations': 3,
            'tolerance': 1e-6,
            'weights': [0.8, 0.6, 0.4]
        },
        'flags': {'strict': True, 'debug': False}
    }
    
    # Step 6: Evaluate stability (only one metric matters)
    stability = evaluate_stability(aux_metrics, eval_config['params'])
    
    # Step 7: Final diagnostic computation (answer point)
    baseline = 420
    modifier = 1 if risk_level == 'critical' else 0.8
    final_diagnostic = baseline + stability * modifier
    
    # Redundant print for confusion
    debug_dump = {
        'raw_count': len(data),
        'retained': len(processed_signal),
        'envelope': envelope,
        'stability_raw': stability
    }
    
    return int(final_diagnostic)

# Execution entry point
if __name__ == '__main__':
    # Simulate input data collection
    sensor_data = collect_telemetry()
    
    # Define classification thresholds (real logic)
    alert_thresholds = {
        3.0: ('critical', 'ERR9'),
        2.0: ('warning', 'WRN5'),
        1.0: ('normal', 'OK1')
    }
    
    # Dead function call (misleading)
    if len(sensor_data) > 10:
        _ = deprecated_analysis(sensor_data)
    
    # Critical execution point
    final_diagnostic = process_metrics(sensor_data, alert_thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")