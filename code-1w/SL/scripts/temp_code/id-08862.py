def analyze_system_modes():
    # Real system configuration
    operational_modes = {1, 2, 4, 8, 16, 32, 64}
    fault_tolerance_profiles = {2, 8, 32, 128}
    security_levels = {1, 4, 16, 64}

    # Target modes for current operation phase
    target_modes = {1, 2, 4, 8, 64}

    # Filter bank definitions (some are decoys)
    legacy_filters = {1, 3, 5, 7, 9}
    experimental_filters = {10, 20, 30, 40}
    active_filters = {1, 2, 4, 8, 16, 32}
    deprecated_filters = {64, 128, 256}

    # Effective filter set is derived from active and non-deprecated filters
    effective_filters = active_filters - deprecated_filters

    # Irrelevant computations - red herrings
    performance_metrics = []
    for i in range(3):
        metric = (i + 1) ** 3 - 2 * i
        performance_metrics.append(metric)

    calibration_sequence = [x % 7 for x in performance_metrics]
    adjustment_factor = sum(calibration_sequence) / len(calibration_sequence)

    # Unused function - dead code path
    def compute_reliability_index():
        index = 0
        for mode in operational_modes:
            if mode in fault_tolerance_profiles:
                index += mode ** 0.5
        return index * 1.5

    # More irrelevant variables
    nominal_bandwidth = 100 * adjustment_factor
    max_packet_size = nominal_bandwidth // 4
    timeout_threshold = max_packet_size % 13

    # Core logic embedded within distractions
    base_rating = 0
    for mode in operational_modes:
        if mode in security_levels and mode in target_modes:
            base_rating += mode // 2

    # Critical statement - answer depends on this
    filtration_score = len(effective_filters.intersection(target_modes)) * base_rating

    # Additional misleading calculation
    false_positive_risk = len(legacy_filters.intersection(target_modes)) * 5

    # Final output
    print(f"Result: {filtration_score}")

    return filtration_score

result = analyze_system_modes()