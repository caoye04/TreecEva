import math

# System health monitoring simulation with data transformation and diagnostic logic

def collect_sensor_data():
    return {
        'temp': [23.4, 24.1, 25.0, 26.8, 22.9],
        'pressure': [101.3, 102.1, 99.7, 103.5, 100.8],
        'vibration': [0.05, 0.07, 0.12, 0.09, 0.11]
    }

def apply_calibration(readings, factor):
    return [round(x * factor, 3) for x in readings]

def detect_anomalies(series, threshold):
    return [i for i, x in enumerate(series) if x > threshold]

def merge_logs(data_dict):
    # Irrelevant aggregation for distraction
    log_entries = []
    for key, values in data_dict.items():
        for idx, val in enumerate(values):
            log_entries.append(f'{key}_{idx}:{val}')
    return '|'.join(log_entries)

def compute_entropy(values):
    # Distractor function - not used in final computation
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def transform_readings(raw):
    calibrated = {}
    temp_offset = 0.8
    
    # Real transformation path
    calibrated['temp'] = apply_calibration(raw['temp'], 1.02)
    calibrated['pressure'] = apply_calibration(raw['pressure'], 0.99)
    calibrated['vibration'] = apply_calibration(raw['vibration'], 1.15)
    
    # Dead code branch - misleading
    if len(calibrated['temp']) > 10:
        calibrated['temp'].append(999.9)
    
    return calibrated

def generate_checksum(label):
    # Unused cryptographic-style distractor
    chk = 0
    for c in label:
        chk ^= ord(c) << (len(label) % 4)
    return chk % 1000

def filter_outliers(stream, limit=0.15):
    mean_val = sum(stream) / len(stream)
    return [x for x in stream if abs(x - mean_val) / mean_val < limit]

def normalize_series(seq):
    min_val, max_val = min(seq), max(seq)
    if max_val == min_val:
        return [0.0] * len(seq)
    return [(x - min_val) / (max_val - min_val) for x in seq]

def aggregate_diagnostics(metrics):
    # Complex but partially irrelevant aggregation
    scores = {}
    for k, v in metrics.items():
        if k == 'temp':
            scores['t_score'] = sum(v) / len(v)
        elif k == 'pressure':
            scores['p_score'] = max(v) - min(v)
        elif k == 'vibration':
            scores['v_score'] = sum(x**2 for x in v)
    return scores

def encrypt_sequence(keys):
    # Bit manipulation red herring
    result = 0
    for k in keys:
        result ^= hash(k) & 0xFFFF
    return result >> 4

def process_metrics(data, cfg):
    interim = {}
    
    # Step 1: Normalize each sensor stream
    for sensor, readings in data.items():
        interim[sensor] = normalize_series(readings)
    
    # Step 2: Filter vibration outliers (relevant)
    interim['vibration'] = filter_outliers(interim['vibration'], 0.25)
    
    # Step 3: Apply weighting using lambda map (actual use)
    weight_map = {'temp': 0.4, 'pressure': 0.3, 'vibration': 0.3}
    weighted_avg = sum(
        weight_map[key] * sum(vals) / len(vals)
        for key, vals in interim.items()
        if key in weight_map
    )
    
    # Step 4: Additional processing chain
    anomaly_flags = {}
    for s, rs in data.items():
        threshold = cfg.get(f'{s}_thresh', 0)
        anomaly_flags[s] = len(detect_anomalies(rs, threshold))
    
    # Misleading entropy calculation (dead end)
    _entropy_probe = {k: compute_entropy(v) for k, v in data.items()}
    
    # Final diagnostic computed from weighted average and anomaly count
    total_anomalies = sum(anomaly_flags.values())
    adjustment_factor = 1 - (total_anomalies * 0.05)
    raw_diagnostic = weighted_avg * 100
    
    # Critical assignment
    final_diagnostic = int(round(raw_diagnostic * adjustment_factor))
    
    # Decoy assignments to mislead
    final_diagnostic_tmp = encrypt_sequence(list(data.keys()))
    final_diagnostic_bak = generate_checksum('system_diagnostic_core')
    
    return final_diagnostic

# Irrelevant global constants
MAX_BUFFER_SIZE = 4096
PROTOCOL_VERSION = '2.1.7'
ACTIVE_MODULES = ['sensor_io', 'calib_engine', 'logger_v3']

# Configuration with decoy fields
config = {
    'sampling_rate': 5,
    'temp_thresh': 26.0,
    'pressure_thresh': 103.0,
    'vibration_thresh': 0.10,
    'debug_mode': False,
    'checksum_required': True,
    'retry_limit': 3
}

# Main execution flow
raw_data = collect_sensor_data()
transformed_data = transform_readings(raw_data)
final_diagnostic = process_metrics(transformed_data, config)

# Output target variable
print(f"Result: {final_diagnostic}")