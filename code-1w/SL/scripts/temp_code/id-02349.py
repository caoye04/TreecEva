from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_logs = [
    'ERROR: disk_usage=95%', 'INFO: cpu_temp=72C', 'WARNING: disk_usage=88%',
    'ERROR: network_latency=220ms', 'INFO: cpu_temp=68C', 'WARNING: memory_usage=82%',
    'ERROR: disk_usage=97%', 'INFO: cpu_temp=70C'
]

# Parse logs into structured metrics
disk_usages = []
temperatures = []
latencies = []
for log in telemetry_logs:
    if 'disk_usage' in log:
        try:
            val = int(log.split('=')[1].replace('%', ''))
            disk_usages.append(val)
        except:
            continue
    if 'cpu_temp' in log:
        try:
            val = int(log.split('=')[1].replace('C', ''))
            temperatures.append(val)
        except:
            continue
    if 'network_latency' in log:
        try:
            val = int(log.split('=')[1].replace('ms', ''))
            latencies.append(val)
        except:
            continue

# Compute basic statistics
avg_disk = sum(disk_usages) / len(disk_usages) if disk_usages else 0
max_temp = max(temperatures) if temperatures else 0
error_count = sum(1 for log in telemetry_logs if 'ERROR' in log)
warning_count = sum(1 for log in telemetry_logs if 'WARNING' in log)

# Irrelevant distraction: character frequency analysis on logs
char_freq = Counter(''.join(telemetry_logs))
top_chars = sorted(char_freq.items(), key=lambda x: -x[1])[:5]

# Decoy function that is never called
def analyze_failure_patterns(logs):
    patterns = defaultdict(int)
    for log in logs:
        if 'ERROR' in log:
            key = log.split(':')[0]
            patterns[key] += 1
    return dict(patterns)

# Another decoy: simulated prediction model (unused)
predicted_failures = 0
if error_count > 2:
    predicted_failures = int((error_count * max_temp) / 10)

# Real metric processing
stability_index = 100 - avg_disk  # inverse relationship
latency_penalty = sum(l**2 for l in latencies) / 100 if latencies else 0
warning_factor = warning_count * 2.5

# Weight configuration (some weights are red herrings)
weights = {
    'stability': 0.4,
    'penalty': 0.3,
    'warnings': 0.2,
    'decoy_a': 0.05,  # unused in final calculation
    'decoy_b': 0.05   # unused
}

# Metrics container
metrics = {
    'stability': stability_index,
    'penalty': latency_penalty,
    'warnings': warning_factor,
    'temp_peak': max_temp,  # collected but not used
    'errors': error_count   # also not directly used
}

# Core evaluation logic
def evaluate_performance(mets, wts):
    # Misleading: sort weights by name but don't use
    sorted_keys = sorted(wts.keys())
    total_weight = sum(wts[k] for k in ['stability', 'penalty', 'warnings'])  # only these three count
    
    # Apply actual weighted score
    score = 0
    if 'stability' in mets and 'stability' in wts:
        score += mets['stability'] * wts['stability']
    if 'penalty' in mets and 'penalty' in wts:
        score -= mets['penalty'] * wts['penalty']  # penalty reduces score
    if 'warnings' in mets and 'warnings' in wts:
        score -= mets['warnings'] * wts['warnings']
    
    # Additional constraint: cap score reduction from warnings
    min_score = 20.0
    if score < min_score:
        score = min_score
    
    # Dead code path: adjustment based on non-existent 'adaptive' key
    if 'adaptive' in wts:
        score = score * (1 + wts['adaptive'])
    
    # Final nonlinear transformation
    adjusted = math.floor(score * 1.15) if score > 50 else math.ceil(score * 0.9)
    
    return adjusted

# Execute main logic
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Target result: {final_score}")