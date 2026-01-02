import math

# Simulated sensor data processing with embedded diagnostics
def collect_samples():
    raw = [0.8, 1.2, -0.5, 3.1, -2.2, 4.0, 1.8, -0.9]
    scale_factor = 1.7
    adjusted = [x * scale_factor for x in raw]
    return adjusted

# Irrelevant auxiliary function (decoy)
def compute_entropy(data):
    entropy = 0.0
    for x in data:
        if x != 0:
            entropy -= x * math.log(abs(x))
    return round(entropy, 4)

# Signal conditioning with red herring operations
def filter_noise(signal):
    filtered = []
    noise_floor = 0.75
    for val in signal:
        if abs(val) > noise_floor:
            filtered.append(val ** 2)
        else:
            filtered.append(0)  # Suppress small values
    
    # Distractor: unused transformation path
    alt_path = [abs(x) ** 0.5 for x in signal if x > 1]
    temp_sum = sum(alt_path) / len(alt_path) if alt_path else 0
    normalized_temp = temp_sum * 0.3  # Dead code branch
    
    return filtered

# Data windowing - relevant but with misleading intermediate stats
def apply_hamming_window(segment):
    N = len(segment)
    windowed = []
    for i in range(N):
        window_weight = 0.54 - 0.46 * math.cos((2 * math.pi * i) / (N - 1))
        windowed.append(segment[i] * window_weight)
    
    # Fake diagnostic metric (not used later)
    avg_mag = sum(abs(x) for x in windowed) / N
    dummy_flag = avg_mag > 2.0
    
    return windowed

# Core transformation with string-based mode selection
def process_mode_selector(config_str):
    modes = {
        'fast': lambda x: x * 2,
        'precise': lambda x: x * 1.5,
        'eco': lambda x: x * 0.8
    }
    # Extract mode using string method (key python feature)
    clean_config = config_str.strip().lower()
    key_token = clean_config.split(':')[0]
    multiplier = modes.get(key_token, modes['fast'])
    return multiplier

# Secondary processing chain (partially relevant)
def extract_peaks(data_list):
    peaks = []
    for i in range(1, len(data_list) - 1):
        if data_list[i] > data_list[i-1] and data_list[i] > data_list[i+1]:
            peaks.append(data_list[i])
    peak_count_metric = len(peaks) + 1  # Slight obfuscation
    scaling_hint = 3.0 / peak_count_metric
    return peaks, scaling_hint

# Primary data processor - combines multiple concepts
def generate_diagnostic_vector(raw_input):
    # Step 1: Filter and transform
    cleaned = filter_noise(raw_input)
    
    # Step 2: Apply windowing
    windowed_signal = apply_hamming_window(cleanled)
    
    # Step 3: Mode-dependent rescaling
    mode_func = process_mode_selector('precise:active')
    enhanced = [mode_func(x) for x in windowed_signal]
    
    # Step 4: Peak analysis (returns extra unused info)
    detected_peaks, hint = extract_peaks(enhanced)
    
    # Step 5: Compute energy proxy (actual relevant computation)
    energy = sum(x**2 for x in enhanced if x > 0)
    
    # Distractor: irrelevant combinatorics on indices
    index_pairs = [(i, j) for i in range(3) for j in range(i+1, min(5, len(enhanced)))]
    pair_count = len(index_pairs)  # Unused
    
    return energy, detected_peaks

# Final analysis with tuple unpacking and conditional logic
def analyze_signal(dataset):
    energy_proxy, peaks_found = generate_diagnostic_vector(dataset)
    
    # Real decision logic
    threshold = 12.5
    if energy_proxy > threshold:
        base_score = 850
        adjustment = len(peaks_found) * 15
        final_score = base_score + adjustment
    else:
        base_score = 400
        penalty = 50 if any(p < 0 for p in peaks_found) else 20
        final_score = base_score - penalty
    
    # Red herring: set operation with no impact
    unique_peak_set = set(round(p, 2) for p in peaks_found)
    reference_marks = {1.23, 2.45, 3.67}
    overlap_count = len(unique_peak_set & reference_marks)  # Unused
    
    # Critical distraction: complex-looking but irrelevant bit manipulation
    debug_key = 0
    for p in peaks_found[:3]:
        shifted = int(abs(p) * 10) << 2
        debug_key ^= shifted & 0xFF
    debug_checksum = debug_key ^ 0xAA  # Dead end
    
    # Actual output depends only on final_score
    diagnostic_level = int(final_score)
    
    return diagnostic_level

# Main execution flow
if __name__ == '__main__':
    # Collect initial data
    samples = collect_samples()
    
    # Compute irrelevant entropy baseline
    entropy_baseline = compute_entropy(samples)
    
    # Process through pipeline
    processed_data = []
    chunk_size = 4
    for i in range(0, len(samples), chunk_size):
        chunk = samples[i:i + chunk_size]
        # Misleading average calculation
        local_avg = sum(chunk) / len(chunk)
        offset_compensation = abs(local_avg) * 0.1
        compensated = [x + offset_compensation for x in chunk]
        processed_data.extend(compensated)
    
    # Final analysis - this is where the answer is determined
    final_diagnostic = analyze_signal(processed_data)
    
    # Output result as required
    print(f"Result: {final_diagnostic}")