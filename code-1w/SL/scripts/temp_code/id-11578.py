import math

# Simulated sensor array diagnostics with heavy code interference
def collect_readings():
    raw_values = [0.7, 1.2, 0.9, 2.4, 3.1, 1.8, 0.5]
    baseline = 1.0
    adjusted = [v - baseline for v in raw_values]
    return raw_values, adjusted

# Irrelevant preprocessing: image normalization (decoy function)
def normalize_image(pixels):
    max_val = max(max(row) for row in pixels)
    return [[p / max_val for p in row] for row in pixels]

# Unused transformation chain
def transform_signal(signal):
    return [math.sin(x) * math.exp(-x/10) for x in signal]

# Misleading diagnostic with decoy logic
def preliminary_check(data):
    if len(data) > 5:
        temp_flag = sum(data) > 5.0
        noise_level = max(data) - min(data)
        return noise_level * (2 if temp_flag else 1)
    return 0

# Distractor: unused recursive filter
def recursive_denoise(seq, depth=0):
    if depth >= 3 or len(seq) < 2:
        return seq
    smoothed = [(seq[i] + seq[i+1]) / 2 for i in range(len(seq)-1)]
    return recursive_denoise(smoothed, depth + 1)

# Real processing begins here — but hidden among noise
processed_signals = []
def process_critical_data(raw, adj):
    global processed_signals
    # Key transformation: amplify anomalies above threshold
    anomalies = [i for i, x in enumerate(adj) if abs(x) > 0.8]
    magnitude_sum = sum(abs(adj[i]) for i in anomalies)
    
    # Red herring: frequency analysis (unused)
    sample_rate = 100
    nyquist = sample_rate / 2
    frequencies = [i * nyquist / 50 for i in range(50)]
    
    # Actual relevant computation
    scaling_factor = 1.75
    processed_signals = [raw[i] * scaling_factor for i in range(len(raw))]
    
    # Dead code path — looks important but unused
    if magnitude_sum < 0:
        processed_signals = [x * 0.5 for x in processed_signals]
    
    return processed_signals

# Core analysis function — contains final answer derivation
def analyze_readings(signals):
    # Compute power spectrum (irrelevant)
    spectrum = [x ** 2 for x in signals]
    total_power = sum(spectrum)
    
    # Conditional expression with meaningful side
    peak = max(signals) if total_power > 0 else 0
    
    # Bit manipulation red herring
    peak_int = int(peak * 10)
    masked = peak_int & 0xFF  # Only uses lower 8 bits
    
    # Real calculation: harmonic distortion index
    harmonic_sum = 0.0
    for i, val in enumerate(signals):
        if i % 2 == 1:  # odd indices
            harmonic_sum += val / (i + 1)
    
    # Critical formula: combines harmonic content and base amplitude
    base_amplitude = sum(signals) / len(signals)
    hdi = harmonic_sum / (base_amplitude + 1e-8)
    
    # Final diagnostic derived from multiple steps
    final_diagnostic = int((hdi * 1000) + 0.5)  # Round to nearest integer
    
    # Distraction: unused correction table
    corrections = {i: (final_diagnostic ^ i) % 100 for i in range(10)}
    
    return final_diagnostic

# --- Execution Sequence ---
raw_data, adjusted_data = collect_readings()

# Call irrelevant image function with fake data (distractor)
fake_pixels = [[120, 150], [100, 200]]
normalized = normalize_image(fake_pixels)

# Process real data through main pipeline
processed_signals = process_critical_data(raw_data, adjusted_data)

# Introduce dead variable with plausible name
consistency_score = preliminary_check(adjusted_data)

# Key statement: compute final diagnostic
final_diagnostic = analyze_readings(processed_signals)

# Output result as required
print(f"Result: {final_diagnostic}")