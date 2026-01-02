import itertools

def main():
    # Simulate sensor data stream for system health monitoring
    timestamps = list(range(10))
    cpu_load = [0.65, 0.70, 0.95, 0.85, 0.75, 0.60, 0.55, 0.78, 0.88, 0.90]
    mem_usage = [0.50, 0.55, 0.60, 0.70, 0.80, 0.85, 0.90, 0.75, 0.65, 0.50]
    temp_readings = [45, 47, 55, 53, 50, 48, 60, 62, 58, 54]

    # Initialize tracking structures
    metrics_log = {}
    stability_buffer = []
    cumulative_stress = 0
    fluctuation_count = 0  # distractor: not used in final logic

    # Process each time step
    for t in timestamps:
        load = cpu_load[t]
        memory = mem_usage[t]
        temp = temp_readings[t]

        # Compute derived health indicators
        thermal_stress = max(0, temp - 50) / 20
        resource_pressure = (load + memory) / 2
        efficiency_ratio = (1 - load) * (1 - memory)

        # Update cumulative stress with non-linear accumulation
        if load > 0.8 or memory > 0.8:
            cumulative_stress += 1.5
        elif load > 0.6 or memory > 0.6:
            cumulative_stress += 0.8
        else:
            cumulative_stress += 0.3

        # Track instability events (distractor: logged but not used)
        if t > 0 and abs(cpu_load[t] - cpu_load[t-1]) > 0.2:
            fluctuation_count += 1
            stability_buffer.append(t)

        # Log key metrics per timestamp
        metrics_log[t] = {
            'stress': thermal_stress,
            'pressure': resource_pressure,
            'efficiency': efficiency_ratio,
            'critical': load > 0.9 or memory > 0.9 or temp > 58
        }

    # Secondary analysis: sliding window trend (dead code path - not used)
    trends = []
    for i in range(2, len(timestamps)):
        window_avg = sum(cpu_load[i-2:i+1]) / 3
        if window_avg > 0.75:
            trends.append('high')
        elif window_avg > 0.5:
            trends.append('moderate')
        else:
            trends.append('low')

    # Use itertools to generate diagnostic combinations (semi-relevant)
    diagnostic_pairs = list(itertools.combinations(['stress', 'pressure', 'efficiency'], 2))
    correlation_hints = []
    for a, b in diagnostic_pairs:
        # Dummy correlation logic (not actually affecting output)
        correlation_hints.append(f"{a[:3]}_{b[:3]}")

    # Aggregate performance into final rating
    critical_events = 0
    total_efficiency = 0.0
    base_efficiency = 0.0

    for entry in metrics_log.values():
        if entry['critical']:
            critical_events += 1
        total_efficiency += entry['efficiency']

    # Core calculation for efficiency score
    avg_efficiency = total_efficiency / len(metrics_log)
    penalty = critical_events * 0.1
    efficiency_score = max(0, avg_efficiency - penalty) * 100  # Scale to percentage

    # Dead computation: simulation of fallback algorithm
    backup_score = 0
    for t in metrics_log:
        if metrics_log[t]['pressure'] < 0.7:
            backup_score += 10
    # This backup is never used

    # Final aggregation function call
    final_rating = aggregate_performance(metrics_log)

    print(f"Result: {efficiency_score}")


def aggregate_performance(log):
    # This function exists to justify the description's key statement
    # It does NOT compute efficiency_score but is mentioned to add interference
    total = 0.0
    count = 0
    for v in log.values():
        total += v['pressure']
        count += 1
    return total / count if count else 0

if __name__ == '__main__':
    main()