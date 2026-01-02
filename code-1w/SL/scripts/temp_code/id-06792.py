import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples():
    raw = [0.3, 0.7, 1.1, 1.8, 2.5, 3.0, 3.6, 4.2, 4.9, 5.5]
    offset = 0.15
    adjusted = [x + offset for x in raw]
    return adjusted

# Irrelevant signal smoothing (dead path)
def smooth_signal(data):
    smoothed = [data[0]]
    for i in range(1, len(data) - 1):
        smoothed.append((data[i-1] + data[i] + data[i+1]) / 3)
    smoothed.append(data[-1])
    return smoothed

# Frequency domain approximation (distractor)
def compute_spectrum(signal):
    spectrum = []
    for k in range(len(signal)//2):
        real = sum(signal[n] * math.cos(2 * math.pi * k * n / len(signal)) for n in range(len(signal)))
        imag = sum(-signal[n] * math.sin(2 * math.pi * k * n / len(signal)) for n in range(len(signal)))
        magnitude = math.sqrt(real**2 + imag**2)
        spectrum.append(magnitude)
    return spectrum

# Data normalization with string-tagged levels (uses string methods)
def normalize_with_tags(data):
    max_val = max(data)
    normalized = [x / max_val for x in data]
    tags = []
    for val in normalized:
        if val > 0.8:
            tags.append('HIGH'.lower())
        elif val > 0.5:
            tags.append('MEDIUM'.lower())
        else:
            tags.append('LOW'.lower())
    return list(zip(normalized, tags))

# Core transformation: non-linear compression
def compress_nonlinear(sample):
    if sample < 1.0:
        return math.log(1 + sample)
    else:
        return 1.5 * (1 - math.exp(-sample / 2))

# Apply compression and filter anomalies
def process_anomalies(tagged_data):
    filtered = []
    anomalies = set()
    for i, (val, tag) in enumerate(tagged_data):
        if tag == 'high' and val > 0.95:
            anomalies.add(i)
        else:
            filtered.append(val)
    return filtered, anomalies

# Signal reconstruction from compressed values
def reconstruct_signal(compressed):
    reconstructed = []
    for c in compressed:
        # Invert compression approximately
        if c < 0.693:  # ln(2)
            original = math.exp(c) - 1
        else:
            original = -2 * math.log(1 - c / 1.5)
        reconstructed.append(round(original, 6))
    return reconstructed

# Diagnostic engine based on entropy-like measure
def calculate_entropy_proxy(data):
    hist = {}
    for x in data:
        key = int(x * 10)
        hist[key] = hist.get(key, 0) + 1
    total = len(data)
    entropy = 0.0
    for count in hist.values():
        p = count / total
        entropy -= p * math.log(p)
    return entropy

# Set operations to identify pattern uniqueness
def assess_uniqueness(zipped_data):
    values = {round(pair[0], 4) for pair in zipped_data}
    tags = {pair[1] for pair in zipped_data}
    common_vals = {0.1, 0.2, 0.3, 0.4, 0.5}
    rare_set = values - common_vals
    return len(rare_set), len(tags)

# Main analysis pipeline
def analyze_signal(data):
    # Step 1: Compress each point
    compressed = [compress_nonlinear(x) for x in data]
    
    # Step 2: Normalize and tag
    tagged = normalize_with_tags(compressed)
    
    # Step 3: Filter anomalies
    clean_data, flagged = process_anomalies(tagged)
    
    # Step 4: Reconstruct signal from clean compressed values
    reconstructed = reconstruct_signal(clean_data)
    
    # Step 5: Compute diagnostic metrics
    entropy_metric = calculate_entropy_proxy(reconstructed)
    rare_count, tag_diversity = assess_uniqueness(tagged)
    
    # Distractor: unused frequency analysis
    freq_analysis = compute_spectrum(reconstructed)
    avg_frequency = sum(freq_analysis[:3]) / 3 if freq_analysis else 0
    
    # Irrelevant text aggregation
    log_entries = []
    for i, val in enumerate(reconstructed):
        status = 'CRITICAL' if val > 4.0 else 'NORMAL'
        log_entries.append(f"Sample_{i}: {status}")
    full_log = '; '.join(log_entries).replace('CRITICAL', 'ALERT')
    alert_count = full_log.count('ALERT')
    
    # Final diagnostic score: combination of entropy and structural counts
    final_score = (entropy_metric * 1000) + (rare_count * 50) + (tag_diversity * 10) - (len(flagged) * 100)
    
    # Key assignment - this is the answer
    final_diagnostic = int(round(final_score))
    
    return final_diagnostic

# Unused recursive helper (red herring)
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, low, mid - 1, target)
    else:
        return binary_search_recursive(arr, mid + 1, high, target)

# Execution flow
if __name__ == '__main__':
    samples = collect_samples()
    processed_data = [round(x * 1.08, 6) for x in samples]  # slight calibration
    final_diagnostic = analyze_signal(processed_data)
    print(f"Target result: {final_diagnostic}")