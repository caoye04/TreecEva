import itertools

# Simulated sensor data processing with embedded diagnostics
raw_readings = [0.7, -1.2, 0.95, -0.3, 1.4, -0.8, 2.1, -1.6, 0.55, 1.8]
baseline_threshold = 0.75
noise_floor = 0.25

def apply_filter(data, method='moving_avg', window=3):
    # Irrelevant filtering method with red herring
    if method == 'moving_avg':
        smoothed = []
        for i in range(len(data) - window + 1):
            smoothed.append(sum(data[i:i+window]) / window)
        return smoothed
    elif method == 'median':
        sorted_data = sorted(data)
        return sorted_data[len(sorted_data)//2]
    return data  # fallback

def detect_anomalies(series, sensitivity=0.8):
    # Complex but partially irrelevant anomaly logic
    anomalies = []
    high_priority = []
    for idx, val in enumerate(series):
        if abs(val) > baseline_threshold * sensitivity:
            anomalies.append(idx)
            if val > baseline_threshold * 1.2:
                high_priority.append(idx)
    return anomalies, high_priority or [None]  # decoy default

def compute_entropy(values):
    # Distractor: entropy calculation not central to final result
    from math import log
    total = sum(abs(x) for x in values)
    if total == 0:
        return 0.0
    probabilities = [abs(x)/total for x in values]
    entropy = -sum(p * log(p) for p in probabilities if p > 0)
    return round(entropy, 4)

def generate_combinations(data):
    # Dead path: generates combinations but unused later
    combo_results = []
    for r in range(2, 4):
        for combo in itertools.combinations(data, r):
            combo_results.append(sum(combo))
    return sorted(combo_results)[:10]

def flag_transients(readings, gap_tolerance=1):
    # Misleading transient detection with side effects
    flags = []
    for i in range(1, len(readings)):
        if abs(readings[i] - readings[i-1]) > noise_floor * 2:
            flags.append(i)
    return flags if len(flags) > gap_tolerance else [0]

# Signal preprocessing pipeline
filtered_signal = apply_filter(raw_readings, method='moving_avg')
residual_noise = [x - 0.1 for x in raw_readings[:len(filtered_signal)]]  # decoy alignment

# Intermediate diagnostics (some used, some not)
anomaly_indices, critical_events = detect_anomalies(filtered_signal, sensitivity=0.9)
entropy_metric = compute_entropy(filtered_signal)
transient_flags = flag_transients(filtered_signal)

# Generate unused combinatorial features
combination_summaries = generate_combinations([int(x*10) for x in filtered_signal])

# Core transformation: relevant but buried among distractions
normalized = [round(x / baseline_threshold, 3) for x in filtered_signal]
squashed = [abs(x)**1.5 for x in normalized]
weighted_sum = sum(x * (i + 1) for i, x in enumerate(squashed))  # Key accumulation

# Conditional data routing - only one branch matters
if len(anomaly_indices) >= 3:
    processed_data = [x for x in squashed if x > 0.5]
elif entropy_metric < 1.0:
    processed_data = [x for x in squashed if x <= 1.0]
else:
    processed_data = squashed  # Actual execution path taken

# Final analysis function with conditional expression
mask_value = 0.77
override_mode = False
def analyze_signal(signal):
    base_score = sum(signal)
    length_factor = len(signal) if len(signal) % 2 == 1 else len(signal) // 2
    adjustment = (base_score / length_factor) if length_factor != 0 else 0
    
    # Critical use of conditional expression and itertools
    peak_count = sum(1 for k, g in itertools.groupby(signal) if next(g) > 1.0)
    
    # Final computation with distractors
    temp_bias = mask_value if override_mode else 0.13
    secondary_offset = sum(x for x in signal if x > 1.0) * temp_bias
    
    # Deterministic answer path
    final_score = adjustment + secondary_offset - peak_count * 0.25
    return round(final_score, 6)

# Execute main computation
diagnostic_trace = compute_entropy(residual_noise)  # Red herring call
final_diagnostic = analyze_signal(processed_data)
print(f"Result: {final_diagnostic}")