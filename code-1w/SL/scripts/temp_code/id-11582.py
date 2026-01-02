from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'temp': 45, 'load': 0.7, 'errors': 2},
    {'node': 'B', 'temp': 65, 'load': 0.9, 'errors': 5},
    {'node': 'A', 'temp': 50, 'load': 0.6, 'errors': 1},
    {'node': 'C', 'temp': 30, 'load': 0.4, 'errors': 0},
    {'node': 'B', 'temp': 70, 'load': 0.95, 'errors': 8},
    {'node': 'C', 'temp': 35, 'load': 0.5, 'errors': 1}
]

# Irrelevant historical thresholds (distractor)
historical_max_temp = 80
legacy_load_warning = 0.85
unused_backup_nodes = ['X', 'Y', 'Z']
shadow_thresholds = { 'critical_temp': 90, 'grace_period': 3 }

# Aggregation logic for diagnostics
def aggregate_node_metrics(data):
    node_stats = defaultdict(list)
    for entry in data:
        node_stats[entry['node']].append(entry)
    
    aggregated = {}
    for node, records in node_stats.items():
        temps = [r['temp'] for r in records]
        loads = [r['load'] for r in records]
        errors = sum(r['errors'] for r in records)
        
        # Real computation path
        avg_temp = sum(temps) / len(temps)
        peak_load = max(loads)
        
        # Distraction: unnecessary intermediate calculations
        smoothed_load = sum(loads) / len(loads) * 1.05
        temp_variance = sum((t - avg_temp) ** 2 for t in temps) / len(temps)
        
        aggregated[node] = {
            'avg_temp': avg_temp,
            'peak_load': peak_load,
            'errors': errors,
            'stability_score': 100 - avg_temp + (1 - peak_load) * 50,  # core metric
            'decoy_metric': temp_variance * smoothed_load
        }
    
    return aggregated

# Secondary processing with red herring functions
def apply_calibration(metrics_map, bias_factor=1.05):
    calibrated = {}
    calibration_log = []  # unused logging path
    
    for node, data in metrics_map.items():
        # Meaningful transformation
        calibrated[node] = {
            'calibrated_score': data['stability_score'] * bias_factor,
            'thermal_rating': 'HIGH' if data['avg_temp'] > 55 else 'NORMAL',
            'error_density': data['errors'] / (data['avg_temp'] + 1)
        }
        
        # Dead code path - looks important but unused
        adjustment_trace = []
        if data['avg_temp'] > 60:
            for i in range(2):
                adjustment_trace.append(math.log(data['avg_temp']) * 0.1)

    # Another distraction: unused summary
    total_trace = sum(len(v) for v in metrics_map.values())
    
    return calibrated

# Final decision engine with decoy control flow
def evaluate_overall_health(calibrated_data, log_data):
    health_counters = Counter()
    risk_nodes = []
    phantom_weights = [0.1, 0.3, 0.6]  # Looks like weighting, never used
    
    for node, attrs in calibrated_data.items():
        health_counters['assessed'] += 1
        
        # Core logic determining outcome
        if attrs['calibrated_score'] < 75 or attrs['thermal_rating'] == 'HIGH':
            health_counters['at_risk'] += 1
            risk_nodes.append(node)
        
        # Distracting nested condition that never triggers due to data
        if attrs['error_density'] > 10:
            shadow_impact = 0
            for _ in range(5):
                shadow_impact += math.sin(attrs['error_density'])
            health_counters['legacy_flagged'] += 1  # never incremented
    
    # Real result computation
    at_risk_ratio = health_counters['at_risk'] / health_counters['assessed']
    final_severity = math.ceil(at_risk_ratio * 100)
    
    # Decoy aggregation using irrelevant parts
    fake_aggregate = 0
    for entry in log_data:
        if 'temp' in entry:
            fake_aggregate += entry['temp'] // 10
    
    return final_severity

# Unused recursive validator (red herring)
def validate_structure(obj, depth=0):
    if depth > 5 or not isinstance(obj, dict):
        return False
    if 'critical' in obj:
        return True
    return any(validate_structure(v, depth+1) for v in obj.values())

# Main execution pipeline
if __name__ == '__main__':
    # Initial processing
    raw_diagnostics = aggregate_node_metrics(telemetry_stream)
    
    # Spurious intermediate check (no effect)
    verification_key = ''.join([chr(97 + len(v['decoy_metric'])) for k, v in raw_diagnostics.items()])
    
    # Actual relevant transformation
    processed_metrics = apply_calibration(raw_diagnostics, bias_factor=1.1)
    
    # Simulated external state (mock)
    system_state = {
        'mode': 'OPERATIONAL',
        'version': '2.5.1',
        'maintenance_window': None
    }
    
    # Critical statement: this produces the target answer
    final_diagnostic = evaluate_overall_health(processed_metrics, telemetry_stream)
    
    # Irrelevant post-processing
    diagnostic_token = hex(final_diagnostic ^ 255)[2:]
    audit_stamp = f"DX-{final_diagnostic % 10}-{len(diagnostic_token)}"
    
    # Output required result
    print(f"Target result: {final_diagnostic}")