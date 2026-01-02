import math

# Simulated sensor array data processing with diagnostic logic
def collect_sensor_readings():
    raw_values = [i * 1.5 + math.sin(i) for i in range(100)]
    offset_correction = sum([math.cos(j) for j in range(10)]) / 10
    calibrated = [v + offset_correction + 0.1 for v in raw_values]
    return calibrated

# Irrelevant auxiliary function – decoy for signal smoothing (never used)
def smooth_signal(data, passes=3):
    temp = data[:]
    for _ in range(passes):
        temp = [(temp[i-1] + temp[i] + temp[i+1]) / 3 if 0 < i < len(temp)-1 else temp[i] for i in range(len(temp))]
    return temp

# Noise filtering using dynamic thresholds (used)
def filter_noise(readings, cutoff=2.0):
    noise_floor = sum([abs(x) for x in readings[:20]]) / 20 * 0.5
    filtered = []
    for val in readings:
        if abs(val) > noise_floor and abs(val) > cutoff:
            filtered.append(val * 0.9)
        elif abs(val) <= noise_floor:
            continue  # drop low-amplitude noise
        else:
            filtered.append(val * 0.2)
    return filtered

# Transform data into frequency domain approximation (used)
def apply_fourier_approximation(data):
    transformed = []
    N = len(data)
    for k in range(N // 10):
        re = sum(data[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        im = -sum(data[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        magnitude = math.sqrt(re * re + im * im) / N
        transformed.append(magnitude)
    return transformed

# Unused legacy function – red herring
def normalize_legacy_scheme(arr):
    max_val = max(abs(x) for x in arr)
    return [x / max_val if max_val != 0 else 0 for x in arr]

# Detect anomalies based on histogram bins (used in part)
def detect_anomalies(signal):
    bins = [0] * 10
    min_s, max_s = min(signal), max(signal)
    if min_s == max_s:
        return [0]
    for val in signal:
        idx = int((val - min_s) / (max_s - min_s) * 9)
        bins[idx] += 1
    peak_bin = bins.index(max(bins))
    anomalies = []
    for i, b in enumerate(bins):
        if abs(i - peak_bin) >= 3 and b > 0:
            anomalies.extend([min_s + (j + 0.5) * (max_s - min_s) / 10 for j in [i]])
    return anomalies or [0.0]

# Conditional transformation map – distractor computation
transformation_map = {i: (i ** 2) % 7 for i in range(15) if i % 3 != 0}
decoy_counter = 0
for key in transformation_map:
    if transformation_map[key] > 4:
        decoy_counter += 1

# Main analysis engine
def analyze_pattern(frequency_data, mask_thresholds):
    total_power = sum([x ** 2 for x in frequency_data])
    dominant_bands = [f for f in frequency_data if f > 1.2]
    
    # Set-based interference: irrelevant feature extraction
    unique_magnitudes = set(round(f, 2) for f in frequency_data)
    rare_peaks = set(round(f, 2) for f in frequency_data if f < 0.5 and f > 0.1)
    spectral_gaps = unique_magnitudes - rare_peaks
    complexity_hint = len(spectral_gaps) % 5 if spectral_gaps else 0
    
    # Dummy branching with misleading intermediate
    adjustment_factor = 1.0
    if len(dominant_bands) > 5:
        adjustment_factor = 0.85
    elif any(mask_thresholds):
        adjustment_factor = 1.15
    else:
        adjustment_factor = 0.95
    
    # Core logic: harmonic coherence metric
    coherence = 0.0
    for i in range(1, len(frequency_data)):
        if frequency_data[i] > 0.5 and frequency_data[i-1] > 0.5:
            coherence += abs(frequency_data[i] - frequency_data[i-1]) * 0.1
    
    # Diagnostic score formation (this is where final answer comes from)
    base_score = total_power * 10 + coherence * 50 - len(detect_anomalies(frequency_data)) * 3
    final_diagnostic = int(base_score * adjustment_factor + complexity_hint)
    
    # Dead code path – unreachable but looks important
    if final_diagnostic < 0:
        raise ValueError("Negative diagnostic not allowed")
    if final_diagnostic > 10000:
        temp_buffer = [final_diagnostic // i for i in range(1, 6)]  # unused
        final_diagnostic = sum(temp_buffer) // 5  # never reached due to actual value
    
    return final_diagnostic

# Orchestrate workflow
if __name__ == "__main__":
    # Step 1: Collect raw sensor data
    readings = collect_sensor_readings()
    
    # Step 2: Filter out noise components
    cleaned = filter_noise(readings, cutoff=1.8)
    
    # Step 3: Transform into frequency representation
    transformed_data = apply_fourier_approximation(cleaned)
    
    # Step 4: Generate threshold mask based on statistical outlier detection
    avg_mag = sum(transformed_data) / len(transformed_data)
    std_dev = math.sqrt(sum((x - avg_mag) ** 2 for x in transformed_data) / len(transformed_data))
    threshold_mask = [abs(x - avg_mag) > 1.5 * std_dev for x in transformed_data]
    
    # Step 5: Run final diagnostic analysis
    final_diagnostic = analyze_pattern(transformed_data, threshold_mask)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")