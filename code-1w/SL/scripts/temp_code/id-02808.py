import math

# Simulated system telemetry data with mixed relevance
technical_logs = [
    {'timestamp': 1623456789, 'cpu_load': 0.78, 'mem_used': 8520, 'disk_io': 120, 'temp_core': 67},
    {'timestamp': 1623456790, 'cpu_load': 0.82, 'mem_used': 8640, 'disk_io': 125, 'temp_core': 69},
    {'timestamp': 1623456791, 'cpu_load': 0.75, 'mem_used': 8450, 'disk_io': 118, 'temp_core': 66},
    {'timestamp': 1623456792, 'cpu_load': 0.91, 'mem_used': 8900, 'disk_io': 145, 'temp_core': 73},
    {'timestamp': 1623456793, 'cpu_load': 0.68, 'mem_used': 8200, 'disk_io': 110, 'temp_core': 64}
]

# Irrelevant aesthetic configuration (red herring)
color_scheme = {'primary': '#1a1a1a', 'accent': '#00ffcc', 'font': 'Fira Code'}

# System thresholds for health monitoring (some values are decoys)
system_thresholds = {
    'load_ceiling': 0.90,
    'memory_warning': 8500,
    'max_temp': 70,
    'disk_spike': 130,
    'network_latency_ms': 45,  # unused parameter
    'retry_attempts': 3       # unused parameter
}

# Auxiliary mapping table (partially used)
priority_mapping = {0: 'low', 1: 'medium', 2: 'high', 3: 'critical'}

# Legacy diagnostic codes (dead code path)
def legacy_diagnose(metrics):
    score = 0
    if metrics['cpu_load'] > 0.85:
        score += 2
    if metrics['temp_core'] > 70:
        score += 3
    return score * 10  # never called

# Core processing function with distractors
def analyze_entry(entry, config):
    # Extract relevant metrics
    load = entry['cpu_load']
    memory = entry['mem_used']
    temperature = entry['temp_core']
    io_activity = entry['disk_io']

    # Compute derived diagnostics (some intermediate values are misleading)
    base_risk = 0
    if load > config['load_ceiling']:
        base_risk += 40
    if memory > config['memory_warning']:
        base_risk += 30
    if temperature > config['max_temp']:
        base_risk += 35
    if io_activity > config['disk_spike']:
        base_risk += 25

    # Use lambda for dynamic weighting (meaningful but obscured)
    severity_weight = lambda x: round(x * (1.1 + load / 10), 2)
    adjusted_risk = severity_weight(base_risk)

    # String-based status (irrelevant to final result)
    status_flag = "HEALTHY" if base_risk < 50 else "DEGRADED"
    entry['status_label'] = status_flag  # side effect, not used later

    # Return only the numeric risk score
    return adjusted_risk


# Secondary transformation (used in aggregation)
def transform_readings(logs):
    # Filter and normalize timestamps (some complexity is irrelevant)
    recent_logs = [log for log in logs if log['timestamp'] > 1623456790]
    normalized = []
    for log in recent_logs:
        norm_entry = {k: v for k, v in log.items() if k != 'timestamp'}
        norm_entry['norm_memory'] = round(log['mem_used'] / 100.0, 1)  # not used
        normalized.append(norm_entry)
    return normalized


# Main processing pipeline
def process_metrics(log_entries, thresholds):
    # Transform input (contains irrelevant normalization)
    processed_logs = transform_readings(log_entries)

    # Analyze each relevant log entry
    risk_scores = []
    for entry in processed_logs:
        score = analyze_entry(entry, thresholds)
        risk_scores.append(score)

    # Aggregate final result using statistical reduction
    if not risk_scores:
        return 0.0

    # Calculate weighted outcome (key computation)
    raw_average = sum(risk_scores) / len(risk_scores)
    peak_stress = max(risk_scores)

    # Apply decay factor based on system recovery heuristic (dummy logic)
    recovery_factor = 0.9 if peak_stress < 80 else 1.0

    # Final diagnostic includes both average and peak influence
    final_value = raw_average * 1.1 + peak_stress * 0.4

    # Use conditional expression to finalize (core step)
    final_diagnostic = round(final_value, 2) if final_value > 0 else 0.0

    return final_diagnostic


# Spurious utility function (never invoked)
def generate_report_snapshot(data):
    count = len(data)
    avg_load = sum(d['cpu_load'] for d in data) / count
    summary = f"Report: {count} entries, Avg Load: {avg_load:.2f}"
    return summary.upper()


# Orchestration block
if __name__ == "__main__":
    # Misleading preliminary calculations (distractor)
    snapshot = generate_report_snapshot(technical_logs)
    baseline_metric = math.log(technical_logs[0]['mem_used']) * 100

    # Actual key execution point
    final_diagnostic = process_metrics(technical_logs, system_thresholds)

    # Output the required result
    print(f"Result: {final_diagnostic}")