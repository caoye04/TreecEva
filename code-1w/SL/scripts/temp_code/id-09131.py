from collections import defaultdict, Counter
import math

# Simulated system telemetry data
telemetry_stream = [
    {'node': 'A', 'load': 85, 'errors': 3, 'active': True, 'timestamp': 1001},
    {'node': 'B', 'load': 45, 'errors': 0, 'active': True, 'timestamp': 1002},
    {'node': 'C', 'load': 92, 'errors': 7, 'active': False, 'timestamp': 1003},
    {'node': 'A', 'load': 88, 'errors': 1, 'active': True, 'timestamp': 1004},
    {'node': 'B', 'load': 53, 'errors': 2, 'active': True, 'timestamp': 1005},
    {'node': 'D', 'load': 12, 'errors': 0, 'active': True, 'timestamp': 1006}
]

# Irrelevant helper function (decoy)
def compute_efficiency_rating(x):
    return sum(i**2 for i in range(1, x+1)) if x > 0 else 0

# Unused statistical function (red herring)
def rolling_average(data, window=3):
    if len(data) < window:
        return [0]
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]

# Misleading transformation chain
def transform_readings(readings):
    temp_log = []
    for r in readings:
        temp_log.append({
            'id': r['node'] + '_proc',
            'val': (r['load'] * 1.05) + (r['errors'] * 2.3),
            'flag': r['load'] > 80 or r['errors'] > 5
        })
    # This computation is never used later (dead path)
    aggregated_flags = sum(1 for t in temp_log if t['flag'])
    return temp_log

# Distractor data structure
cache_simulator = {}
for i in range(6):
    key = f"block_{i}"
    cache_simulator[key] = {
        'size': (i + 1) * 16,
        'valid': i % 3 != 0,
        'tag': pow(2, i) ^ 255
    }

# Simulated log preprocessor with irrelevant string operations
def preprocess_logs(raw_logs):
    processed = []
    node_counter = Counter()
    status_map = defaultdict(int)
    
    for entry in raw_logs:
        node_id = entry['node'].lower()
        node_counter[node_id] += 1
        status_key = f"{entry['active']}_{node_id}"
        status_map[status_key] += 1
        
        # String manipulation distractions
        encoded_tag = ''.join([chr(ord(c) ^ 3) for c in node_id])
        padded_tag = encoded_tag.rjust(10, '*')
        
        processed.append({
            'node': entry['node'],
            'critical': entry['load'] > 80 and entry['errors'] > 0,
            'timestamp': entry['timestamp'],
            'meta_hash': hash(padded_tag + str(entry['timestamp'])) % 10000
        })
    
    # Unused aggregate statistics (distractor)
    avg_frequency = sum(node_counter.values()) / len(node_counter) if node_counter else 0
    max_status = max(status_map.values()) if status_map else 0
    
    return processed

# Core diagnostic engine
system_state = {
    'nodes_online': 3,
    'threshold_load': 80,
    'tolerance_errors': 5,
    'quorum_reached': True
}

def evaluate_node_health(metrics, config):
    risk_score = 0
    critical_nodes = 0
    
    for m in metrics:
        load_risk = 1 if m['load'] > config['threshold_load'] else 0
        error_risk = 1 if m['errors'] >= config['tolerance_errors'] else 0
        inactive_penalty = 2 if not m['active'] else 0
        
        if load_risk or error_risk:
            risk_score += 1.5 + (m['load'] / 100) * 0.5
        if load_risk and error_risk:
            risk_score += 1.0
        risk_score += inactive_penalty
        
        if m['load'] > config['threshold_load'] and m['errors'] > 0:
            critical_nodes += 1
    
    # Secondary scoring using bitwise logic (partially relevant)
    final_flag = 0
    if critical_nodes > 0:
        final_flag |= 1 << 3
    if risk_score > 5.0:
        final_flag |= 1 << 1
    
    return risk_score, critical_nodes, final_flag

# Data fusion layer with dictionary operations
def fuse_diagnostics(primary, secondary, weights=None):
    if weights is None:
        weights = {'primary': 0.7, 'secondary': 0.3}
    
    # Simulate score calibration
    calibrated = (primary * weights['primary']) + (secondary * weights['secondary'])
    
    # Extra map-reduce style distraction
    dummy_map = {k: v*1.1 for k, v in weights.items()}
    dummy_reduce = sum(dummy_map.values())
    
    return round(calibrated, 4)

# Main processing pipeline
log_data = preprocess_logs(telemetry_stream)

# Irrelevant list transformation
reversed_logs = []
for i in range(len(log_data) - 1, -1, -1):
    reversed_logs.append({
        'node': log_data[i]['node'],
        'rev_hash': log_data[i]['meta_hash'] ^ 0xFFFF
    })

# Another decoy operation: string-based checksum
def compute_string_checksum(items):
    total = 0
    for item in items:
        s = item['node'] + str(item['timestamp'])
        total += sum(ord(c) for c in s)
    return total % 97

checksum_val = compute_string_checksum(log_data)  # Never used

# Actual evaluation
base_risk, crit_count, flag_code = evaluate_node_health(telemetry_stream, system_state)

# Simulate auxiliary diagnostic from logs
log_severity = 0
for record in log_data:
    if record['critical']:
        log_severity += 2.5

# Key integration function
def process_metrics(log_diagnostics, state_config):
    # Extract meaningful signals
    active_node_count = sum(1 for entry in telemetry_stream if entry['active'])
    total_error_incidents = sum(e['errors'] for e in telemetry_stream)
    
    # Compute primary indicators
    load_distribution = [e['load'] for e in telemetry_stream]
    avg_load = sum(load_distribution) / len(load_distribution)
    peak_load = max(load_distribution)
    
    # Diagnostic fusion
    base_score = 100.0
    if avg_load > 60:
        base_score -= 15
    if peak_load > 90:
        base_score -= 20
    if total_error_incidents > 10:
        base_score -= 25
    if crit_count > 1:
        base_score -= 30
    
    # Apply log-derived adjustments
    adjustment_factor = 1.0
    if log_severity > 4.0:
        adjustment_factor *= 0.8
    
    intermediate_result = base_score * adjustment_factor
    
    # Final nonlinear transformation
    final_value = int(intermediate_result - (math.log(peak_load + 1) * 3))
    
    # Dead code branch (misleading)
    if final_value < 0:
        fallback = pow(abs(final_value), 0.5)
        final_value = int(fallback)
    
    return final_value

# Execute main diagnostic
diagnostic_snapshot = process_metrics(log_data, system_state)
final_diagnostic = process_metrics(log_data, system_state)

print(f"Result: {final_diagnostic}")