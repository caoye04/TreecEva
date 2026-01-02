from collections import defaultdict, Counter
import math

def analyze_node_traffic(node_id, logs):
    # Irrelevant analysis function (dead end)
    counts = defaultdict(int)
    for log in logs:
        if log['node'] == node_id:
            counts[log['type']] += 1
    return sum(counts.values()) * 0.1  # Red herring result

def validate_checksum(data):
    # Unused validation function (distractor)
    chk = 0
    for b in data.encode():
        chk ^= b
    return chk == 0

def build_routing_table(nodes):
    # Complex but irrelevant routing logic
    table = {}
    for i, node in enumerate(nodes):
        hops = (i * 37) % 7
        table[node['id']] = {'hops': hops, 'active': node['status'] == 'up'}
    return table

def extract_anomalies(logs):
    # Misleading anomaly detection with no impact
    anomalies = []
    for log in logs:
        if 'ERROR' in log['msg'] and log['priority'] > 5:
            anomalies.append(log['timestamp'])
    smoothed = [a + 0.5 for a in anomalies]  # Decoy transformation
    return len(smoothed) > 3

def calculate_entropy(values):
    # Real computation, but used indirectly
    freq = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * math.log(p)
    return round(entropy, 4)

def compute_integrity_score(nodes, logs):
    # Core relevant function
    status_weights = {'up': 1.0, 'degraded': 0.5, 'down': 0.0}
    total_weight = 0.0
    active_count = 0

    # Extract node statuses
    for node in nodes:
        weight = status_weights.get(node['status'], 0.0)
        total_weight += weight
        if node['status'] == 'up':
            active_count += 1

    # Parse firewall logs for suspicious activity
    blocked_count = 0
    severity_sum = 0
    for log in logs:
        if log['action'] == 'blocked':
            blocked_count += 1
            severity_sum += log['risk_level']

    avg_severity = severity_sum / blocked_count if blocked_count > 0 else 0

    # Compute node diversity metric using set operations
    regions = {n['region'] for n in nodes}
    critical_regions = {'us-east', 'eu-west'}
    region_overlap = len(regions & critical_regions)

    # Combine metrics with weighted formula
    base_score = total_weight * 100
    penalty = avg_severity * 2.5
    bonus = region_overlap * 5

    # Final integrity score
    final_score = base_score - penalty + bonus

    # Additional red herrings below
    temp_debug = [math.sin(i) for i in range(active_count)]  # Dead computation
    dummy_map = defaultdict(lambda: 'unknown')
    for log in logs:
        dummy_map[log['src_ip']] += '_logged'  # Meaningless accumulation

    return int(round(final_score))

# Simulated network infrastructure data
network_nodes = [
    {'id': 'N001', 'status': 'up', 'region': 'us-east', 'load': 0.6},
    {'id': 'N002', 'status': 'up', 'region': 'us-west', 'load': 0.4},
    {'id': 'N003', 'status': 'degraded', 'region': 'eu-west', 'load': 0.8},
    {'id': 'N004', 'status': 'up', 'region': 'ap-south', 'load': 0.3},
    {'id': 'N005', 'status': 'down', 'region': 'us-east', 'load': 0.0},
]

firewall_logs = [
    {'timestamp': 1710000001, 'src_ip': '192.168.1.10', 'action': 'allowed', 'risk_level': 1, 'msg': 'normal'},
    {'timestamp': 1710000002, 'src_ip': '10.5.8.22', 'action': 'blocked', 'risk_level': 8, 'msg': 'malware'},
    {'timestamp': 1710000003, 'src_ip': '172.16.3.9', 'action': 'blocked', 'risk_level': 6, 'msg': 'scan'},
    {'timestamp': 1710000004, 'src_ip': '192.168.1.15', 'action': 'allowed', 'risk_level': 2, 'msg': 'normal'},
    {'timestamp': 1710000005, 'src_ip': '8.8.8.8', 'action': 'blocked', 'risk_level': 9, 'msg': 'attack'},
    {'timestamp': 1710000006, 'src_ip': '10.0.0.1', 'action': 'allowed', 'risk_level': 1, 'msg': 'keepalive'},
]

# Trigger irrelevant functions to increase distraction
_ = analyze_node_traffic('N001', firewall_logs)
_ = build_routing_table(network_nodes)
dummy_anomalies = extract_anomalies(firewall_logs)

# Critical execution point
final_diagnostic = compute_integrity_score(network_nodes, firewall_logs)

# Output the target result
print(f"Result: {final_diagnostic}")