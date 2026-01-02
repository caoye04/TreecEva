import math

def analyze_signal_strength(signal):
    if not signal:
        return 0
    peak = max(signal)
    avg = sum(signal) / len(signal)
    normalized_peak = peak / (avg + 1e-5)
    return int(normalized_peak * 100) // 10 * 10

def validate_checksum(data_str):
    checksum = 0
    for char in data_str:
        checksum += ord(char) % 7
    return checksum % 3 == 0

def decode_sensor_array(raw_array):
    decoded = []
    for val in raw_array:
        shifted = (val << 2) & 0xFF
        inverted = shifted ^ 0xAA
        if inverted > 100:
            decoded.append(inverted - 50)
        else:
            decoded.append(inverted + 25)
    return [d for d in decoded if d % 2 == 1]

def evaluate_stability_index(config_flags):
    base_score = 0
    for flag in config_flags:
        if flag.startswith('ENABLE_'):
            base_score += 3
        elif flag.endswith('_DEBUG'):
            base_score -= 2
        else:
            base_score += 1
    return base_score * len(config_flags)

def process_metrics(log_entry, status_flag):
    # Core relevant logic begins here
    timestamp_str = log_entry.get('timestamp', '')
    uptime_hours = log_entry.get('uptime', 0)
    
    # Irrelevant string processing (distractor)
    cleaned_ts = timestamp_str.strip().upper().replace('-', '').split('T')[0]
    year_part = cleaned_ts[:4] if len(cleaned_ts) >= 4 else '2000'
    month_code = sum(ord(c) for c in year_part) % 12 + 1
    
    # Key computation path
    error_count = len(log_entry.get('errors', []))
    warning_list = log_entry.get('warnings', [])
    severity_weight = sum(len(w.split()) for w in warning_list)
    
    # Conditional expression with meaningful impact
    base_metric = severity_weight if error_count < 5 else error_count * 2
    
    # Dictionary operations (relevant)
    diagnostics = {
        'initial': base_metric,
        'penalty': 0,
        'correction': 0
    }
    
    if status_flag['power'] == 'unstable':
        diagnostics['penalty'] += 8
    if status_flag['thermal'] == 'overheating':
        diagnostics['penalty'] += 12
    
    # Bit manipulation red herring
    temp_register = 0x1A5
    masked = (temp_register ^ 0xFF) & 0x0F
    decoy_value = (masked << 3) | 0x07  # unused later
    
    # String method chain distraction
    mode_desc = log_entry.get('mode', 'standby').lower()
    if 'active' in mode_desc and mode_desc.islower():
        active_boost = len(mode_desc) * 3
    else:
        active_boost = 0
    
    # Unused recursive-like function (dead path)
    def calculate_depth(x):
        return x + calculate_depth(x-1) if x > 0 else 0  # never called
    
    # Critical conditional expression
    adjustment_factor = 1.5 if 'critical' in warning_list else 0.8
    
    # Final diagnostic calculation (answer depends on this)
    raw_diagnostic = (diagnostics['initial'] + active_boost - diagnostics['penalty']) * adjustment_factor
    final_diagnostic = int(math.floor(raw_diagnostic))
    
    # More distractions
    metadata_summary = {k: len(str(v)) for k, v in log_entry.items()}
    summary_score = sum(metadata_summary.values()) % 17
    
    # Unused complex list comprehension
    _ = [math.sin(i * 0.1) for i in range(100) if i % 7 == 0 and summary_score > 10]
    
    return final_diagnostic

# Simulated input data
log_data = {
    'timestamp': '2023-11-05T08:45:30Z',
    'uptime': 142.5,
    'errors': [404, 500, 403],
    'warnings': ['high memory usage', 'critical disk latency'],
    'mode': 'ACTIVE_MODE',
    'version': 'v2.1.0-beta'
}
system_status = {
    'power': 'unstable',
    'thermal': 'normal',
    'network': 'degraded'
}

# Trigger execution
final_diagnostic = process_metrics(log_data, system_status)
print(f"Result: {final_diagnostic}")