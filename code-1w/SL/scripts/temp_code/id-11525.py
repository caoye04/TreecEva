import math

# Simulated agricultural cluster data with sensor readings
def generate_irrelevant_metrics():
    return {"vibration": 0.87, "humidity_drift": 2.3, "noise_floor": 41}

def parse_sensor_string(raw):    
    parts = raw.split('|')
    parsed = {}
    for p in parts:
        k, v = p.split(':')
        parsed[k] = float(v)
    return parsed

def decode_legacy_format(code):
    # Decoding logic irrelevant to final result
    base = int(code[:3])
    offset = sum([ord(c) for c in code[3:]]) % 100
    return base + offset

def compute_buffer_score(sequence):
    # Dead-end computation
    score = 0
    for i, val in enumerate(sequence):
        if i % 2 == 0:
            score += val * 1.5
        else:
            score -= val // 2
    return score

def filter_outliers(data_list, threshold=3.0):
    mean_val = sum(data_list) / len(data_list)
    std_dev = (sum((x - mean_val) ** 2 for x in data_list) / len(data_list)) ** 0.5
    return [x for x in data_list if abs(x - mean_val) <= threshold * std_dev]

def transform_readings(readings):
    # Real transformation used later
    adjusted = []
    for r in readings:
        if r < 50:
            adjusted.append(r * 1.8)
        elif r < 100:
            adjusted.append(r * 1.3)
        else:
            adjusted.append(r * 0.9)
    return adjusted

def calculate_cluster_entropy(values):
    # Distractor function: not used in final path
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

def detect_synchronization_peaks(timing_log):
    peaks = []
    for i in range(1, len(timing_log) - 1):
        if timing_log[i] > timing_log[i-1] and timing_log[i] > timing_log[i+1]:
            peaks.append(i)
    return peaks

def calculate_harvest_efficiency(data, cfg):
    # Core logic begins
    raw_readings = data['readings']
    valid_readings = filter_outliers(raw_readings)
    processed = transform_readings(valid_readings)
    
    # Summation with conditional scaling based on configuration
    base_accum = 0
    for idx, value in enumerate(processed):
        if idx in cfg['boost_indices']:
            base_accum += value * cfg['boost_factor']
        else:
            base_accum += value
    
    # Use of zip: pairing with auxiliary metadata that has partial relevance
    aux_weights = [1.0, 0.95, 0.9, 0.85, 0.8]
    weighted_sum = 0
    for val, weight in zip(processed[:5], aux_weights):
        weighted_sum += val * weight
    
    # Final efficiency combines both accumulation methods under condition
    if cfg['use_weighted']:
        efficiency = weighted_sum * cfg['efficiency_curve'][len(processed)]
    else:
        efficiency = base_accum * 0.75
    
    # Additional adjustment using string method distraction
    tag = data['tag'].strip().upper()
    if 'URGENT' in tag:
        efficiency *= 1.1
    
    return int(efficiency)

# Main execution block
if __name__ == '__main__':
    # Irrelevant initialization
    sys_metrics = generate_irrelevant_metrics()
    legacy_code = "450XZY"
    decoded_val = decode_legacy_format(legacy_code)
    
    # Actual input data
    cluster_data = {
        'readings': [45, 67, 89, 120, 43, 76, 95, 134, 52],
        'tag': 'CLUSTER|A|NORMAL|zone:7',
        'timestamp': '2023-11-05T08:45:12'
    }
    
    # Configuration with red herring fields
    config = {
        'boost_indices': [0, 2, 4],
        'boost_factor': 1.4,
        'use_weighted': True,
        'efficiency_curve': {
            7: 0.82,
            8: 0.85,
            9: 0.88  # matches length of processed list
        },
        'calibration_mode': False,
        'log_verbosity': 3
    }
    
    # Buffer score calculation - dead end
    dummy_seq = [10, 20, 30, 40]
    buffer_result = compute_buffer_score(dummy_seq)
    
    # Entropy calculation - unused
    entropy = calculate_cluster_entropy(cluster_data['readings'])
    
    # Synchronization detection - irrelevant
    timing_log = [1.2, 3.4, 2.8, 4.5, 3.9, 2.1]
    sync_peaks = detect_synchronization_peaks(timing_log)
    
    # String parsing distractor
    raw_sensor_str = "temp:23.5|pressure:1013.2|flow:87.3|status:OK"
    sensor_dict = parse_sensor_string(raw_sensor_str)
    
    # Critical statement
    final_yield = calculate_harvest_efficiency(cluster_data, config)
    
    # Output result as required
    print(f"Target result: {final_yield}")