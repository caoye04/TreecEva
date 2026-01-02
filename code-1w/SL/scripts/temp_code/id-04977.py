from collections import defaultdict, Counter
import math

# Simulate system telemetry data
telemetry_data = [
    {'cpu': 78, 'mem': 43, 'disk': 12, 'net_in': 56, 'net_out': 61},
    {'cpu': 85, 'mem': 50, 'disk': 15, 'net_in': 60, 'net_out': 65},
    {'cpu': 90, 'mem': 55, 'disk': 10, 'net_in': 70, 'net_out': 75}
]

# Irrelevant helper (decoy)
def analyze_security_logs():
    events = ['login', 'scan', 'access_denied', 'firewall']
    log_counter = Counter(events * 2)
    return sum([len(e) for e in log_counter.keys()])

# Unused transformation function
def transform_metrics(data):
    return [d['cpu'] * 1.1 for d in data if d['mem'] > 40]

# Core evaluation logic
def normalize(value, max_val=100):
    return round(value / max_val, 3)

def compute_stability_factor(values):
    mean_v = sum(values) / len(values)
    variance = sum((v - mean_v) ** 2 for v in values) / len(values)
    return round(math.exp(-variance / 10), 3)

# Distractor: Network-specific scoring (not used in final path)
def network_priority_score(data):
    in_flux = [d['net_in'] for d in data]
    out_flux = [d['net_out'] for d in data]
    return (sum(in_flux) + sum(out_flux)) / 2

# Real metric processor with red herring variables
def extract_key_metrics(data):
    metrics = defaultdict(float)
    cpu_vals = []
    
    for entry in data:
        # Relevant extraction
        cpu_vals.append(entry['cpu'])
        metrics['avg_cpu'] += entry['cpu']
        metrics['avg_mem'] += entry['mem']
        
        # Distractor accumulations
        metrics['temp_disk_io'] += entry['disk'] * 2.5  # unused later
        metrics['ghost_metric'] = abs(entry['cpu'] - entry['mem'])  # overwritten
    
    # Final relevant assignments
    metrics['avg_cpu'] = normalize(metrics['avg_cpu'] / len(data))
    metrics['avg_mem'] = normalize(metrics['avg_mem'] / len(data))
    metrics['stability'] = compute_stability_factor(cpu_vals)
    
    # Fake cleanup
    if metrics['ghost_metric'] > 30:
        metrics['ghost_metric'] = 0  # dead code branch
    
    return dict(metrics)

# Weight configuration (some weights are decoys)
def get_weights():
    weights = defaultdict(float)
    weights['avg_cpu'] = 0.4
    weights['avg_mem'] = 0.3
    weights['stability'] = 0.3
    # Unused weights below
    weights['temp_disk_io'] = 0.1  # irrelevant
    weights['security_factor'] = 0.2  # never computed
    return dict(weights)

# Recursive depth-limited scorer (simple recursion)
def recursive_boost(score, level=3):
    if level <= 0 or score >= 0.95:
        return score
    boosted = min(score + 0.05, 0.95)
    return recursive_boost(boosted, level - 1)

# Main evaluation function
def evaluate_performance(metrics, weights):
    base_score = 0.0
    
    # Only these three keys are actually used
    relevant_keys = ['avg_cpu', 'avg_mem', 'stability']
    for key in relevant_keys:
        base_score += metrics[key] * weights[key]
    
    # Dead code: conditional on non-existent flag
    if 'calibration_mode' in metrics:
        base_score *= 0.8
    
    # Apply recursive boost (only increases slightly)
    final = recursive_boost(base_score)
    
    # Decoy rounding (never reached due to final assignment)
    _ = round(final * 1000) / 1000
    
    # Actual result
    final_score = int(round(final * 1000))  # Scale to integer
    return final_score

# Execution flow begins
metrics = extract_key_metrics(telemetry_data)
weights = get_weights()

# Distractor call
_ = analyze_security_logs()
_ = network_priority_score(telemetry_data)

# Critical statement
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")