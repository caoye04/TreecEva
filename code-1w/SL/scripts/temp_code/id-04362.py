def preprocess_readings(readings):
    # Irrelevant transformation: normalize to z-scores (not used in final calculation)
    mean_val = sum(readings) / len(readings)
    variance = sum((x - mean_val) ** 2 for x in readings) / len(readings)
    z_scores = [(x - mean_val) / (variance ** 0.5) for x in readings]
    return z_scores  # Dead end


def validate_entry(record):
    # Misleading validation that looks important but isn't used
    if not isinstance(record, dict):
        return False
    required = {'id', 'vital', 'timestamp'}
    return required.issubset(record.keys())


def accumulate_diagnostics(data_list):
    accumulator = []
    for entry in data_list:
        # Real but obfuscated logic path
        temp_flag = entry['vital'] > entry['threshold'] * 1.1
        warning_code = 2 if temp_flag else 0
        accumulator.append(warning_code)
    return accumulator


def compute_baseline(series, method='median'):
    # Distractor function with unused capability
    if method == 'mean':
        return sum(series) / len(series)
    elif method == 'median':
        sorted_s = sorted(series)
        mid = len(sorted_s) // 2
        return sorted_s[mid] if len(sorted_s) % 2 else (sorted_s[mid-1] + sorted_s[mid]) / 2
    return 0  # Unused fallback


def filter_anomalies(dataset, lower_q=0.1, upper_q=0.9):
    # Another red herring: computes quantiles but result ignored
    values = [d['vital'] for d in dataset]
    sorted_vals = sorted(values)
    n = len(sorted_vals)
    low_thresh = sorted_vals[int(n * lower_q)]
    high_thresh = sorted_vals[int(n * upper_q)]
    anomalies = [v for v in values if v < low_thresh or v > high_thresh]
    return anomalies  # Computed but unused


def analyze_metrics(records, limits):
    # Core logic buried in noise
    status_flags = []
    
    # Real processing begins
    vital_values = [r['vital'] for r in records]
    avg_vital = sum(vital_values) / len(vital_values)
    
    # Decoy intermediate
    deviation_pool = [abs(v - avg_vital) for v in vital_values]
    high_deviation_count = sum(1 for d in deviation_pool if d > 15.0)
    
    # Critical path: compare each reading against threshold
    for i, record in enumerate(records):
        base_limit = limits[i % len(limits)]
        raw_value = record['vital']
        
        # Multi-step evaluation
        exceeds_soft = raw_value > base_limit
        exceeds_hard = raw_value > base_limit * 1.2
        
        # Weighted impact score
        impact = 0
        if exceeds_soft:
            impact += 3
        if exceeds_hard:
            impact += 5
        
        # Boolean logic with tuple unpacking distraction
        codes = (exceeds_soft, exceeds_hard, impact > 0)
        has_warning, _, active = codes
        if has_warning and active:
            status_flags.append(impact)
    
    # Final computation
    aggregate_risk = sum(status_flags)
    adjustment_factor = len([v for v in vital_values if v > avg_vital]) - len(vital_values) // 2
    
    # Key assignment: this is the answer
    final_diagnostic = aggregate_risk * 7 + adjustment_factor
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Simulated health monitoring data (real input)
health_data = [
    {'id': 'P001', 'vital': 88, 'threshold': 80, 'timestamp': 1678886400},
    {'id': 'P002', 'vital': 95, 'threshold': 82, 'timestamp': 1678886500},
    {'id': 'P003', 'vital': 76, 'threshold': 85, 'timestamp': 1678886600},
    {'id': 'P004', 'vital': 92, 'threshold': 83, 'timestamp': 1678886700},
    {'id': 'P005', 'vital': 89, 'threshold': 81, 'timestamp': 1678886800}
]

# Threshold baselines (used in core logic)
thresholds = [80, 82, 85, 83, 81]

# Irrelevant preprocessing calls (distractors)
data_z = preprocess_readings([h['vital'] for h in health_data])
valid_flags = [validate_entry(h) for h in health_data]
baseline = compute_baseline([h['vital'] for h in health_data], method='median')
anomalies = filter_anomalies(health_data)

# Real execution point
flag_sequence = accumulate_diagnostics(health_data)
final_diagnostic = analyze_metrics(health_data, thresholds)