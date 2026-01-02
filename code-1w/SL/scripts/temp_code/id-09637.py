import math

# Simulated system telemetry data
def fetch_telemetry():
    raw_signals = [256, 1024, 512, 2048]
    signal_power = sum([math.log2(x) for x in raw_signals])  # Irrelevant aggregation
    return {'power': signal_power, 'readings': [77, 85, 90, 88, 92]}

def decode_transmission(encoded_str):
    # Distractor function: looks important but unused in critical path
    return encoded_str[::-1].upper().replace('X', '').strip()

def validate_checksum(data_list):
    # Red herring validation with bit manipulation
    checksum = 0
    for d in data_list:
        checksum ^= d
        checksum = (checksum << 1) & 0xFF
    return checksum == 0

def compute_entropy(values):
    # Seemingly advanced but irrelevant computation
    total = sum(values)
    probabilities = [v / total for v in values]
    entropy = -sum(p * math.log2(p) for p in probabilities if p > 0)
    return round(entropy, 3)

def extract_critical_events(log_text):
    # Processes string but result not used in final answer
    lines = log_text.split('\n')
    events = {i: line for i, line in enumerate(lines) if 'CRITICAL' in line}
    event_keys = set(events.keys())
    mask = len(event_keys) << 2 if event_keys else 0
    return mask  # Dead end

def analyze_health_trend(metrics):
    # Complex-looking trend analysis with decoy logic
    trend_score = 0
    for i in range(1, len(metrics)):
        if metrics[i] > metrics[i-1]:
            trend_score += 1
        elif metrics[i] < metrics[i-1]:
            trend_score -= 1
    adjustment = math.sin(trend_score)  # Misleading float conversion
    return int(abs(adjustment) * 100)

def build_diagnostic_summary(reading_set, flags):
    # Builds dictionary but only one field matters
    summary = {
        'baseline': min(reading_set),
        'peak': max(reading_set),
        'stability': len(reading_set) > 4,
        'flags_active': len(flags),
        'version': 'DX-8'
    }
    summary['diagnostic_code'] = (summary['peak'] - summary['baseline']) * summary['flags_active']
    return summary

def analyze_system_state(readings, log):
    # Core function with embedded distractors
    if not readings:
        return -1
    
    # Real processing begins
    base_offset = readings[0] // 10
    temp_flag = any(r > 95 for r in readings)
    
    # Irrelevant nested block with complex control flow
    anomaly_count = 0
    for r in readings:
        if r < 70 or r > 100:
            anomaly_count += 1
    if anomaly_count > 1:
        base_offset += 5
    
    # Meaningful computation mixed with noise
    log_lines = log.split('\n')
    severity_weight = sum(1 for line in log_lines if 'ERROR' in line) * 10
    
    # Decoy dictionary operations
    error_map = {i: line for i, line in enumerate(log_lines) if 'ERROR' in line}
    error_hash = sum(len(k.encode()) for k in error_map.values() if isinstance(k, str)) % 99
    
    # Actual answer derivation (well-hidden)
    reading_set = set(readings)
    valid_range = {x for x in reading_set if 80 <= x <= 95}
    size_factor = len(valid_range)
    
    # Critical formula
    candidate_value = (base_offset + severity_weight) * size_factor
    
    # Dead code branch that looks plausible
    if candidate_value > 100:
        candidate_value = math.floor(candidate_value / 2.5)
    
    # Final red herring: unused sophisticated transform
    hex_trace = ''.join(format(ord(c), 'x') for c in log[:10])
    final_shift = int(hex_trace[:2], 16) % 7 if hex_trace else 0
    
    # Only this line matters
    final_diagnostic = candidate_value + 7
    return final_diagnostic

# Main execution sequence
if __name__ == '__main__':
    telemetry = fetch_telemetry()
    health_metrics = telemetry['readings']  # [77, 85, 90, 88, 92]
    
    # Fabricated system log with misleading content
    system_log = """START INIT DX-8
STATUS OK
DATA STREAM ACTIVE
ERROR DISK WRITE TIMEOUT
CALIBRATION COMPLETE
ERROR MEMORY ECC TRIGGERED
NORMAL TERMINATION
"""
    
    # Irrelevant pre-processing
    processed_log = system_log.strip().lower()
    line_count = len(processed_log.split('\n'))
    char_freq = {c: processed_log.count(c) for c in 'abcdef'}
    
    # Key statement
    final_diagnostic = analyze_system_state(health_metrics, system_log)
    
    # Additional distraction
    metadata_tag = decode_transmission('x9k2m')
    entropy_metric = compute_entropy(health_metrics)
    
    # Output required
    print(f"Result: {final_diagnostic}")