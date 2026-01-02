import math

def analyze_signal(strength, threshold=0.65):
    if strength < threshold:
        return 'weak'
    elif strength > 1.3 * threshold:
        return 'strong'
    else:
        return 'moderate'

# Irrelevant helper (dead function)
def decrypt_key(key_str):
    return ''.join([chr(ord(c)-1) for c in key_str[::-1]])

# Unused transformation
def normalize_vector(v):
    mag = sum(x**2 for x in v) ** 0.5
    return [x / mag for x in v] if mag else v

# Distractor data
template_config = {
    'version': '2.1',
    'mode': 'legacy',
    'flags': [1, 0, 1],
    'padding': 'none'
}

# Real configuration used
config = {
    'sampling_rate': 44100,
    'window_size': 1024,
    'overlap': 512,
    'features': ['mfcc', 'chroma', 'rms'],
    'calibration': {
        'offset': 0.037,
        'scale': 1.02
    }
}

# Sensor log with mixed status and numeric data
log_data = [
    {'time': 0.0, 'value': 0.81, 'status': 'OK', 'sensor': 'A'},
    {'time': 0.1, 'value': 0.45, 'status': 'ERROR', 'sensor': 'B'},
    {'time': 0.2, 'value': 1.15, 'status': 'OK', 'sensor': 'A'},
    {'time': 0.3, 'value': 0.93, 'status': 'OK', 'sensor': 'C'},
    {'time': 0.4, 'value': 0.22, 'status': 'ERROR', 'sensor': 'B'},
    {'time': 0.5, 'value': 1.42, 'status': 'OK', 'sensor': 'D'}
]

# Auxiliary mapping (partially used)
status_severity = {
    'OK': 0,
    'WARNING': 1,
    'ERROR': 2,
    'CRITICAL': 3
}

# Decoy accumulator
shadow_score = 0
for entry in log_data:
    if entry['status'] == 'ERROR':
        shadow_score += status_severity[entry['status']]

# Real processing function
def extract_features(entries, cfg):
    raw_values = [e['value'] for e in entries]
    calibrated = [
        (v + cfg['calibration']['offset']) * cfg['calibration']['scale']
        for v in raw_values
    ]
    
    # Compute moving average over window
    smoothed = []
    window = 3
    for i in range(len(calibrated)):
        start = max(0, i - window + 1)
        segment = calibrated[start:i+1]
        smoothed.append(sum(segment) / len(segment))
    
    return raw_values, calibrated, smoothed

# Secondary analysis (distractor)
def evaluate_consistency(trace):
    trend = 0
    for i in range(1, len(trace)):
        if trace[i] > trace[i-1]:
            trend += 0.1
        elif trace[i] < trace[i-1]:
            trend -= 0.05
    return round(trend, 3)

# Main processing pipeline
def process_metrics(data, settings):
    raw, calibrated, filtered = extract_features(data, settings)
    
    # Assess signal quality per sample
    qualities = [analyze_signal(v, 0.5) for v in calibrated]
    
    # Count transitions in quality
    transitions = 0
    for i in range(1, len(qualities)):
        if qualities[i] != qualities[i-1]:
            transitions += 1
    
    # Aggregate statistics
    stats = {
        'total': len(data),
        'errors': len([e for e in data if e['status'] == 'ERROR']),
        'high_val': len([v for v in calibrated if v >= 1.0]),
        'transitions': transitions,
        'mean_filtered': sum(filtered) / len(filtered)
    }
    
    # Irrelevant string transformation (red herring)
    feature_keys = ''.join(settings['features']).upper()
    checksum = sum(ord(c) for c in feature_keys) % 17
    
    # Core diagnostic logic
    base = stats['mean_filtered'] * 1000
    penalty = stats['errors'] * 50 + stats['transitions'] * 20
    bonus = stats['high_val'] * 15
    
    intermediate = base - penalty + bonus
    
    # Final nonlinear adjustment
    if intermediate < 400:
        final = intermediate * 1.1
    elif intermediate > 700:
        final = intermediate * 0.9 + 50
    else:
        final = intermediate + 10 * math.sin(intermediate / 100)
    
    # This is the actual answer variable
    final_diagnostic = int(round(final))
    
    return final_diagnostic

# Execute main logic
final_diagnostic = process_metrics(log_data, config)

# Print result as required
print(f"Result: {final_diagnostic}")