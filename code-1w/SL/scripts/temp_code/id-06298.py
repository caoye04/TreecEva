from collections import defaultdict, Counter
import math

# Simulated sensor data from a distributed monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1, 23.7]
humidity_readings = [45, 47, 50, 44, 52, 48, 46, 51]
pressure_readings = [1013, 1015, 1012, 1016, 1014, 1011, 1017, 1013]

# Irrelevant auxiliary data (distractor)
legacy_codes = {'A': 10, 'B': 20, 'C': 30, 'D': 40}
scaling_factor = 1.05
dummy_matrix = [[i * j for j in range(3)] for i in range(3)]

# System state flags
system_state = {
    'nodes_active': 8,
    'primary_redundant': True,
    'failover_mode': False,
    'last_sync_delta': 127
}

# Log data with mixed event types
log_data = [
    {'event': 'TEMP_NORMAL', 'node': 3, 'timestamp': 1678886400},
    {'event': 'HUMIDITY_HIGH', 'node': 5, 'timestamp': 1678886405},
    {'event': 'PRESSURE_DROP', 'node': 2, 'timestamp': 1678886410},
    {'event': 'TEMP_NORMAL', 'node': 7, 'timestamp': 1678886415},
    {'event': 'HUMIDITY_HIGH', 'node': 1, 'timestamp': 1678886420},
    {'event': 'PRESSURE_STABLE', 'node': 4, 'timestamp': 1678886425}
]

# Decoy function – never called (dead code path)
def deprecated_analysis(data):
    return sum(x ** 0.5 for x in data if x > 30)

# Auxiliary transformation (partially relevant)
def normalize(values):
    mean_val = sum(values) / len(values)
    return [v - mean_val for v in values]

# Bit manipulation for checksum (misleading intermediate)
def compute_checksum(timestamp):
    ts_bin = bin(timestamp ^ 0xABCD)[2:]
    return ts_bin.count('1') % 4

# Core processing pipeline
checksums = [compute_checksum(entry['timestamp']) for entry in log_data]
event_counter = Counter([entry['event'] for entry in log_data])

# Set operations to detect anomaly patterns (relevant)
anomaly_events = {'HUMIDITY_HIGH', 'PRESSURE_DROP'}
observed_events = {entry['event'] for entry in log_data}
critical_occurrences = len(anomaly_events & observed_events)

# Distractor: unused statistical computation
variance_temp = sum((x - sum(temperature_readings)/len(temperature_readings))**2 for x in temperature_readings) / len(temperature_readings)
entropy_humidity = -sum((h/100) * math.log(h/100 + 1e-9) for h in humidity_readings)

# Conditional logic with nested dependencies
def evaluate_stability(metrics):
    base_score = 100
    if metrics['nodes_active'] >= 6:
        base_score += 20
        if not metrics['failover_mode']:
            base_score += 30
            if metrics['last_sync_delta'] < 200:
                base_score += 15
    return base_score

# Data transformation using defaultdict (relevant)
aggregated_logs = defaultdict(list)
for entry in log_data:
    aggregated_logs[entry['event']].append(entry['node'])

# Complex conditional expression (python idiom)
consensus_state = 'STABLE' if system_state['primary_redundant'] and system_state['nodes_active'] > 5 else 'WARNING'

# Secondary metric derived from set and list operations
effective_coverage = len(aggregated_logs.keys()) * system_state['nodes_active'] // 2

# Main processing function
def process_metrics(logs, state):
    # Step 1: Count critical anomalies
    event_types = [record['event'] for record in logs]
    severity_levels = defaultdict(int)
    for etype in event_types:
        if 'HIGH' in etype or 'DROP' in etype:
            severity_levels[etype] += 1
    
    # Step 2: Compute weighted impact
    impact_score = 0
    for event, count in severity_levels.items():
        if 'HUMIDITY' in event:
            impact_score += count * 17
        elif 'PRESSURE' in event:
            impact_score += count * 23
    
    # Step 3: Adjust by system stability
    stability_bonus = evaluate_stability(state)
    
    # Step 4: Apply bit-derived modifier (red herring: looks important but minor)
    checksum_modifier = sum(checksums) % 5
    
    # Step 5: Combine using non-linear transformation
    raw_diagnostic = (impact_score * 3) + stability_bonus - (effective_coverage * 2)
    
    # Step 6: Final adjustment using conditional expression
    final_adjustment = 10 if consensus_state == 'STABLE' else -10
    
    # FINAL COMPUTATION (key statement)
    final_diagnostic = int(raw_diagnostic + final_adjustment - checksum_modifier)
    
    # Irrelevant formatting (distractor)
    formatted_result = f"DIAG-{final_diagnostic:04d}"
    
    return final_diagnostic

# Execute main logic
final_diagnostic = process_metrics(log_data, system_state)

# Print result as required
print(f"Result: {final_diagnostic}")