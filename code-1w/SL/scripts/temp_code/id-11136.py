def analyze_efficiency(logs):
    total_entries = len(logs)
    valid_count = sum(1 for log in logs if 'ERROR' not in log)
    error_rate = (total_entries - valid_count) / total_entries if total_entries > 0 else 0
    
    # Distractor: irrelevant transformation
    processed_logs = [log.strip().upper() for log in logs]
    suspicious_patterns = [log for log in processed_logs if 'WARNING' in log and 'DISK' in log]
    
    efficiency = (valid_count * 100) // total_entries if total_entries > 0 else 0
    return efficiency, len(suspicious_patterns)


def calculate_stability(metrics):
    baseline = metrics.get('uptime', 0)
    fluctuations = metrics.get('fluctuations', [])
    
    # Dead computation: not used later
    peak_load = max(fluctuations) if fluctuations else 0
    avg_load = sum(fluctuations) / len(fluctuations) if fluctuations else 0
    
    stability_score = baseline - (len([f for f in fluctuations if f > avg_load]) * 2)
    
    # Misleading normalization
    normalized_stability = round(stability_score / 10.0, 2)
    return stability_score  # Ignore normalized version

productivity = 0
risk_factor = 0

# Simulated system telemetry
telemetry_logs = [
    'INFO: task completed successfully',
    'INFO: data pipeline running',
    'WARNING: high memory usage detected',
    'INFO: checkpoint saved',
    'WARNING: DISK I/O latency increasing',
    'ERROR: database timeout',
    'INFO: retrying connection'
]

metrics_data = {
    'uptime': 94,
    'fluctuations': [12, 8, 15, 6, 20, 10, 25],
    'reboots': 3
}

# Step 1: Analyze log efficiency
efficiency, disk_warnings = analyze_efficiency(telemetry_logs)

# Step 2: Calculate system stability
stability = calculate_stability(metrics_data)

# Step 3: Derive productivity score (relevant)
if efficiency >= 85:
    productivity += 40
elif efficiency >= 70:
    productivity += 30
else:
    productivity += 15

productivity += min(stability, 60) // 2

# Step 4: Assess risk factor using modular arithmetic and string analysis
length_analysis = [len(log.split()) for log in telemetry_logs]
long_lines = [count for count in length_analysis if count > 4]
risk_factor = len(long_lines) % 7

# Irrelevant slicing distraction
snippet = telemetry_logs[1:5:2]
dummy_slice_sum = sum(len(s) % 5 for s in snippet)

# Step 5: Use list comprehension with filtering (partially relevant)
warning_count = len([log for log in telemetry_logs if log.startswith('WARNING')])
risk_factor += warning_count * 3

# Step 6: Final adjustment using integer division
if risk_factor > 10:
    risk_factor = risk_factor // 2 + 1

# Key statement
final_score = evaluate_performance(productivity, risk_factor)

# Definition provided after usage (test ordering reasoning)
def evaluate_performance(prod, risk):
    base = prod - risk * 1.5
    if base < 0:
        return 0
    # Apply bonus only if no critical errors
    has_critical = any('ERROR' in log for log in telemetry_logs)
    bonus = 10 if not has_critical else 0
    return int(base + bonus)

print(f"Result: {final_score}")