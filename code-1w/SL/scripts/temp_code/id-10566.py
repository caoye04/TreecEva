from collections import defaultdict, Counter
from itertools import zip_longest

# Simulated sensor network data with noise and redundancy
def collect_sensor_readings():
    raw_streams = [
        [12, 15, 14, 13, 17, 22, 25, 21, 19, 18],
        [8, 11, 10, 9, 14, 19, 24, 20, 17, 16],
        [5, 7, 6, 5, 9, 13, 15, 12, 10, 9],
        [20, 22, 21, 20, 24, 29, 34, 30, 28, 27]
    ]

    # Irrelevant transformation - scrambles order but not used in final path
    scrambled = []
    for stream in raw_streams:
        temp = []
        for i in range(len(stream)):
            if i % 2 == 0:
                temp.append(stream[i] + 3)
            else:
                temp.append(stream[i] - 2)
        scrambled.append(temp)

    # Decoy aggregation - looks important but unused
    decoy_stats = {}
    for idx, s in enumerate(raw_streams):
        decoy_stats[f'sensor_{idx}'] = {
            'peak': max(s),
            'trough': min(s),
            'variance_proxy': sum(x*x for x in s) / len(s) - (sum(s)/len(s))**2
        }

    # Actual working data
    return raw_streams

# Misleading preprocessing function that appears critical but is only partially used
def analyze_patterns(data_matrix):
    pattern_log = defaultdict(int)
    for row in data_matrix:
        for a, b in zip(row, row[1:]):
            if a < b:
                pattern_log['rising'] += 1
            elif a > b:
                pattern_log['falling'] += 1
            else:
                pattern_log['stable'] += 1

    # This part is never used - red herring
    secondary_analysis = []
    for seq in data_matrix:
        trend_changes = 0
        for i in range(1, len(seq) - 1):
            prev_diff = seq[i] - seq[i-1]
            curr_diff = seq[i+1] - seq[i]
            if prev_diff * curr_diff < 0:  # sign change
                trend_changes += 1
        secondary_analysis.append(trend_changes)

    # Only returns the first part
    return dict(pattern_log)

# Core filtering logic with hidden thresholds
def apply_quality_filter(readings):
    # These thresholds appear tunable but are actually fixed in logic
    config = {'tolerance': 1.8, 'hysteresis': 0.95, 'window': 3}
    buffer = []

    # Dead code path - simulated calibration that doesn't affect output
    def calibrate_stream(stream):
        offset = sum(stream[:3]) / 3 - 10
        return [x - offset for x in stream]  # never called

    for series in readings:
        cleaned = []
        for i, val in enumerate(series):
            if i < 2:
                cleaned.append(val)
                continue
            # Moving average comparison
            window_avg = (series[i-2] + series[i-1]) / 2
            deviation = abs(val - window_avg)
            if deviation <= config['tolerance'] * 2.5:  # effective threshold
                cleaned.append(val)
            # Otherwise drop (simulate missing)
        buffer.append(cleaned)

    # Return incomplete sequences - expected by next stage
    return buffer

# Final processing with multiple concept layers
def process_readings(dataset, thresholds):
    # thresholds contains irrelevant keys
    base_ref = thresholds.get('primary', 18)
    adjustment = thresholds.get('delta_offset', 0)
    effective_base = base_ref - adjustment

    # Complex counting with defaultdict
    severity_count = defaultdict(lambda: 0)
    total_points_assessed = 0

    for seq in dataset:
        for measurement in seq:
            total_points_assessed += 1
            if measurement > effective_base + 5:
                severity_count['critical'] += 1
            elif measurement > effective_base + 2:
                severity_count['elevated'] += 1
            elif measurement > effective_base - 2:
                severity_count['normal'] += 1
            else:
                severity_count['low'] += 1

    # Dummy normalization factor - distractor
    norm_factor = sum(severity_count.values()) or 1
    ratios = {k: v / norm_factor for k, v in severity_count.items()}

    # Hidden calculation: diagnostic score based on weighted risk
    weights = {'critical': 4, 'elevated': 2, 'normal': 0, 'low': -1}
    raw_score = sum(severity_count[k] * weights[k] for k in weights)

    # Secondary adjustment using tuple unpacking distraction
    adjustments = [(1, -0.5), (2, 0.3), (3, 0.7)]
    impact = 0
    for level, modifier in adjustments:
        if total_points_assessed > level * 10:
            impact += modifier

    # Final deterministic computation
    final_diagnostic = raw_score + int(impact)  # impact truncated to int

    # Dead branch - unreachable due to logic
    if effective_base < 0:
        fallback = 0
        for k, v in severity_count.items():
            fallback += hash(k) % 5 * v
        final_diagnostic = fallback  # never executed

    return final_diagnostic

# --- Execution Flow ---
sensor_data = collect_sensor_readings()

# Red herring call that does nothing with return
_ = analyze_patterns(sensor_data)

# Real preprocessing
filtered_data = apply_quality_filter(sensor_data)

# Threshold map with decoy entries
threshold_map = {
    'primary': 15,
    'delta_offset': 2,
    'calibration_key': 'N/A',
    'version': '2.1',
    'spurious_metric': 999
}

# Key execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

print(f"Target result: {final_diagnostic}")