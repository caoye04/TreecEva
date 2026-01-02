import math

# System health monitoring with network diagnostics

def detect_loopback(nodes):
    loopbacks = set()
    for node in nodes:
        if node.startswith('127.') or node == '::1':
            loopbacks.add(node)
    return loopbacks


def calculate_latency_score(base, jitter, packet_loss):
    # Irrelevant computation - distractor
    score = base * (1 + jitter / 100)
    penalty = packet_loss * 5
    return max(1, 100 - penalty - jitter)


def simulate_propagation_delay(distance_km):
    # Physics-based delay (ms) - red herring
    speed_of_light_fraction = 200000  # km/s approx
    return round((distance_km / speed_of_light_fraction) * 1000, 3)


def analyze_segment(segments, threshold=85):
    unstable = []
    for seg_name, metrics in segments.items():
        load = metrics['utilization']
        errors = metrics['error_count']
        if load > threshold and errors > 10:
            unstable.append(seg_name)
    return unstable


def compute_redundancy_factor(primary, backup_list):
    # Unused function - dead code path
    return 1 + len([b for b in backup_list if b != ''])


def identify_unique_ips(log_entries):
    # Extracts unique IPs from logs - seems relevant but not used in final result
    ips = set()
    for entry in log_entries:
        if 'src_ip' in entry:
            ips.add(entry['src_ip'])
        if 'dst_ip' in entry:
            ips.add(entry['dst_ip'])
    return ips


def flag_anomalous_ports(port_list):
    # Misleading function: checks for unusual ports but not used
    privileged = [p for p in port_list if p < 1024]
    ephemeral = [p for p in port_list if p > 49152]
    return len(privileged) > 5 or len(ephemeral) > 20


def aggregate_anomalies(network_segments):
    # Core logic buried in noise
    anomalies = []
    
    # Distractor: fake data structures
    temp_cache = {'state': 'pending', 'retry_count': 3}
    audit_trail = []
    
    for seg_name, data in network_segments.items():
        # Key logic: count how many times error rate exceeds dynamic threshold
        baseline = data['baseline_error_rate']
        readings = data['recent_readings']  # list of error counts per minute
        window_size = 5
        triggers = 0
        
        # Sliding window analysis - actual critical computation
        for i in range(len(readings) - window_size + 1):
            window = readings[i:i + window_size]
            avg = sum(window) / len(window)
            if avg > baseline * 2.5:  # Threshold condition
                triggers += 1
        
        # Only add if triggers exceed secondary filter
        if triggers >= 3:
            anomalies.append(triggers)
    
    # Final accumulation - this is the real answer
    total_anomalies = sum(anomalies)
    
    # More distractions below
    compression_ratio = len(anomalies) / (total_anomalies + 1) if total_anomalies else 0
    diagnostic_code = hash('anomaly_engine_v2') % 1000
    
    # Critical assignment - target of the question
    final_diagnostic = total_anomalies
    
    # Fake reporting layer
    report = {
        'status': 'completed',
        'entries_processed': 1,
        'final_diagnostic': final_diagnostic,
        'debug_hash': diagnostic_code
    }
    
    return final_diagnostic

# Simulated input data
network_segments = {
    'core-alpha': {
        'baseline_error_rate': 4,
        'recent_readings': [3, 5, 12, 14, 16, 18, 4, 6, 2, 3, 11, 13, 15, 17, 19, 21, 5, 4]
    },
    'edge-bravo': {
        'baseline_error_rate': 6,
        'recent_readings': [2, 3, 1, 4, 2, 3, 5, 6, 7, 8, 9, 10, 2, 1]
    },
    'dmz-gamma': {
        'baseline_error_rate': 5,
        'recent_readings': [4, 6, 15, 18, 20, 22, 25, 3, 5, 14, 16, 19, 24, 26, 28]
    }
}

# Log entries - look important but unused in final calculation
log_entries = [
    {'src_ip': '192.168.1.10', 'dst_ip': '10.0.0.5', 'port': 8080},
    {'src_ip': '172.16.2.20', 'dst_ip': '127.0.0.1', 'port': 22},
    {'src_ip': '10.0.0.5', 'dst_ip': '8.8.8.8', 'port': 443}
]

# Port list - part of decoy logic
active_ports = [22, 80, 443, 8080, 3389, 53, 25, 110, 143, 993, 995, 50000, 50001, 50002]

# Initial setup - irrelevant calls
loopback_nodes = detect_loopback(['127.0.0.1', '10.1.1.1', '::1'])
latency_score = calculate_latency_score(95, 4.2, 0.8)
distance_delay = simulate_propagation_delay(5000)

# Real execution begins here
unstable_segs = analyze_segment({
    'core-alpha': {'utilization': 92, 'error_count': 25},
    'edge-bravo': {'utilization': 78, 'error_count': 8},
    'dmz-gamma': {'utilization': 89, 'error_count': 18}
})

# This call looks like it depends on prior results but doesn't
unique_ips = identify_unique_ips(log_entries)
port_alert = flag_anomalous_ports(active_ports)

# Critical statement - target of the evaluation question
final_diagnostic = aggregate_anomalies(network_segments)

# Output result as required
print(f"Result: {final_diagnostic}")