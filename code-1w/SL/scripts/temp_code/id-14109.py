import math

# Simulated sensor health monitoring system

def analyze_readings(readings):
    if not readings:
        return 0
    avg = sum(readings) / len(readings)
    variance = sum((x - avg) ** 2 for x in readings) / len(readings)
    return math.sqrt(variance)


def evaluate_stability(metric, baseline):
    # Irrelevant complexity: stability analysis with decoy logic
    adjustment_factor = 1.75
    threshold_map = {k: v * adjustment_factor for k, v in baseline.items()}
    score = 0
    for key in ['temp', 'pressure', 'flow']:
        if key in metric and key in threshold_map:
            if metric[key] < threshold_map[key] * 0.9:
                score += 1
    return score  # Red herring: never used in final computation


def compute_gradient(values):
    # Dead function: looks relevant but unused
    return [values[i+1] - values[i] for i in range(len(values)-1)]


def filter_anomalies(data_stream):
    # Distractor: complex filtering that isn't used
    z_scores = [abs(x - sum(data_stream)/len(data_stream)) / 
               (sum((x - sum(data_stream)/len(data_stream))**2 for x in data_stream)/len(data_stream))**0.5 
               for x in data_stream]
    return [data_stream[i] for i in range(len(data_stream)) if z_scores[i] < 2]


def generate_synthetic_data(seed=42):
    # Misleading function: generates data but not the one used
    result = []
    val = seed
    for i in range(8):
        val = (val * 17 + 31) % 100
        result.append(val)
    return result


def extract_key_features(raw_data):
    # Looks important but output partially ignored
    features = {}
    features['peak'] = max(raw_data)
    features['trough'] = min(raw_data)
    features['delta'] = features['peak'] - features['trough']
    features['noise_floor'] = sum(1 for x in raw_data if x < 10)  # Unused field
    return {'delta': features['delta']}  # Only part used


def process_metrics(sensor_data, config):
    # Core logic buried in distractions
    base_metric = 0
    
    # Relevant path begins here
    for sensor, readings in sensor_data.items():
        if sensor.startswith('primary_'):
            stat = analyze_readings(readings)
            if stat > config['tolerance']:
                base_metric += int(stat * 100)
    
    # Extract delta from secondary processing
    aux_data = [12, 15, 8, 23, 19, 11]
    extracted = extract_key_features(aux_data)
    
    # Combine core elements
    enhancement = config['boost_factor'] * extracted['delta']
    
    # Final computation
    intermediate = base_metric * enhancement
    scaling = len([k for k in sensor_data.keys() if k.startswith('primary_')])
    if scaling > 0:
        intermediate //= scaling
    
    # Final transformation
    final_diagnostic = intermediate + config['offset']
    
    # Debug print (irrelevant)
    debug_state = {'stage': 'complete', 'code': 200}
    
    return final_diagnostic

# Main execution
if __name__ == '__main__':
    # Real data used in computation
    health_data = {
        'primary_a': [3.2, 3.5, 2.8, 4.1, 3.9],
        'primary_b': [5.1, 4.8, 5.3, 5.0, 4.9],
        'auxiliary_x': [1.0, 1.1, 0.9],  # Won't be processed
        'primary_c': [2.0, 2.2, 1.8, 2.5]  # Included
    }
    
    # Configuration with misleading entries
    thresholds = {
        'tolerance': 0.3,
        'boost_factor': 3,
        'offset': 42,
        'decay_rate': 0.85,  # Unused
        'window_size': 5,      # Unused
        'temp': 75,            # Decoy from evaluate_stability
        'pressure': 30        # Another decoy
    }
    
    # Variables designed to distract
    calibration_sequence = [generate_synthetic_data(i) for i in range(3)]
    system_flags = {'active': True, 'mode': 'diagnostic', 'level': 9}
    telemetry_log = []
    
    # Critical execution point
    final_diagnostic = process_metrics(health_data, thresholds)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")