import math

# Simulated telemetry data from a distributed sensor network
telemetry_packets = [
    {'id': 'S1', 'readings': [23.1, 45.6, 12.8], 'status': 'active', 'version': 1},
    {'id': 'S2', 'readings': [19.5, 41.2, 15.3], 'status': 'active', 'version': 1},
    {'id': 'S3', 'readings': [], 'status': 'inactive', 'version': 0}
]

# Auxiliary lookup table for calibration (irrelevant to final result)
calibration_map = {
    'gain': 1.02,
    'offset': -0.35,
    'thresholds': {'low': 10.0, 'high': 50.0}
}

# System-wide constants (some are decoys)
MAX_NODES = 32
HEALTHY_THRESHOLD = 0.75
CRC_POLY = 0xEDB88320
DEFAULT_TIMEOUT = 5000

# Raw binary configuration flags (misleading intermediate values)
config_flags = 0b1101011010101101
encryption_enabled = bool(config_flags & 0b1000000000000000)
compression_mode = (config_flags >> 8) & 0b111
priority_level = config_flags & 0xFF

# Historical node states - mostly inactive (distractor data structure)
historical_states = {
    'S1': ['active', 'active', 'failed', 'active'],
    'S2': ['active', 'degraded', 'active'],
    'S3': ['inactive', 'inactive']
}

# Active node registry built from telemetry (partially relevant)
active_nodes = []
node_health = {}
consolidated_readings = []

for packet in telemetry_packets:
    if packet['status'] == 'active':
        active_nodes.append(packet['id'])
        if packet['readings']:
            avg_reading = sum(packet['readings']) / len(packet['readings'])
        else:
            avg_reading = 0.0
        node_health[packet['id']] = avg_reading > 15.0
        consolidated_readings.extend(packet['readings'])

# Derived metrics with red herrings
packet_count = len(telemetry_packets)
healthy_node_count = sum(1 for h in node_health.values() if h)
average_sensor_value = sum(consolidated_readings) / len(consolidated_readings) if consolidated_readings else 0.0

# Bit manipulation routine (completely irrelevant)
def compute_checksum(data_list):
    checksum = 0xFFFF
    for val in data_list:
        checksum ^= int(val)
        for _ in range(8):
            if checksum & 1:
                checksum = (checksum >> 1) ^ CRC_POLY
            else:
                checksum >>= 1
    return checksum

# Decoy function that's never called
def analyze_historical_trends(hist):
    trend_scores = {}
    for node_id, states in hist.items():
        score = 0
        for i in range(1, len(states)):
            if states[i] == 'active' and states[i-1] != 'active':
                score += 1
            elif states[i] != 'active' and states[i-1] == 'active':
                score -= 2
        trend_scores[node_id] = score
    return trend_scores

# Real processing begins here
system_state = {
    'nodes': active_nodes,
    'health': node_health,
    'metrics': {
        'avg_value': average_sensor_value,
        'count': healthy_node_count
    }
}

log_data = []
for reading in consolidated_readings:
    entry = {
        'raw': reading,
        'normalized': reading * calibration_map['gain'] + calibration_map['offset'],
        'category': 'critical' if reading > 40.0 else 'standard'
    }
    log_data.append(entry)

# Secondary processing with sorting (partially relevant)
sorted_logs = sorted(log_data, key=lambda x: x['raw'], reverse=True)

critical_count = sum(1 for e in sorted_logs if e['category'] == 'critical')

# Diagnostic calculation tree
base_score = len(active_nodes) * 10
health_bonus = sum(15 for h in node_health.values() if h)  # S1 and S2 healthy
size_penalty = 0
if len(consolidated_readings) > 5:
    size_penalty = 10

# Another decoy computation using sets (irrelevant)
unique_values = set(round(entry['raw']) for entry in log_data)
expected_range = set(range(10, 50))
coverage_rate = len(unique_values & expected_range) / len(expected_range)

# Main aggregation function
def aggregate_diagnostics(logs, state):
    total_magnitude = 0.0
    for entry in logs:
        if entry['category'] == 'critical':
            total_magnitude += entry['raw'] ** 0.5
        else:
            total_magnitude += entry['raw'] / 10
    
    node_factor = len(state['nodes'])
    health_ratio = sum(state['health'].values()) / len(state['health']) if state['health'] else 0
    
    # Complex formula with dummy components
    temp_debug = math.sin(math.pi / 6)  # Always 0.5, but looks important
    adjustment = 1.0
    if health_ratio >= HEALTHY_THRESHOLD:
        adjustment = 1.25
    
    return total_magnitude * node_factor * adjustment

# Final processing pipeline
intermediate_metric = aggregate_diagnostics(log_data, system_state)

# Red herring: string processing with case conversion (irrelevant)
node_signatures = [f"{nid}-{priority_level}" for nid in active_nodes]
upper_sigs = [sig.upper() for sig in node_signatures]
flattened_sig = ''.join(upper_sigs).replace('S', '5')

# Critical statement containing the answer
def process_metrics(log_entries, sys_state):
    # Extract critical readings
    critical_sum = sum(e['raw'] for e in log_entries if e['category'] == 'critical')
    
    # Node-based multiplier
    multiplier = len(sys_state['nodes'])
    
    # Health-weighted offset
    healthy_nodes = sum(1 for h in sys_state['health'].values() if h)
    offset = healthy_nodes * 2
    
    # Irrelevant sort operation
    sorted_critical = sorted([e['raw'] for e in log_entries if e['category'] == 'critical'], reverse=True)
    
    # Decoy dictionary operations
    stats_cache = {
        'first_pass': {'result': 999, 'valid': False},
        'debug_snapshot': {'timestamp': 1678886400, 'level': 'warning'}
    }
    stats_cache['first_pass']['processed'] = True
    
    # Actual answer computation
    result = critical_sum * multiplier + offset
    
    # More decoys
    if 'debug_snapshot' in stats_cache:
        stats_cache['debug_snapshot']['result_code'] = 0xDEAD
    
    return result

final_diagnostic = process_metrics(log_data, system_state)
print(f"Target result: {final_diagnostic}")