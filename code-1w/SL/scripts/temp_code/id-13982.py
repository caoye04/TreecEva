import math

# Simulated system telemetry and configuration
def collect_telemetry():
    raw_signals = [0.88, 0.92, 0.76, 0.81, 0.94]
    weights = [0.2, 0.3, 0.15, 0.1, 0.25]
    weighted_sum = sum(s * w for s, w in zip(raw_signals, weights))
    return {'base_metric': weighted_sum, 'anomalies': 2, 'version': 'v2.1'}

def deprecated_normalization(x):
    # Obsolete function - not used in current logic
    return (x - min(x)) / (max(x) - min(x)) if max(x) != min(x) else [0] * len(x)

def extract_features(log_str: str) -> dict:
    lines = log_str.strip().split('\n')
    feature_map = {}
    for line in lines:
        if ':' in line:
            k, v = line.split(':', 1)
            feature_map[k.strip()] = v.strip()
    
    # Distractor: irrelevant parsing logic
    if 'ERROR' in feature_map.get('status', ''):
        feature_map['severity'] = 'high'
    elif 'WARN' in feature_map.get('status', ''):
        feature_map['severity'] = 'medium'
    else:
        feature_map['severity'] = 'low'
    
    # Actual needed data
    feature_map['duration_ms'] = int(feature_map.get('duration_ms', 0))
    feature_map['retry_count'] = int(feature_map.get('retry_count', 0))
    return feature_map

def calculate_entropy(data: list) -> float:
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 4)

def bitwise_flag_check(code: int) -> bool:
    # Check if bits 3 and 5 are set (irrelevant to final result)
    return (code & (1 << 3)) and (code & (1 << 5))

def validate_checksum(token: str) -> bool:
    # Dummy checksum validation (not actually used)
    if not token.isdigit():
        return False
    digits = list(map(int, token))
    return sum(digits) % 7 == 0

def transform_payload(payload: dict) -> dict:
    # Irrelevant transformation chain
    temp = {}
    for k, v in payload.items():
        if isinstance(v, str):
            temp[f'encoded_{k}'] = v.upper().replace(' ', '_')
        else:
            temp[f'scaled_{k}'] = v * 1.05
    
    # Nested dictionary manipulation (mostly red herring)
    temp['meta'] = {
        'version': 'alpha',
        'flags': [True, False, True],
        'debug_mode': False
    }
    
    # One actual useful field
    if 'raw_value' in payload:
        temp['adjusted_value'] = payload['raw_value'] * 0.9
    
    return temp

def evaluate_performance(metrics: dict, config: dict) -> int:
    base = metrics['base_metric']
    duration = metrics.get('duration_ms', 0)
    retries = metrics.get('retry_count', 0)
    anomalies = metrics.get('anomalies', 0)
    
    # Real computation begins
    score = int(base * 100)
    
    # Penalty for long duration
    if duration > 500:
        score -= 15
    elif duration > 200:
        score -= 5
    
    # Penalty for retries
    score -= retries * 10
    
    # Bonus for low anomalies
    if anomalies == 0:
        score += 20
    elif anomalies < 3:
        score += 5
    else:
        score -= anomalies * 3
    
    # Conditional multiplier based on config mode
    mode = config.get('mode', 'balanced')
    multipliers = {'aggressive': 1.2, 'balanced': 1.0, 'conservative': 0.85}
    score = int(score * multipliers.get(mode, 1.0))
    
    # Bitwise trick: flip every odd bit in the lower byte of score
    # Only affects final result in specific cases
    lower_byte = score & 0xFF
    flipped = 0
    for i in range(8):
        if i % 2 == 1:  # Odd bit positions (1,3,5,7)
            flipped |= ((lower_byte >> i) & 1) << i
        else:
            flipped |= ((~lower_byte >> i) & 1) << i
    score = (score & 0xFFFFFF00) | flipped
    
    # Final adjustment based on string pattern in metadata
    meta_str = config.get('description', '')
    if 'legacy' in meta_str.lower():
        score -= 10
    if 'optimized' in meta_str.lower() and 'v2' in meta_str:
        score += 15
    
    return score

# --- Main Execution ---
if __name__ == '__main__':
    # Collect real metric data
    metric_data = collect_telemetry()
    
    # Parse auxiliary log data (only some fields matter)
    log_text = '''
    status: OK
    duration_ms: 320
    retry_count: 1
    timestamp: 2023-09-15T10:30:45
    source: sensor_array_7
    '''
    parsed_log = extract_features(log_text)
    metric_data.update(parsed_log)
    
    # Configuration with mixed relevance
    user_config = {
        'mode': 'aggressive',
        'timeout_sec': 30,
        'retries_allowed': True,
        'description': 'System profile: optimized pathfinding v2.1',
        'flags': { 'enable_cache': True, 'strict_mode': False },
        'thresholds': [0.5, 0.75, 0.9]
    }
    
    # Transform dummy payload (distractor)
    dummy_payload = {
        'raw_value': 42,
        'label': 'test_entry',
        'priority': 3
    }
    transformed = transform_payload(dummy_payload)
    
    # Calculate entropy of signal distribution (unused but computed)
    signals = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    signal_entropy = calculate_entropy(signals)
    
    # Validate token (irrelevant to main logic)
    api_token = "1234567"
    is_valid = validate_checksum(api_token)
    
    # Bit check on arbitrary code (dead end)
    flag_state = bitwise_flag_check(0b101100)
    
    # --- KEY STATEMENT ---
    final_score = evaluate_performance(metric_data, user_config)
    
    # Print result as required
    print(f"Target result: {final_score}")