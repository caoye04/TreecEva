import math

# Simulated sensor array data from environmental monitoring station
def acquire_sensor_data():
    raw_values = [127, 255, 192, 64, 224, 32, 160, 96]
    timestamps = [1623456780 + i*30 for i in range(len(raw_values))]
    metadata = {"location": "Zone-7", "version": "2.1", "calibrated": True}
    
    # Irrelevant transformation (distractor)
    scaled_temp = [(v * 0.3) + 25.5 for v in raw_values]
    
    return dict(data=raw_values, time=timestamps, meta=metadata)

# Signal conditioning with red herring operations
def filter_noise(signal_packet):
    raw_data = signal_packet['data']
    filtered = []
    noise_floor = 32
    spike_threshold = 200
    
    # Real processing
    for val in raw_data:
        if val > noise_floor:
            if val < spike_threshold:
                filtered.append(val ^ 0x55)  # Bitwise obfuscation key
            else:
                adjusted = val & 0x7F
                filtered.append(adjusted)

    # Distractor: unused advanced filter
    def wavelet_denoise(x):
        return [i / 1.5 for i in x]  # Never called
    
    # Fake aggregation (misleading)
    avg_raw = sum(raw_data) / len(raw_data)
    peak_simulated = int(avg_raw * 1.2)

    signal_packet['processed'] = filtered
    return signal_packet

# Data normalization with irrelevant side computations
def normalize_amplitude(packet):
    if 'processed' not in packet:
        packet = filter_noise(packet)
    
    raw = packet['data']
    proc = packet['processed']
    
    # Actual work: normalize to 0-1 range using min-max
    min_val = min(proc)
    max_val = max(proc)
    normalized = [(x - min_val) / (max_val - min_val) if max_val != min_val else 0 for x in proc]
    
    # Distractor: physics-based model (unused)
    impedance = 50
    power_estimates = [((x / 255)**2) * impedance for x in raw]
    
    # Another red herring: frequency emulation
    sample_rate = 1000
    nyquist_zone = [sample_rate // (i+1) for i in range(5)]
    
    packet['normalized'] = normalized
    return packet

# Feature extraction with decoy logic paths
def extract_signatures(dataset):
    norm_data = dataset['normalized']
    features = []
    
    # Real feature: zero-crossing rate approximation
    crossings = 0
    for i in range(1, len(norm_data)):
        if norm_data[i-1] < 0.5 <= norm_data[i]:
            crossings += 1
    features.append(crossings)
    
    # Real feature: entropy approximation
    hist = [0]*4
    for x in norm_data:
        bin_idx = min(3, int(x * 4))
        hist[bin_idx] += 1
    entropy = 0
    total = len(norm_data)
    for count in hist:
        if count > 0:
            p = count / total
            entropy -= p * math.log2(p)
    features.append(round(entropy, 3))
    
    # Decoy ML-inspired transform (never used)
    def autoencode(feat):
        return [f * 0.9 for f in feat]
    
    # Fake pattern detection (distraction)
    patterns_found = 0
    for i in range(len(norm_data)-2):
        if norm_data[i] < norm_data[i+1] > norm_data[i+2]:
            patterns_found += 1
    
    dataset['features'] = features
    return dataset

# Core diagnostic analyzer (key function)
def analyze_readings(complete_dataset):
    if 'features' not in complete_dataset:
        complete_dataset = extract_signatures(complete_dataset)
    
    feats = complete_dataset['features']
    zcr = feats[0]  # Zero-crossing rate
    ent = feats[1]  # Entropy
    
    # Real computation path
    base_score = zcr * 100
    entropy_contribution = int(ent * 25)
    diagnostic_value = base_score + entropy_contribution
    
    # Misleading secondary analysis (dead path)
    def legacy_diagnostic(f):
        return (f[0] ** 1.5) + (f[1] * 10)
    
    # Fake failure mode simulation
    stress_test_results = [diagnostic_value * (1.1 ** i) for i in range(3)]
    
    # Final decision logic
    threshold = 150
    if diagnostic_value > threshold:
        status_code = 200
    else:
        status_code = 404
    
    # This is the actual answer variable
    final_diagnostic = diagnostic_value + status_code
    
    # Print required at end
    print(f"Result: {final_diagnostic}")
    
    return final_diagnostic

# Orchestration pipeline with multiple decoy stages
def run_monitoring_suite():
    # Stage 1: Acquire data
    sensor_data = acquire_sensor_data()
    
    # Stage 2: Filter noise
    cleaned = filter_noise(sensor_data)
    
    # Stage 3: Normalize signals
    calibrated = normalize_amplitude(cleaned)
    
    # Stage 4: Extract features
    analyzed = extract_signatures(calibrated)
    
    # Stage 5: Generate final diagnostic (KEY EXECUTION POINT)
    final_diagnostic = analyze_readings(analyzed)
    
    # Unused validation chain (red herring)
    def validate_pipeline(data):
        if 'meta' in data and data['meta']['calibrated']:
            return sum(data.get('processed', [])) % 100
        return -1
    
    return final_diagnostic

# Execute main workflow
result = run_monitoring_suite()
