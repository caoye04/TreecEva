from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 0.45, 'errors': 2, 'temp': 67},
    {'node': 'B', 'load': 0.78, 'errors': 1, 'temp': 73},
    {'node': 'A', 'load': 0.82, 'errors': 5, 'temp': 79},
    {'node': 'C', 'load': 0.33, 'errors': 0, 'temp': 61},
    {'node': 'B', 'load': 0.91, 'errors': 8, 'temp': 85},
    {'node': 'C', 'load': 0.29, 'errors': 1, 'temp': 58}
]

# Irrelevant baseline profile (distractor)
baseline_profile = {
    'avg_load': 0.5,
    'tolerance': 0.15,
    'decay_factor': 0.9,
    'noise_floor': 0.05
}

# System thresholds for diagnostics
system_thresholds = {
    'critical_load': 0.85,
    'high_error_rate': 3,
    'overheat_temp': 80,
    'stability_window': 3
}

# Aggregation structures (some are red herrings)
node_metrics = defaultdict(lambda: {'loads': [], 'errors': [], 'temps': []})
node_weights = {'A': 1.0, 'B': 1.2, 'C': 0.9}  # Unused in final logic
priority_queue = []  # Dead code path
snapshot_buffer = []  # Unused buffer

# Process raw stream into node-specific time series
for entry in telemetry_stream:
    node = entry['node']
    node_metrics[node]['loads'].append(entry['load'])
    node_metrics[node]['errors'].append(entry['errors'])
    node_metrics[node]['temps'].append(entry['temp'])

# Derived metrics (some irrelevant)
avg_loads = {}
peak_temps = {}
error_bursts = defaultdict(int)

for node, data in node_metrics.items():
    avg_loads[node] = sum(data['loads']) / len(data['loads'])
    peak_temps[node] = max(data['temps'])
    # Count bursts (consecutive high errors) — unused
    for i in range(1, len(data['errors'])):
        if data['errors'][i] > 2 and data['errors'][i-1] > 2:
            error_bursts[node] += 1

# Decoy transformation function (never called)
def calculate_stress_score(metrics, weights):
    score = 0
    for node, data in metrics.items():
        score += weights.get(node, 1.0) * (
            data['loads'][-1] * 10 + data['errors'][-1] * 5
        )
    return score / len(metrics)

# Simulate historical comparison (irrelevant computation)
historical_avg = 0.52
variance_drift = sum(abs(avg_loads[n] - historical_avg) for n in avg_loads)
adjustment_factor = math.exp(-variance_drift)  # Not used

# Primary diagnostic processor
def analyze_node_health(node, metrics, thresholds):
    loads = metrics['loads']
    errors = metrics['errors']
    temps = metrics['temps']
    
    # Check for instability: rapid load spikes
    load_spikes = 0
    for i in range(1, len(loads)):
        if loads[i] > thresholds['critical_load'] and loads[i-1] < 0.6:
            load_spikes += 1
    
    # Count critical conditions
    critical_count = 0
    for i in range(len(loads)):
        is_critical_load = loads[i] >= thresholds['critical_load']
        is_high_error = errors[i] >= thresholds['high_error_rate']
        is_overheated = temps[i] >= thresholds['overheat_temp']
        
        if is_critical_load and (is_high_error or is_overheated):
            critical_count += 1
    
    # Stability test over sliding window
    unstable_periods = 0
    window = thresholds['stability_window']
    for i in range(len(loads) - window + 1):
        window_loads = loads[i:i+window]
        if max(window_loads) - min(window_loads) > 0.4:  # High volatility
            unstable_periods += 1
    
    # Composite health score (only one value matters at end)
    health_flags = {
        'spikes': load_spikes,
        'critical_events': critical_count,
        'volatile_windows': unstable_periods,
        'peak_temp': max(temps),
        'final_load': loads[-1]
    }
    
    # Return only the number of critical events for this node
    return health_flags['critical_events']

# Secondary processing with dictionary slicing (red herring)
def compute_efficiency_ratio(metrics):
    ratios = {}
    for node, data in metrics.items():
        total_ops = sum(data['loads']) * 100
        energy_cost = sum(data['temps']) * 1.5
        ratios[node] = total_ops / (energy_cost + 1) if energy_cost else 0
    return {k: round(v, 3) for k, v in ratios.items()}[list(ratios.keys())[-1]:]  # Slicing distraction

# Main data structure for processing
log_data = node_metrics  # Renamed reference

# Auxiliary statistical summary (unused)
error_counter = Counter([e for m in log_data.values() for e in m['errors']])
mode_error = error_counter.most_common(1)[0][0]  # Distractor

# Core processing function
def process_metrics(log_data, thresholds):
    node_risk = {}
    total_critical = 0
    
    # Analyze each node
    for node, metrics in log_data.items():
        risk_level = analyze_node_health(node, metrics, thresholds)
        node_risk[node] = risk_level
        total_critical += risk_level
    
    # Apply fake normalization (dead calculation)
    normalized_risk = {}
    max_risk = max(node_risk.values()) if node_risk else 1
    for n, r in node_risk.items():
        norm_value = r / (max_risk + 1e-8)
        normalized_risk[n] = round(norm_value, 4)
    
    # Additional decoy logic: simulate mitigation impact
    mitigated = {}
    for n in node_risk:
        mitigated[n] = math.floor(node_risk[n] * 0.7 + 0.5)
    
    # Final aggregation: sum of raw critical events
    aggregate_diagnostic = sum(node_risk.values())
    
    # Secondary index: count how many nodes had any critical event
    affected_nodes = sum(1 for r in node_risk.values() if r > 0)
    
    # Final diagnostic uses a transformed combination
    final_diagnostic = (aggregate_diagnostic * 100) + (affected_nodes * 10)
    
    # Irrelevant min/max/average calculations (distractors)
    all_risks = list(node_risk.values())
    mean_risk = sum(all_risks) / len(all_risks) if all_risks else 0
    peak_risk = max(all_risks) if all_risks else 0
    risk_range = peak_risk - mean_risk  # Unused
    
    return int(final_diagnostic)

# Execute main logic
final_diagnostic = process_metrics(log_data, system_thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")