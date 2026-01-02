import itertools

# Simulated system telemetry data with mixed signal types
def collect_telemetry():
    signals = []
    for i in range(18):
        if i % 3 == 0:
            signals.append(('voltage', i * 2.1 + 0.5))
        elif i % 5 == 0:
            signals.append(('current', i / 2.3))
        else:
            signals.append(('temp', (i * 1.2) % 70))
    return signals

# Irrelevant preprocessing: transforms data in unused ways
def transform_signals(signal_list):
    processed = []
    scaling_factor = 1.07
    for typ, val in signal_list:
        if typ == 'voltage':
            processed.append((typ, val * scaling_factor + 1.1))
        elif typ == 'current':
            processed.append((typ, val / scaling_factor))
        else:
            processed.append((typ, max(val, 20)))
    return processed

# Decoy function - looks important but never called in critical path
def analyze_failures(data):
    failure_count = 0
    for entry in data:
        if 'err' in entry.get('status', ''):
            failure_count += 1
    return failure_count

# Core aggregation logic - relevant
def group_by_type(telemetry):
    grouped = {'voltage': [], 'current': [], 'temp': []}
    for typ, val in telemetry:
        if typ in grouped:
            grouped[typ].append(val)
    return grouped

# Red herring computation: calculates median but not used in final result
def compute_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_lst[mid-1] + sorted_lst[mid]) / 2
    else:
        return sorted_lst[mid]

# Heavily distracted processing with distractor variables
def calculate_stability_index(values):
    if len(values) == 0:
        return 0.0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    stability = 1 / (1 + variance)  # Inverse relationship to variance
    
    # Distractor block: computes percentile but unused
    sorted_vals = sorted(values)
    p90_idx = int(0.9 * len(sorted_vals))
    p90_val = sorted_vals[p90_idx] if p90_idx < len(sorted_vals) else sorted_vals[-1]
    
    # Another red herring: entropy-like calculation on binned data
    bins = [0, 0, 0, 0]
    for v in values:
        if v < mean_val * 0.7:
            bins[0] += 1
        elif v < mean_val:
            bins[1] += 1
        elif v < mean_val * 1.3:
            bins[2] += 1
        else:
            bins[3] += 1
    total = sum(bins)
    if total == 0:
        entropy = 0
    else:
        entropy = -sum((b/total) * __import__('math').log(b/total + 1e-9) for b in bins)
    
    return stability  # Only this is actually used later

# Real processing chain
log_entries = collect_telemetry()
transformed_logs = transform_signals(log_entries)  # Dead assignment

# Unused statistical summaries
temp_med = compute_median([v for t, v in log_entries if t == 'temp'])
current_med = compute_median([v for t, v in log_entries if t == 'current'])

signal_groups = group_by_type(log_entries)

# Distractor variables - look like threshold adjustments but irrelevant
baseline_offset = 0.87
calibration_curve = [round(1.1 ** i, 3) for i in range(10)]
system_flags = {f'flag_{i}': False for i in range(5)}

# Real thresholds
system_thresholds = {
    'voltage': 0.75,
    'current': 0.65,
    'temp': 0.80
}

# Complex conditional processing with list comprehensions and filtering
def filter_anomalies(grouped_data, threshold_map):
    anomalies = {}
    for key in grouped_data:
        thresh = threshold_map[key]
        # Compute z-score like metric using stability index as baseline
        ref_stab = calculate_stability_index(grouped_data[key])
        filtered = [v for v in grouped_data[key] if abs(v - sum(grouped_data[key])/len(grouped_data[key])) > (1 - ref_stab) * 10]
        anomalies[key] = len(filtered)
    return anomalies

# Secondary transformation - partially relevant
def normalize_keys(raw_dict):
    return {k.upper(): v for k, v in raw_dict.items()}

# Key processing function - integrates multiple concepts
def process_metrics(entries, thresholds):
    groups = group_by_type(entries)
    
    # Irrelevant dictionary transformation
    inverted = {v: k for k, vals in groups.items() for v in vals}
    
    # Real computation begins
    indices = {}
    for typ in ['voltage', 'current', 'temp']:
        if typ in groups and len(groups[typ]) > 0:
            stab = calculate_stability_index(groups[typ])
            indices[typ] = round(stab * thresholds[typ], 6)
    
    # Complex reduction using itertools
    paired = list(itertools.combinations(indices.values(), 2))
    diff_sum = sum(abs(a - b) for a, b in paired)
    
    # Final diagnostic score computed from consistency across systems
    total_score = 0
    weights = {'voltage': 1.2, 'current': 1.0, 'temp': 0.9}
    for k, v in indices.items():
        total_score += v * weights.get(k, 1.0)
    
    # Distractor: unused aggregation
    flat_vals = list(itertools.chain.from_iterable([
        [v] * 2 if k == 'voltage' else [v] for k, v in indices.items()
    ]))
    avg_flat = sum(flat_vals) / len(flat_vals) if flat_vals else 0
    
    # Final result based on weighted index and inter-signal divergence
    final_diagnostic = int((total_score * 1000) - (diff_sum * 500))
    
    # This print is required
    print(f"Target result: {final_diagnostic}")
    return final_diagnostic

# Execute main logic
final_diagnostic = process_metrics(log_entries, system_thresholds)