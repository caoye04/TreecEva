import itertools

# Simulated system health monitoring with performance scoring
def collect_diagnostics():
    # Real sensor readings (simulated)
    cpu_load = [0.78, 0.82, 0.75, 0.91, 0.83]
    memory_usage = [0.64, 0.71, 0.69, 0.75, 0.72]
    disk_iops = [1200, 1150, 1300, 1250, 1180]
    network_latency = [23, 26, 21, 28, 24]
    temperature = [67, 70, 68, 72, 69]

    # Irrelevant diagnostic data (distraction)
    audio_noise_levels = [45, 47, 44, 46, 48]  # Not used in score
    screen_brightness = [70, 75, 68, 72, 70]   # Dead end
    fan_speeds = [2000, 2100, 1950, 2200, 2050]  # Unused

    return {
        'cpu': cpu_load,
        'memory': memory_usage,
        'disk': disk_iops,
        'latency': network_latency,
        'temp': temperature
    }


def preprocess_data(raw_data):
    # Normalize CPU and memory to 0-1 scale (they already are)
    normalized_cpu = [min(1.0, load) for load in raw_data['cpu']]
    normalized_memory = [min(1.0, usage) for usage in raw_data['memory']]

    # Transform disk IOPS to throughput score (0-1)
    max_iops = 2000
    disk_scores = [iops / max_iops for iops in raw_data['disk']]

    # Latency penalty: lower is better, convert to inverse score
    latency_scores = [max(0, (30 - lat)) / 30 for lat in raw_data['latency']]

    # Temperature risk factor (higher temp = lower score)
    temp_risk = [max(0, (80 - temp)) / 80 for temp in raw_data['temp']]

    # Distractor transformations (not used later)
    power_draw_est = [0.85 + (temp - 60) * 0.02 for temp in raw_data['temp']]  # unused
    predicted_failures = [0.01 * load * (temp / 60) for load, temp in zip(raw_data['cpu'], raw_data['temp'])]  # decoy

    return {
        'cpu_norm': normalized_cpu,
        'memory_norm': normalized_memory,
        'disk_score': disk_scores,
        'latency_score': latency_scores,
        'thermal_score': temp_risk
    }


def calculate_stability_index(values):
    # Simple variance-based stability (lower variance = higher stability)
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    stability = 1 / (1 + variance)  # Higher stability for lower variance
    return stability


def evaluate_performance(metrics, weights):
    # Compute weighted average of latest metric values
    latest_cpu = metrics['cpu_norm'][-1]
    latest_memory = metrics['memory_norm'][-1]
    latest_disk = metrics['disk_score'][-1]
    latest_latency = metrics['latency_score'][-1]
    latest_thermal = metrics['thermal_score'][-1]

    # Actual performance components
    performance_vector = [
        latest_cpu,
        latest_memory,
        latest_disk,
        latest_latency,
        latest_thermal
    ]

    # Apply weights
    weighted_sum = sum(val * weights[i] for i, val in enumerate(performance_vector))

    # Stability adjustments (real logic)
    cpu_stability = calculate_stability_index(metrics['cpu_norm'])
    memory_stability = calculate_stability_index(metrics['memory_norm'])
    disk_stability = calculate_stability_index(metrics['disk_score'])

    # Combine stabilities with equal weight
    avg_stability = (cpu_stability + memory_stability + disk_stability) / 3

    # Final score is weighted performance adjusted by stability
    final_raw = weighted_sum * (0.7 + 0.3 * avg_stability)

    # Misleading adjustment path (dead code - not actually used)
    peak_utilization = max(max(metrics['cpu_norm']), max(metrics['memory_norm']))
    overload_penalty = 0.9 if peak_utilization > 0.9 else 1.0
    stress_factor = 1.0 - (peak_utilization * 0.1)  # Looks important but isn't applied

    # Another red herring: historical trend analysis
    trend_pairs = list(itertools.pairwise(metrics['cpu_norm']))
    positive_trends = sum(1 for a, b in trend_pairs if b > a)
    negative_trends = sum(1 for a, b in trend_pairs if b < a)
    net_trend = positive_trends - negative_trends
    trend_boost = 1 + (net_trend * 0.02)  # Computed but not used

    # REAL final score (no boost or penalty applied)
    return final_raw


# --- Main execution ---
raw_diagnostics = collect_diagnostics()
processed_metrics = preprocess_data(raw_diagnostics)

# Weight vector: [cpu, memory, disk, latency, thermal]
benchmark_weights = [0.3, 0.25, 0.2, 0.15, 0.1]

# Key statement
final_score = evaluate_performance(processed_metrics, benchmark_weights)

# Output result
print(f"Target result: {final_score}")