def analyze_phase_severity(phase_data, thresholds):
    severe_count = 0
    for reading in phase_data:
        if reading > thresholds['critical']:
            severe_count += 1
        elif reading > thresholds['warning']:
            severe_count += 0.5
    return round(severe_count)


def evaluate_redundancy(network_nodes):
    primary_set = {node for node in network_nodes if 'primary' in node}
    backup_set = {node for node in network_nodes if 'backup' in node}
    overlap = primary_set & backup_set
    return len(overlap) == 0 and len(primary_set) >= 3


def compute_integrity_score(phases, flags):
    base_score = 100
    adjustment = 0
    
    # Irrelevant statistical summary (distractor)
    total_readings = sum(len(data) for data in phases.values())
    avg_per_phase = total_readings / len(phases) if phases else 0
    
    # Critical path: severity analysis
    critical_thresholds = {
        'warning': 75,
        'critical': 90
    }
    
    high_stress_phases = 0
    for phase_name, data in phases.items():
        severity = analyze_phase_severity(data, critical_thresholds)
        if severity > 2:
            high_stress_phases += 1

    # Red herring: complex but unused redundancy check
    node_config = [f'node_{i}_{"primary" if i % 2 == 0 else "backup"}' for i in range(10)]
    system_redundancy_valid = evaluate_redundancy(node_config)
    optimization_log = []
    
    for i in range(5):
        temp_flag = (i * 2) in flags
        debug_state = f'debug_{i}'
        optimization_log.append(debug_state)
        
        # Dead code branch (never executed due to flag logic)
        if temp_flag and len(optimization_log) > 100:
            base_score += 10

    # Real adjustment logic buried among distractions
    if high_stress_phases >= 2:
        adjustment -= 30
    elif high_stress_phases == 1:
        adjustment -= 15

    if 42 in flags:
        adjustment += 10
    
    if len(flags) > 5:
        adjustment -= 5 * (len(flags) - 5)

    # Another decoy operation
    aggregate_flag_sum = sum(f * f for f in flags if f % 3 == 0)
    dummy_transform = [abs(x - 50) for x in range(100) if x in flags]

    final_score = base_score + adjustment
    
    # Key diagnostic computation
    anomaly_ratio = high_stress_phases / len(phases) if phases else 0
    safety_margin = 1 - abs(anomaly_ratio - 0.25)
    
    final_diagnostic = int(final_score * safety_margin)
    
    # Unrelated telemetry output (misleading print)
    print(f"Telemetry: {len(dummy_transform)} transient states observed")
    
    return final_diagnostic

# Simulated system telemetry
current_phases = {
    'startup': [68, 72, 70, 69],
    'calibration': [85, 88, 92, 95],
    'execution': [93, 97, 89, 76],
    'monitoring': [70, 65, 78, 82]
}

system_flags = {12, 42, 15, 9, 30, 6, 21}  # Includes 42 (positive) and multiple of 3

# Execution point of interest
final_diagnostic = compute_integrity_score(current_phases, system_flags)
print(f"Result: {final_diagnostic}")