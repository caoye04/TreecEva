from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
def fetch_sensor_stream():
    raw_signals = [24, 17, 24, 35, 12, 12, 24, 17, 41, 35]
    timestamps = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
    statuses = ['OK', 'ERR', 'OK', 'OK', 'WARN', 'WARN', 'OK', 'ERR', 'OK', 'OK']
    return list(zip(raw_signals, timestamps, statuses))

def filter_anomalies(signal_stream):
    filtered = []
    error_count = 0
    for sig, ts, stat in signal_stream:
        if stat == 'ERR':  # Irrelevant filtering path (not used)
            error_count += 1
            continue
        if stat == 'WARN':  # Decoy logic: Warnings are actually not skipped
            sig = sig * 2  # Misleading transformation
        filtered.append(sig)
    return filtered

def generate_baseline(length):
    # Dead code path: never used in final computation
    return [int(30 + 10 * math.sin(i)) for i in range(length)]

def enhance_resolution(data):
    # Real but partially obfuscated processing
    amplified = [x * 3 for x in data]  # Triple all values
    shifted = [x + 5 for x in amplified]  # Add offset
    return shifted

def compute_entropy(values):
    # Distractor function: computes something plausible but unused
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    return round(entropy, 4)

def build_threshold_map(config_level=2):
    # Complex configuration map with red herring entries
    defaults = defaultdict(lambda: 100)
    defaults['low'] = 50
    defaults['med'] = 75
    defaults['high'] = 90
    # Unused nested structure to distract
    defaults['profiles'] = {'A': [10, 20], 'B': [30, 40], 'C': None}
    mode = 'med' if config_level > 1 else 'low'
    scale_factor = 2 if config_level == 3 else (1.5 if config_level == 2 else 1)
    adjusted = {key: int(val * scale_factor) for key, val in defaults.items() if isinstance(val, int)}
    adjusted['dynamic_cap'] = 200  # Irrelevant cap
    return adjusted

def validate_integrity(data_chunk):
    # Checksum decoy
    checksum = sum(x % 7 for x in data_chunk) * 11
    return checksum < 500  # Always true, distractor

def multiplex_channels(primary, secondary=None):
    # Unused complex merging logic
    if secondary is None:
        secondary = [1] * len(primary)
    return [(a ^ b) + 1 for a, b in zip(primary, secondary)]

def analyze_signal(clean_data, thresholds):
    # Core logic buried in distractions
    base_score = sum(clean_data)
    penalty = 0
    
    # Actual conditional logic determining result
    if base_score > thresholds['med']:
        penalty += 15
    if base_score > thresholds['high']:
        penalty += 25
    
    # Real computation hidden among irrelevant ones
    temp_log = [math.log(x) for x in clean_data if x > 0]
    log_sum = sum(temp_log)
    
    # Key decision point
    adjustment = int(log_sum) if log_sum > 20 else 30
    
    # Final calculation
    result = (base_score // 3) - penalty + adjustment
    
    # Dead branches below
    if result < 0:
        result = 0
    elif result > 1000:
        result = 999  # Never reached
        
    return result

# Orchestration with multiple distractions
def main_pipeline():
    stream = fetch_sensor_stream()
    
    # Irrelevant baseline generation (dead code)
    _ = generate_baseline(len(stream))
    
    # Real data flow begins here
    cleaned = filter_anomalies(stream)
    processed_data = enhance_resolution(cleaned)
    
    # Spurious validation (no effect on output)
    _ = validate_integrity(processed_data)
    
    # Unused channel multiplexing (distractor)
    _ = multiplex_channels(processed_data)
    
    # Entropy computed but ignored
    _ = compute_entropy(processed_data)
    
    # Threshold map is actually used
    threshold_map = build_threshold_map(config_level=2)
    
    # Critical execution point
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Additional red herring variables
    final_diagnostic_shadow = final_diagnostic * 2 + 10
    if final_diagnostic_shadow > 1000:
        final_diagnostic_shadow = 100  # Unused
    
    print(f"Result: {final_diagnostic}")

# Execute
main_pipeline()