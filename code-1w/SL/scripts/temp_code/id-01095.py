import math

# Simulated sensor array data from environmental monitoring system
def fetch_sensor_readings():
    raw_values = [127, 255, 192, 64, 80, 240, 168, 32]
    return raw_values

# Irrelevant auxiliary function – dead code path (distractor)
def calculate_checksum(data):
    checksum = 0
    for val in data:
        checksum ^= val * 3
    return checksum % 256

# Signal normalization using z-score with fake baseline adjustments
def normalize_signal(signal_data, baseline_offset=1.5):
    mean_val = sum(signal_data) / len(signal_data)
    variance = sum((x - mean_val) ** 2 for x in signal_data) / len(signal_data)
    std_dev = math.sqrt(variance + 1e-8)
    
    # Apply normalization and add irrelevant transformation
    normalized = [(x - mean_val) / std_dev for x in signal_data]
    inverted_norm = [1.0 / (1 + math.exp(-x)) for x in normalized]  # unused distractor
    return normalized

# Frequency domain weighting simulation (red herring: includes complex math but only real part used)
def compute_fourier_weights(n):
    weights = []
    for k in range(n):
        real_part = math.cos(2 * math.pi * k / n)
        imag_part = math.sin(2 * math.pi * k / n)  # deliberately unused
        weight = abs(real_part) if real_part > 0 else 0.5
        weights.append(weight + 0.1)  # bias added
    return weights

# Decoy function – appears important but never called in execution path
def trigger_alert_system(code, threshold=0.75):
    if code > threshold:
        print("CRITICAL: Anomaly detected")
    else:
        print("Status: Nominal")

# Data smoothing via moving average — irrelevant to final result
def smooth_data(stream, window=3):
    smoothed = []
    for i in range(len(stream)):
        start = max(0, i - window + 1)
        segment = stream[start:i+1]
        smoothed.append(sum(segment) / len(segment))
    return smoothed

# Core diagnostic logic — only this contributes to final answer
def evaluate_integrity_score(components):
    score = 0
    for comp in components:
        if comp > 0.5:
            score += int(comp * 10) * 2
        elif comp < -0.5:
            score -= int(abs(comp) * 10) * 3
        else:
            score += 5
    return score

# Aggregation engine combining normalized signals and weights
def aggregate_metrics(signals, weights):
    # Element-wise scaling
    scaled = [s * w for s, w in zip(signals, weights)]
    
    # Introduce misleading intermediate calculation (unused)
    magnitude = math.sqrt(sum(s ** 2 for s in scaled))  # distractor
    phase_shift = [math.atan(s / (w + 1e-6)) for s, w in zip(scaled, weights)]  # unused
    
    # Only the following line matters
    filtered = [val for val in scaled if val > 0.0]
    base_metric = sum(filtered)
    adjustment = len([x for x in scaled if x < 0]) * 1.5
    final_score = base_metric - adjustment
    
    # Secondary processing chain that actually determines output
    diagnostics = evaluate_integrity_score(scaled)
    final_diagnostic = int(final_score * 100) + diagnostics
    
    return final_diagnostic

# --- MAIN EXECUTION FLOW ---
if __name__ == "__main__":
    # Step 1: Fetch raw sensor data
    readings = fetch_sensor_readings()
    
    # Step 2: Compute checksum (irrelevant)
    chksum = calculate_checksum(readings)
    
    # Step 3: Normalize signal data
    normalized_signals = normalize_signal(readings, baseline_offset=1.2)
    
    # Step 4: Generate Fourier weights (only real weights used, imaginary ignored)
    weights = compute_fourier_weights(len(normalized_signals))
    
    # Step 5: Smooth data (completely irrelevant — not used later)
    smoothed_signals = smooth_data(readings)
    
    # Step 6: Perform aggregation (key statement)
    final_diagnostic = aggregate_metrics(normalized_signals, weights)
    
    # Output target result
    print(f"Result: {final_diagnostic}")