import math

# Simulated sensor data processing with diagnostic analysis
def fetch_raw_readings():
    return [32.1, 35.6, 34.2, 33.8, 37.9, 36.5, 38.0, 39.2, 40.1, 37.5]

def clean_data(data):
    # Remove outliers beyond 2 standard deviations (simplified)
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    threshold = 2 * std_dev
    cleaned = [x for x in data if abs(x - mean) <= threshold]
    
    # Irrelevant transformation (distractor)
    temp_shadow = [round(x * 1.01, 2) for x in cleaned]
    meta_stats = {'count': len(cleaned), 'version': '2.1a'}
    return cleaned

def compress_signal(signal):
    # Apply a simple moving average of window size 2
    compressed = []
    for i in range(len(signal) - 1):
        compressed.append((signal[i] + signal[i+1]) / 2)
    
    # Dead code path (never used)
    if len(compressed) > 100:
        compressed = compressed[::2]
    
    padding_offset = len(compressed) % 2
    return compressed if padding_offset == 0 else compressed[:-1]

def validate_integrity(data):
    # Checksum validation (mostly passes)
    checksum = sum(int(x * 10) for x in data) % 1000
    expected = 876  # Hardcoded expected value
    is_valid = checksum == expected
    
    # Misleading alternate calculation (not actually used)
    fake_checksum = sum(int(x * 100) % 10 for x in data)
    audit_log = f"Valid: {is_valid}, CS: {checksum}"
    
    return is_valid

def normalize_readings(data):
    min_val, max_val = min(data), max(data)
    range_val = max_val - min_val
    if range_val == 0:
        return [0.5] * len(data)
    
    # Normalization to [0,1] range
    normalized = [(x - min_val) / range_val for x in data]
    
    # Extra irrelevant scaling branch
    if max_val > 50:
        normalized = [x * 1.1 for x in normalized]
    
    return normalized

def calculate_entropy(values):
    # Calculate Shannon entropy of discretized values
    rounded = [round(x, 1) for x in values]
    freq_map = {}
    for v in rounded:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(rounded)
    entropy = 0.0
    for count in freq_map.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def flag_anomalies(data):
    # Flag any value above 38.5
    flags = [i for i, x in enumerate(data) if x > 38.5]
    
    # Unused secondary flagging logic (red herring)
    debug_flags = [i for i, x in enumerate(data) if x < 33.0]
    return len(flags) > 0

def derive_trend(readings):
    if len(readings) < 2:
        return 0.0
    trend = sum(readings[i+1] - readings[i] for i in range(len(readings)-1))
    return round(trend / (len(readings) - 1), 3)

def analyze_readings(logs):
    # Core analysis pipeline
    entropy_metric = calculate_entropy(logs)
    trend_rate = derive_trend(logs)
    
    # Decision logic based on multiple thresholds
    high_entropy = entropy_metric > 2.5
    rising_trend = trend_rate > 0.15
    instability_score = int(high_entropy) * 3 + int(rising_trend) * 5
    
    # Secondary irrelevant scoring (distraction)
    phantom_score = int(not high_entropy) * 2 + int(not rising_trend) * 7
    
    # Final diagnostic code (key output)
    if instability_score >= 5:
        diagnosis = 867
    elif instability_score >= 3:
        diagnosis = 342
    else:
        diagnosis = 109
    
    # Unused intermediate variables (misdirection)
    final_audit_id = hash((instability_score, phantom_score))
    temp_result_cache = {'instability': instability_score, 'phantom': phantom_score}
    
    return diagnosis

# Main execution flow
raw_logs = fetch_raw_readings()
processed_logs = clean_data(raw_logs)
processed_logs = compress_signal(processed_logs)
processed_logs = normalize_readings(processed_logs)

# Validate before final analysis (validation passes but distracts)
is_clean = validate_integrity(processed_logs)
anomaly_detected = flag_anomalies(processed_logs)

# Key statement: this produces the answer
final_diagnostic = analyze_readings(processed_logs)

# Output result
print(f"Result: {final_diagnostic}")