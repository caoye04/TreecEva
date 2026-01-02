import math

# Simulated system performance analysis with decoy calculations
def analyze_throughput(data_stream, window_size):
    if len(data_stream) == 0:
        return 0
    
    # Irrelevant preprocessing (distractor)
    normalized = [x / max(data_stream) for x in data_stream if x > 0]
    smoothed = [sum(normalized[i:i+window_size]) / window_size 
                 for i in range(len(normalized) - window_size + 1)]
    
    # Unused transformation path (dead code)
    def fourier_approx(signal):
        return [sum(signal[j] * math.cos(2 * math.pi * j * k / len(signal)) 
                     for j in range(len(signal))) for k in range(10)]
    
    # Real but obscured logic
    raw_total = sum(data_stream)
    penalty = len([x for x in data_stream if x < 50]) * 1.5
    return raw_total - penalty

# Misleading utility function (never called)
def compute_efficiency_rating(inputs, outputs):
    ratio = [o / i if i != 0 else 0 for o, i in zip(outputs, inputs)]
    return sum(ratio) / len(ratio)

# Core evaluation logic with red herrings
def evaluate_component_health(sensor_readings):
    thresholds = {'temp': 75, 'voltage': 12.5, 'current': 3.2}
    status_flags = {}
    
    # String-based diagnostics (slicing distraction)
    diag_code = "ERR_NONE, WARN_VOLT_HIGH, CRIT_TEMP_SPIKE, INFO_STABLE"
    codes = diag_code.split(", ")
    latest_status = codes[-1].lower().replace("info_", "")
    
    # Dictionary manipulation red herring
    health_map = {i: val for i, val in enumerate(sensor_readings)}
    filtered = {k: v for k, v in health_map.items() if v > 40}
    
    # Actual calculation buried in noise
    base_health = sum(1 for v in sensor_readings if v < thresholds['temp'])
    stress_factor = math.sqrt(len(sensor_readings) ** 2 / (1 + len(filtered)))
    return base_health * stress_factor

# Primary function with multiple distractions
def evaluate_performance(log_entries, config):
    # Irrelevant data structure transformations
    history_buffer = log_entries[::-1]  # reversed order (unused)
    recent_batch = history_buffer[:config.get('lookback', 10)]
    
    # Complex dictionary operations (partly irrelevant)
    metrics_summary = {}
    for entry in log_entries:
        for k, v in entry.items():
            if k not in metrics_summary:
                metrics_summary[k] = []
            metrics_summary[k].append(v)
    
    # String processing decoy
    signature = "PERF_LOG_V2"
    version_code = int(signature[9]) if len(signature) > 9 else 1
    
    # Multiple unused variables and computations
    overhead_penalty = 0
    for i in range(len(log_entries)):
        if i % 7 == 0:
            overhead_penalty += math.log(i + 1) * 0.1
    
    # Bit manipulation distraction (XOR shift pattern)
    magic_seed = 0
    for val in [len(log_entries), config['base_scale'], version_code]:
        magic_seed ^= (val << 2) | (val >> 1)
    
    # Real signal extraction
    throughput_data = [e['throughput'] for e in log_entries if 'throughput' in e]
    health_readings = [e['health'] for e in log_entries if 'health' in e]
    
    # Critical nested computation chain
    t_score = analyze_throughput(throughput_data, window_size=3)
    h_score = evaluate_component_health(health_readings)
    
    # Modular arithmetic red herring
    cyclic_adjustment = (len(log_entries) ** 2) % 7 / 10.0
    
    # Final calculation with misleading components
    base_performance = t_score + h_score
    config_modifier = config['base_scale'] * config['multiplier']
    adjustment_factor = (config_modifier + cyclic_adjustment) / (1 + overhead_penalty)
    
    # Key result determination
    final_raw = base_performance * adjustment_factor
    
    # Normalize to integer score
    return int(round(final_raw))

# Ground truth input data
baseline_config = {
    'base_scale': 2,
    'multiplier': 3,
    'lookback': 5,
    'threshold_mode': 'adaptive'
}

metrics_log = [
    {'throughput': 120, 'health': 65, 'timestamp': 'T1'},
    {'throughput': 95, 'health': 70, 'timestamp': 'T2'},
    {'throughput': 130, 'health': 45, 'timestamp': 'T3'},
    {'throughput': 80, 'health': 85, 'timestamp': 'T4'},
    {'throughput': 110, 'health': 60, 'timestamp': 'T5'},
    {'throughput': 90, 'health': 55, 'timestamp': 'T6'}
]

# Execution point of interest
final_score = evaluate_performance(metrics_log, baseline_config)

# Output requirement
print(f"Target result: {final_score}")