import math

# Simulated sensor fusion system for environmental anomaly detection
def collect_readings(base_freq, harmonics):
    readings = []
    for i in range(1, harmonics + 1):
        phase_shift = (i % 4) * math.pi / 2
        amplitude = (100 + i * 7) / (i ** 1.5)
        value = amplitude * math.sin(base_freq * i + phase_shift)
        readings.append(round(value, 6))
    return readings

def generate_baseline(n):
    # Irrelevant function - simulates environmental noise but unused in final calculation
    return [math.cos(j * 0.3) * 12.5 for j in range(n)]

def filter_outliers(data, limit=25.0):
    # Filters values beyond ±limit; used in real path
    return [x for x in data if abs(x) <= limit]

def compute_entropy(values):
    # Unused distractor: calculates Shannon entropy of binned data
    counts = {}
    for v in values:
        bin_key = int(v * 2)  # Quantize
        counts[bin_key] = counts.get(bin_key, 0) + 1
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 6)

def extract_features(signal):
    # Extract statistical and spectral features
    n = len(signal)
    avg = sum(signal) / n
    variance = sum((x - avg) ** 2 for x in signal) / n
    peak_magnitude = max(abs(x) for x in signal)
    zero_crossings = sum(1 for i in range(1, n) if signal[i-1] * signal[i] < 0)
    
    # Transform into frequency domain via simple power-of-two energy proxy
    energy_bins = [0]*4
    for i, val in enumerate(signal):
        bin_idx = (i * 4) // n
        energy_bins[bin_idx] += val ** 2
    
    # Return feature vector (some elements used later)
    return {
        'mean': avg,
        'variance': variance,
        'peak': peak_magnitude,
        'zero_cross': zero_crossings,
        'energy_distribution': energy_bins
    }

def validate_checksum(data_tuple):
    # Dead code path — never called in execution
    a, b, c, d = data_tuple
    checksum = (a ^ b) & 0xFFFF
    return checksum == ((c << 8) | (d & 0xFF))

def merge_segments(segments):
    # Unused complex logic — looks important but irrelevant
    combined = []
    for seg in segments:
        normalized = [x / max(abs(max(seg)), abs(min(seg))) for x in seg if x != 0]
        combined.extend(normalized)
    return combined

def detect_coherent_patterns(seq):
    # Uses set operations to find recurring magnitude clusters
    magnitudes = {round(abs(x), 3) for x in seq if abs(x) > 1.0}  # Use set for uniqueness
    reference_pool = {round(5.0 * (k + 1) / 7, 3) for k in range(7)}
    common = magnitudes.intersection(reference_pool)
    coherence_score = len(common) * 100 / len(reference_pool)
    return coherence_score, common

def analyze_signal(pattern, criteria):
    # Core analysis with decoys and multiple concepts
    
    # Step 1: Feature extraction
    features = extract_features(pattern)
    
    # Step 2: Apply dynamic threshold filtering using criteria
    active_energy_bands = [
        idx for idx, e in enumerate(features['energy_distribution'])
        if e > criteria['min_energy']
    ]
    
    # Step 3: Coherence analysis using set logic
    coherence_score, matched_peaks = detect_coherent_patterns(pattern)
    
    # Step 4: Conditional diagnostic path
    if features['variance'] < criteria['variance_floor']:
        base_diagnostic = features['mean'] * 100
    elif len(active_energy_bands) >= 3:
        base_diagnostic = features['peak'] * 50
    else:
        base_diagnostic = features['zero_cross'] * -25
    
    # Step 5: Adjust by coherence only if certain bands are active (key dependency)
    adjustment_factor = 1.0
    if 0 in active_energy_bands and 3 in active_energy_bands:
        adjustment_factor = (1 + coherence_score / 100)  # Up to 2x boost
    
    # Step 6: Final computation
    raw_result = base_diagnostic * adjustment_factor
    
    # Irrelevant post-processing block (looks significant but skipped)
    if False:  # Dead branch
        temp_log = []
        for x in pattern:
            if x > 0:
                temp_log.append(math.log(x))
        smoothed = sum(temp_log) / len(temp_log)
        raw_result -= smoothed
    
    # Final mapping through modular arithmetic
    final_value = int((raw_result ** 2) % 97321)
    
    # Red herring variables that look diagnostic but aren't used
    entropy_distractor = compute_entropy(pattern)
    baseline_ref = generate_baseline(len(pattern))
    merged_data = merge_segments([pattern[:5], pattern[5:]])
    
    return final_value

# --- Main Execution ---
if __name__ == '__main__':
    # Generate primary signal
    raw_signal = collect_readings(base_freq=0.8, harmonics=18)
    
    # Filter to create composite pattern
    composite_pattern = filter_outliers(raw_signal, limit=22.5)
    
    # Define decision thresholds
    thresholds = {
        'min_energy': 18.3,
        'variance_floor': 150.0
    }
    
    # Perform final analysis
    final_diagnostic = analyze_signal(composite_pattern, thresholds)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")