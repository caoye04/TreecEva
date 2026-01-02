from collections import defaultdict, Counter
from itertools import combinations

# Simulated sensor network diagnostic system
def collect_diagnostics():
    raw_readings = [234, 567, 89, 23, 67, 890, 12, 45, 67, 89, 90, 123]
    device_ids = ['D-7A', 'D-8B', 'D-9C', 'D-10D', 'D-11E']
    timestamps = list(range(1000, 1012))

    # Irrelevant aggregation (red herring)
    avg_reading = sum(raw_readings) / len(raw_readings)
    peak = max(raw_readings)
    noise_floor = 20

    # Misleading transformation chain
    transformed = []
    for val in raw_readings:
        if val > 100:
            transformed.append(val ^ 15)  # Bitwise distraction
        else:
            transformed.append(val | 7)

    # Distractor: unused statistical analysis
    freq_count = Counter(raw_readings)
    mode_val = freq_count.most_common(1)[0][0] if freq_count else None

    # Real processing begins here
    valid_range = lambda x: 50 <= x <= 900
    filtered_data = [x for x in raw_readings if valid_range(x)]

    # Complex threshold logic with decoy structure
    threshold_map = defaultdict(lambda: 100)
    threshold_map.update({
        'critical': 900,
        'warning': 450,
        'info': 200,
        'debug': 50
    })

    # Dead code path - never accessed (distractor)
    def legacy_calibrate(data):
        return [d * 0.95 for d in data if d > 100]  # Unused

    # Another red herring: combinatorial explosion check
    pairs_above_500 = 0
    for a, b in combinations(raw_readings, 2):
        if a + b > 500:
            pairs_above_500 += 1

    # Core logic hidden among distractions
    def analyze_stability(data):
        if len(data) < 3:
            return 0
        sorted_vals = sorted(data)
        median = sorted_vals[len(sorted_vals) // 2]
        variance = sum((x - median) ** 2 for x in data) / len(data)
        return round(variance, 2)

    stability_score = analyze_stability(filtered_data)

    # Key conditional expression with embedded logic
    base_weight = 1.75 if stability_score < 10000 else 0.85

    # Decoy assignment (looks important but unused)
    calibration_offset = (peak - noise_floor) * 0.01

    # Actual answer computation buried in complexity
    def process_readings(data, thresholds):
        total = 0
        weights = {'critical': 3.0, 'warning': 1.5, 'info': 0.5, 'debug': 0.1}
        for val in data:
            if val >= thresholds['critical']:
                total += val * weights['critical']
            elif val >= thresholds['warning']:
                total += val * weights['warning']
            elif val >= thresholds['info']:
                total += val * weights['info']
            elif val >= thresholds['debug']:
                total += val * weights['debug']
        # Final adjustment based on stability
        adjustment_factor = 1.0 if len(data) > 5 else 0.9
        return int(total * adjustment_factor * base_weight)

    # Critical execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)

    # Output required result
    print(f"Result: {final_diagnostic}")

    # Unused cleanup function (dead code)
    def purge_cache():
        nonlocal transformed
        transformed.clear()

    return final_diagnostic

# Entry point
collect_diagnostics()