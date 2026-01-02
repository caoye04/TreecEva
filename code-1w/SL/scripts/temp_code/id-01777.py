import itertools

# Simulated sensor array data from a distributed monitoring system
def collect_sensor_data():
    base_values = [2.1, 3.5, 4.0, 1.8, 5.2]
    noise_offsets = [0.1 * i for i in range(5)]
    return [base_values[i] + noise_offsets[i] for i in range(5)]

# Irrelevant auxiliary function: processes unrelated telemetry (red herring)
def analyze_telemetry(stream):
    cumulative = 0
    for val in stream:
        if val > 3.0:
            cumulative += val * 0.5
        else:
            cumulative -= val * 0.1
    return cumulative  # Never used in final result

# Misleading intermediate transformation (dead path)
def deprecated_normalization(data):
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data] if max_val != min_val else [0] * len(data)

# Core metric processor with conditional logic and bit manipulation
def compute_stability_index(x, y):
    if x < 2.5 or y > 4.5:
        return int((x * 10) ^ int(y)) % 7  # Bitwise XOR in stability calc
    elif 2.5 <= x <= 4.0 and y <= 4.5:
        return int((x + y) * 1.5) & 15  # Bitwise AND masking
    else:
        return (int(x) | int(y)) + 3  # Bitwise OR fallback

# Main processing pipeline
def generate_health_flags(metrics):
    flags = []
    for m in metrics:
        if m > 4.0:
            flags.append(3)  # Critical threshold
        elif m > 2.5:
            flags.append(1)  # Warning level
        else:
            flags.append(0)  # Normal
    return flags

# Higher-order reduction using itertools (core relevant usage)
def reduce_with_rolling(metrix, window_size=2):
    rolling_windows = list(itertools.pairwise(metrix)) if hasattr(itertools, 'pairwise') else \
        list(zip(metrix, metrix[1:]))
    return [sum(pair) / window_size for pair in rolling_windows]

# Complex conditional routing with decoy branches
def route_processing_path(data, load_level):
    threshold = 3.8 if load_level > 60 else 3.2
    
    # Dead branch: never taken due to hard-coded condition below
    def legacy_comp(data):
        return sum(data) / len(data)
    
    # Another red herring variable
    temp_correction = -0.3 if sum(data) > 10.0 else 0.0
    
    if False:  # Explicitly unreachable block
        return [x + temp_correction for x in data]
    
    filtered = [x for x in data if x >= threshold]
    return filtered if filtered else [threshold]  # Ensures non-empty

# Primary metric processor combining arithmetic, logic, and data flow
def process_metrics(indicators, load):
    # Step 1: Generate flag indicators
    flag_signals = generate_health_flags(indicators)
    
    # Step 2: Apply rolling average on original indicators
    rolled = reduce_with_rolling(indicators)
    
    # Step 3: Compute pairwise stability indices
    stability_scores = []
    for i in range(len(rolled)):
        score = compute_stability_index(rolled[i], flag_signals[i % len(flag_signals)])
        stability_scores.append(score)
    
    # Step 4: Aggregate stability with weighted influence
    total_influence = 0
    weight_sequence = itertools.cycle([0.8, 1.1, 0.9])
    
    for s, w in zip(stability_scores, weight_sequence):
        if len(stability_scores) > 3:  # Only applies here
            total_influence += s * w
        else:
            total_influence += s * 1.0
    
    # Step 5: Apply load-based adjustment (conditional)
    adjustment_factor = 0.95 if load > 75 else 1.05
    adjusted_influence = total_influence * adjustment_factor
    
    # Step 6: Final diagnostic via integer truncation
    final_value = int(adjusted_influence * 10) / 10.0  # Round to 1 decimal
    
    # Irrelevant post-processing (never used)
    outlier_check = [v for v in stability_scores if v > 10]
    report_timestamp = "2023-12-15T10:30:00Z"
    
    return final_value

# --- Execution Context ---

# Real data collection
raw_diagnostics = collect_sensor_data()  # [2.1, 3.6, 4.1, 1.9, 5.3]

# Simulated system load (percent)
system_load = 68

# Spurious analysis (distraction)
technical_readout = analyze_telemetry(raw_diagnostics)  # Unused
normalized_legacy = deprecated_normalization(raw_diagnostics)  # Unused

# Routing decision (with embedded dead code)
filtered_stream = route_processing_path(raw_diagnostics, system_load)

# Key statement: main processing
health_indicators = raw_diagnostics
final_diagnostic = process_metrics(health_indicators, system_load)

# Output target result
print(f"Result: {final_diagnostic}")