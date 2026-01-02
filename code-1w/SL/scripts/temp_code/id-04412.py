def main():
    # Domain: System performance evaluation with mixed metrics
    base_frequency = 2400
    turbo_boost = 3600
    core_count = 8
    thermal_throttle = 0.88

    # Irrelevant hardware stats (distractor)
    ram_gb = 32
    disk_speed_mbps = 550
    network_latency_ms = 42

    # Key metric components
    clock_ratio = turbo_boost / base_frequency
    efficiency_cores = core_count // 2
    hyperthreading_factor = 1.3 if core_count > 4 else 1.0

    # Bitwise feature flags for instruction sets (some relevant, some not)
    instruction_flags = 0b101101
    avx_enabled = instruction_flags & 0b100000  # Bit 6
    sse4_enabled = instruction_flags & 0b000100  # Bit 3
    neon_enabled = instruction_flags & 0b000010  # Irrelevant (ARM)

    # Build metric set using set operations
    required_features = {"avx", "sse4", "power_efficient"}
    available_features = {"sse4", "avx", "neon", "power_efficient", "rdtsc"}
    supported_features = required_features & available_features

    # Add fake features to distract
    deprecated_features = {"mmx", "3dnow"}
    available_features |= deprecated_features  # Merges but irrelevant

    # Lambda for scoring based on feature compliance and frequency scaling
    benchmark_lambda = lambda freq, count, features: (
        (freq * count * len(features)) ** 0.5 * (1 + 0.1 * (len(features) - 3))
        if len(features) >= 3 else 0
    )

    # Secondary distraction: thermal modeling (not used in final score)
    def compute_thermal_headroom(temp_c):
        max_safe = 95
        return max(0, (max_safe - temp_c) / max_safe)

    current_temp = 78
    headroom = compute_thermal_headroom(current_temp)

    # Simulated intermediate scores (only one actually used)
    memory_bound_score = (ram_gb * disk_speed_mbps) / network_latency_ms
    cpu_bound_score = base_frequency * core_count * 0.001
    hybrid_score = memory_bound_score * 0.3 + cpu_bound_score * 0.7

    # Actual key computation
    raw_metric = clock_ratio * hyperthreading_factor * thermal_throttle
    metric_set = {
        'raw': raw_metric,
        'cores': efficiency_cores,
        'features': supported_features
    }

    # Final evaluation function
    def evaluate_performance(metrics, scorer):
        raw_val = metrics['raw']
        cores = metrics['cores']
        feats = metrics['features']
        score = scorer(raw_val * 1000, cores, feats)
        return int(score) if score > 0 else -1

    # Execution point of interest
    final_score = evaluate_performance(metric_set, benchmark_lambda)

    # Distraction: unused alternative calculation path
    if core_count > 16:
        fallback_mode = True
        final_score *= 1.2
    elif ram_gb < 16:
        final_score -= 100
    # Else branch never taken — dead code

    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()