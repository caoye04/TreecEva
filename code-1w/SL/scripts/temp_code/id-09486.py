import math

# Simulated system metrics from a distributed computing environment
def collect_metrics():
    raw_data = {
        'cpu_load': [0.78, 0.82, 0.75, 0.91, 0.88],
        'memory_usage': [0.64, 0.71, 0.69, 0.76, 0.73],
        'network_latency_ms': [45, 52, 49, 61, 55],
        'disk_io_ops': [1200, 1150, 1300, 1250, 1180],
        'temp_sensor_readings': [67, 69, 72, 70, 68],  # Irrelevant to performance score
        'fan_rpm': [2800, 2900, 3100, 3000, 2850]       # Irrelevant hardware detail
    }

    # Derived metrics (some relevant, some not)
    avg_cpu = sum(raw_data['cpu_load']) / len(raw_data['cpu_load'])
    avg_memory = sum(raw_data['memory_usage']) / len(raw_data['memory_usage'])
    avg_latency = sum(raw_data['network_latency_ms']) / len(raw_data['network_latency_ms'])
    total_disk_io = sum(raw_data['disk_io_ops'])

    # Distractor computation: thermal analysis (not used in final score)
    avg_temp = sum(raw_data['temp_sensor_readings']) / len(raw_data['temp_sensor_readings'])
    temp_variance = sum((t - avg_temp) ** 2 for t in raw_data['temp_sensor_readings']) / len(raw_data['temp_sensor_readings'])
    cooling_efficiency = (avg_temp / avg_cpu) * 10 if avg_cpu > 0 else 0

    # Relevant normalized metrics for performance scoring
    normalized_latency = 100 / (1 + avg_latency)  # Lower latency → higher score
    normalized_cpu = 100 * avg_cpu
    normalized_memory = 100 * avg_memory
    disk_throughput_score = math.log(total_disk_io) * 10

    # Unused distractor metrics
    peak_load = max(raw_data['cpu_load'])
    jitter = max(raw_data['network_latency_ms']) - min(raw_data['network_latency_ms'])
    io_jitter = max(raw_data['disk_io_ops']) - min(raw_data['disk_io_ops'])

    return {
        'normalized_cpu': normalized_cpu,
        'normalized_memory': normalized_memory,
        'normalized_latency': normalized_latency,
        'disk_throughput_score': disk_throughput_score,
        'peak_load': peak_load,  # Collected but unused
        'jitter': jitter,       # Collected but unused
        'cooling_efficiency': cooling_efficiency  # Collected but unused
    }

# Weight assignment with red herring alternatives
def get_weights():
    default_weights = {
        'cpu': 0.3,
        'memory': 0.25,
        'latency': 0.35,
        'disk': 0.1
    }

    # Alternative weighting schemes (distractors)
    alt_weights_1 = {'cpu': 0.4, 'memory': 0.3, 'latency': 0.2, 'disk': 0.1}
    alt_weights_2 = {'cpu': 0.2, 'memory': 0.2, 'latency': 0.5, 'disk': 0.1}
    alt_weights_3 = {'cpu': 0.35, 'memory': 0.35, 'latency': 0.2, 'disk': 0.1}

    # Conditional logic that appears meaningful but is actually dead code
    scenario = 'standard'
    if scenario == 'high_cpu':
        return alt_weights_1
    elif scenario == 'low_latency':
        return alt_weights_2
    elif scenario == 'balanced':
        return alt_weights_3
    # Default case is taken, others are dead paths

    return default_weights

# Core evaluation logic with dictionary-based aggregation
def evaluate_performance(metrics, weights):
    # Map metric keys to actual values
    score_components = {
        'cpu': metrics['normalized_cpu'] * weights['cpu'],
        'memory': metrics['normalized_memory'] * weights['memory'],
        'latency': metrics['normalized_latency'] * weights['latency'],
        'disk': metrics['disk_throughput_score'] * weights['disk']
    }

    # Additional derived scores (only one used)
    total_unweighted = sum(score_components.values())
    weighted_average = total_unweighted  # Already weighted

    max_possible = 100 * sum(weights.values())
    efficiency_ratio = weighted_average / max_possible if max_possible > 0 else 0

    # Distractor: complexity penalty (never applied)
    component_count = len(score_components)
    if component_count > 5:
        weighted_average *= 0.95

    # Final nonlinear transformation (key step)
    final_score = math.sqrt(weighted_average) * 10

    # Dead code: adjustment for hypothetical future metrics
    if 'future_metric' in metrics:
        bonus = metrics['future_metric'] * 0.1
        final_score += bonus

    return final_score

# Orchestration function with irrelevant setup
def main():
    # Initialize system (simulated)
    system_state = {"status": "active", "mode": "performance"}
    calibration_offset = 0.05  # Unused in calculation
    debug_mode = False  # Never toggled

    # Collect and process data
    metrics = collect_metrics()
    weights = get_weights()

    # Perform evaluation
    final_score = evaluate_performance(metrics, weights)

    # Print result
    print(f"Result: {final_score}")

    # Post-processing distractors
    if debug_mode:
        for k, v in metrics.items():
            print(f"[DEBUG] {k}: {v}")

    return final_score

# Execute
if __name__ == "__main__":
    main()