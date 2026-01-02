import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [i * 0.5 for i in range(20)]
    noise_floor = sum([math.sin(x) for x in raw_samples])
    return [x + math.cos(x) for x in raw_samples]

# Irrelevant auxiliary function – dead code path (distractor)
def legacy_calibrate(x):
    if x < 0:
        return abs(x) ** 0.5
    else:
        return x // 3

# Signal transformation with bit manipulation obfuscation
def transform_signal(samples):
    shifted = []
    mask = 0b11110000
    for i, val in enumerate(samples):
        # Apply phase shift and encode index via XOR
        encoded_index = i ^ 7
        adjusted = round(val * 1.5 + (encoded_index & 0x0F), 4)
        # Bitwise red herring: masking has no real effect due to float conversion
        fake_int = int(abs(adjusted)) & mask
        shifted.append(adjusted if adjusted > 0 else -adjusted)
    return shifted

# Data normalization with misleading intermediate metrics
def normalize_stream(data):
    mean_val = sum(data) / len(data)
    variance = sum([(x - mean_val)**2 for x in data]) / len(data)
    std_dev = math.sqrt(variance)
    
    # Distractor variables – used nowhere important
    outlier_threshold = mean_val + 2 * std_dev
    filtered = [x for x in data if x <= outlier_threshold]
    compression_ratio = len(data) / len(filtered) if filtered else 0
    
    # Actual normalization
    return [(x - mean_val) / std_dev for x in data]

# Core analysis logic
validity_map = {True: 1, False: -1}

def assess_coherence(window):
    if len(window) < 3:
        return 0.0
    trend = all(window[i] <= window[i+1] for i in range(len(window)-1))
    oscillation = sum(1 for i in range(1, len(window)-1) if (window[i]-window[i-1])*(window[i+1]-window[i]) < 0)
    # Complex but ultimately unused metric
    decoy_score = math.log(oscillation + 1) * validity_map[trend]
    return sum(window) / len(window)

# Higher-order function with lambda abstraction (required feature)
def generate_filter(threshold):
    return lambda x: x > threshold

# Main processing pipeline
def process_signal(raw_data):
    stage1 = transform_signal(raw_data)
    stage2 = normalize_stream(stage1)
    
    # Sliding window analysis
    windows = [stage2[i:i+5] for i in range(0, len(stage2), 4) if len(stage2[i:i+5]) == 5]
    
    # Apply filter using lambda (required feature)
    critical_threshold = 0.1
    significance_filter = generate_filter(critical_threshold)
    significant_windows = [w for w in windows if significance_filter(sum(w)/len(w))]
    
    # Dummy aggregation with distracting statistics
    avg_window_sum = sum([sum(w) for w in significant_windows]) / len(significant_windows) if significant_windows else 0
    entropy_proxy = -sum([math.log(abs(w[0])+1e-8) for w in windows])
    
    # Real computation path
    coherence_scores = [assess_coherence(w) for w in significant_windows]
    return {
        'processed': stage2,
        'scores': coherence_scores,
        'diagnostics': {
            'baseline_drift': stage1[0] - stage1[-1],
            'signal_entropy': entropy_proxy,
            'valid_windows': len(significant_windows)
        }
    }

# Final diagnostic engine
def analyze_signal(pipe_output):
    scores = pipe_output['scores']
    if not scores:
        return -999.0
    
    # Real answer computation
    raw_moment = sum([x**3 for x in scores])
    adjustment_factor = math.atan(len(scores))
    
    # Multiple layers of distraction
    dummy_lookup = {i: math.factorial(i % 5) for i in range(10)}
    phantom_correction = sum(dummy_lookup[k] * (-1)**k for k in dummy_lookup if k % 2 == 0)
    
    # Key result obscured by irrelevant terms
    base_result = raw_moment * adjustment_factor
    final_value = base_result + math.sin(phantom_correction)  # sine of large number ≈ bounded
    return round(final_value, 4)

# --- Execution ---
raw_input = collect_readings()
processed_data = process_signal(raw_input)
final_diagnostic = analyze_signal(processed_data)
print(f"Result: {final_diagnostic}")