def analyze_signal(samples, threshold=0.7):
    # Irrelevant preprocessing (distractor)
    normalized = [s / max(samples) for s in samples]
    filtered = [s for s in normalized if s > 0.1]
    stats = {'mean': sum(filtered) / len(filtered), 'count': len(filtered)}

    # Core logic disguised among distractions
    peaks = []
    for i, val in enumerate(normalized):
        if i > 0 and i < len(normalized) - 1:
            if normalized[i-1] < val > normalized[i+1] and val > threshold:
                peaks.append(i)

    # Red herring: unused transformation
    transformed_peaks = [(p**2 + 1) % len(normalized) for p in peaks if p % 2 == 0]
    peak_distances = [peaks[i+1] - peaks[i] for i in range(len(peaks)-1)] if len(peaks) > 1 else [0]

    # Decoy function call with misleading name
    def compute_robustness_index(data):
        return sum(d ** 0.5 for d in data) * 0.3  # Not actually used in final result

    _ = compute_robustness_index(peak_distances)  # Dead code path

    return peaks, peak_distances


def generate_basis(size):
    # Unused auxiliary function (distractor)
    return [i * 0.1 for i in range(size)]


def evaluate_stability(peaks, distances):
    if not peaks:
        return 0
    # Real but obfuscated contribution
    stability = len(peaks) * 100 + sum(distances)
    penalty = 0
    for i, d in enumerate(distances):
        if d < 3:
            penalty += 25
    return stability - penalty


def aggregate_metrics(components, scaling_factors):
    # Complex combination with irrelevant unpacking
    raw_score, extra_data = components[0], components[1:]
    factor_main, _, _ = scaling_factors  # Tuple unpacking with decoy values

    # Distracting list comprehension with zip
    adjustments = [abs(a - b) for a, b in zip(extra_data[0], extra_data[0][::-1])]
    adjustment_sum = sum(adjustments) // 2 if adjustments else 0

    # Critical calculation buried in logic
    base = raw_score * factor_main
    if base > 100:
        base -= adjustment_sum * 1.5

    # Final red herring: string processing that does nothing
    log_tag = "DIAG" + "_".join([str(len(extra_data))])
    log_tag.strip().upper().replace("X", "Y")  # No-op operations

    return int(base)

# Main execution flow
sensor_readings = [0.2, 0.85, 0.3, 0.92, 0.88, 0.15, 0.96, 0.4, 0.75]

# Dead assignments and irrelevant data structures
auxiliary_grid = [[i+j for j in range(3)] for i in range(3)]
dummy_map = {k: v for k, v in enumerate(['A', 'B', 'C'])}
placeholder_tuple = ('temp', 'buffer', 'cache')

# Real work hidden in distraction
detected_peaks, intervals = analyze_signal(sensor_readings, threshold=0.8)
score_component = evaluate_stability(detected_peaks, intervals)

# Multiple dummy computations
shadow_value = sum(x * x for x in auxiliary_grid[0]) / 3
scaling_weights = (2.5, shadow_value, len(placeholder_tuple))  # Two decoy weights

# Key data structure with mixed relevance
processing_chain = (score_component, intervals, detected_peaks)

# Critical statement
final_diagnostic = aggregate_metrics(processing_chain, scaling_weights)

Result: final_diagnostic