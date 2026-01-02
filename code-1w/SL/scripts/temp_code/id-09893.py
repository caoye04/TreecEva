from collections import defaultdict, Counter
import math

# Simulated system telemetry data
def generate_telemetry():
    return [
        ('cpu_load', 0.76), ('memory_usage', 0.45), ('disk_io', 0.33),
        ('cpu_load', 0.81), ('network_latency', 44.2), ('memory_usage', 0.51),
        ('disk_io', 0.41), ('cpu_load', 0.69), ('network_latency', 52.1),
        ('memory_usage', 0.49), ('disk_io', 0.37), ('cpu_load', 0.74)
    ]

def filter_critical(entries, severity_level):
    # Irrelevant filtering function (dead code path)
    return [e for e in entries if isinstance(e[1], float) and e[1] > severity_level]

def compute_rolling_average(data, window=3):
    # Unused rolling average calculation (distractor)
    averages = []
    for i in range(len(data) - window + 1):
        avg = sum([x[1] for x in data[i:i+window]]) / window
        averages.append(avg)
    return averages

def extract_signals(telemetry):
    signals = defaultdict(list)
    for key, value in telemetry:
        signals[key].append(value)
    return signals

def calculate_entropy(values):
    # Decoy entropy function not used in final logic
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def normalize_score(raw, min_val, max_val):
    # Unused normalization utility (red herring)
    return (raw - min_val) / (max_val - min_val) if max_val > min_val else 0.5

def detect_spikes(signal_list, factor=1.5):
    # Calculates volatility but ultimately unused
    mean = sum(signal_list) / len(signal_list)
    std_dev = (sum((x - mean) ** 2 for x in signal_list) / len(signal_list)) ** 0.5
    return [i for i, x in enumerate(signal_list) if abs(x - mean) > factor * std_dev]

def build_threshold_map(signals):
    # Constructs actual thresholds used in analysis
    t_map = {}
    for metric, readings in signals.items():
        base = sum(readings) / len(readings)
        if metric == 'cpu_load':
            t_map[metric] = {'base': base, 'alert': 0.75, 'weight': 3.0}
        elif metric == 'memory_usage':
            t_map[metric] = {'base': base, 'alert': 0.50, 'weight': 2.5}
        elif metric == 'disk_io':
            t_map[metric] = {'base': base, 'alert': 0.35, 'weight': 1.8}
        elif metric == 'network_latency':
            t_map[metric] = {'base': base, 'alert': 50.0, 'weight': 2.0}
    return t_map

def assess_anomalies(signals, thresholds):
    anomalies = defaultdict(int)
    for metric, values in signals.items():
        if metric not in thresholds:
            continue
        alert_level = thresholds[metric]['alert']
        for val in values:
            if val > alert_level:
                anomalies[metric] += 1
    return anomalies

def derive_stability_index(anomaly_count, total_entries):
    # Stability index - misleading intermediate result
    penalty = sum(anomaly_count.values())
    return round((total_entries - penalty) / total_entries, 4) if total_entries else 0.0

def analyze_metrics(log_entries, threshold_config):
    # Core analysis logic
    cumulative_risk = 0.0
    total_weighted_hits = 0
    
    # Extract relevant metrics
    log_signals = extract_signals(log_entries)
    
    # Assess anomalies per metric
    found_anomalies = assess_anomalies(log_signals, threshold_config)
    
    # Calculate weighted anomaly score
    for metric, counts in found_anomalies.items():
        weight = threshold_config[metric]['weight']
        total_weighted_hits += counts * weight
    
    # Apply non-linear risk scaling
    if total_weighted_hits > 0:
        cumulative_risk = math.log(1 + total_weighted_hits) * 100
    
    # Secondary adjustment based on CPU-memory correlation
    cpu_vals = log_signals['cpu_load']
    mem_vals = log_signals['memory_usage']
    high_cpu_mem_pairs = sum(
        1 for cpu, mem in zip(cpu_vals, mem_vals)
        if cpu > 0.70 and mem > 0.40
    )
    
    if high_cpu_mem_pairs >= 2:
        cumulative_risk *= 1.25  # Correlation bonus multiplier
    
    # Final diagnostic score
    final_score = int(round(cumulative_risk))
    
    # Irrelevant post-processing (distraction)
    diagnostics = []
    if final_score < 50:
        diagnostics.append('GREEN: System stable')
    elif final_score < 100:
        diagnostics.append('YELLOW: Moderate fluctuations')
    else:
        diagnostics.append('RED: High stress detected')
    
    return final_score

# Generate data
raw_log = generate_telemetry()

# Dead code assignments (irrelevant variables)
decoy_signal = compute_rolling_average(raw_log)
entropy_profile = {k: calculate_entropy(v) for k, v in extract_signals(raw_log).items()}

# Build necessary components
system_log = generate_telemetry()
threshold_map = build_threshold_map(extract_signals(system_log))

# Execute main analysis
final_diagnostic = analyze_metrics(system_log, threshold_map)

# Print result
print(f"Result: {final_diagnostic}")