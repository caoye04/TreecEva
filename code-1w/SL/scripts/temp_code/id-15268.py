def analyze_system_efficiency(log_data):
    # Irrelevant preprocessing: normalize timestamps (distractor)
    base_time = log_data[0]['timestamp']
    normalized_times = [(entry['timestamp'] - base_time) * 1000 for entry in log_data]

    # Extract resource metrics (some are decoys)
    cpu_loads = [entry['cpu'] for entry in log_data]
    memory_usage = [entry['memory'] for entry in log_data]
    disk_io = [entry['disk'] for entry in log_data]  # Unused later - red herring
    network_latency = [entry['network'] for entry in log_data]  # Distractor

    # Compute derived statistics (only avg_cpu and peak_memory are used)
    avg_cpu = sum(cpu_loads) / len(cpu_loads)
    peak_memory = max(memory_usage)
    min_disk = min(disk_io)  # Dead computation
    avg_network = sum(network_latency) / len(network_latency)  # Irrelevant

    # Simulate false dependency with lambda (misleading)
    adjust = lambda x, f: x * (1 + f * 0.1)
    adjusted_avg = adjust(avg_cpu, 0.5)  # Looks important but unused

    # Focus shifts to performance scoring
    stability_score = 100 - (sum(abs(x - avg_cpu) for x in cpu_loads) / len(cpu_loads))
    efficiency_ratio = (avg_cpu + 1) / (peak_memory + 1)

    # Set up weight system using enumerate and zip (required features)
    raw_metrics = [stability_score, efficiency_ratio, avg_cpu, peak_memory]
    metric_names = ['stability', 'efficiency', 'cpu_base', 'mem_peak']

    # Assign arbitrary importance (decoy logic with enumeration)
    importance_map = {}
    for i, name in enumerate(metric_names):
        if name in ['efficiency', 'stability']:
            importance_map[name] = 0.4
        else:
            importance_map[name] = 0.1  # These won't be used

    # Actual weights are hardcoded here (bypassing map - misleading structure)
    weights = [0.4, 0.4, 0.1, 0.1]  # Corresponds to raw_metrics

    # Introduce set operations for filtering (required feature - artificial use)
    critical_metrics = {'stability', 'efficiency'}
    reported_metrics = {name for name in metric_names if 'score' not in name}  # All non-score names
    active_set = critical_metrics & reported_metrics  # Yields {'stability','efficiency'}

    # Core transformation via zip (required feature)
    metrics = list(zip(raw_metrics, weights))

    # Aggregate function (key logic buried)
    def aggregate_performance(perf_list, w_list):
        total = 0
        for val, wt in perf_list:
            total += val * wt
        return int(total)  # Final answer derivation

    final_score = aggregate_performance(metrics, weights)

    # DEAD CODE PATHS (unused functions - interference)
    def compute_anomaly_score():
        return sum(1 for x in cpu_loads if x > 90) * 100 // len(cpu_loads)

    def generate_report():
        return {'status': 'OK', 'score': adjusted_avg}  # Uses decoy var

    # PRINT FINAL ANSWER (required output format)
    print(f"Result: {final_score}")
    return final_score

# Simulated input data (deterministic)
data_log = [
    {'timestamp': 1680000000, 'cpu': 75, 'memory': 400, 'disk': 20, 'network': 120},
    {'timestamp': 1680000001, 'cpu': 78, 'memory': 410, 'disk': 22, 'network': 115},
    {'timestamp': 1680000002, 'cpu': 74, 'memory': 395, 'disk': 18, 'network': 130},
    {'timestamp': 1680000003, 'cpu': 77, 'memory': 405, 'disk': 24, 'network': 118},
    {'timestamp': 1680000004, 'cpu': 76, 'memory': 400, 'disk': 21, 'network': 122}
]

# Execute
analyze_system_efficiency(data_log)
