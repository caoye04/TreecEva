import itertools

def monitor_subsystem(subsystem_data, threshold=75):
    # Irrelevant monitoring logic
    alert_count = 0
    for entry in subsystem_data:
        if entry > threshold:
            alert_count += 1
    return alert_count

def compute_diagnostic_score(data_stream):
    # Complex but ultimately unused scoring function
    base_score = sum(data_stream) / len(data_stream)
    variance = sum((x - base_score) ** 2 for x in data_stream) / len(data_stream)
    penalty = 0
    for i in range(1, len(data_stream)):
        if data_stream[i] < data_stream[i-1]:
            penalty += 1
    return base_score - (penalty * 0.5) + (variance / 10)

def evaluate_consistency(patterns):
    # Unused consistency checker
    transitions = 0
    for p in patterns:
        transitions += len([i for i in range(1, len(p)) if p[i] != p[i-1]])
    return transitions > 10

def generate_status_fingerprint(timestamps, mode='basic'):
    # Distractor: generates hash-like fingerprint but not used in final result
    fingerprint = 1
    for t in timestamps:
        fingerprint ^= int(t % 100) * 31
    return fingerprint ^ len(timestamps)

def analyze_system_state(metrics, log_entries):
    # Core logic hidden among distractions
    cumulative = 0
    event_flags = []
    
    # Process metrics through multiple filters
    filtered_metrics = [m for m in metrics if 20 <= m <= 90]
    
    # Red herring: complex transformation with no impact
    temp_analysis = {}
    for idx, val in enumerate(filtered_metrics):
        temp_analysis[f'node_{idx}'] = {
            'raw': val,
            'adj': (val * 1.05) % 88,
            'flag': val > 70
        }
    
    # Real logic begins here — counting critical events
    critical_threshold = 80
    for entry in log_entries:
        if 'ERROR' in entry and 'RECOVERED' not in entry:
            cumulative += 1
    
    # Decoy conditional branch that looks important
    if len(log_entries) > 50:
        snapshot = metrics[::3]
        avg_snapshot = sum(snapshot) / len(snapshot)
        if avg_snapshot > 60:
            cumulative += 2  # Misleading adjustment never actually needed

    # Actual key computation — count high-severity entries
    severity_count = 0
    for log in log_entries:
        words = log.split()
        for word in words:
            if word == 'CRITICAL':
                severity_count += 1

    # Combine with metric outliers
    outlier_count = len([m for m in metrics if m > 85])

    # Final computation buried in noise
    intermediate = cumulative * 3 + severity_count * 2
    correction = 0
    
    # Real correction based on dictionary lookup
    level_map = {'low': 1, 'med': 3, 'high': 6}
    refs = ['med', 'high', 'low']
    for r in refs:
        correction += level_map[r]
    
    # Key line: this is where the answer is determined
    final_diagnostic = intermediate - correction + outlier_count
    
    # Dead code path — never reached
    if final_diagnostic < 0:
        final_diagnostic = 0
    
    return final_diagnostic

# Simulated input data
health_metrics = [65, 70, 88, 92, 73, 86, 68, 77, 89, 74, 62, 91, 69, 81, 75]
system_log = [
    'INFO: system boot',
    'DEBUG: module init',
    'ERROR: disk read timeout',
    'WARNING: high latency',
    'ERROR: network drop',
    'CRITICAL: memory overflow',
    'INFO: retrying connection',
    'ERROR: auth failure',
    'CRITICAL: memory overflow',
    'RECOVERED: disk read',
    'INFO: checkpoint saved',
    'ERROR: cache corruption',
    'CRITICAL: memory overflow',
    'DEBUG: garbage collection',
    'ERROR: database lock'
]

# Unused auxiliary data structures
auxiliary_nodes = {f'node_{i}': {'status': 'active', 'load': val} for i, val in enumerate(health_metrics)}
timestamp_sequence = list(itertools.chain(*[[t]*2 for t in range(10, 60, 3)]))

# Distractor function calls
monitor_subsystem(health_metrics, threshold=80)
generate_status_fingerprint(timestamp_sequence)

# Core execution point
final_diagnostic = analyze_system_state(health_metrics, system_log)
print(f"Result: {final_diagnostic}")