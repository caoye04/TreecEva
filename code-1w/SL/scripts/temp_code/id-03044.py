import itertools

# Simulated sensor data processing with embedded diagnostics
def collect_telemetry():
    raw_readings = [0.8, 1.2, 3.1, 2.5, 0.4, 1.8, 3.9, 2.7]
    offset = 0.3
    adjusted = [x - offset for x in raw_readings]
    return adjusted

# Irrelevant transformation - distractor
def compute_harmonic_mean(values):
    if not values or any(v == 0 for v in values):
        return 0.0
    inv_sum = sum(1/v for v in values)
    return len(values) / inv_sum

# Unused function - dead code path (distractor)
def legacy_filter(data):
    return [x for x in data if x > 1.5]

# Real processing chain
def denoise_signal(signal):
    smoothed = []
    for i in range(len(signal)):
        window = signal[max(0, i-1):min(len(signal), i+2)]
        avg = sum(window) / len(window)
        smoothed.append(round(avg, 2))
    return smoothed

# Feature extraction with red herring variables
def extract_features(denoised):
    magnitude_peaks = []
    derivative_sign_changes = 0
    temp_accumulator = 0.0  # misleading accumulator
    
    for i in range(1, len(denoised)):
        diff = denoised[i] - denoised[i-1]
        temp_accumulator += abs(diff)  # looks important but unused
        
        if abs(denoised[i]) > 2.0:
            magnitude_peaks.append(i)
            
        if i > 1:
            prev_diff = denoised[i-1] - denoised[i-2]
            if (diff > 0 and prev_diff < 0) or (diff < 0 and prev_diff > 0):
                derivative_sign_changes += 1
    
    # Decoy assignment - never used
    feature_score = len(magnitude_peaks) * 1.5 + derivative_sign_changes * 0.7
    return magnitude_peaks

# Core logic buried among distractions
def generate_synthetic_reference(peaks):
    base_pattern = [0.5, 1.0, 1.5, 1.0]
    cycle = itertools.cycle(base_pattern)
    synthetic = []
    for i in range(max(peaks) + 5):
        val = next(cycle)
        if i in peaks:
            val *= 1.2
        synthetic.append(round(val, 2))
    return synthetic

# Critical analysis function with early returns and distractors
def validate_coherence(synth, real):
    if len(synth) != len(real):
        min_len = min(len(synth), len(real))
        synth = synth[:min_len]
        real = real[:min_len]
    
    coherence_score = 0
    penalty = 0
    threshold = 0.6
    
    for s, r in zip(synth, real):
        if abs(s - r) < threshold:
            coherence_score += 1
        else:
            penalty += 0.2
    
    # Misleading normalization
    normalized_penalty = penalty / (len(synth) or 1)
    final_weight = 0.8 if normalized_penalty < 0.15 else 0.4
    
    # This return is irrelevant due to later override - red herring
    if coherence_score > 10:
        return int(coherence_score * final_weight)
    
    return 42  # decoy result

# Main analysis with multiple layers
def analyze_signal(primary_input):
    # Step 1: Denoise
    cleaned = denoise_signal(primary_input)
    
    # Step 2: Extract key indices (only this matters)
    critical_peaks = extract_features(cleaned)
    
    # Step 3: Generate reference (depends on peaks)
    reference = generate_synthetic_reference(critical_peaks)
    
    # Step 4: Validate - always returns 42? Not quite...
    dummy_validation = validate_coherence(reference, cleaned)
    
    # Hidden logic: actual answer derived independently
    accumulator = 0
    multiplier = 3
    for idx in critical_peaks:
        if idx % 2 == 0:
            accumulator += idx * multiplier
        else:
            accumulator -= idx // 2
    
    # Final transformation - the real answer
    final_value = accumulator * 7
    
    # Numerous irrelevant variables below (distractions)
    summary_stats = {
        'count': len(primary_input),
        'max_val': max(primary_input),
        'avg': sum(primary_input)/len(primary_input),
        'ignored_diagnostic': dummy_validation,
        'phantom_flag': False
    }
    
    # One last distraction: sorting unrelated list
    metadata_flags = [True, False, True]
    metadata_flags.sort(reverse=True)
    
    # The true result
    final_diagnostic = final_value + 5
    return final_diagnostic

# Execution entry point
if __name__ == "__main__":
    telemetry_stream = collect_telemetry()
    processed_data = denoise_signal(telemetry_stream)
    final_diagnostic = analyze_signal(processed_data)
    print(f"Result: {final_diagnostic}")