import math

# Simulated sensor array data with noise injection
def generate_noisy_readings(baseline, count):
    readings = []
    for i in range(count):
        noise = math.sin(i * 0.5) * math.cos(i * 0.3)
        readings.append(baseline + i * 0.1 + noise)
    return readings

# Irrelevant auxiliary function - dead code path (distractor)
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [x / mean_val for x in data]

# Signal preprocessing with multiple transformation layers
def preprocess_signal(raw_data, threshold=5.0):
    filtered = [x for x in raw_data if abs(x) > threshold]  # Noise filtering
    stabilized = [math.tanh(x) * 10 for x in filtered]     # Stabilization
    
    # Misleading intermediate calculation (not used later)
    avg_stabilized = sum(stabilized) / len(stabilized) if stabilized else 0
    temp_correction = math.log(abs(avg_stabilized) + 1) * 0.2
    corrected = [s + temp_correction for s in stabilized]
    
    # Key transformation: quantize to discrete levels
    quantized = [int(x * 2) / 2 for x in corrected]  # Round to nearest 0.5
    return quantized

# Advanced metric computation with conditional logic
def compute_diagnostics(signal_chunk):
    if not signal_chunk:
        return 0.0
    
    # Composite metric calculation
    magnitude = sum(abs(x) for x in signal_chunk)
    variance = sum((x - magnitude/len(signal_chunk))**2 for x in signal_chunk) / len(signal_chunk) if len(signal_chunk) > 1 else 0
    peak_ratio = max(signal_chunk) / (min(signal_chunk) + 1e-5)
    
    # Bit manipulation red herring (appears relevant but isn't directly used)
    bit_encoded = 0
    for x in signal_chunk[:4]:
        shifted = int(abs(x) * 10) & 0xFF
        bit_encoded ^= shifted << (int(x) % 4 * 8)
    
    # Actual metric formula (depends only on magnitude and variance)
    score = magnitude * 1.5 - variance * 0.8
    return round(score, 4)

# Recursive frequency analysis (unused distractor)
def recursive_frequency(data, level=0):
    if level >= 3 or len(data) < 2:
        return len(data)
    split = len(data) // 2
    return recursive_frequency(data[:split], level+1) + recursive_frequency(data[split:], level+1)

# Main analysis pipeline
def analyze_metrics(signals):
    if isinstance(signals, dict):
        # Extract values and flatten
        flat_signals = []
        for key in sorted(signals.keys()):
            flat_signals.extend(signals[key])
    else:
        flat_signals = signals
    
    # Secondary filtering based on pattern
    pattern_filtered = [x for x in flat_signals if math.fmod(x * 10, 3) != 1]
    
    # Compute final diagnostic value
    raw_value = compute_diagnostics(pattern_filtered)
    adjustment = len(pattern_filtered) % 7 * 0.3
    final_score = raw_value + adjustment
    
    return int(final_score * 100) / 100  # Round to 2 decimal places

# Unused complexity: nested dictionary structure with decoy entries
diagnostic_cache = {
    'session_7A': {
        'readings': [1.2, 3.4, 5.6],
        'status': 'calibrated',
        'aux_data': {'temp': 23.5, 'humidity': 45}
    },
    'session_9C': {
        'readings': [-2.1, 0.5, 4.3],
        'status': 'pending',
        'aux_data': {'temp': 25.1, 'humidity': 52}
    }
}

# Real data generation
base_readings = generate_noisy_readings(baseline=4.2, count=25)
processed_signals = preprocess_signal(base_readings, threshold=4.8)

# Structured data packaging (adds abstraction layer)
signal_packets = {
    'primary': processed_signals[::2],
    'secondary': processed_signals[1::2],
    'tertiary': [x * 0.9 for x in processed_signals]  # unused branch
}

# Final computation
final_diagnostic = analyze_metrics(processed_signals)
print(f"Result: {final_diagnostic}")