import math

# Simulated sensor array data with noise and calibration factors
def acquire_sensor_data():
    raw_readings = [127, 255, 89, 180, 203]
    noise_floor = 7
    calibrated = [x + noise_floor for x in raw_readings]
    return calibrated

# Irrelevant auxiliary function – dead code path (distractor)
def legacy_compatibility_mode(data):
    if sum(data) > 500:
        return [x // 2 for x in data if x % 2 == 0]
    else:
        return [x * 3 for x in data]

# Signal processing pipeline
def filter_outliers(signal, threshold=190):
    filtered = [x for x in signal if x <= threshold]
    return filtered

# Bit manipulation for error detection (relevant)
def compute_parity(word):
    parity = 0
    temp = word
    while temp:
        parity ^= 1
        temp &= temp - 1
    return parity

# Apply bitwise integrity check across data (used later)
def apply_integrity_scan(data):
    scan_results = []
    for val in data:
        if val % 2 == 0:
            scan_results.append(compute_parity(val))
        else:
            scan_results.append(0)
    return scan_results

# Secondary transformation: normalize and scale (distractor unless inspected deeply)
def normalize_readings(data):
    max_val = max(data)
    return [round(x / max_val, 4) for x in data]

# Unused normalization trace – misleading intermediate
normalization_trace = []

# Data enhancement with decoy logic
def enhance_resolution(data, factor=2):
    enhanced = []
    for i in range(len(data)):
        if i > 0 and data[i] > data[i-1]:
            enhanced.append(data[i] * factor)
        else:
            enhanced.append(data[i])
    # Following line appears important but is unused
    enhanced_squared = [x**2 for x in enhanced]
    return enhanced

# Core analysis function combining multiple concepts
def analyze_signal(data_packet):
    # Step 1: Reduce dimensionality via filtering
    clean_signal = filter_outliers(data_packet)
    
    # Step 2: Compute statistical baseline
    mean_level = sum(clean_signal) / len(clean_signal)
    deviation_pool = [abs(x - mean_level) for x in clean_signal]
    avg_deviation = sum(deviation_pool) / len(deviation_pool)
    
    # Step 3: Trigger synthetic correction if deviation is high (red herring)
    if avg_deviation > 40:
        adjustment = 0.85
        corrected = [int(x * adjustment) for x in clean_signal]
    else:
        corrected = clean_signal  # No change applied
    
    # Step 4: Perform bit-level diagnostics on corrected values
    integrity_flags = apply_integrity_scan(corrected)
    total_parity = sum(integrity_flags)
    
    # Step 5: Apply conditional transformation based on parity count
    if total_parity > 2:
        base_anchor = min(corrected)
    else:
        base_anchor = max(corrected)
    
    # Step 6: Calculate diagnostic fingerprint
    entropy_score = 0
    for x in corrected:
        if x > 0:
            entropy_score += x * math.log(x, 2)
    
    # Step 7: Combine anchor with entropy (truncated to integer)
    rough_metric = int(entropy_score // 3)
    
    # Step 8: Final computation using anchor and metric
    final_diagnostic = base_anchor + rough_metric - total_parity
    
    # Dead assignment – looks meaningful but unused
    diagnostic_checksum = (final_diagnostic ^ 0xFF) & 0xFFFF
    
    return final_diagnostic

# Orchestration block
if __name__ == "__main__":
    # Acquire initial data
    raw_data = acquire_sensor_data()
    
    # Apply enhancement (but don't use enhanced version in main path)
    enhanced_data = enhance_resolution(raw_data)
    
    # Normalize for display? Not actually used in analysis
    normalized_data = normalize_readings(raw_data)
    normalization_trace.append(normalized_data)
    
    # Filter real working data
    processed_data = filter_outliers(raw_data, threshold=200)
    
    # Main analysis call
    final_diagnostic = analyze_signal(processed_data)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")