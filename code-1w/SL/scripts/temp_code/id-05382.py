from collections import defaultdict, Counter

# Simulated system telemetry data
timestamps = [1623456780, 1623456789, 1623456795, 1623456801, 1623456810]
raw_logs = [
    'ERR:cpu=98|mem=45|disk=88',
    'DBG:cpu=40|mem=60|disk=70',
    'INF:cpu=55|mem=50|disk=65',
    'ERR:cpu=92|mem=88|disk=91',
    'WRN:cpu=75|mem=80|disk=85'
]

# Irrelevant mapping table (distractor)
status_codes = {'OK': 200, 'WARN': 206, 'ERROR': 500, 'CRIT': 503}
code_lookup = defaultdict(lambda: 'UNKNOWN')
for k, v in status_codes.items():
    code_lookup[v] = k

# Misleading precomputed stats (red herring)
precomputed_avg = sum([88, 60, 50, 91, 85]) / 5  # Manual calc for disk only
adjusted_factor = 1.05
heuristic_offset = precomputed_avg * 0.15

# System thresholds (used later)
system_thresholds = {
    'critical_cpu': 90,
    'high_memory': 85,
    'disk_warning': 80
}

# Parse logs into structured format
def parse_log_entry(entry):
    level, specs = entry.split(':', 1)
    metrics = {}
    for pair in specs.split('|'):
        k, v = pair.split('=')
        metrics[k] = int(v)
    metrics['level'] = level
    return metrics

# Unused recursive function (dead code path)
def calculate_depth(n):
    if n <= 1:
        return 1
    return n + calculate_depth(n - 2)

# Another decoy function with bit manipulation (irrelevant)
def scramble_value(x):
    x = (x ^ 7) << 2
    x = (x ^ (x >> 3)) & 0xFF
    return x

# Real processing begins here
def analyze_errors(entries):
    error_count = 0
    cpu_loads = []
    for entry in entries:
        if 'ERR' in entry:
            error_count += 1
        parsed = parse_log_entry(entry)
        cpu_loads.append(parsed['cpu'])
    avg_cpu = sum(cpu_loads) / len(cpu_loads)
    return error_count, avg_cpu

# Accumulate diagnostic vectors
def build_diagnostic_vector(logs, thresholds):
    vec = defaultdict(int)
    temp_store = []  # Unused accumulation (distractor)

    for i, log in enumerate(logs):
        parts = log.split('|')
        cpu_val = int(parts[0].split('=')[1])
        mem_val = int(parts[1].split('=')[1])
        disk_val = int(parts[2].split('=')[1])

        # Real conditionals affecting outcome
        if cpu_val > thresholds['critical_cpu']:
            vec['crit_cpu_events'] += 1
        if mem_val > thresholds['high_memory']:
            vec['high_mem_events'] += 1
        if disk_val > thresholds['disk_warning']:
            vec['disk_warn_events'] += 1

        # Fake transformation chain (misdirection)
        scaled_disk = disk_val * 1.07
        adjusted_disk = scaled_disk - heuristic_offset
        temp_store.append(adjusted_disk)

    # Use of zip and enumerate together (required feature)
    indices = list(range(len(logs)))
    for idx, (ts, log) in enumerate(zip(timestamps, logs)):
        if idx % 2 == 0:
            vec['even_timestamp_alerts'] += 1

    return vec

# Main processing function
def process_metrics(log_data, config):
    # Step 1: Analyze raw errors
    err_count, mean_cpu = analyze_errors(log_data)
    
    # Step 2: Build diagnostic vector
    diagnosis = build_diagnostic_vector(log_data, config)
    
    # Step 3: Compute derived heuristics
    spike_ratio = mean_cpu / 50.0
    diagnosis['spike_ratio'] = spike_ratio
    
    # Step 4: Aggregate final score using weighted factors
    weight_cpu = 3.0
    weight_mem = 2.0
    weight_disk = 1.5
    
    severity = (
        diagnosis['crit_cpu_events'] * weight_cpu +
        diagnosis['high_mem_events'] * weight_mem +
        diagnosis['disk_warn_events'] * weight_disk +
        diagnosis['even_timestamp_alerts']
    )
    
    # Apply ratio modulation
    severity *= diagnosis['spike_ratio']
    
    # Dead branch with misleading calculation (distractor)
    if severity < 10:
        correction = scramble_value(int(severity))
        severity += correction * 0.01
    
    # Final computation
    baseline = 100
    final_score = baseline - severity
    
    # Critical output variable
    final_diagnostic = int(round(baseline - final_score))
    
    # Print required result
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execution point of interest
log_entries = raw_logs
final_diagnostic = process_metrics(log_entries, system_thresholds)