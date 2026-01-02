from collections import defaultdict, Counter
import itertools

# Simulated sensor data: timestamp -> readings (temperature, pressure, vibration)
sensor_readings = [
    (1000, 36.8, 101.3, 0.45), (1001, 37.1, 101.2, 0.47), (1002, 37.3, 100.9, 0.53),
    (1003, 38.0, 100.7, 0.61), (1004, 38.2, 100.8, 0.72), (1005, 38.5, 101.0, 0.85),
    (1006, 38.7, 101.4, 0.93), (1007, 39.0, 101.5, 1.05), (1008, 39.2, 101.6, 1.20),
    (1009, 39.5, 101.7, 1.35), (1010, 39.8, 101.8, 1.50)
]

# Irrelevant baseline for distraction
baseline_stats = {'avg_temp': 37.0, 'std_dev': 0.8, 'outlier_count': 0}

# Extract time series
timestamps = [r[0] for r in sensor_readings]
temperatures = [r[1] for r in sensor_readings]
pressures = [r[2] for r in sensor_readings]
vibrations = [r[3] for r in sensor_readings]

# Distractor: unused transformation
delayed_vibrations = [0] * 3 + vibrations[:-3]  # Shifted by 3

# Real-time anomaly scoring (used)
def compute_anomaly_score(vibration, temp, base_threshold=0.5):
    return (vibration / base_threshold) * (1 + (temp - 37.0) / 10)

# Irrelevant helper (dead code path)
def deprecated_normalization(x, axis=0):
    return [val / max(x) for val in x]

# Core processing
health_data = defaultdict(list)
for t, temp, p, vib in sensor_readings:
    health_data['times'].append(t)
    health_data['metrics'].append((temp, p, vib))
    health_data['scores'].append(compute_anomaly_score(vib, temp))

# Threshold configuration (key input)
thresholds = {
    'fever': 38.0,
    'pressure_drop': 101.0,
    'vibration_rising': 0.8,
    'score_spike': 1.5
}

# Misleading aggregation (unused but plausible)
spike_windows = list(itertools.pairwise([int(s > thresholds['score_spike']) for s in health_data['scores']]))
duplicate_pairs = [pair for pair in spike_windows if pair[0] == pair[1]]

# Actual processing function
def process_metrics(data, config):
    critical_events = 0
    warning_events = 0
    score_history = data['scores']
    metric_snapshots = data['metrics']
    
    # Unused slicing distraction
    mid_window = score_history[3:-3] if len(score_history) > 6 else score_history
    
    # Main logic chain
    for idx, ((temp, press, vib), score) in enumerate(zip(metric_snapshots, score_history)):
        triggered = []
        
        # Condition 1: fever check
        if temp >= config['fever']:
            triggered.append('fever')
            
        # Condition 2: pressure drop
        if press < config['pressure_drop']:
            triggered.append('pressure')
            
        # Condition 3: vibration rising beyond threshold
        if vib > config['vibration_rising']:
            triggered.append('vibration')
            
        # Condition 4: anomaly score spike
        if score > config['score_spike']:
            triggered.append('anomaly')

        # Evaluate severity
        if len(triggered) >= 3:
            critical_events += 1
        elif len(triggered) >= 1 and idx % 2 == 0:  # Only even-indexed warnings count
            warning_events += 1
    
    # Secondary analysis: trend consistency
    score_pairs = list(itertools.pairwise(score_history))
    rising_trend = sum(1 for a, b in score_pairs if b > a)
    stable_or_falling = len(score_pairs) - rising_trend
    
    # Distractor: unused pattern counter
    pattern_counter = Counter(['up' if b > a else 'down' for a, b in score_pairs])
    
    # Final diagnostic calculation (this is the answer)
    base_risk = critical_events * 100
    conditional_mod = warning_events * 10
    trend_factor = rising_trend - stable_or_falling  # net upward trend
    
    # Complex composite formula
    final_risk_index = (base_risk + conditional_mod) * (1 + trend_factor * 0.1)
    
    # Additional distractor: entropy calculation (unused)
    all_vals = temperatures + pressures + vibrations
    avg_val = sum(all_vals) / len(all_vals)
    variance = sum((v - avg_val)**2 for v in all_vals) / len(all_vals)
    
    return int(final_risk_index)

# Execute main logic
final_diagnostic = process_metrics(health_data, thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")