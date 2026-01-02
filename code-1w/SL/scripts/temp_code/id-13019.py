import itertools

# Simulated sensor data preprocessing with red herrings
def preprocess_sensor_stream(raw_readings):
    filtered = [x for x in raw_readings if x > -50 and x < 150]
    baseline_shift = sum(filtered) // len(filtered)
    adjusted = [x - baseline_shift for x in filtered]
    return adjusted

# Irrelevant transformation: spectral decomposition (unused later)
def spectral_decompose(signal):
    result = []
    for i in range(len(signal)):
        component = 0
        for j in range(len(signal)):
            component += signal[j] * (1 if (i * j) % 2 == 0 else -1)
        result.append(component)
    return result

# Core pattern analyzer
def count_monotonic_segments(seq):
    if not seq:
        return 0
    segments = 1
    increasing = None
    for a, b in zip(seq, seq[1:]):
        if a != b:
            now_increasing = b > a
            if increasing is not None and now_increasing != increasing:
                segments += 1
            increasing = now_increasing
    return segments

# Misleading peak detection (dead function - never called in execution path)
def detect_peaks(signal, threshold=10):
    peaks = []
    for i in range(1, len(signal) - 1):
        if signal[i] > max(signal[i-1], signal[i+1]) and signal[i] > threshold:
            peaks.append(i)
    return peaks  # Unused

# Real transformation chain
def transform_sequence(seq):
    doubled = [x * 2 for x in seq]
    shifted = [x + 1 for x in doubled]
    return [x for x in shifted if x % 3 != 0]  # Filter out multiples of 3

# Data fusion from multiple sources (some irrelevant)
def fuse_streams(stream_a, stream_b):
    combined = []
    for a, b in zip(stream_a, stream_b):
        fused_val = (a * 3 + b * 7) % 100  # Weighted fusion
        combined.append(fused_val)
    padding = [0] * (len(stream_a) - len(combined))
    return combined + padding  # Rarely used padding

# Main analysis function with key logic
def analyze_pattern(data, config):
    # Step 1: Segment into chunks
    chunk_size = config.get('chunk_size', 4)
    chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
    
    # Step 2: Analyze each chunk
    results = []
    for idx, chunk in enumerate(chunks):
        if len(chunk) < 3:
            continue
        
        # Compute local metrics
        avg = sum(chunk) / len(chunk)
        variance = sum((x - avg) ** 2 for x in chunk) / len(chunk)
        trend = sum(b - a for a, b in zip(chunk, chunk[1:]))
        
        # Hidden key computation: longest run of even numbers
        max_even_run = 0
        current_run = 0
        for val in chunk:
            if val % 2 == 0:
                current_run += 1
                max_even_run = max(max_even_run, current_run)
            else:
                current_run = 0
        
        # Store structured result
        results.append({
            'idx': idx,
            'avg': avg,
            'variance': variance,
            'trend': trend,
            'max_even_run': max_even_run,
            'score': avg + variance - abs(trend)  # Red herring metric
        })
    
    # Final aggregation: sum of max_even_run across chunks
    total_even_streak = sum(r['max_even_run'] for r in results)
    
    # Secondary effect: interaction with config threshold
    threshold = config.get('threshold', 5)
    modifier = 1
    if total_even_streak > threshold:
        modifier = 2
    
    # Critical answer computation
    return total_even_streak * modifier

# Decoy post-processing (never reached in control flow)
def post_process_diagnostics(diag_list):
    sorted_diags = sorted(diag_list, reverse=True)
    smoothed = []
    for i, val in enumerate(sorted_diags):
        neighbor_avg = (sorted_diags[i-1] + val + sorted_diags[(i+1) % len(sorted_diags)]) / 3
        smoothed.append(int(neighbor_avg))
    return smoothed

# --- Execution Body ---
if __name__ == '__main__':
    # Raw input data
    sensor_input = [12, 14, 16, 21, 23, 18, 15, 27, 30, 32, 34, 36, 39, 45, 48, 50]
    
    # Irrelevant secondary stream (used in dead code only)
    aux_stream = [5, 8, 11, 14, 17, 20, 23, 26]
    
    # Preprocessing step
    processed = preprocess_sensor_stream(sensor_input)
    
    # Apply real transformation
    transformed_data = transform_sequence(processed)
    
    # Dead branch - simulated alternate path
    if False:  # Never taken
        alt_data = fuse_streams(processed, aux_stream)
        spectrum = spectral_decompose(alt_data)
        transformed_data = [x % 40 for x in spectrum]
    
    # Configuration with misleading keys
    thresholds = {
        'chunk_size': 4,
        'threshold': 5,
        'sensitivity': 0.8,
        'calibration': 'high',
        'peak_filter': True
    }
    
    # Key statement
    final_diagnostic = analyze_pattern(transformed_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")