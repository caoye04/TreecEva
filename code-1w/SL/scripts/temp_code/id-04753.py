import math

def analyze_signal_strength(signal, noise):
    """Irrelevant helper function for signal processing distractions."""
    snr = 10 * math.log10(sum(s**2 for s in signal) / sum(n**2 for n in noise))
    return round(snr, 2)

def compute_checksum(data):
    """Unused checksum function — red herring."""
    chk = 0
    for d in data:
        chk ^= hash(str(d)) % 256
    return chk

def evaluate_thresholds(values, limit=100):
    """Dead code path — never called in execution."""
    above = [v for v in values if v > limit]
    return len(above)

def filter_outliers(dataset, factor=1.5):
    """Decoy function: looks important but not used in main logic."""
    q1 = sorted(dataset)[len(dataset)//4]
    q3 = sorted(dataset)[3*len(dataset)//4]
    iqr = q3 - q1
    low_bound = q1 - factor * iqr
    high_bound = q3 + factor * iqr
    return [x for x in dataset if low_bound <= x <= high_bound]

def normalize_readings(readings):
    min_val, max_val = min(readings), max(readings)
    return [(r - min_val) / (max_val - min_val) if max_val != min_val else 0 for r in readings]

def aggregate_diagnostics(metrics):
    trend = sum(1 for i in range(1, len(metrics)) if metrics[i] > metrics[i-1])
    volatility = sum(abs(metrics[i] - metrics[i-1]) for i in range(1, len(metrics)))
    baseline = sum(metrics) / len(metrics)
    adjusted_score = baseline * (1 + volatility / 100) - (trend * 0.5)
    return round(adjusted_score, 4)

def process_metrics(log_data, config):
    # Normalize sensor inputs
    normalized = normalize_readings([entry['reading'] for entry in log_data])
    
    # Extract timestamps and categorize by period
    recent_entries = [e for e in log_data if e['timestamp'] > config['window']]
    peak_readings = [e['reading'] for e in log_data if e['reading'] >= config['peak_threshold']]
    
    # Compute weighted diagnostic index
    weights = [1.0, 0.8, 0.6, 0.4, 0.2][:len(recent_entries)]
    weighted_sum = sum(entry['reading'] * w for entry, w in zip(reversed(recent_entries), weights))
    
    # Simulate historical comparison (irrelevant to final result)
    historical_avg = sum(e['reading'] for e in log_data[:-3]) / len(log_data[:-3]) if len(log_data) > 3 else 0
    deviation = abs(weighted_sum - historical_avg)
    
    # Apply false alarm risk adjustment (unused branch)
    risk_factor = 0
    if len(peak_readings) > 4:
        risk_factor = 0.9
    elif len(peak_readings) > 2:
        risk_factor = 0.6
    else:
        risk_factor = 0.2  # This is computed but never used
    
    # Critical calculation chain begins here
    raw_index = aggregate_diagnostics([n * 100 for n in normalized])
    scaling_factor = math.sin(math.pi / len(log_data)) if len(log_data) > 0 else 0
    intermediate = raw_index * (scaling_factor or 0.5)
    
    # Conditional override based on decoy condition
    if any('error' in str(e.get('status', '')) for e in log_data):
        intermediate *= 0.1  # Never triggers — no 'error' status in data
    
    # Final computation with distractor variables
    offset = sum(1 for e in log_data if e['reading'] < config['baseline']) * 0.01
    adjustment = math.log(len(log_data) + 1, 2) if len(log_data) > 0 else 0
    final_diagnostic = intermediate + offset - adjustment
    
    # Print irrelevant statistics (distraction)
    print(f'Data points: {len(log_data)}, Peaks detected: {len(peak_readings)}')
    print(f'Checksum (unused): {compute_checksum(log_data)}')
    return round(final_diagnostic, 6)

# Irrelevant global constants (distractors)
MAX_BUFFER_SIZE = 1024
DEFAULT_TIMEOUT = 30
DEBUG_MODE = False

# Main execution block
if __name__ == '__main__':
    # Simulated telemetry log from environmental sensors
    sensor_log = [
        {'timestamp': 10, 'reading': 12.5, 'source': 'A1'},
        {'timestamp': 25, 'reading': 14.2, 'source': 'A2'},
        {'timestamp': 40, 'reading': 13.8, 'source': 'A3'},
        {'timestamp': 55, 'reading': 16.1, 'source': 'A4'},
        {'timestamp': 70, 'reading': 15.3, 'source': 'A5'},
        {'timestamp': 85, 'reading': 17.9, 'source': 'A6'},
        {'timestamp': 100, 'reading': 18.2, 'source': 'A7'},
        {'timestamp': 115, 'reading': 19.0, 'source': 'A8'}
    ]
    
    # Configuration with misleading parameters
    threshold_config = {
        'window': 50,
        'peak_threshold': 17.0,
        'baseline': 15.0,
        'critical_level': 20.0  # Unused in logic
    }
    
    # Execute main processing step
    final_diagnostic = process_metrics(sensor_log, threshold_config)
    
    # Output target result
    Target result: {final_diagnostic}