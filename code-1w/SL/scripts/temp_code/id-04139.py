from collections import defaultdict, Counter

# Simulated network node diagnostic system
def analyze_node_health(metrics):
    healthy = True
    stress_flags = 0
    for k, v in metrics.items():
        if 'latency' in k and v > 150:
            stress_flags += 1
        if 'error_rate' in k and v > 0.05:
            stress_flags += 2
    return stress_flags < 3

def compute_stability_index(metrics):
    base = 0
    for val in metrics.values():
        if isinstance(val, (int, float)):
            base += val * 0.1
    return round(base, 3)

def extract_diagnostic_codes(events):
    codes = []
    for e in events:
        if e['severity'] > 2:
            codes.append(e['code'])
    return codes

def dummy_analysis_pass(metrics):  # Dead function - red herring
    total = 0
    for v in metrics.values():
        total += v ** 0.5
    return total // 7

def assess_connectivity_pattern(links):
    graph = defaultdict(list)
    for src, dst in links:
        graph[src].append(dst)
    
    visited = set()
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
    
    if graph:
        dfs(next(iter(graph)))
    
    return len(visited) == len(graph)

def calculate_bandwidth_efficiency(logs):
    total_packets = 0
    dropped = 0
    for log in logs:
        total_packets += log.get('sent', 0)
        dropped += log.get('failed', 0)
    if total_packets == 0:
        return 0.0
    return round((total_packets - dropped) / total_packets, 4)

def evaluate_redundancy_factor(topology):
    counts = defaultdict(int)
    for node, connections in topology.items():
        for peer in connections:
            counts[peer] += 1
    redundancy = [c for c in counts.values() if c > 1]
    return sum(redundancy) / len(redundancy) if redundancy else 0.0

def aggregate_performance(nodes):
    performance_log = []
    debug_values = []
    temp_storage = {}
    
    for idx, node in enumerate(nodes):
        node_id = f"node_{idx}"
        metrics = node['metrics']
        
        # Core metric computation
        stability = compute_stability_index(metrics)
        health = analyze_node_health(metrics)
        
        # Irrelevant intermediate calculation (distractor)
        dummy_value = dummy_analysis_pass(metrics)
        debug_values.append((node_id, dummy_value))
        
        if health:
            performance_log.append(stability)
        
        # Extract diagnostic codes (seemingly important but unused)
        codes = extract_diagnostic_codes(node.get('events', []))
        temp_storage[node_id] = {'codes': codes, 'temp_flag': False}
        
        # Bit manipulation red herring
        flag = 0b1010
        for c in codes:
            flag ^= ord(c[0])
        
    # Secondary analysis on connectivity
    links = nodes[0].get('connections', [])
    is_connected = assess_connectivity_pattern(links)
    efficiency = calculate_bandwidth_efficiency(nodes[0].get('logs', []))
    
    # Redundant aggregation (misleading path)
    all_metrics = [val for n in nodes for val in n['metrics'].values() if isinstance(val, (int, float))]
    avg_metric = sum(all_metrics) / len(all_metrics) if all_metrics else 0
    
    # Final score depends only on specific conditions
    base_score = sum(performance_log)
    if is_connected:
        base_score *= 1.5
    if efficiency > 0.9:
        base_score += 10
    
    # Critical assignment
    final_score = int(round(base_score + evaluate_redundancy_factor(nodes[0].get('topology', {}))))
    
    # Unused complex structure - distractor
    summary_report = {
        'nodes_analyzed': len(nodes),
        'healthy_count': len(performance_log),
        'stability_avg': sum(performance_log) / len(performance_log) if performance_log else 0,
        'connectivity': is_connected,
        'efficiency': efficiency,
        'debug_snippets': debug_values[:2]
    }
    
    return final_score

# Setup test data
events_data = [
    {'code': 'ERR_CRITICAL', 'severity': 3},
    {'code': 'WARN_TIMEOUT', 'severity': 2},
    {'code': 'INFO_RETRY', 'severity': 1}
]

network_nodes = [
    {
        'metrics': {
            'latency_ms': 120,
            'error_rate': 0.03,
            'cpu_load': 75,
            'mem_usage': 800
        },
        'events': events_data,
        'connections': [('A', 'B'), ('B', 'C'), ('C', 'A')],
        'logs': [
            {'sent': 100, 'failed': 5},
            {'sent': 200, 'failed': 10}
        ],
        'topology': {'A': ['B', 'C'], 'B': ['A', 'C'], 'C': ['A', 'B']}
    },
    {
        'metrics': {
            'latency_ms': 180,
            'error_rate': 0.07,
            'cpu_load': 85,
            'mem_usage': 900
        }
    },
    {
        'metrics': {
            'latency_ms': 90,
            'error_rate': 0.02,
            'cpu_load': 60,
            'mem_usage': 700
        }
    }
]

# Execute critical statement
final_score = aggregate_performance(network_nodes)
print(f"Result: {final_score}")