import math

# Simulated system telemetry data with mixed signal types
def generate_telemetry():
    base_signals = [i * 0.5 for i in range(20)]
    noise_floor = [0.1 * (j % 3) for j in range(20)]
    return [base_signals[k] + noise_floor[k] for k in range(20)]

# Irrelevant helper: formats timestamp strings (not used in final computation)
def format_timestamp(unix_time):
    hours = int(unix_time // 3600)
    mins = int((unix_time % 3600) // 60)
    secs = int(unix_time % 60)
    return f'{hours:02}:{mins:02}:{secs:02}'

# Decoy function: appears useful but unused
def compute_entropy(data_list):
    total = sum(data_list)
    if total == 0:
        return 0.0
    probabilities = [x / total for x in data_list]
    return -sum(p * math.log(p) for p in probabilities if p > 0)

# Misleading intermediate transformation (used only in dead path)
def apply_filter(signal, mode='lowpass'):
    if mode == 'lowpass':
        return [sum(signal[i:i+3]) / 3 for i in range(len(signal)-2)]
    return signal

# Core processing pipeline
telemetry_log = generate_telemetry()
baseline_offset = 2.5
adjusted_log = [x + baseline_offset for x in telemetry_log]

# Statistical summaries (some irrelevant)
mean_value = sum(adjusted_log) / len(adjusted_log)
variance = sum((x - mean_value) ** 2 for x in adjusted_log) / len(adjusted_log)
std_deviation = math.sqrt(variance)
median_value = sorted(adjusted_log)[len(adjusted_log)//2]

# Dead code path with misleading calculations
if len(adjusted_log) < 10:
    dummy_correction = sum(apply_filter(adjusted_log))
else:
    dummy_correction = 0  # Dead end

# System thresholds and diagnostic rules
system_thresholds = {
    'critical_level': 8.0,
    'warning_band': (4.0, 6.0),
    'stability_zone': lambda x: 2.0 <= x <= 3.5,
    'decay_constant': 0.85
}

# Data transformation map (dictionary operation)
transformation_map = {
    i: round(math.sin(val) * 100) / 100 
    for i, val in enumerate(adjusted_log)
}

# Secondary derived metrics (mostly distractions)
signal_peaks = [i for i, x in enumerate(adjusted_log) if x > 7.0]
peak_count_metric = len(signal_peaks) if signal_peaks else -1

# Another decoy structure
auxiliary_cache = {}
for idx in range(len(adjusted_log)):
    aux_key = f'cache_{idx}'
    auxiliary_cache[aux_key] = math.cos(adjusted_log[idx])

# Real logic begins: count how many transformed values exceed threshold
transformed_exceeds = 0
for raw_idx, transformed_val in transformation_map.items():
    if transformed_val > 0.7:
        transformed_exceeds += 1

# Hidden logical condition using boolean chain
is_stable = all(
    system_thresholds['stability_zone'](x) 
    for x in adjusted_log[:5]
) or (transformed_exceeds > 3 and mean_value > 5.0)

# Lambda-based dynamic evaluator (key concept)
evaluate_response = lambda x, thresh: 1 if x > thresh else -1

# Simulated response curve evaluation
response_codes = [
    evaluate_response(val, system_thresholds['critical_level']) 
    for val in adjusted_log
]

# Count critical responses
critical_alerts = sum(1 for code in response_codes if code == 1)

# Diagnostic processor combining multiple concepts
def process_metrics(log_data, config):
    # Local shadowing variables (distractors)
    mean_value = sum(log_data) / len(log_data)
    temp_flags = [0] * len(log_data)
    
    # Bit manipulation red herring
    bit_accumulator = 0
    for i in range(min(10, len(log_data))):
        shifted = int(log_data[i]) << 1
        bit_accumulator ^= shifted
    
    # Actual relevant logic (obscured)
    high_count = sum(1 for x in log_data if x > config['warning_band'][1])
    in_stability = sum(1 for x in log_data[:6] if config['stability_zone'](x))
    
    # Complex conditional integration
    if high_count > 4 and not is_stable:
        base_score = 850 + (high_count * 12)
    elif in_stability >= 4:
        base_score = 420
    else:
        base_score = 612
    
    # Final adjustment using decay model (actually deterministic)
    decay_factor = config['decay_constant']
    adjusted_score = base_score * decay_factor
    
    # Inject subtle override based on transformed space (real key)
    if transformed_exceeds >= 5:
        adjusted_score += 38.0
    
    return round(adjusted_score, 4)

# Execution point of interest
final_diagnostic = process_metrics(log_data=adjusted_log, system_thresholds=system_thresholds)

# Print result as required
print(f"Target result: {final_diagnostic}")