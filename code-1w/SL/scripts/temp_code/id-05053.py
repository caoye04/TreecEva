def analyze_signal(x):
    return (x ** 2 + 3 * x + 1) % 100

def validate_sequence(seq):
    return sum(1 for i in seq if i % 3 == 0)

def decode_pattern(text):
    parts = text.split('-')
    combined = ''.join(reversed([p[::-1] for p in parts]))
    return int(combined[::2]) if combined[::2].isdigit() else 0

def transform_values(arr, factor=2):
    shifted = [((val << 1) ^ factor) & 255 for val in arr]
    normalized = [n - min(shifted) for n in shifted]
    return [n // (max(normalized) or 1) for n in normalized]

def accumulate_diagnostics(logs):
    total = 0
    for entry in logs:
        if isinstance(entry, dict) and 'flag' in entry:
            total += entry['value'] * (2 if entry['flag'] else 1)
    return total

def filter_anomalies(data, limit):
    anomalies = []
    for i, v in enumerate(data):
        temp_calc = (v * 1.7 + i) % 50
n        if temp_calc > limit:
            anomalies.append(v)
    return sorted(anomalies)

def extract_timing(signal_str):
    segments = signal_str.split(':')
    timing_vals = []
    for seg in segments:
        cleaned = ''.join(filter(str.isdigit, seg))
        if cleaned:
            timing_vals.append(int(cleaned) % 100)
    return timing_vals[::1]

def process_readings(raw_data, thresh):
    # Core transformation chain
    base_readings = [int(d * 1.5) for d in raw_data if d > 0]
    filtered = [x for x in base_readings if x < 200]
    
    # Irrelevant distraction: complex but unused calculation
    shadow_buffer = []
    for r in raw_data:
        encoded = ''.join([chr((int(r) + i) % 26 + 97) for i in range(3)])
        decoded_val = sum(ord(c) - 96 for c in encoded)
        shadow_buffer.append(decoded_val)
    
    # Distractor: multiple unused intermediate variables
    stats_snapshot = {
        'count': len(filtered),
        'sum': sum(filtered),
        'peak': max(filtered) if filtered else 0,
        'checksum': sum(transform_values(filtered[:10]))
    }
    
    # Key computation path
    processed = []
    for val in filtered:
        shifted = (val ^ 0xAA) >> 2
        applied_threshold = shifted > thresh
        if applied_threshold:
            processed.append(shifted * 3)
        else:
            processed.append(shifted // 2)
    
    # Secondary irrelevant function call (no impact)
    dummy_log = [{'value': i, 'flag': i % 4 == 0} for i in range(len(processed))]
    debug_total = accumulate_diagnostics(dummy_log)
    
    # Final aggregation with slicing distraction
    window = processed[-8:] if len(processed) >= 8 else processed
    aggregate = sum(window[::2]) * 1.5 + sum(window[1::2]) * 0.5
    
    # Real answer derivation
    final_diagnostic = int(aggregate + 0.5)
    
    # Red herring output
    print(f"Debug stats: {stats_snapshot}")
    print(f"Shadow buffer sum: {sum(shadow_buffer)}")
    print(f"Anomalies count: {len(filter_anomalies(raw_data, 45))}")
    
    return final_diagnostic

# Main execution
sensor_data = [120, -5, 88, 150, 205, 73, 94, 110, 67]
thresh = 40

# Unused decoy data structures
signal_trace = "abc-123-def-456"
timing_data = extract_timing("ping:12ms:seq:4:time:987")
decoded_key = decode_pattern(signal_trace)

# Actual target computation
final_diagnostic = process_readings(sensor_data, thresh)
print(f"Result: {final_diagnostic}")