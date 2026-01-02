from collections import defaultdict, Counter

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_streams = {
        'temp': [23.5, 24.1, 22.9, 25.0, 23.8],
        'humidity': [45, 47, 50, 44, 46],
        'co2': [410, 425, 405, 430, 395],
        'pm25': [12, 15, 11, 18, 14]
    }
    
    # Irrelevant transformation (distractor)
    normalized = {}
    for k, v in raw_streams.items():
        avg = sum(v) / len(v)
        normalized[k] = [x - avg for x in v]
    
    # Dead code path (never used)
    def deprecated_filter(x):
        return x if x > 0 else 0
    
    # Actual returned data
    timestamped = [{'t': i, **{k: v[i] for k, v in raw_streams.items()}} for i in range(5)]
    return timestamped

# Misleading auxiliary function (looks important but unused)
def calculate_air_quality_index(pm25, co2):
    return int((pm25 * 1.5) + (co2 / 10))

# Unused statistical helper (red herring)
def rolling_window(data, window_size=3):
    for i in range(len(data) - window_size + 1):
        yield data[i:i + window_size]

# Core processing with distractors
def analyze_trend(readings, metric):
    values = [r[metric] for r in readings]
    deltas = [values[i+1] - values[i] for i in range(len(values)-1)]
    
    # Distractor variables
    volatility_score = sum(abs(d) for d in deltas) / len(deltas)
    trend_magnitude = sum(deltas)
    
    # Early return red herring (condition never met)
    if len(values) < 2:
        return 0
        
    # Actual logic masked by noise
    increasing = sum(1 for d in deltas if d > 0.5)
    decreasing = sum(1 for d in deltas if d < -0.5)
    return 'up' if increasing > decreasing else 'down'

# Main processing function with multiple distractions
def process_readings(data, config):
    # Initialize various irrelevant accumulators
    diagnostic_log = defaultdict(list)
    anomaly_count = 0
    severity_weight = 0.0
    
    # Real processing begins
    metrics = ['temp', 'humidity', 'co2', 'pm25']
    status = {}
    
    # Complex nested logic with decoy operations
    for metric in metrics:
        values = [d[metric] for d in data]
        current = values[-1]
        historical_avg = sum(values[:-1]) / len(values[:-1]) if len(values) > 1 else current
        
        # Bit manipulation distraction (irrelevant)
        bit_fingerprint = int(current * 10) ^ int(historical_avg * 10)
        bit_fingerprint = (bit_fingerprint << 2) | (bit_fingerprint >> 3)
        
        # String-based red herring
        tag = f"{metric}_v{len(values)}"
        tag_hash = sum(ord(c) for c in tag) % 100
        
        # Actual threshold check hidden among noise
        threshold = config[metric]
        deviation = abs(current - historical_avg)
        
        # Multiple conditions with one actually mattering
        if current > threshold['max']:
            level = 'critical'
        elif current < threshold['min']:
            level = 'warning'
        else:
            trend = analyze_trend(data, metric)  # Called but result not fully used
            if trend == 'up' and deviation > 1.0:
                level = 'elevated'
            else:
                level = 'normal'
        
        status[metric] = level
        diagnostic_log[metric].append(level)
        
        # Decoy aggregation
        if level == 'critical':
            severity_weight += 3.0
        elif level == 'warning':
            severity_weight += 1.5
        
    # Irrelevant counter operation
    log_counter = Counter([s for sublist in diagnostic_log.values() for s in sublist])
    dominant_status = log_counter.most_common(1)[0][0] if log_counter else 'unknown'
    
    # Critical computation buried in distractions
    critical_count = sum(1 for s in status.values() if s == 'critical')
    elevated_count = sum(1 for s in status.values() if s == 'elevated')
    
    # Real answer calculation (obscured)
    base_score = 100
    base_score -= critical_count * 25      # Penalty for critical
    base_score -= elevated_count * 8       # Smaller penalty
    
    # Integer division and rounding distraction
    if base_score > 0:
        adjusted = (base_score // 7) * 3
        final_diagnostic = int(round(base_score - (adjusted * 0.4)))
    else:
        final_diagnostic = -100
    
    # Dead code branch (never reached due to logic above)
    if dominant_status == 'unknown':
        final_diagnostic = 0
    
    # One more red herring
    checksum = sum(len(str(v)) for v in config.values().popitem()[1].values())
    
    return final_diagnostic

# Configuration with misleading structure
thresholds = {
    'temp': {'min': 20, 'max': 24},
    'humidity': {'min': 30, 'max': 50},
    'co2': {'min': 350, 'max': 420},
    'pm25': {'min': 5, 'max': 15}
}

# Collect real data
sensor_data = collect_sensor_data()

# Process through main pipeline
final_diagnostic = process_readings(sensor_data, thresholds)

# Output the target result
print(f"Target result: {final_diagnostic}")