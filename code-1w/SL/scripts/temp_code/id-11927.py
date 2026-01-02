from itertools import accumulate

# System load simulation over time with maintenance cycles and scaling policies
def compute_system_capacity():
    base_load = [120, 150, 135, 142, 128, 160, 175, 140, 130, 155]
    fluctuation_adjusters = [0.95, 1.08, 0.92, 1.03, 0.97, 1.10, 1.07, 0.94, 0.99, 1.05]
    maintenance_impact = [0, 0, -30, 0, 0, -25, 0, 0, -20, 0]  # Scheduled downtimes

    # Apply real-time fluctuation and maintenance
    adjusted_loads = [
        int(base_load[i] * fluctuation_adjusters[i] + maintenance_impact[i])
        for i in range(len(base_load))
    ]

    # Simulate gradual resource exhaustion and recovery (memory leak compensation)
    drift_factors = [1.02, 0.99, 1.01, 1.03, 0.98, 1.04, 1.02, 1.00, 0.97, 1.05]
    degraded_performance = [int(adjusted_loads[i] * drift_factors[i]) for i in range(len(adjusted_loads))]

    # Hidden cumulative stress tracking (not directly used in final answer)
    stress_accumulation = list(accumulate(degraded_performance, lambda acc, x: min(acc + x - 50, x * 2)))
    average_stress = sum(stress_accumulation) / len(stress_accumulation)

    # Redundant health check computations
    health_score = 100
    for val in degraded_performance:
        if val > 160:
            health_score -= 3
        elif val < 130:
            health_score += 1

    # Primary usage trajectory based on smoothed response times
    smoothing_window = 3
    smoothed_usage = [
        sum(degraded_performance[max(0, i - smoothing_window + 1):i + 1]) // (i - max(0, i - smoothing_window + 1) + 1)
        for i in range(len(degraded_performance))
    ]

    # Simulate auto-scaling response: capacity grows if usage exceeds threshold
    scaling_history = []
    current_capacity = 150
    for usage in smoothed_usage:
        if usage > current_capacity * 0.85:
            current_capacity *= 1.2
        scaling_history.append(int(current_capacity))
    
    # Final usage trajectory after capacity adaptation
    usage_trajectory = [
        min(smoothed_usage[i], scaling_history[i]) for i in range(len(smoothed_usage))
    ]

    # Key computation point
    peak_capacity = max(usage_trajectory)

    # Irrelevant telemetry logging (distractor)
    telemetry_snapshot = {
        'final_health': health_score,
        'avg_stress': average_stress,
        'scale_events': sum(1 for i in range(1, len(scaling_history)) if scaling_history[i] > scaling_history[i-1])
    }

    # Debug assertions (no effect on logic)
    assert len(usage_trajectory) == len(base_load)
    assert peak_capacity > 0

    print(f"Result: {peak_capacity}")

compute_system_capacity()