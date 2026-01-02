def analyze_readings(values):
    """Irrelevant helper function for sensor noise filtering."""
    return [v for v in values if v > 0.1]

# Simulated health monitoring system
def compute_baseline(x):
    return (x ** 2 + 3 * x + 1) // 5

def evaluate_risk_level(metric, profile):
    if metric < profile['safe']:
        return 'low'
    elif metric < profile['caution']:
        return 'moderate'
    else:
        return 'high'

def extract_signals(data_dict):
    # Distractor: processes unrelated signal features
    signals = []
    for k, v in data_dict.items():
        if 'signal' in k:
            signals.append(sum(v) / len(v))
    return signals

def transform_entries(raw_list):
    # Dead code path - never used in final computation
    adjusted = []
    for item in raw_list:
        if item % 3 == 0:
            adjusted.append(item // 3)
        elif item % 5 == 0:
            adjusted.append(item * 2)
        else:
            adjusted.append(item + 1)
    return adjusted

def decode_flag(status_code):
    # Misleading intermediate logic
    binary_rep = bin(status_code)[2:]
    parity = sum(int(b) for b in binary_rep) % 2
    return parity == 1

def aggregate_diagnostics(metrics, config):
    total = 0
    weights = config.get('weights', [1, 1, 1])
    for i, val in enumerate(metrics):
        if i % 2 == 0:
            total += val * weights[0]
        else:
            total += (val // 2) * weights[1]
    return total

def process_metrics(data, thresholds):
    # Core logic begins here
    stage_one = []
    for key, value in data.items():
        if key in thresholds:
            if value > thresholds[key]:
                stage_one.append(value * 0.8)
            else:
                stage_one.append(value * 1.1)
    
    # Apply non-linear adjustment
    adjusted_metrics = [int(x ** 1.5) for x in stage_one]
    
    # Secondary filtering based on modulo pattern
    filtered = []
    for idx, val in enumerate(adjusted_metrics):
        if idx == 0 or val % 7 != 0:  # Keep first or non-divisible by 7
            filtered.append(val)
    
    # Aggregate using complex formula
    accumulator = 0
    for i, v in enumerate(filtered):
        if i % 3 == 0:
            accumulator += v * 2
        elif i % 3 == 1:
            accumulator += v + 50
        else:
            accumulator -= v // 4
    
    # Final transformation with rounding
    result = int((accumulator * 1.23) // 1)
    
    # Irrelevant diagnostic flag (distractor)
    flag_status = decode_flag(result)
    if flag_status:
        result += 100  # This will not trigger
    
    return result

# Main execution block
if __name__ == '__main__':
    # Real input data
    health_data = {
        'oxygen_level': 92,
        'heart_rate': 78,
        'temperature': 37,
        'neural_activity': 65,
        'respiration_rate': 18
    }
    
    # Threshold configuration (critical)
    threshold_map = {
        'oxygen_level': 90,
        'heart_rate': 80,
        'temperature': 37.5,
        'neural_activity': 60,
        'respiration_rate': 20
    }
    
    # Irrelevant auxiliary data structures
    signal_data = {
        'signal_a': [0.5, 0.7, 0.6],
        'signal_b': [0.9, 0.3],
        'noise_floor': [-0.1, -0.2]
    }
    
    metadata_log = [
        {'timestamp': '2023-01-01T10:00:00', 'node': 'A1', 'status': 1},
        {'timestamp': '2023-01-01T10:05:00', 'node': 'A2', 'status': 0}
    ]
    
    # Unused computational traces
    baseline_scores = [compute_baseline(i) for i in range(5)]
    risk_profile = {'safe': 50, 'caution': 75, 'danger': 90}
    
    # Key irrelevant list comprehension (distractor)
    derived_flags = [decode_flag(code) for code in [7, 13, 14, 15]]
    
    # Signal extraction (dead end)
    extracted = extract_signals(signal_data)
    
    # Actual target computation
    final_diagnostic = process_metrics(health_data, threshold_map)
    
    # Print final answer as required
    print(f"Result: {final_diagnostic}")