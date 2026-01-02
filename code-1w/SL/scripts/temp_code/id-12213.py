import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(base_signal, noise_level, sample_count):
    samples = []
    for i in range(sample_count):
        noise = math.sin(i * 0.5) * noise_level
        samples.append(base_signal[i % len(base_signal)] + noise)
    return samples

# Irrelevant helper: signal smoothing (not used in final path)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return tuple(smoothed)

# Core transformation: apply frequency modulation and threshold slicing
def modulate_frequency(data, factor):
    modulated = []
    for x in data:
        modulated.append(x * math.cos(x * factor))
    return [round(val, 6) for val in modulated]

# Decoy function: spectral analysis (never called)
def compute_spectrum(signal):
    spectrum = set()
    for i in range(len(signal) - 1):
        delta = abs(signal[i+1] - signal[i])
        if delta > 0.1:
            spectrum.add(round(delta * 100, 2))
    return sorted(spectrum, reverse=True)

# Data binning based on dynamic thresholds
def bin_data(values, limits):
    bins = {'low': [], 'mid': [], 'high': []}
    for v in values:
        if v < limits[0]:
            bins['low'].append(v)
        elif v < limits[1]:
            bins['mid'].append(v)
        else:
            bins['high'].append(v)
    return bins

# Set-based anomaly detection using intersection heuristics
def detect_anomalies(buckets, ref_set):
    low_set = set([round(x) for x in buckets['low'] if abs(x) > 0.5])
    mid_set = set([round(x*2) for x in buckets['mid'] if x < 15])
    high_set = set([int(x) for x in buckets['high']])
    
    # Meaningless intersections (distraction)
    false_alerts = low_set & mid_set
    system_noise = mid_set ^ high_set
    
    # Actual relevant logic: count how many high values are in reference
    confirmed = high_set.intersection(ref_set)
    return len(confirmed) > 0, confirmed

# Main pattern analyzer combining multiple concepts
def analyze_pattern(seq, thres):
    # Step 1: Modulate input
    processed = modulate_frequency(seq, 0.7)
    
    # Step 2: Generate dynamic thresholds (only upper used later)
    avg_val = sum(processed) / len(processed)
    lower_bound = avg_val - thres[0]
    upper_bound = avg_val + thres[1]
    
    # Step 3: Bin the data
    grouped = bin_data(processed, [lower_bound, upper_bound])
    
    # Step 4: Prepare reference set (simulates known fault signatures)
    base_signatures = {x for x in range(-5, 25, 3)}
    extended_sig = base_signatures.copy()
    for x in list(base_signatures):
        extended_sig.add(x * -1)
        extended_sig.add(x + 10)
    
    # Step 5: Detect anomalies
    is_critical, matches = detect_anomalies(grouped, extended_sig)
    
    # Step 6: Compute entropy-like metric on modulated data (distractor)
    nonzero = [x for x in processed if x != 0]
    entropy = 0.0
    if nonzero:
        squares = [x*x for x in nonzero]
        mean_sq = sum(squares) / len(squares)
        entropy = math.log(mean_sq) if mean_sq > 0 else 0
    
    # Step 7: Final diagnostic logic (depends only on anomaly match size)
    score_basis = len(matches) * 100
    adjustment = 27  # Magic constant from calibration
    
    # Dead code branch: optimization flag never set
    optimization_mode = False
    if optimization_mode:
        adjustment = int(entropy * 10)
    
    final_score = score_basis + adjustment
    return final_score

# Entry point simulation
if __name__ == "__main__":
    # Initial signal configuration
    base_waveform = [1.0, 2.5, 3.2, 4.8, 5.1, 4.3, 3.7, 2.9]
    readings = collect_samples(base_waveform, noise_level=0.3, sample_count=32)
    
    # Unused derived data (red herring)
    filtered_readings = smooth_signal(readings, window=5)
    spectral_components = compute_spectrum(readings)  # Never defined!
    
    # Transform data for analysis
    transformed_data = modulate_frequency(readings, 0.7)
    
    # Define thresholds for binning
    thresholds = (1.8, 2.2)
    
    # Execute key diagnostic step
    final_diagnostic = analyze_pattern(transformed_data, thresholds)
    
    # Output result
    print(f"Result: {final_diagnostic}")