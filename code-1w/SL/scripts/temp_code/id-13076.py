import math

# Simulated sensor data processing with red herrings and distractions
def preprocess_signal(raw):
    amplitude = sum([x ** 2 for x in raw]) ** 0.5
    normalized = [x / amplitude for x in raw if x != 0]
    return normalized

# Irrelevant transformation - looks important but unused later
def deprecated_filter(x):
    return [val for val in x if val > 0.1] + [0] * 5

# Unused helper function (decoy)
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = -sum((count / total) * math.log2(count / total) for count in counts.values())
    return round(entropy, 4)

# Distractor: Real-time clock simulation (not used in final result)
def get_timestamp():
    return sum(list(range(5))) * 0.1 + 2.5

timestamp_log = []
for i in range(3):
    timestamp_log.append(get_timestamp() + i * 0.5)

# Core transformation pipeline
raw_sensor_data = [1, -3, 4, 2, -1, 5]
scaling_factor = 2.5
scaled_data = [x * scaling_factor for x in raw_sensor_data]
filtered_data = [x for x in scaled_data if x > 0]
transformed_data = [int(abs(x)) ** 2 for x in filtered_data]  # Becomes [25, 100, 25, 625]

# Misleading intermediate calculation (dead end)
aggregate_metrics = {
    'peak': max(transformed_data),
    'baseline_offset': 17,
    'history_buffer': [88, 92, 95],
    'temporal_weight': 0.85
}

# Another decoy structure
auxiliary_map = {
    'flags': [True, False, True],
    'debug_mode': True,
    'version': '2.1.0',
    'unused_result': compute_entropy([1, 2, 2, 3])
}

# Control flow with red herring branch
data_context = 'diagnostic'
if data_context == 'calibration':
    offset_correction = 12
elif data_context == 'test':
    offset_correction = -3
else:
    offset_correction = 0  # This runs but isn't critical

# Primary configuration dict with multiple irrelevant fields
config = {
    'mode': 'analysis',
    'threshold': 50,
    'precision': 6,
    'active_filters': ['f1', 'f2'],
    'cache_enabled': True,
    'retry_limit': 3,
    'timeout_ms': 500,
    'debug_trace': False,
    'version_check': 'disabled',
    'normalization_depth': 2
}

# Bit manipulation distraction
flag_register = 0b1101
mask = 0b1010
masked_flag = flag_register & mask  # Result: 8

# Unused recursive function (looks important)
def trace_path(n):
    if n <= 1:
        return 1
    return trace_path(n - 1) + trace_path(n - 2)

# Actual analysis logic (buried in noise)
def analyze_pattern(seq, cfg):
    threshold = cfg['threshold']
    count_above = sum(1 for x in seq if x > threshold)
    total = sum(seq)
    ratio = total / (count_above + 1e-8)
    
    # Secondary filter based on index position (even indices only)
    even_index_values = [seq[i] for i in range(0, len(seq), 2)]
    adjusted_sum = sum(even_index_values) - count_above
    
    # Final diagnostic combines multiple subtle effects
    diagnostic_score = adjusted_sum + int(ratio) - cfg['normalization_depth']
    return diagnostic_score

# Execution point of interest
final_diagnostic = analyze_pattern(transformed_data, config)

# Redundant logging block (distractor)
log_entry = f"Diagnostic run at t={get_timestamp()} with mode={config['mode']}"
print(f"Log: {log_entry}")

# Critical output - do not modify format
print(f"Target result: {final_diagnostic}")