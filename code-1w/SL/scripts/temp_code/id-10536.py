import math

def analyze_signal_strength(signal, noise_floor):
    # Irrelevant helper function (dead code path)
    return int((signal - noise_floor) * 1.5)

def validate_checksum(data):
    # Unused validation logic (distractor)
    checksum = 0
    for b in data:
        checksum ^= b
    return checksum == 0

def decode_payload(payload):
    # Complex but irrelevant transformation (red herring)
    decoded = []
    shift = len(payload) % 7
    for i, val in enumerate(payload):
        if i % 3 == 0:
            decoded.append((val >> shift) ^ 0xA)
        else:
            decoded.append(val + (i % 5))
    return decoded

def compute_entropy(values):
    # Misleading statistical computation (intermediate distractor)
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def filter_anomalies(records, limit=100):
    # Dead-end filtering with unused parameters
    anomalies = []
    upper_bound = limit * 1.3
    lower_bound = limit * 0.4
    for r in records:
        if r < lower_bound or r > upper_bound:
            anomalies.append(r)
    return anomalies  # Never used in main flow

def aggregate_diagnostics(metrics, config):
    # Core processing chain - relevant but mixed with noise
    base_score = config.get('base_score', 10)
    multiplier = config.get('multiplier', 1.0)
    offset = config.get('offset', 0)
    
    temp_adjustment = 0
    for k, v in metrics.items():
        if 'temp' in k and v > 40:
            temp_adjustment += v // 10
    
    # Real computation buried in noise
    raw_total = sum(v for v in metrics.values() if isinstance(v, int))
    adjustment_factor = max(1, int(multiplier * 10))
    adjusted_total = (raw_total + offset) * adjustment_factor
    
    # Decoy dictionary operations
    decoy_map = {i: chr(65 + (i % 26)) for i in range(15)}
    decoy_map.update({20: 'Z', 25: 'X'})
    decoy_map.pop(5, None)
    
    return adjusted_total - (temp_adjustment * 2)

def process_metrics(log_entries, thresholds):
    cumulative = 0
    state_log = []
    
    for entry in log_entries:
        # Conditional expression usage (required)
        severity = 'high' if entry['error_count'] > thresholds['error'] else 'normal'
        priority_flag = 1 if severity == 'high' else 0
        
        # Dictionary operation with conditional update
        stats = {
            'latency': entry.get('latency', 0),
            'temp_peak': entry.get('temp_max', 30),
            'retry_count': entry.get('retries', 0)
        }
        
        if stats['latency'] > thresholds['latency']:
            stats['latency_adj'] = int(stats['latency'] * 0.75)
        else:
            stats['latency_adj'] = stats['latency']
        
        # Real contribution to result
        score_component = stats['latency_adj'] + stats['retry_count']
        if priority_flag:
            score_component *= 2
        
        cumulative += score_component
        state_log.append(priority_flag)
        
        # Early termination red herring (never triggered due to data)
        if cumulative > 10000:
            break
    
    # Key dictionary operation (required)
    summary = {flag: state_log.count(flag) for flag in (0, 1)}
    high_severity_count = summary.get(1, 0)
    
    # Final aggregation using helper
    config = {
        'base_score': 5,
        'multiplier': 1.2,
        'offset': high_severity_count * 3
    }
    auxiliary_metrics = {
        'temp_zone1': 45,
        'temp_zone2': 52,
        'cycles_completed': 88,
        'voltage_stable': 1
    }
    bonus = aggregate_diagnostics(auxiliary_metrics, config)
    
    # Actual answer computation
    final_value = cumulative + bonus - (high_severity_count * 5)
    
    # Unused sorting distraction
    sorted_logs = sorted(state_log, reverse=True)
    median_flag = sorted_logs[len(sorted_logs)//2] if sorted_logs else 0
    
    return final_value

# Main execution block
if __name__ == '__main__':
    # Simulated sensor log data
    log_data = [
        {'timestamp': 1678886400, 'latency': 120, 'error_count': 3, 'temp_max': 48, 'retries': 2},
        {'timestamp': 1678886401, 'latency': 85, 'error_count': 0, 'temp_max': 42, 'retries': 0},
        {'timestamp': 1678886402, 'latency': 200, 'error_count': 5, 'temp_max': 55, 'retries': 4},
        {'timestamp': 1678886403, 'latency': 95, 'error_count': 1, 'temp_max': 39, 'retries': 1},
        {'timestamp': 1678886404, 'latency': 300, 'error_count': 6, 'temp_max': 60, 'retries': 6}
    ]
    
    # Threshold configuration
    system_thresholds = {
        'latency': 100,
        'error': 2
    }
    
    # Irrelevant data structures (distractors)
    network_trace = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E]
    decoded = decode_payload(network_trace)
    signal_metric = analyze_signal_strength(87, 45)
    entropy_val = compute_entropy(decoded)
    
    # Critical assignment
    final_diagnostic = process_metrics(log_data, system_thresholds)
    
    # Output requirement
    print(f"Target result: {final_diagnostic}")