import math

# Simulated sensor array diagnostics with heavy interference

def collect_raw_data():
    # Irrelevant sensor metadata
    calibration_offset = 0.023
    sampling_rate = 128
    noise_floor = [0.004, 0.005, 0.003, 0.006]
    raw_sequence = [i * 1.5 + (-1)**i * 0.7 for i in range(10)]
    return raw_sequence

# Dead function - never called
def deprecated_filter(x):
    return [val for val in x if val > 1.0]

# Unused transformation chain
temp_correction_matrix = [[0.98, 0.01], [0.03, 0.97]]
baseline_drift = sum([0.001 * i for i in range(20)])

# Core signal processing with distractors
def preprocess_signal(data):
    filtered = []
    cumulative_shift = 0.0
    
    for val in data:
        adjusted = val + 0.018  # Minor correction
        if abs(adjusted) > 1.0:
            adjusted *= 0.95  # Damping
        filtered.append(round(adjusted, 4))
    
    # Red herring: complex but unused calculation
    spectral_entropy = -sum([x * math.log(abs(x)+1e-8) for x in filtered])
    peak_to_peak = max(filtered) - min(filtered)
    
    # Actual relevant transformation
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered) + 1e-8) for x in filtered]
    return normalized

# Decoy analysis function
def legacy_diagnostic(signal):
    score = 0
    for s in signal:
        if s > 0.5:
            score += int(s * 10)
    return score * 2

# Bit manipulation distraction
def encode_status_code(code):
    a = code ^ 255
    b = a << 2
    c = b | 17
    d = (c & 128) >> 7
    return d  # Only uses last bit

status_flags = [encode_status_code(i) for i in range(50, 55)]

# Linear search with misleading purpose
def find_threshold_crossing(signal, thresh=0.7):
    for i, val in enumerate(signal):
        if val > thresh:
            return i  # Index of first crossing
    return -1

# Unused recursive structure
def recursive_smooth(arr, depth=0):
    if depth >= 2 or len(arr) < 2:
        return arr
    smoothed = [(arr[i] + arr[i+1]) / 2 for i in range(len(arr)-1)]
    return recursive_smooth(smoothed, depth + 1)

# Primary processing pipeline
def analyze_readings(signals):
    # Step 1: Transform via polynomial enhancement
    enhanced = [math.pow(s, 3) - 2*math.pow(s, 2) + s for s in signals]
    
    # Step 2: Apply windowing function (only center matters)
    windowed = []
    n = len(enhanced)
    for i in range(n):
        window_factor = 0.54 - 0.46 * math.cos((2 * math.pi * i) / (n - 1))
        windowed.append(enhanced[i] * window_factor)
    
    # Step 3: Compute energy signature
    energy = sum([abs(w) for w in windowed])
    
    # Step 4: Extract bit signature from fractional parts
    bits = ''
    for w in windowed:
        frac = abs(w) - math.floor(abs(w))
        bit = '1' if frac * 10 > 5 else '0'
        bits += bit
    
    # Step 5: Convert first 8 bits to integer (critical step)
    if len(bits) >= 8:
        bit_sample = bits[:8]
        diagnostic_int = int(bit_sample, 2)
    else:
        diagnostic_int = 0
    
    # Step 6: Final adjustment using irrelevant status flags
    adjustment = sum(status_flags) % 7
    final_value = diagnostic_int - adjustment  # Main result
    
    # Multiple decoy assignments
    summary_report = {
        'readings_count': len(signals),
        'max_value': max(signals),
        'entropy_metric': -sum([x * math.log(x+1e-8) for x in signals]),
        'legacy_score': legacy_diagnostic(signals),
        'spectral_index': energy * 100
    }
    
    return final_value

# Orchestration with distractions
def main_pipeline():
    # Collect and preprocess
    raw = collect_raw_data()
    processed_signals = preprocess_signal(raw)
    
    # Calculate auxiliary metrics (distractors)
    avg_signal = sum(processed_signals) / len(processed_signals)
    variance = sum([(x - avg_signal)**2 for x in processed_signals]) / len(processed_signals)
    
    # Find anomalies (unused)
    anomaly_indices = [i for i, x in enumerate(processed_signals) if x > 0.8]
    
    # Critical execution point
    final_diagnostic = analyze_readings(processed_signals)
    
    # Print result as required
    print(f"Target result: {final_diagnostic}")
    
    return final_diagnostic

# Execute
result = main_pipeline()