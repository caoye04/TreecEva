import math

# Irrelevant data structures and variables (distractors)
user_preferences = {'theme': 'dark', 'notifications': True, 'auto_save': False}
temp_buffer = [0] * 15
device_id = hash('sensor_node_7')

# Simulated system log with mixed metrics (real + noise)
data_log = [
    {'type': 'cpu', 'value': 72.5, 'timestamp': 1678886400},
    {'type': 'mem', 'value': 4096, 'timestamp': 1678886401},
    {'type': 'net_in', 'value': 150, 'timestamp': 1678886402},
    {'type': 'net_out', 'value': 200, 'timestamp': 1678886403},
    {'type': 'cpu', 'value': 85.0, 'timestamp': 1678886404},
    {'type': 'disk_read', 'value': 320, 'timestamp': 1678886405},
    {'type': 'disk_write', 'value': 180, 'timestamp': 1678886406},
    {'type': 'cpu', 'value': 67.0, 'timestamp': 1678886407}
]

# Decoy function – looks relevant but unused in critical path
def calculate_health_score(metrics):
    base = sum(m.get('value', 0) for m in metrics if m['type'] == 'mem')
    penalty = len([m for m in metrics if m['type'] == 'disk_write']) * 10
    return max(0, base - penalty)

# Auxiliary transformation (partially used)
def extract_cpu_loads(log_entries):
    cpu_entries = [e['value'] for e in log_entries if e['type'] == 'cpu']
    normalized = [min(100, load + 3.5) for load in cpu_entries]  # Artificial boost
    filtered = [load for load in normalized if load > 70]  # Only high loads
    return filtered if filtered else [0]

# Complex processing with conditional logic and distractors
def analyze_response_time(entry):
    if entry['type'] in ['net_in', 'net_out']:
        return entry['value'] * 0.01
    elif entry['type'] == 'disk_read':
        return math.log(entry['value']) * 0.5
    return 0.0

# Main processing chain with red herrings and multiple concepts
def process_metrics(log):
    total_events = len(log)
    critical_count = 0
    response_accum = 0.0
    peak_memory = 0
    cpu_load_list = []

    # Irrelevant counters (distractor)
    security_checks_run = 0
    encryption_rounds = 0
    for i in range(3):
        encryption_rounds += pow(2, i)  # Dead computation
        security_checks_run += 1

    # Real processing begins
    for record in log:
        if record['type'] == 'mem':
            peak_memory = max(peak_memory, record['value'])

        # Accumulate transformed response times
        response_accum += analyze_response_time(record)

        # Track high-severity events
        if record['type'] in ['cpu', 'disk_write'] and record['value'] > 175:
            critical_count += 1

        # Populate CPU list for later analysis
        if record['type'] == 'cpu':
            cpu_load_list.append(record['value'])

    # Secondary processing with conditional expression
    avg_cpu = sum(cpu_load_list) / len(cpu_load_list) if cpu_load_list else 0
    high_load_periods = len([load for load in cpu_load_list if load >= 80])

    # Distractor: unused complex structure
    diagnostics = {
        'stability_index': 100 - avg_cpu,
        'throughput': sum(e['value'] for e in log if e['type'].startswith('net')),
        'io_ratio': (lambda x, y: x / (y + 1))(sum(e['value'] for e in log if e['type'] == 'disk_write'), 100),
        'temporal_density': total_events / (log[-1]['timestamp'] - log[0]['timestamp'] + 1)
    }

    # Core efficiency formula (this determines the answer)
    base_efficiency = 100 - avg_cpu
    penalty_factor = critical_count * 3.7
    bonus = 5 if high_load_periods < 2 else 0
    dynamic_adjustment = 2.5 if response_accum > 4.0 else -1.2

    # Key statement: final efficiency rating
    efficiency_rating = base_efficiency - penalty_factor + bonus + dynamic_adjustment

    # Dead code path (misleading)
    if efficiency_rating < 0:
        efficiency_rating = abs(efficiency_rating)  # Never reached in this case

    # Final output construction (includes irrelevant fields)
    final_output = {
        'result_code': 200,
        'efficiency_rating': efficiency_rating,
        'diagnostics': diagnostics,
        'checksum': hash(str(efficiency_rating)) % 10000
    }

    return final_output

# Execution point of interest
final_output = process_metrics(data_log)

# Output target result
print(f"Target result: {final_output['efficiency_rating']}")