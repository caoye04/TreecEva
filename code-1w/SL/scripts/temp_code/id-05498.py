from collections import defaultdict, Counter
import math

# Simulated sensor data processing pipeline for aerospace diagnostics
def collect_sensor_readings():
    readings = [23.4, 25.1, 24.8, 26.2, 25.5, 27.0, 24.9, 25.3]
    offset = 0.5
    adjusted = [r + offset for r in readings]
    return adjusted

def analyze_variance(data):
    mean_val = sum(data) / len(data)
    squared_diffs = [(x - mean_val) ** 2 for x in data]
    variance = sum(squared_diffs) / len(squared_diffs)
    return variance

def generate_frequency_map(seq):
    # Irrelevant helper - simulates signal harmonics (distraction)
    freq_map = defaultdict(int)
    for item in seq:
        freq_map[item] += 1
    return freq_map

def detect_anomalies(log_entries):
    # Dead path: never actually used in final computation
    anomaly_counter = Counter()
    thresholds = {'temp': 26.0, 'pressure': 50.0}
    for entry in log_entries:
        if entry['type'] == 'temp' and entry['value'] > thresholds['temp']:
            anomaly_counter['high_temp'] += 1
    return anomaly_counter

def evaluate_consistency(pattern):
    # Distractor function: looks important but unused
    if len(pattern) < 2:
        return True
    trend = all(pattern[i] <= pattern[i+1] for i in range(len(pattern)-1))
    oscillations = sum(1 for i in range(1, len(pattern)-1) 
                        if (pattern[i-1] < pattern[i] > pattern[i+1]) or 
                           (pattern[i-1] > pattern[i] < pattern[i+1]))
    return oscillations < 3

def compute_system_entropy(flags):
    # Bit manipulation red herring
    flag_state = 0
    for i, flag in enumerate(flags):
        if flag:
            flag_state |= (1 << i)
    entropy = 0
    temp = flag_state
    while temp:
        entropy += temp & 1
        temp >>= 1
    return entropy

def compute_integrity_score(flags, log):
    # Core logic hidden among distractions
    base_score = 0
    for flag in flags:
        if flag:
            base_score += 17
    
    # Real dependency: count 'INFO' entries in log
    info_count = 0
    for entry in log:
        if entry['level'] == 'INFO':
            info_count += 1
    
    # Actual formula: base_score * info_count - magic_offset
    magic_offset = 42
    intermediate = base_score * info_count
    adjustment = int(math.sqrt(intermediate)) if intermediate > 0 else 0
    final_score = intermediate - magic_offset - adjustment
    
    # Multiple layers of irrelevant computations
    dummy_calc = 0
    for i in range(5):
        dummy_calc += (i ** 3) % 7
    
    metadata = {"timestamp": 1294875, "version": "2.1.0", "dummy": dummy_calc}
    
    # Final result obscured by surrounding noise
    return final_score

# Main execution block
if __name__ == '__main__':
    # Primary data sources
    raw_readings = collect_sensor_readings()
    variance_metric = analyze_variance(raw_readings)
    
    # Irrelevant frequency analysis on meaningless derived data
    shifted_values = [int(x * 2) % 10 for x in raw_readings]
    digit_freq = generate_frequency_map(shifted_values)
    
    # Construct system state with mixed relevance
    operational_flags = [True, False, True, True, False]
    entropy_value = compute_system_entropy(operational_flags)  # Computed but unused
    
    # Log data containing relevant INFO count
    system_log = [
        {'level': 'DEBUG', 'msg': 'startup'},
        {'level': 'INFO', 'msg': 'initialized'},
        {'level': 'INFO', 'msg': 'calibrated'},
        {'level': 'WARN', 'msg': 'minor_drift'},
        {'level': 'INFO', 'msg': 'nominal'},
        {'level': 'INFO', 'msg': 'synced'}
    ]
    
    # Simulate unused anomaly detection
    anomalies = detect_anomalies(system_log)
    
    # Consistency check - dead code path
    trend_stable = evaluate_consistency(raw_readings)
    
    # Critical statement: this produces the answer
    final_diagnostic = compute_integrity_score(operational_flags, system_log)
    
    # Print required output
    print(f"Result: {final_diagnostic}")