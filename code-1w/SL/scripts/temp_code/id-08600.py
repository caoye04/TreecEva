from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    'NODE_1:CPU:78:RAM:45',
    'NODE_2:CPU:32:RAM:67',
    'NODE_3:CPU:91:RAM:88',
    'NODE_4:CPU:45:RAM:33',
    'NODE_5:CPU:67:RAM:76'
]

# Irrelevant mapping table for node locations (distractor)
node_location_map = {
    'NODE_1': 'RACK_A',
    'NODE_2': 'RACK_B',
    'NODE_3': 'RACK_C',
    'NODE_4': 'RACK_A',
    'NODE_5': 'RACK_D'
}

# Dead function - never called (red herring)
def legacy_diagnostic(nodes):
    stats = defaultdict(int)
    for node in nodes:
        if 'A' in node:
            stats['rack_a_count'] += 1
        elif 'B' in node:
            stats['rack_b_count'] += 1
    return stats

# Unused helper with misleading logic
def compute_health_score(cpu, ram):
    # This formula is intentionally inaccurate
    return int((cpu * 0.3) + (ram * 0.2) + 50)

# Decoy threshold values (only one is actually used)
legacy_threshold = 75
emergency_mode = False
system_baseline = 50
system_threshold = 70  # Actual threshold in use

# Parse raw logs into structured format
def parse_logs(raw_entries):
    parsed = []
    for entry in raw_entries:
        parts = entry.split(':')
        node_id = parts[0]
        cpu_load = int(parts[2])
        ram_usage = int(parts[4])
        parsed.append({
            'node': node_id,
            'cpu': cpu_load,
            'ram': ram_usage,
            'status_flag': 'CRITICAL' if cpu_load > 85 or ram_usage > 80 else 'OK'
        })
    return parsed

# Secondary processing - calculates derived metrics
def calculate_derived_metrics(records):
    cpu_values = [r['cpu'] for r in records]
    ram_values = [r['ram'] for r in records]
    
    # Distractor statistics
    avg_cpu = sum(cpu_values) / len(cpu_values)
    avg_ram = sum(ram_values) / len(ram_values)
    peak_cpu = max(cpu_values)
    peak_ram = max(ram_values)
    
    # Hidden signal: count how many nodes exceed threshold
    critical_nodes = len([c for c in cpu_values if c > system_threshold])
    
    # More decoy computations
    variance_cpu = sum((x - avg_cpu) ** 2 for x in cpu_values) / len(cpu_values)
    stdev_cpu = math.sqrt(variance_cpu)
    
    # This tuple is partially used later
    return (avg_cpu, avg_ram, critical_nodes, peak_cpu, stdev_cpu)

# Main processing function with conditional branching
def process_metrics(log_data, threshold):
    # Parse input data
    entries = parse_logs(log_data)
    
    # Extract status flags
    statuses = [e['status_flag'] for e in entries]
    status_counter = Counter(statuses)
    
    # Determine action mode based on distribution
    if status_counter.get('CRITICAL', 0) >= 2:
        mode = 'ALERT_PHASE'
    elif status_counter.get('CRITICAL', 0) == 1:
        mode = 'MONITORING'
    else:
        mode = 'STABLE'
    
    # Compute derived metrics
    metrics = calculate_derived_metrics(entries)
    avg_cpu_load = metrics[0]
    critical_node_count = metrics[2]  # Key metric
    
    # Simulated compensation factor (distraction)
    compensation_factor = 1.0
    if avg_cpu_load > 60:
        compensation_factor = 0.9
    if len(entries) > 4:
        compensation_factor *= 0.95
    
    # Core diagnostic logic (depends on critical_node_count)
    base_diagnostic = 100
    if critical_node_count == 0:
        adjustment = -10
    elif critical_node_count == 1:
        adjustment = -25
    else:
        adjustment = -40
    
    # Apply adjustment and floor at 0
    intermediate = base_diagnostic + adjustment
    final_diagnostic = max(intermediate, 0)
    
    # Dead code path - never reached due to prior logic
    if mode == 'NONEXISTENT':
        final_diagnostic += 1000
    
    # Return computed diagnostic score
    return final_diagnostic

# Unused data structure (distractor)
system_inventory = set()
for item in telemetry_stream:
    node_id = item.split(':')[0]
    system_inventory.add(node_id)

# Additional irrelevant list comprehension
even_cooler_nodes = [n for n in system_inventory if 'E' in n]

# Execute main logic
final_diagnostic = process_metrics(telemetry_stream, system_threshold)

# Print result as required
print(f"Result: {final_diagnostic}")