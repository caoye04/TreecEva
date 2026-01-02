import math

# Simulated network node data with diagnostic flags
def collect_node_metrics(node_list):
    metrics = {}
    for node in node_list:
        base_load = node['load']
        temp_factor = math.sin(node['temp']) + 0.5
        jitter = math.log(abs(node['response_time']) + 1)
        # Irrelevant transformation (distractor)
        phantom_score = (base_load ** 0.5) * (jitter / (temp_factor + 1e-5))
        health_indicator = base_load * temp_factor + jitter
        metrics[node['id']] = {
            'health': max(0, min(100, health_indicator)),
            'critical': node['temp'] > 75,
            'redundant_flag': phantom_score > 10
        }
    return metrics

# Parse system logs for anomaly patterns
def analyze_log_stream(log_entries):
    severity_map = {'INFO': 1, 'WARN': 2, 'ERROR': 3, 'CRITICAL': 4}
    pattern_count = {key: 0 for key in severity_map.keys()}
    timestamps = []n    redundant_aggregates = []

    for entry in log_entries:
        level = entry['level']
        if level in pattern_count:
            pattern_count[level] += 1
            timestamps.append(entry['ts'])

        # Dead code path - never used later (red herring)
        if 'trace' in entry and entry['trace'] > 1000:
            adjusted = entry['trace'] // 17
            redundant_aggregates.append(adjusted ** 0.3)

    # Compute meaningless derived stats (distraction)
    total_severity = sum(severity_map[k] * v for k, v in pattern_count.items())
    avg_interval = (timestamps[-1] - timestamps[0]) / len(timestamps) if len(timestamps) > 1 else 0
    decay_weight = sum(math.exp(-i * 0.1) for i in range(len(timestamps)))

    return {
        'severity_index': total_severity,
        'temporal_density': avg_interval,
        'phantom_decay': decay_weight,  # unused downstream
        'raw_counts': pattern_count
    }

# Secondary helper that appears important but returns unused fields
def compute_stability_factors(nodes):
    uptime_list = [n['uptime'] for n in nodes]
    mean_uptime = sum(uptime_list) / len(uptime_list)
    variance = sum((t - mean_uptime) ** 2 for t in uptime_list) / len(uptime_list)
    stability_score = math.exp(-variance / 1000)

    # Fake redundancy computation (dead end)
    backup_ratio = sum(1 for n in nodes if n.get('backup', False)) / len(nodes)
    recovery_vectors = [math.tanh(mean_uptime / u) if u > 0 else 0 for u in uptime_list]

    # Return some values, only one actually used
    return {
        'score': stability_score,
        'recovery_profile': recovery_vectors,  # ignored
        'backup_coverage': backup_ratio     # ignored
    }

# Main aggregation function combining multiple sources
def aggregate_metrics(nodes, logs):
    # Real usage branch
    node_diagnostics = collect_node_metrics(nodes)
    log_analysis = analyze_log_stream(logs)
    stability_data = compute_stability_factors(nodes)  # partially used

    # Extract relevant health metrics
    active_nodes = [v['health'] for k, v in node_diagnostics.items() if not v['critical']]
    critical_count = sum(1 for v in node_diagnostics.values() if v['critical'])

    # Core logic: weighted combination
    base_health = sum(active_nodes) / len(active_nodes) if active_nodes else 0
    severity_penalty = log_analysis['severity_index'] * 0.25
    stability_bonus = stability_data['score'] * 10

    # Distractor variables (appear in computation but are neutralized)
    dummy_contrib = 0
    for k, v in log_analysis['raw_counts'].items():
        if v > 5:
            dummy_contrib += math.sqrt(v) * 0.1  # has minimal effect

    # Final diagnostic calculation
    raw_diagnostic = base_health - severity_penalty + stability_bonus - (critical_count * 8)
    final_diagnostic = int(round(raw_diagnostic))

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated input data
network_nodes = [
    {'id': 'N1', 'load': 45.0, 'temp': 68.0, 'response_time': 120, 'uptime': 1200, 'backup': True},
    {'id': 'N2', 'load': 67.0, 'temp': 83.0, 'response_time': 95, 'uptime': 3000, 'backup': False},
    {'id': 'N3', 'load': 34.0, 'temp': 70.0, 'response_time': 200, 'uptime': 2100, 'backup': True},
    {'id': 'N4', 'load': 89.0, 'temp': 91.0, 'response_time': 310, 'uptime': 800, 'backup': False},
    {'id': 'N5', 'load': 55.0, 'temp': 72.0, 'response_time': 145, 'uptime': 4500, 'backup': True}
]

system_logs = [
    {'ts': 1623456000, 'level': 'INFO', 'msg': 'node sync completed'},
    {'ts': 1623456060, 'level': 'WARN', 'msg': 'high latency detected'},
    {'ts': 1623456120, 'level': 'ERROR', 'msg': 'connection timeout'},
    {'ts': 1623456180, 'level': 'ERROR', 'msg': 'retry limit exceeded'},
    {'ts': 1623456240, 'level': 'CRITICAL', 'msg': 'node failure N4'},
    {'ts': 1623456300, 'level': 'WARN', 'msg': 'resource pressure'},
    {'ts': 1623456360, 'level': 'INFO', 'msg': 'heartbeat OK'},
    {'ts': 1623456420, 'level': 'CRITICAL', 'msg': 'shutdown initiated'},
    {'ts': 1623456480, 'level': 'ERROR', 'msg': 'disk write failed'}
]

# Key execution point
final_diagnostic = aggregate_metrics(network_nodes, system_logs)
