import math

# Simulated sensor data processing with embedded diagnostics
def collect_readings():
    raw_samples = [x * 0.1 for x in range(100, 200)]
    offset = 42
    scale_factor = 2.718
    adjusted = [round(math.sin(x) * scale_factor + offset, 4) for x in raw_samples]
    return adjusted

# Irrelevant transformation: frequency domain mockup
def compute_frequencies(signal):
    n = len(signal)
    freq_spectrum = []
    for k in range(n // 2):
        real = sum(signal[i] * math.cos(2 * math.pi * k * i / n) for i in range(n))
        imag = sum(-signal[i] * math.sin(2 * math.pi * k * i / n) for i in range(n))
        magnitude = math.sqrt(real**2 + imag**2)
        freq_spectrum.append(magnitude)
    # Dead code path — never used
    if len(freq_spectrum) > 100:
        return [f * 1.5 for f in freq_spectrum]
    return freq_spectrum[:50]

# Data filtering with red herring logic
def filter_anomalies(data):
    threshold = 3.0
    variance_proxy = sum((x - 42) ** 2 for x in data[:50]) / 50
    noise_level = math.sqrt(variance_proxy)
    
    # Distractor: complex conditional that doesn't affect outcome
    if noise_level > threshold:
        cleaned = [x for x in data if 40 <= x <= 44]
    elif len(data) % 7 == 0:
        cleaned = [x for x in data if x > 41]
    else:
        cleaned = [x for x in data]  # Actual path taken

    # Unused statistical decoy
    mean_cleaned = sum(cleaned) / len(cleaned) if cleaned else 0
    stdev = math.sqrt(sum((x - mean_cleaned)**2 for x in cleaned)/len(cleaned)) if cleaned else 0

    return cleaned

# Core transformation with subtle arithmetic chain
def transform_phase(signal):
    shifted = [(x - 42) * 100 for x in signal]
    encoded = []
    for val in shifted:
        bit_shifted = int((val * 3) & 0xFF)  # Scale and mask to byte range
        if bit_shifted < 0:
            bit_shifted = ~bit_shifted & 0xFF
        encoded.append(bit_shifted)
    return encoded

# Higher-level feature extraction (distractor-heavy)
def extract_patterns(encoded):
    pattern_map = {}
    total_runs = 0
    current_run = 1
    
    for i in range(1, len(encoded)):
        if encoded[i] == encoded[i-1]:
            current_run += 1
        else:
            if current_run > 1:
                key = f"run_{encoded[i-1]}"
                pattern_map[key] = pattern_map.get(key, 0) + current_run
                total_runs += current_run
            current_run = 1
    
    # Never accessed aggregation
    avg_run_length = total_runs / len(pattern_map) if pattern_map else 0
    entropy = 0.0
    for count in pattern_map.values():
        p = count / total_runs
        if p > 0:
            entropy -= p * math.log(p, 2)
    
    # Decoy return
    return {'count': len(pattern_map), 'total': total_runs, 'entropy': entropy}

# Critical diagnostic computation (answer depends only on this)
def analyze_signal(data):
    base_sum = sum(data)
    correction_factor = 0.987
    penalty = 0
    
    # Key logic step 1: character-based adjustment from literal
    debug_tag = 'STATUS_OK'
    uppercase_count = len([c for c in debug_tag if c.isupper()])  # Always 8
    lowercase_count = len([c for c in debug_tag if c.islower()])  # Always 0
    
    # Key logic step 2: derived adjustment
    mode_flag = 1 if uppercase_count > 5 else -1
    
    # Key logic steps 3–5: composite calculation
    intermediate = base_sum * correction_factor
    intermediate += mode_flag * (uppercase_count ** 2)
    if intermediate < 0:
        penalty = 1000
    
    final_score = int(intermediate - penalty)
    
    # Final adjustment based on string length (hidden dependency)
    tag_length = len(debug_tag)
    final_diagnostic = final_score + (tag_length * 5)  # +40
    
    return final_diagnostic

# Main execution flow
if __name__ == '__main__':
    readings = collect_readings()
    filtered = filter_anomalies(readings)
    processed_data = transform_phase(filtered)
    patterns = extract_patterns(processed_data)  # Unused result
    spectral_analysis = compute_frequencies(readings)  # Dead end
    final_diagnostic = analyze_signal(processed_data)
    print(f"Result: {final_diagnostic}")