from collections import defaultdict

# Simulate system performance metrics with noise and irrelevant data
def collect_diagnostics():
    raw_data = [
        'cpu_temp: 72', 'gpu_temp: 68', 'fan_speed: 2200',
        'disk_read: 140MB/s', 'disk_write: 95MB/s',
        'latency_spike: true', 'retry_count: 3'
    ]
    
    diagnostics = defaultdict(float)
    for entry in raw_data:
        if ':' in entry:
            key, val = entry.split(':', 1)
            key = key.strip()
            val = val.strip()
            if val.replace('.', '').isdigit():
                diagnostics[key] = float(val)
    
    # Irrelevant transformations (distraction)
    temp_ratio = diagnostics['cpu_temp'] / (diagnostics['gpu_temp'] + 1)
    diagnostics['overclock_factor'] = temp_ratio * 1.2
    diagnostics['baseline_stability'] = 0.87
    
    return dict(diagnostics)

# Parse configuration with red herrings
def load_config():
    config_lines = """
    timeout=30;
    retries=3;
    mode=aggressive;
    debug_log=true;
    cache_ttl=120;
    """
    
    config = {}
    for line in config_lines.strip().split(';'):
        if '=' in line:
            k, v = line.split('=', 1)
            config[k.strip()] = v.strip()
    
    # Decoy calculations
    if config.get('debug_log') == 'true':
        log_volume = 1024 * 16
        buffer_size = log_volume // 8
    
    config['threshold_adjustment'] = 1.15  # unused later
    return config

# Signal processing with multiple distractions
def preprocess_signal(raw_samples):
    processed = []
    noise_floor = 0.05
    for sample in raw_samples:
        cleaned = abs(sample) ** 0.5
        if cleaned > noise_floor:
            processed.append(cleaned * 1.03)
    
    # Dead code path (never executed due to logic)
    if len(processed) > 1000:
        downsampled = processed[::2]
        return downsampled
    
    # Distractor: complex but unused calculation
    spectral_density = sum(p**2 for p in processed) / len(processed) if processed else 0
    peak_to_avg = max(processed) / (sum(processed)/len(processed)) if processed else 0
    
    return processed

# Core evaluation logic buried among decoys
def calculate_health_factor(stats):
    base = stats.get('disk_read', 0) * 0.4
    penalty = stats.get('retry_count', 0) * 15
    bonus = 10 if stats.get('latency_spike') == 'true' else 0  # string comparison trap
    
    # Misleading intermediate
    dummy_metric = (base - penalty + bonus) % 7
    
    # Actual health signal
    temperature_risk = 1 if stats.get('cpu_temp', 0) > 70 else 0
    return base - penalty - temperature_risk * 5

# Main scoring logic with tuple unpacking and distractors
def evaluate_performance(metrics, weights):
    # Unpack relevant metrics with destructuring
    keys = ['disk_read', 'disk_write', 'cpu_temp']
    vals = [metrics.get(k, 0) for k in keys]
    read_spd, write_spd, temp = vals  # tuple unpacking
    
    # Irrelevant list transformation
    speed_pairs = list(zip([read_spd]*3, [write_spd]*3))
    avg_pair = sum(a + b for a, b in speed_pairs) / len(speed_pairs) if speed_pairs else 0
    
    # Real computation hidden among distractions
    thermal_throttle = 1.0
    if temp > 75:
        thermal_throttle = 0.8
    elif temp > 70:
        thermal_throttle = 0.9

    # Weighted score calculation (actual answer source)
    weighted_components = [
        read_spd * weights['throughput'] * thermal_throttle,
        write_spd * weights['endurance'],
        (100 - temp) * weights['stability']
    ]
    
    # Decoy aggregation methods
    simple_avg = sum(vals) / len(vals)
    geometric_mean = (read_spd * write_spd * (100-temp)) ** (1/3) if all(vals) else 0
    
    # Final score - the real answer
    final_score = sum(weighted_components) - 20  # fixed adjustment
    
    # Unused complex structure (distractor)
    report_summary = {
        'score_details': {
            'components': weighted_components,
            'throttle': thermal_throttle,
            'raw_metrics': dict(zip(keys, vals))
        },
        'version': '2.1',
        'calibrated': True
    }
    
    return final_score

# Orchestration with early returns and noise
def main():
    # Collect system data
    metrics = collect_diagnostics()
    config = load_config()
    
    # Generate synthetic signal (distraction)
    import math
    samples = [math.sin(i * 0.1) + 0.1*i for i in range(50)]
    filtered = preprocess_signal(samples)
    
    # Fake decision path
    if len(filtered) < 10:
        return -999  # dead path
    
    # Real weights with one unused
    weights = {
        'throughput': 0.6,
        'endurance': 0.3,
        'stability': 0.4,
        'reliability': 0.5  # never used
    }
    
    # Key statement
    final_score = evaluate_performance(metrics, weights)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

if __name__ == '__main__':
    main()