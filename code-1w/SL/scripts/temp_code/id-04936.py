import math

# Simulated sensor data acquisition
def acquire_signal():
    raw_samples = [i * 0.01 for i in range(500)]
    noise_floor = sum([math.sin(x * 0.5) * 0.3 for x in raw_samples])
    return [math.cos(x) * 2.0 + math.sin(x * 7) * 0.5 + 0.1 for x in raw_samples]

# Irrelevant auxiliary function (decoy)
def calculate_entropy(data):
    total = 0.0
    for x in data:
        if x > 0:
            total -= x * math.log(x)
    return total

# Signal conditioning with red herring processing steps
def preprocess(signal):
    amplified = [x * 3.5 for x in signal]
    filtered = [x for x in amplified if abs(x) > 0.5]  # Energy thresholding
    
    # Distraction: statistical summary with no downstream use
    mean_val = sum(filtered) / len(filtered) if filtered else 0
    variance = sum((x - mean_val) ** 2 for x in filtered) / len(filtered) if filtered else 0
    peak_to_peak = max(filtered) - min(filtered) if filtered else 0
    
    # Dummy transformation chain
    temp_result = [abs(x) ** 0.5 * (-1)**i for i, x in enumerate(filtered)]
    normalized = [x / (max(temp_result) or 1) for x in temp_result]
    
    # Actual relevant transformation (buried)
    folded = [abs(x) for x in amplified][:256]  # Rectify and truncate
    return folded

# Data binning - irrelevant but plausible
def create_histogram(data, bins=16):
    if not data:
        return [0] * bins
    min_d, max_d = min(data), max(data)
    counts = [0] * bins
    for x in data:
        idx = min(bins - 1, int((x - min_d) / (max_d - min_d + 1e-9) * bins))
        counts[idx] += 1
    return counts

# Core analysis function with conditional logic red herrings
def evaluate_coherence(signal_part):
    if len(signal_part) < 100:
        return 0.0
    
    # Compute multiple metrics, most unused
    rms = math.sqrt(sum(x*x for x in signal_part) / len(signal_part))
    kurtosis = sum((x/rms)**4 for x in signal_part) / len(signal_part) if rms > 0 else 0
    zero_crossings = sum(1 for i in range(1, len(signal_part)) if signal_part[i-1] * signal_part[i] < 0)
    
    # Distractor: complex frequency-like estimation (unused)
    spectral_centroid = 0.0
    fft_proxy = []
    for k in range(len(signal_part)//8):
        component = sum(signal_part[n] * math.cos(2*math.pi*k*n/len(signal_part)) for n in range(len(signal_part)))
        fft_proxy.append(abs(component))
    if sum(fft_proxy) > 0:
        spectral_centroid = sum(i * v for i, v in enumerate(fft_proxy)) / sum(fft_proxy)
    
    # Actual key computation (obscured)
    if rms > 1.0:
        return 1.75 + (kurtosis * 0.1)
    else:
        return 0.85 + (zero_crossings * 0.001)

# Higher-level fusion with misleading control flow
def integrate_diagnostics(metrics):
    base_score = metrics.get('coherence', 0)
    reliability = metrics.get('entropy', 0)
    stability = metrics.get('variance_ratio', 1.0)
    
    # Complex condition that never triggers (dead path)
    if base_score > 2.0 and reliability < 0.1:
        return base_score * 0.3
    
    # Another decoy branch
    if stability < 0.5:
        adjustment = math.tanh(reliability * 2)
        return base_score * (0.7 + adjustment * 0.3)
    
    # Real path
    return base_score * (1.1 if base_score > 1.0 else 0.9)

# Final analysis combining multiple concepts
def analyze_signal(data_chunk):
    # Step 1: Segment data
    chunk_size = 64
    segments = [data_chunk[i:i+chunk_size] for i in range(0, len(data_chunk), chunk_size)][:4]
    
    # Step 2: Extract features with list comprehensions and lambdas
    segment_energies = [sum(x**2 for x in seg) for seg in segments]
    energy_threshold = sum(segment_energies) / len(segment_energies) * 0.8
    high_energy_mask = [e > energy_threshold for e in segment_energies]
    
    # Step 3: Apply evaluation only to active segments
    coherence_scores = []
    for i, seg in enumerate(segments):
        if high_energy_mask[i]:
            score = evaluate_coherence(seg)
            coherence_scores.append(score)
    
    # Step 4: Aggregate with distractor statistics
    avg_coherence = sum(coherence_scores) / len(coherence_scores) if coherence_scores else 0
    peak_coherence = max(coherence_scores) if coherence_scores else 0
    consistency = sum(1 for x in coherence_scores if abs(x - avg_coherence) < 0.2)
    
    # Step 5: Spurious normalization chain
    normalized_consistency = consistency / 4.0
    adjusted_avg = avg_coherence * (1 + normalized_consistency * 0.1)
    
    # Step 6: Final diagnostic calculation (answer depends only on this)
    diagnostic_weight = 0.6 if adjusted_avg > 1.5 else 0.4
    final_diagnostic = int((adjusted_avg * diagnostic_weight * 1000)) / 1000.0
    
    return final_diagnostic

# --- Execution Flow ---
sensor_data = acquire_signal()
processed_data = preprocess(sensor_data)

# Unused functions and variables to increase interference
unused_histogram = create_histogram(processed_data, bins=32)
unused_entropy = calculate_entropy(processed_data[::10])
placeholder_metrics = {
    'entropy': unused_entropy,
    'variance_ratio': 0.95,
    'baseline_drift': sum(processed_data[:50]) / 50
}

temp_diagnostic = integrate_diagnostics(placeholder_metrics)
final_diagnostic = analyze_signal(processed_data)

print(f"Target result: {final_diagnostic}")