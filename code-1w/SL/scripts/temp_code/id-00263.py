def normalize(s):
    return s.lower().replace(' ', '_').strip('_')

# Simulated system metrics from different subsystems
temp_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
status_flags = [True, False, True, True, False]
error_logs = ['None', 'Warning: Disk usage high', 'Critical: Memory leak', 'None', 'Info: Restarted']

def analyze_errors(logs):
    counts = {'none': 0, 'info': 0, 'warning': 0, 'critical': 0}
    for log in logs:
        key = normalize(log.split(':')[0]) if ':' in log else normalize(log)
        if key in counts:
            counts[key] += 1
    return counts

error_analysis = analyze_errors(error_logs)
severity_weight = 0.0
if error_analysis['critical'] > 0:
    severity_weight += 1.5
if error_analysis['warning'] > 0:
    severity_weight += 0.7

# Irrelevant temperature processing (distractor)
avg_temp = sum(temp_readings) / len(temp_readings)
adjusted_temps = [t * 1.02 for t in temp_readings if t > 23.0]
fluctuation = max(adjusted_temps) - min(adjusted_temps)

temp_penalty = 0.0
if avg_temp > 24.0:
    temp_penalty = 0.3

# Simulated performance metrics (core data)
metrics = {
    'response_time': 142.5,
    'throughput': 89.3,
    'consistency': 94.1,
    'availability': 96.7
}

# Weight configuration (some are red herrings)
weights = {
    'response_time': -0.2,  # negative weight (penalty)
    'throughput': 0.3,
    'consistency': 0.4,
    'availability': 0.35,
    'redundancy': 0.1,      # unused weight
    'latency': 0.05        # unused
}

# Dead code path - never executed but looks relevant
def calculate_reliability_index():
    return (metrics['availability'] * 0.6) + (100 - fluctuation * 2) * 0.4

# Unused helper
unused_flags = [int(f) for f in status_flags]
flag_sum = sum(unused_flags)

# Core evaluation logic with string-based routing
method = 'weighted_v2'
if 'v2' in method:
    base = 0.0
    impact = 0.0
    for key in metrics:
        if key in weights:
            contribution = metrics[key] * weights[key]
            if weights[key] < 0:
                impact -= contribution  # penalty inversion
            else:
                base += contribution
    
    # Apply severity and temperature penalties
    base -= severity_weight * 3.5
    base -= temp_penalty * 2.0
    
    # Final nonlinear adjustment
    if base > 85:
        final_score = base * 0.92 + 6.5
    elif base > 70:
        final_score = base * 0.95
    else:
        final_score = base * 0.98
else:
    final_score = sum(metrics.values()) / len(metrics)

Result: {final_score}