from collections import defaultdict, Counter

# Simulate sensor array data with noise and calibration offsets
def generate_raw_signals():
    base_frequency = 17
    signal_length = 64
    raw_samples = [((i * base_frequency) % 256) ^ (i % 73) for i in range(signal_length)]
    noise_floor = [i % 3 for i in range(signal_length)]
    calibrated = [raw_samples[i] - noise_floor[i] + 5 for i in range(signal_length)]
    return calibrated

# Parse configuration profile (mostly irrelevant except for 'gain')
def load_config():
    config = defaultdict(lambda: 'default')
    config['version'] = '2.1'
    config['mode'] = 'diagnostic'
    config['gain'] = 3
    config['timeout'] = 1500
    config['buffer_size'] = 1024
    return config

# Heavy preprocessing with red herrings: FFT simulation (not actually used in final result)
def simulate_fft(data):
    transformed = []
    for i in range(len(data)):
        acc = 0
        for j in range(len(data)):
            angle = (i * j) % 8
            acc += data[j] * (angle + 1)
        transformed.append(acc % 256)
    return transformed

# Apply non-linear gain correction (only gain=3 produces correct path)
def apply_gain_correction(data, factor):
    if factor <= 0:
        return data[:]
    corrected = []
    for x in data:
        if x < 0:
            corrected.append(-((-x) ** 0.5) * factor)
        else:
            corrected.append((x ** 0.5) * factor)
    return [int(x) for x in corrected]

# Filter out outliers using IQR logic (distractor: never called)
def remove_outliers_quartile(data):
    sorted_data = sorted(data)
    q1 = sorted_data[len(sorted_data)//4]
    q3 = sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower, upper = q1 - 1.5*iqr, q3 + 1.5*iqr
    return [x for x in data if lower <= x <= upper]

# Core transformation: fold and compress via bit manipulation
def fold_signal_chunks(data):
    folded = []
    for i in range(0, len(data), 4):
        chunk = data[i:i+4]
        while len(chunk) < 4:
            chunk.append(0)
        # Key computation: XOR + shift folding
        folded_val = (chunk[0] ^ chunk[1]) << 1
        folded_val ^= (chunk[2] ^ chunk[3])
        folded.append(folded_val & 255)  # Keep in byte range
    return folded

# Analyze frequency peaks (dead code path - not used)
def detect_peaks(arr):
    peaks = []
    for i in range(1, len(arr)-1):
        if arr[i-1] < arr[i] > arr[i+1]:
            peaks.append(i)
    return peaks

# Main analysis with conditional dispatch (only one branch matters)
def analyze_signal(data, thresholds):
    temp_stats = Counter()
    for val in data:
        temp_stats[val // 32] += 1
    
    mode_key = temp_stats.most_common(1)[0][0]
    aggregate = 0
    
    # Critical path: depends on prior gain correction
    for item in data:
        if item > thresholds.get(mode_key, 50):
            aggregate += (item & 15) ^ 7
        else:
            aggregate -= item & 3
    
    # Decoy accumulation
    decoy_sum = sum((i * data[i]) % 19 for i in range(len(data)) if i % 4 == 0)
    decoy_sum += len(temp_stats) * 100
    
    return aggregate  # Only this matters

# Irrelevant utility: checksum validation (never invoked)
def compute_crc8(data):
    crc = 0
    for b in data:
        crc ^= b
n        crc &= 0xFF
    return crc

# High-level orchestration with misleading intermediate outputs
def main_pipeline():
    # Step 1: Load raw data
    raw_sensor_data = generate_raw_signals()
    
    # Step 2: Load config (only 'gain' is relevant)
    system_config = load_config()
    gain_factor = system_config['gain']
    
    # Step 3: Apply critical gain correction
    amplified_signal = apply_gain_correction(raw_sensor_data, gain_factor)
    
    # Step 4: Simulate FFT (irrelevant)
    fft_result = simulate_fft(amplified_signal)
    
    # Step 5: Fold signal chunks - this modifies structure
    processed_data = fold_signal_chunks(amplified_signal)
    
    # Step 6: Create threshold map based on static heuristics
    threshold_map = defaultdict(int)
    for i in range(8):
        threshold_map[i] = (i * 13 + 7) % 64
    
    # Step 7: Dead code assignments (red herrings)
    outlier_free = processed_data[:]  # Never filtered
    peak_locations = lambda d: [j for j in range(1,len(d)-1) if d[j-1]<d[j]>d[j+1]]
    spectral_entropy = sum(x*x for x in fft_result[:10]) / 100.0
    
    # Step 8: The key statement
    final_diagnostic = analyze_signal(processed_data, threshold_map)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Execute main logic
result = main_pipeline()