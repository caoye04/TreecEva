def analyze_system_metrics(raw_data, config):
    # Preprocessing: extract relevant time-series metrics
    timestamps = [entry['ts'] for entry in raw_data]
    cpu_loads = [entry['cpu'] for entry in raw_data]
    memory_usage = [entry['mem'] for entry in raw_data]

    # Distractor: network latency stats (not used later)
    network_latency = [entry.get('net', 0) * 1.5 for entry in raw_data]
    avg_latency = sum(network_latency) / len(network_latency) if network_latency else 0

    # Normalize CPU loads to percentage
    max_cpu = max(cpu_loads) if cpu_loads else 1
    normalized_cpu = [load / max_cpu * 100 for load in cpu_loads]

    # Identify peak usage windows using enumerate
    peak_windows = []
    for i, cpu_val in enumerate(normalized_cpu):
        if cpu_val > 90 and i > 0 and normalized_cpu[i-1] <= 90:
            peak_windows.append(i)

    # Compute rolling average of memory (3-point window)
    smoothed_memory = []
    for i in range(2, len(memory_usage)):
        smoothed_memory.append((memory_usage[i-2] + memory_usage[i-1] + memory_usage[i]) / 3)

    # Aggregate baseline statistics
    baseline_stats = {
        'avg_cpu': sum(normalized_cpu) / len(normalized_cpu),
        'peak_count': len(peak_windows),
        'stability_index': len(smoothed_memory)
    }

    return baseline_stats


def calculate_performance(results, limits):
    # Apply thresholds to determine performance grade
    score = 0
    penalty = 0

    # Use of zip to align results with threshold bounds
    for metric, (key, value) in zip(limits.items(), results.items()):
        if key == 'avg_cpu' and value > metric:
            penalty += 10
        elif key == 'peak_count' and value >= metric:
            penalty += 15
        elif key == 'stability_index' and value < metric:
            penalty += 5

    # Secondary scoring based on set logic (critical thresholds exceeded)
    exceeded_thresholds = set()
    for k, v in results.items():
        threshold_val = limits.get(k, 0)
        if (k == 'avg_cpu' and v > threshold_val) or \
           (k == 'peak_count' and v >= threshold_val):
            exceeded_thresholds.add(k)

    # Bonus only if no critical issues
    bonus = 20 if len(exceeded_thresholds) == 0 else 0

    # Additional distractor computation: unused efficiency ratio
    efficiency_ratio = (results.get('avg_cpu', 0) + 1) / (results.get('peak_count', 1) + 1)
    adjusted_efficiency = efficiency_ratio * 0.85  # Not used in final score

    score = 100 - penalty + bonus
    return int(score)

# Main execution block
if __name__ == '__main__':
    # Simulated system telemetry data
    telemetry_data = [
        {'ts': 1001, 'cpu': 76, 'mem': 3200, 'net': 12},
        {'ts': 1002, 'cpu': 85, 'mem': 3400, 'net': 14},
        {'ts': 1003, 'cpu': 92, 'mem': 3800, 'net': 13},
        {'ts': 1004, 'cpu': 95, 'mem': 4100, 'net': 16},
        {'ts': 1005, 'cpu': 88, 'mem': 3900, 'net': 15},
        {'ts': 1006, 'cpu': 70, 'mem': 3600, 'net': 11},
        {'ts': 1007, 'cpu': 65, 'mem': 3300, 'net': 10},
        {'ts': 1008, 'cpu': 96, 'mem': 4300, 'net': 17},
        {'ts': 1009, 'cpu': 94, 'mem': 4000, 'net': 14},
        {'ts': 1010, 'cpu': 80, 'mem': 3700, 'net': 12}
    ]

    system_config = {'sampling_rate': '1s', 'version': '2.1'}

    # Call analysis function
    benchmark_results = analyze_system_metrics(telemetry_data, system_config)

    # Define performance thresholds
    thresholds = {
        'avg_cpu': 85.0,
        'peak_count': 2,
        'stability_index': 5
    }

    # Key statement
    final_score = calculate_performance(benchmark_results, thresholds)

    print(f"Result: {final_score}")