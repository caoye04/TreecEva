from collections import defaultdict, Counter
import itertools

# Simulated sensor log entries with diagnostic codes
def generate_logs():
    logs = [
        {'time': 100, 'sensor': 'temp', 'value': 78, 'status': 'OK'},
        {'time': 105, 'sensor': 'pressure', 'value': 45, 'status': 'WARN'},
        {'time': 110, 'sensor': 'temp', 'value': 82, 'status': 'OK'},
        {'time': 115, 'sensor': 'flow', 'value': 12, 'status': 'ERROR'},
        {'time': 120, 'sensor': 'temp', 'value': 85, 'status': 'OK'},
        {'time': 125, 'sensor': 'pressure', 'value': 50, 'status': 'OK'},
        {'time': 130, 'sensor': 'flow', 'value': 15, 'status': 'OK'},
        {'time': 135, 'sensor': 'vibration', 'value': 95, 'status': 'WARN'},
        {'time': 140, 'sensor': 'temp', 'value': 88, 'status': 'OK'},
        {'time': 145, 'sensor': 'pressure', 'value': 55, 'status': 'OK'}
    ]
    return logs

# Irrelevant helper: counts status occurrences (distractor)
def count_statuses(logs):
    counter = Counter()
    for entry in logs:
        counter[entry['status']] += 1
    return counter

# Misleading transformation: applies arbitrary scaling (dead path)
def transform_values(logs, factor=1.0):
    new_logs = []
    for entry in logs:
        scaled = entry['value'] * factor
        new_logs.append({**entry, 'value': scaled})
    return new_logs

# Decoy function: looks important but unused in critical path
def analyze_trends(data_list):
    if not data_list:
        return 0
    diffs = [data_list[i+1] - data_list[i] for i in range(len(data_list)-1)]
    return sum(1 for d in diffs if d > 0)

# Real processing begins here
system_thresholds = {
    'temp_high': 80,
    'pressure_high': 52,
    'flow_low': 14,
    'vibration_high': 90
}

# Aggregates sensor values by type
def aggregate_sensor_data(logs):
    aggregated = defaultdict(list)
    for entry in logs:
        aggregated[entry['sensor']].append(entry['value'])
    return aggregated

# Computes statistical metrics (only mean is used later)
def compute_metrics(sensor_data):
    metrics = {}
    for sensor, values in sensor_data.items():
        total = sum(values)
        count = len(values)
        mean_val = total / count
        max_val = max(values)
        min_val = min(values)
        # Only mean is used in final logic; others are distractions
        metrics[sensor] = {
            'mean': mean_val,
            'max': max_val,
            'min': min_val,
            'range': max_val - min_val,
            'stdev_guess': (max_val - min_val) / 4  # crude estimate
        }
    return metrics

# Evaluates each metric against thresholds (core logic)
def evaluate_health(metrics, thresholds):
    issues = 0
    
    # Temp check
    if 'temp' in metrics:
        if metrics['temp']['mean'] > thresholds['temp_high']:
            issues += 2
    
    # Pressure check
    if 'pressure' in metrics:
        if metrics['pressure']['mean'] > thresholds['pressure_high']:
            issues += 3
    
    # Flow check
    if 'flow' in metrics:
        if metrics['flow']['mean'] < thresholds['flow_low']:
            issues += 1
    
    # Vibration check
    if 'vibration' in metrics:
        if metrics['vibration']['mean'] > thresholds['vibration_high']:
            issues += 4
    
    return issues

# Main processor combining multiple concepts
def process_metrics(logs, thresholds):
    # Step 1: Aggregate sensor data
    sensor_data = aggregate_sensor_data(logs)
    
    # Step 2: Compute comprehensive metrics
    all_metrics = compute_metrics(sensor_data)
    
    # Step 3: Evaluate health status
    health_issues = evaluate_health(all_metrics, thresholds)
    
    # Step 4: Apply complex weighting using conditional logic and itertools
    weights = [2, 3, 5]
    cycle = itertools.cycle(weights)
    weighted_score = 0
    
    for i, issue_type in enumerate(['critical', 'major', 'minor']):
        shift = next(cycle)
        # Only first iteration meaningfully contributes
        if issue_type == 'critical':
            weighted_score += (health_issues << 2) >> shift  # (issues * 4) / 2^shift
        else:
            # Dead computations with no effect
            temp = (health_issues * 10) >> (shift + i)
            weighted_score += 0  # Explicit neutral contribution
    
    # Step 5: Final adjustment based on status diversity (distraction)
    status_counter = count_statuses(logs)
    diversity_bonus = len(status_counter) * 0.5
    
    # Step 6: Apply bitmask obfuscation (irrelevant)
    mask = 0b11111111
    masked_issues = health_issues & mask
    
    # Step 7: Core answer derivation
    base_result = health_issues * 100
    final_value = base_result + (masked_issues ^ 10)  # XOR adds distraction
    
    # Step 8: Final diagnostic score
    final_diagnostic = int(final_value - diversity_bonus)
    
    return final_diagnostic

# Generate input data
log_data = generate_logs()

# Execute main logic
final_diagnostic = process_metrics(log_data, system_thresholds)

# Print result
print(f"Result: {final_diagnostic}")