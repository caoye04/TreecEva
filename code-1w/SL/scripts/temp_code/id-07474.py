def analyze_pattern(seq):
    return sum(x * (i + 1) for i, x in enumerate(seq)) if len(seq) > 3 else 0

# Simulated sensor data stream
temp_readings = [23.5, 24.1, 22.8, 25.6, 26.3]
humidity_readings = [45, 48, 50, 55, 60]
pressure_readings = [1013, 1015, 1012, 1010, 1008]

# Irrelevant transformation - red herring
decoy_signal = [abs(x - y) for x, y in zip(temp_readings[::2], temp_readings[1::2])]
scaling_factor = sum(decoy_signal) / (len(decoy_signal) or 1)
scaled_noise = [x * scaling_factor for x in reversed(decoy_signal)]

# Real processing begins
baseline = sum(temp_readings) / len(temp_readings)
anomaly_score = sum(1 for x in temp_readings if abs(x - baseline) > 1.5)

def compute_stability(data):
    diffs = [abs(data[i] - data[i-1]) for i in range(1, len(data))]
    return round(sum(diffs) / len(diffs), 3) if diffs else 0.0

stability_index = compute_stability(temp_readings)

# Conditional expression with string method distraction
status_flag = 'stable' if stability_index < 1.0 else 'volatile'
flag_code = {'stable': 1, 'warning': 2, 'critical': 3}.get(status_flag, 0)

# Dummy function that looks important but isn't used in final path
def calculate_entropy(values):
    from math import log
    total = sum(values)
    probs = [v / total for v in values if v > 0]
    return -sum(p * log(p) for p in probs)

# Data fusion with multiple concepts
fusion_weight = len([x for x in humidity_readings if x > 50])
adjusted_baseline = baseline * (1 + fusion_weight * 0.05)

# String-based decoy
system_log = "ERROR: Calibration failed | WARNING: High variance | INFO: Running diagnostics"
error_count = system_log.count("ERROR")
warning_fragments = [x.strip() for x in system_log.split('|') if 'WARNING' in x]

# Core logic hidden among distractors
health_data = [
    int(adjusted_baseline),
    int(stability_index * 100),
    anomaly_score,
    len(scaled_noise),  # irrelevant
    error_count           # irrelevant
]

threshold = 25

# Key distracting computation
shadow_metric = min(max(anomaly_score, 1), 5) ** 2 - len(warning_fragments)

# Main processing function with conditional logic and nesting
def process_metrics(metrics, limit):
    if not metrics:
        return -1
    
    primary = metrics[0]
    secondary = metrics[1]
    tertiary = metrics[2]
    
    # Nested conditionals with logical operations
    if primary >= limit:
        if secondary < 50:
            adjustment = primary * 0.8
        else:
            adjustment = primary + tertiary * 2
    else:
        if tertiary > 2 and 'volatile' in status_flag.upper():
            adjustment = primary + 15
        else:
            adjustment = primary + (secondary // 10)
    
    # Complex decision with decoy usage
    confidence = 1
    if len(metrics) > 3 and metrics[3] > 0:
        confidence += metrics[3]  # uses scaled_noise length - a red herring
    
    intermediate = adjustment * confidence
    
    # Final adjustment using string-derived flag (real dependency)
    multiplier = 1.5 if 'INFO' in system_log else 1.0
    
    # Critical statement
    final_diagnostic = int(intermediate * multiplier)
    
    return final_diagnostic

# Execute
final_diagnostic = process_metrics(health_data, threshold)
print(f"Target result: {final_diagnostic}")