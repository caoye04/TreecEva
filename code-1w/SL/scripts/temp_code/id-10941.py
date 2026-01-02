def analyze_pattern(sequence):
    if len(sequence) < 3:
        return 0
    count = 0
    for i in range(1, len(sequence) - 1):
        if sequence[i-1] < sequence[i] > sequence[i+1]:
            count += 1
    return count

# Irrelevant helper (distractor)
def smooth_data(arr):
    if not arr:
        return []
    smoothed = [arr[0]]
    for i in range(1, len(arr)-1):
        smoothed.append((arr[i-1] + arr[i] + arr[i+1]) / 3)
    smoothed.append(arr[-1])
    return smoothed

# Unused transformation (dead path)
def transform_to_zscore(values):
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    std_dev = variance ** 0.5
    return [(x - mean_val) / std_dev for x in values] if std_dev != 0 else [0] * len(values)

# Decoy function with misleading logic
def calculate_rolling_metric(series, window=3):
    if len(series) < window:
        return [0]
    result = []
    for i in range(len(series) - window + 1):
        window_avg = sum(series[i:i+window]) / window
        result.append(window_avg * (i+1))
    return result

# Real processing begins here
def parse_log_entry(entry_str):
    parts = entry_str.split('|')
    timestamp = parts[0].strip()
    event_type = parts[1].strip()
    magnitude = float(parts[2].strip())
    status_flag = parts[3].strip().lower() == 'active'
    # Extract quality code from string
    qc_str = parts[4].strip()
    qc_sum = sum(ord(c) for c in qc_str if c.isalpha()) % 10
    return {
        'time': timestamp,
        'type': event_type,
        'mag': magnitude,
        'active': status_flag,
        'qc': qc_sum
    }

def collect_magnitudes(log_entries):
    mags = []
    for entry in log_entries:
        parsed = parse_log_entry(entry)
        if parsed['active'] and parsed['type'] != 'DEBUG':
            mags.append(parsed['mag'])
    return mags

# Heavily distracts with multiple layers
def filter_anomalies(data, threshold):
    anomalies = []
    normals = []
    for x in data:
        if abs(x - sum(data)/len(data)) > threshold * 2:
            anomalies.append(x)
        else:
            normals.append(x)
    # This branch is never taken due to logic, but looks important
    if len(anomalies) > len(normals) and False:  
        return sorted(anomalies)[:3]
    return normals

# Real evaluation logic hidden among noise
def recursive_weight(acc, values, idx=0, depth=0):
    if idx >= len(values) or depth > 5:
        return acc
    factor = 1.5 if depth % 2 == 0 else 0.8
    acc += values[idx] * factor
    return recursive_weight(acc, values, idx + 1, depth + 1)

def evaluate_performance(log_lines, base):
    magnitudes = collect_magnitudes(log_lines)
    filtered = filter_anomalies(magnitudes, base)
    pattern_peaks = analyze_pattern(filtered)
    # Real computation starts
    base_adjust = base ** 2
    temp_result = 0
    for val in filtered:
        if val > base_adjust:
            temp_result += int(val // 1)
    # Apply recursive weighting on subset
    subset = filtered[:4] if len(filtered) >= 4 else filtered
    weighted_total = recursive_weight(0, subset)
    score_component_a = int(weighted_total * 10)
    score_component_b = pattern_peaks * 100
    fake_normalization = sum(transform_to_zscore([base, pattern_peaks, len(filtered)]))  # unused
    final_value = score_component_a + score_component_b - 150
    # Critical assignment
    final_score = final_value
    return final_score

# Simulated input data
raw_data = [
    "2023-05-01 10:00:01 | EVENT | 7.2 | active | ABCD",
    "2023-05-01 10:02:15 | WARNING | 3.1 | active | EFGH",
    "2023-05-01 10:03:22 | DEBUG | 9.8 | active | IJKL",
    "2023-05-01 10:05:10 | EVENT | 6.4 | inactive | MNOP",
    "2023-05-01 10:06:44 | EVENT | 8.7 | active | QRST",
    "2023-05-01 10:08:03 | WARNING | 5.5 | active | UVWX",
    "2023-05-01 10:09:11 | EVENT | 7.9 | active | YZAB"
]

threshold_base = 5.0

# Misleading pre-processing (unused)
dummy_series = [1, 3, 2, 5, 4, 6]
spurious_peak_count = analyze_pattern(dummy_series)
suppressed_data = smooth_data([10, 20, 30])

# Key execution point
final_score = evaluate_performance(raw_data, threshold_base)
print(f"Target result: {final_score}")