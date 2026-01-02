import math

# Simulated system telemetry data with mixed signal types
def collect_telemetry():
    signals = [
        {'id': 'S1', 'type': 'voltage', 'readings': [3.2, 3.5, 3.1, 2.9, 3.6]},
        {'id': 'S2', 'type': 'temperature', 'readings': [45, 47, 44, 50, 46]},
        {'id': 'S3', 'type': 'voltage', 'readings': [3.0, 3.3, 3.1, 3.4, 3.2]}
    ]
    return signals

# Legacy function - unused but looks relevant
def analyze_signal_legacy(signal):
    avg = sum(signal['readings']) / len(signal['readings'])
    peak = max(signal['readings'])
    return {'avg': avg, 'peak': peak, 'status': 'legacy_ok'}

# Signal normalization (distraction)
def normalize_readings(signal_list):
    normalized = []
    for s in signal_list:
        factor = 1.0 / max(s['readings']) if max(s['readings']) > 0 else 1.0
        norm_vals = [round(r * factor, 3) for r in s['readings']]
        normalized.append({**s, 'readings': norm_vals})
    return normalized

# Real-time filter stub (dead code path)
def apply_realtime_filter(stream):
    if not stream:
        return []
    filtered = []
    for point in stream:
        if 'quality' in point and point['quality'] < 0.5:
            continue
        filtered.append(point)
    return filtered  # Never actually used

# Core processing pipeline
def extract_diagnostics(signals):
    diagnostics = {}
    for sig in signals:
        readings = sig['readings']
        r_len = len(readings)
        mid = r_len // 2
        left_half = readings[:mid] or [0]
        right_half = readings[mid:] or [0]
        
        # Compute inter-quartile trend (relevant)
        trend = (sum(right_half) - sum(left_half)) / r_len
        
        # Variance-based stability index
        mean_val = sum(readings) / r_len
        variance = sum((x - mean_val) ** 2 for x in readings) / r_len
        stability = round(1 / (1 + variance), 3)
        
        # Masked bit-score for anomaly (bit manipulation red herring)
        anomaly_score = 0
        for val in readings:
            shifted = int(val * 10) << 2
            masked = shifted & 0xFF
            anomaly_score ^= masked  # XOR accumulation - looks important
        
        diagnostics[sig['id']] = {
            'trend': trend,
            'stability': stability,
            'raw_anomaly_hint': anomaly_score  # Distractor
        }
    return diagnostics

# Unused auxiliary transform (misleading)
def frequency_shift(data_map):
    shifted = {}
    for k, v in data_map.items():
        shift_val = v.get('trend', 0) * 1.5
        shifted[k] = {**v, 'shift': shift_val}
    return shifted

# Log generation with metadata decoys
def generate_logs(diag_data):
    logs = []
    timestamp = 1000
    for sid, metrics in diag_data.items():
        entry = {
            'log_id': f'L-{sid}',
            'timestamp': timestamp,
            'metrics': metrics,
            'context': {
                'location': 'NODE_UNKNOWN',
                'priority': 3,
                'version': '2.1.0'
            },
            'debug_payload': f"<encrypted>{sid[::-1]}{len(metrics)}"  # Obfuscation red herring
        }
        logs.append(entry)
        timestamp += 10
    return logs

# Threshold configuration with irrelevant fields
def get_system_thresholds():
    return {
        'voltage': {'min': 2.8, 'max': 3.6, 'weight': 0.7},
        'temperature': {'min': 40, 'max': 50, 'weight': 0.9},
        'default': {'min': 0, 'max': 1, 'weight': 0.5},
        'legacy_mode': False,
        'calibration_offset': 0.034,
        'timeout_grace_period': 150
    }

# Main processing with dictionary operations and lambda folding
def process_metrics(logs, thresholds):
    # Extract relevant metric trends using dictionary comprehension
    trend_values = [
        log['metrics']['trend'] 
        for log in logs 
        if 'metrics' in log and 'trend' in log['metrics']
    ]
    
    # Stability map via lambda and enumerate (actual relevance)
    stability_list = [
        log['metrics']['stability'] 
        for log in logs
    ]
    indexed_stability = {
        i: val for i, val in enumerate(stability_list)
    }
    
    # Weighted fusion using zip and lambda (key step)
    weights = [0.6, 0.3, 0.1][:len(trend_values)]
    weighted_trend = sum(
        w * t for w, t in zip(weights, trend_values)
    )
    
    # Phantom correlation check (distractor)
    correlations = []
    for i in range(len(trend_values) - 1):
        corr = trend_values[i] * trend_values[i+1]
        correlations.append(abs(corr) > 0.5)
    phantom_flag = any(correlations)  # Looks important, unused
    
    # Hidden aggregation: product of non-zero stabilities (answer source)
    non_zero_stabilities = [s for s in stability_list if s > 0]
    if not non_zero_stabilities:
        base_score = 0
    else:
        base_score = 1
        for s in non_zero_stabilities:
            base_score *= s  # Multiplicative chain
        base_score = round(base_score, 6)
    
    # Decoy calculation using raw_anomaly_hint (misleading)
    total_hint = 0
    for log in logs:
        total_hint += log['metrics'].get('raw_anomaly_hint', 0)
    security_checksum = total_hint % 97  # Looks critical, unused
    
    # Final diagnostic computed from stability product
    final_score = int(round(base_score * 10000))
    
    # UNUSED: complex fallback logic (dead path)
    def deep_recheck():
        return sum(trend_values) * 1000 if len(trend_values) > 1 else -999
    
    return final_score

# Orchestration sequence
if __name__ == '__main__':
    # Step 1: Collect raw signals
    raw_signals = collect_telemetry()
    
    # Step 2: Normalize signals (irrelevant to final result)
    normalized_signals = normalize_readings(raw_signals)
    
    # Step 3: Extract core diagnostics
    diagnostics = extract_diagnostics(normalized_signals)
    
    # Step 4: Generate structured logs
    log_entries = generate_logs(diagnostics)
    
    # Step 5: Load system thresholds
    system_thresholds = get_system_thresholds()
    
    # Step 6: Process metrics into final diagnostic
    final_diagnostic = process_metrics(log_entries, system_thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")