def analyze_system_load(usage_log, config_params):
    # Irrelevant transformation: reverses log but not used in final calculation
    reversed_log = [x for x in reversed(usage_log)]

    # Distractor: complex-looking but unused function
    def calculate_entropy(data):
        from math import log
        freq = {}
        for item in data:
            freq[item] = freq.get(item, 0) + 1
        total = len(data)
        entropy = -sum((count / total) * log(count / total) for count in freq.values())
        return entropy

    # Unused recursive red herring
    def binary_partition(arr, depth=0):
        if len(arr) <= 1:
            return depth
        mid = len(arr) // 2
        return max(binary_partition(arr[:mid], depth + 1),
                   binary_partition(arr[mid:], depth + 1))

    partition_depth = binary_partition(usage_log)  # Computed but irrelevant

    # Real processing begins: filter high-load entries
    threshold = config_params.get('load_threshold', 75)
    high_load_entries = list(filter(lambda x: x > threshold, usage_log))

    # Distractor: character counting in debug mode (meaningless here)
    debug_tag = "DIAGNOSTIC_RUN_V2"
    char_count = sum(1 for c in debug_tag if c.isalpha())

    # Simulated secondary metric (unused but looks important)
    avg_load = sum(usage_log) / len(usage_log) if usage_log else 0
    peak_load = max(usage_log) if usage_log else 0
    load_variance = sum((x - avg_load) ** 2 for x in usage_log) / len(usage_log) if usage_log else 0

    # Key computation chain starts here — actual logic path
    normalized_peaks = [x / peak_load for x in high_load_entries] if peak_load else []
    weighted_score = 0.0
    for i, norm_val in enumerate(normalized_peaks):
        weight = 0.9 ** i  # Exponential decay weighting
        weighted_score += norm_val * weight

    # Secondary data structure: zipped diagnostics
    indices = list(range(len(high_load_entries)))
    zipped_diagnostics = list(zip(indices, high_load_entries, normalized_peaks))

    # Redundant operation: creates tuple unpacking distraction
    total_impact = 0
    for idx, raw_val, norm_val in zipped_diagnostics:
        # This loop appears meaningful but only contributes partially
        if idx % 2 == 0:
            total_impact += norm_val * raw_val

    # Final transformation using lambda and enumerate together
    adjustment_factor = sum(map(lambda pair: pair[1] * (pair[0] + 1), 
                                enumerate(normalized_peaks)))

    # Core formula: combines multiple derived values
    base_metric = len(high_load_entries) * weighted_score
    adjustment = adjustment_factor * 0.3
    stability_penalty = abs(avg_load - 50) * 0.1  # Assume ideal at 50

    # Final diagnostic computed from mixed sources
    final_diagnostic = int(base_metric + adjustment - stability_penalty)

    # Dead code path: looks like it affects result but doesn't execute
    if False:
        final_diagnostic *= 2
        final_diagnostic += partition_depth

    return final_diagnostic


def process_metrics(log_data, system_thresholds):
    # Wrapper that appears to do more but just forwards
    temp_offset = sum(1 for _ in filter(lambda x: x < 0, system_thresholds))  # always 0
    adjusted_log = [x + temp_offset for x in log_data]  # no real effect
    return analyze_system_load(adjusted_log, {'load_threshold': system_thresholds[0]})

# Input data — realistic system monitoring log
log_data = [68, 72, 76, 81, 64, 85, 89, 77, 90, 62, 88, 73]
system_thresholds = [75, 80, 95]  # Only first element used

# Execution point of interest
final_diagnostic = process_metrics(log_data, system_thresholds)
print(f"Target result: {final_diagnostic}")