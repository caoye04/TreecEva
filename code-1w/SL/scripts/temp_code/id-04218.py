import math

# Simulated sensor fusion system for environmental monitoring

def collect_metrics(base_offset):
    readings = []
    for i in range(5):
        val = (base_offset * i) ** 1.5 + math.sin(i)
        if val > 10:
            val -= 5
        readings.append(round(val, 3))
    return readings

# Irrelevant helper: format timestamp (dead utility)
def format_timestamp(ts):
    hours = int(ts // 3600)
    mins = int((ts % 3600) // 60)
    secs = int(ts % 60)
    return f'{hours:02}:{mins:02}:{secs:02}'

# Unused transformation path
def legacy_transform(data_list):
    shifted = [x * 0.9 + 2 for x in data_list]
    return [max(0, x - 1) for x in shifted]

# Core processing pipeline
def filter_outliers(raw_vals, threshold=12.0):
    clean_vals = []
    temp_stats = {'sum': 0, 'count': 0}
    for v in raw_vals:
        temp_stats['sum'] += v
        temp_stats['count'] += 1
    mean_val = temp_stats['sum'] / temp_stats['count']
    for v in raw_vals:
        if abs(v - mean_val) < threshold:
            clean_vals.append(v)
    return clean_vals

# Bit manipulation red herring
def encode_flags(mode, debug=False):
    flag = 0
    flag |= (mode & 0b111)
    flag <<= 3
    flag |= (int(debug) << 2)
    flag ^= 0b101
    # Result never used beyond this function
    decoded = ((flag ^ 0b101) >> 2) & 1
    return flag  # Dead end

# Recursive smoothing function
def smooth_recursive(seq, depth=0):
    if depth >= 2 or len(seq) < 2:
        return seq
    smoothed = []
    for i in range(len(seq)):
        neighbors = seq[max(0, i-1):min(len(seq), i+2)]
        smoothed.append(sum(neighbors) / len(neighbors))
    return smooth_recursive(smoothed, depth + 1)

# Set-based anomaly detection (key component)
def detect_anomalies(values):
    rounded_set = {round(x) for x in values}
    expected_set = set(range(int(min(rounded_set)), int(max(rounded_set)) + 1))
    missing = expected_set - rounded_set
    extra = rounded_set - expected_set
    return len(missing) - len(extra)

# Data enrichment with decoy logic
def enrich_data(filtered):
    augmented = []
    stats_log = []
    for idx, item in enumerate(filtered):
        # Meaningless scaling sequence
        scaled = item * 1.05
        normalized = scaled / (abs(scaled) + 1e-8)
        bucket = int(normalized * 10) if normalized >= 0 else 0
        
        # Fake security tag
        security_token = (idx + 7) * 13 % 17
        
        # Actual useful data point
        transformed = item + math.log(abs(item) + 1)
        augmented.append(transformed)
        
        # Logged but unused statistics
        stats_log.append({
            'index': idx,
            'raw': item,
            'token': security_token,
            'bucket': bucket
        })
    
    # Critical: only the augmented values are carried forward
    return augmented

# Main analysis engine
def analyze_readings(log_entries):
    if not log_entries:
        return -1
    
    # Compute distribution characteristics
    total = sum(log_entries)
    count = len(log_entries)
    avg = total / count
    variance = sum((x - avg) ** 2 for x in log_entries) / count
    stdev = math.sqrt(variance)
    
    # Determine stability class using recursive result
    smoothed_data = smooth_recursive(log_entries)
    stable_avg = sum(smoothed_data) / len(smoothed_data)
    
    # Use set operation to assess integrity
    anomaly_score = detect_anomalies(log_entries)
    
    # Final diagnostic calculation (this is where answer comes from)
    final_diagnostic = int(
        (avg * 0.6) + 
        (stdev * 0.2) + 
        (anomaly_score * -3) + 
        (len(smoothed_data) * 0.5)
    )
    
    # Dead branch: never executed due to hard-coded condition
    if False and 'debug_mode' in globals():
        audit_trail = []
        for entry in log_entries:
            audit_trail.append(hex(int(entry)))

    return final_diagnostic

# --- Execution Sequence ---
if __name__ == "__main__":
    # Initial data collection
    raw_sensor_data = collect_metrics(base_offset=3.2)
    
    # Apply filtering
    processed_logs = filter_outliers(raw_sensor_data, threshold=12.0)
    
    # Enrich data (some side effects ignored)
    enriched_set = enrich_data(processed_logs)
    
    # Encode flags for non-existent hardware layer
    control_flag = encode_flags(mode=5, debug=True)  # No effect on output
    
    # Timestamp logging (irrelevant)
    current_time = 3721
    time_label = format_timestamp(current_time)
    
    # Key statement: compute final diagnostic
    final_diagnostic = analyze_readings(processed_logs)
    
    # Output the required result
    print(f"Result: {final_diagnostic}")