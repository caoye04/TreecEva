import math

def analyze_signal_strength(base_freq, harmonics):
    # Irrelevant signal processing function (dead end)
    total = 0
    for h in harmonics:
        total += base_freq * (h ** 2)
    return total if total > 100 else 0

def compute_entropy(data_stream):
    # Misleading entropy calculation with unused logic
    if not data_stream:
        return 0.0
    entropy = 0.0
    freq_map = {}
    for val in data_stream:
        freq_map[val] = freq_map.get(val, 0) + 1
    for count in freq_map.values():
        p = count / len(data_stream)
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 3)

def validate_checksum(frame):
    # Decoy validation function that looks important but isn't used in final result
    checksum = 0
    for byte in frame:
        checksum ^= byte
    return checksum == 0xFF

def evaluate_response_time(latencies):
    # Unused performance metric
    avg = sum(latencies) / len(latencies)
    peak = max(latencies)
    return {'average': avg, 'peak': peak, 'jitter': peak - avg}

def aggregate_metrics(chain, load):
    # Core function that computes the actual answer
    baseline = chain['stage_3']['output']
    adjustment_factor = load['peak_phase'] if load['voltage_stable'] else load['backup_phase']
    
    # Complex conditional expression (required Python feature)
    modifier = 1.75 if (baseline % 4 == 0 and adjustment_factor > 50) else (0.85 if baseline < 200 else 1.15)
    
    intermediate = (baseline * adjustment_factor) // 100
    
    # Logical operations and min/max usage (suggested paradigms)
    safety_limit = min(950, max(600, load['thermal_threshold']))
    critical_flag = (intermediate > safety_limit) and (load['voltage_stable'] or not load['overclock_mode'])
    
    # Final computation path
    if critical_flag:
        result = int(intermediate * modifier) + 37
    else:
        result = int(intermediate * 0.92)
    
    # Distractor: multiple irrelevant variables below
    debug_trace = [result ^ i for i in range(5)]  # Bit manipulation red herring
    anomaly_score = compute_entropy([result & 0xFF, result >> 8])  # Calls decoy function
    validation_log = [validate_checksum([i % 256 for i in debug_trace])]  # Useless checksum
    
    return result

# Simulated system telemetry (complex data structure)
processing_chain = {
    'stage_1': {
        'input': 142,
        'filters': [0x1A, 0x2C, 0x3F],
        'active': True
    },
    'stage_2': {
        'buffer': [5, 8, 13, 21],
        'checksum': 0xDEAD,
        'output': 188
    },
    'stage_3': {
        'input_source': 'sensor_array',
        'calibration': {'gain': 2.1, 'offset': -7},
        'output': 204  # This feeds into baseline
    }
}

# System load profile with misleading fields
system_load = {
    'peak_phase': 62,
    'backup_phase': 41,
    'voltage_stable': True,
    'overclock_mode': False,
    'thermal_threshold': 725,
    'fan_speed_rpm': 3400,
    'uptime_seconds': 87430,
    'power_cycles': 12,
    'last_reset_cause': 'watchdog_timeout'
}

# Dead code path - never called but looks important
signal_harmonics = [3, 5, 7, 11]
current_entropy = compute_entropy([1, 2, 2, 3, 3, 3, 4, 4, 5])
signal_diagnostic = analyze_signal_strength(13.7, signal_harmonics)

# Key execution point
final_diagnostic = aggregate_metrics(processing_chain, system_load)

# Print result as required
print(f"Target result: {final_diagnostic}")