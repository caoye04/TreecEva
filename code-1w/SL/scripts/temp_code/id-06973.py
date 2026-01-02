from collections import defaultdict, Counter
import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    signals = []
    for i in range(150):
        raw_value = (i * 17) % 97
        timestamp = i + 1000
        category = 'sensor_' + str(i % 5)
        signals.append({'ts': timestamp, 'val': raw_value, 'cat': category})
    return signals

# Irrelevant auxiliary function - dead code path
def analyze_pattern(sequence):
    frequency_map = {}
    for item in sequence:
        frequency_map[item] = frequency_map.get(item, 0) + 1
    return sorted(frequency_map.values(), reverse=True)

# Decoy transformation - never used but looks important
def transform_data(data_list):
    transformed = []
    for entry in data_list:
        x = entry['val']
        y = (x ** 3 - x) % 89
        z = math.sin(y / 10.0)
        transformed.append({'index': x, 'encoded': z})
    return transformed

# Core processing pipeline
def filter_critical(entries, threshold):
    filtered = []
    stats = defaultdict(int)
    cumulative_shift = 0

    for e in entries:
        val = e['val']
        cat = e['cat']

        # Bit manipulation red herring
        bit_analysis = (val ^ 255) & 0x0F
        if bit_analysis > 7:
            stats['high_nibble'] += 1

        # Actual filtering condition buried in noise
        if val > threshold and cat != 'sensor_3':
            adjusted_val = val - (cumulative_shift % 7)
            filtered.append({**e, 'adj': adjusted_val})
            cumulative_shift += val % 11

        # Dead branch with misleading calculation
        if cat == 'sensor_99':  # Never true
            temp = math.log(val + 1) * 100
            stats['phantom_count'] += int(temp)

    return filtered

# Aggregation with distractor metrics
def aggregate_by_category(filtered_entries):
    agg = defaultdict(list)
    decoy_sum = 0

    for entry in filtered_entries:
        cat = entry['cat']
        adj_val = entry['adj']
        agg[cat].append(adj_val)

        # Irrelevant running sum
        decoy_sum += adj_val * 0.1

    result = {}
    for k, v in agg.items():
        count = len(v)
        peak = max(v)
        avg = sum(v) / count
        # Multiple unused metrics to distract
        variance_proxy = sum((x - avg) ** 2 for x in v) / count if count else 0
        result[k] = {'count': count, 'peak': peak, 'avg': round(avg, 3), 'volatility': variance_proxy}

    # Fake normalization
    total_entries = sum(r['count'] for r in result.values())
    if total_entries > 0:
        for r in result.values():
            r['weight'] = r['count'] / total_entries

    return result

# Main metric processor with key logic hidden among decoys
def process_metrics(logs, threshold):
    # Initial decoy counters
    pre_scan = Counter()
    for log in logs:
        pre_scan[log['cat']] += 1
        if log['val'] % 13 == 0:
            pre_scan['div13'] += 1  # Unused statistic

    # Real processing begins
    filtered_logs = filter_critical(logs, threshold)
    categorized = aggregate_by_category(filtered_logs)

    # Critical variables intermixed with irrelevant ones
    diagnostic_score = 0
    entropy_like = 0.0
    mode_tracker = []
    total_valid = 0

    for cat_data in categorized.values():
        count = cat_data['count']
        avg = cat_data['avg']
        peak = cat_data['peak']
        total_valid += count

        # Real contribution to answer
        if count >= 3:
            diagnostic_score += int(avg) * 2
        if peak > 50:
            diagnostic_score += 5

        # Distracting entropy calculation
        if count > 1:
            entropy_like -= (count / 200) * math.log(count / 200)

        mode_tracker.append(peak)

    # Misleading final adjustment
    if len(mode_tracker) > 4:
        modal_peak = max(set(mode_tracker), key=mode_tracker.count)
        diagnostic_score += modal_peak // 10

    # Key computation step - this determines the answer
    adjustment_factor = (threshold // 10) * 3
    final_diagnostic = diagnostic_score - adjustment_factor

    # Dead code: post-processing that does nothing
    if final_diagnostic < 0:
        final_diagnostic = abs(final_diagnostic)
        consistency_check = ''.join(sorted(set(str(final_diagnostic))))
    else:
        hex_trace = hex(final_diagnostic)[2:]
        for c in hex_trace:
            if c in 'abcdef':
                final_diagnostic += 1  # Never reached due to input constraints

    return final_diagnostic

# Generate input data
log_entries = generate_telemetry()
system_threshold = 65

# Execute main logic
final_diagnostic = process_metrics(log_entries, system_threshold)
print(f"Target result: {final_diagnostic}")