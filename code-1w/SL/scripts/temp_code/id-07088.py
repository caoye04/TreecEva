from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    (100, 'cpu', 'high'), (105, 'mem', 'normal'), (98, 'disk', 'critical'),
    (203, 'cpu', 'normal'), (198, 'mem', 'high'), (400, 'network', 'critical'),
    (50, 'disk', 'normal'), (150, 'cpu', 'high'), (300, 'network', 'critical')
]

# Irrelevant baseline configuration (distractor)
system_baseline = {
    'version': '2.1.0',
    'mode': 'debug',
    'timeout': 300,
    'retries': 3
}

# Parse raw stream into structured format
def parse_telemetry(stream):
    parsed = defaultdict(list)
    for val, comp, status in stream:
        parsed[comp].append({'value': val, 'status': status})
    return parsed

# Secondary processing - extracts only 'critical' flagged entries (partially relevant)
def extract_critical_components(parsed_data):
    critical = []
    for component, records in parsed_data.items():
        for r in records:
            if r['status'] == 'critical':
                critical.append((component, r['value']))
    return critical

# Legacy function - unused but looks important (dead code path)
def legacy_diagnostic_scan(data):
    score = 0
    for entry in data:
        if entry[1] > 100:
            score += 1
    return score * 10  # Never called

# Real-time anomaly detector (red herring - computes but not used in final result)
def detect_anomalies(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = math.sqrt(variance)
    return [v for v in values if abs(v - mean_val) > 2 * std_dev]

# Core metric processor
system_thresholds = {
    'cpu': 200,
    'mem': 150,
    'disk': 100,
    'network': 350
}

def evaluate_component_health(value, comp, thresholds):
    limit = thresholds.get(comp, 500)
    if value > limit:
        return 'overload'
    elif value > limit * 0.8:
        return 'elevated'
    else:
        return 'stable'

# Data transformation pipeline
log_data = parse_telemetry(telemetry_stream)

# Extract all CPU values for decoy analysis
cpu_values = [entry['value'] for entry in log_data['cpu']]

# Fake statistical summary (distractor computation)
mean_cpu = sum(cpu_values) / len(cpu_values)
peak_cpu = max(cpu_values)
decoy_score = int((peak_cpu - mean_cpu) * 1.5)

# Unused list comprehension generating misleading intermediate (red herring)
spike_flags = [True for v in cpu_values if v > 200]
flag_count = len(spike_flags)  # Looks important but unused

# Another irrelevant transformation: count status distribution
status_counter = Counter()
for comp_list in log_data.values():
    for record in comp_list:
        status_counter[record['status']] += 1

# Diagnostic engine core
health_states = []
for comp, records in log_data.items():
    for record in records:
        state = evaluate_component_health(record['value'], comp, system_thresholds)
        health_states.append(state)

# Aggregate health occurrences
state_freq = defaultdict(int)
for state in health_states:
    state_freq[state] += 1

# Compute overload penalty points (key logic)
penalty_points = 0
for comp, records in log_data.items():
    for record in records:
        category_state = evaluate_component_health(record['value'], comp, system_thresholds)
        if category_state == 'overload':
            penalty_points += 2
        elif category_state == 'elevated':
            penalty_points += 1

# Secondary weight adjustment based on historical depth (fake recursion)
def calculate_adaptive_weight(depth):
    if depth <= 1:
        return 1
    return calculate_adaptive_weight(depth - 1) + 0.5  # Simulates decay

adaptive_factor = calculate_adaptive_weight(3)  # Returns 2.0

# Auxiliary calculation: total events (used in final formula)
total_events = len([r for sublist in log_data.values() for r in sublist])

# Misleading complex expression (not used)
theoretical_load = sum(v['value'] for k, v_list in log_data.items() for v in v_list) / total_events * 0.75

# Critical diagnostic processor (key statement)
def process_metrics(data, thresholds):
    total_penalty = 0
    for comp, records in data.items():
        for r in records:
            # Re-evaluate using same logic
            if r['value'] > thresholds[comp]:
                total_penalty += 2
            elif r['value'] > thresholds[comp] * 0.8:
                total_penalty += 1
    # Apply adaptive scaling and normalize by event count
    normalized_risk = (total_penalty * adaptive_factor) / total_events
    return int(normalized_risk * 1000)  # Final diagnostic code

# Execute main diagnostic
final_diagnostic = process_metrics(log_data, system_thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")