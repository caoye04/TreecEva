import math

# Simulated sensor data processing with diagnostic logic
def collect_sensor_samples():
    samples = []
    for i in range(180):
        sample = int((math.sin(i * 0.1) * 100) + (math.cos(i * 0.05) * 50) + 127)
        samples.append(sample % 256)
    return samples

# Irrelevant transformation: color space simulation (distractor)
def rgb_to_grayscale(pixels):
    gray_vals = []
    for px in pixels:
        g = int((px * 0.299) + (px * 0.587) + (px * 0.114))
        gray_vals.append(g % 256)
    return gray_vals

# Unused function: audio envelope follower (dead code path)
def compute_envelope(signal):
    envelope = []
    prev = 0
    for s in signal:
        diff = abs(s - prev)
        env_val = max(prev, prev + 0.1 * diff) if s > prev else max(s, s + 0.05 * diff)
        envelope.append(env_val)
        prev = env_val
    return envelope

# Bit manipulation analysis (partially relevant)
def extract_frequency_bands(data):
    low_band = 0
    mid_band = 0
    high_band = 0
    for val in data[::3]:
        if val & 0b11000000 == 0b11000000:  # Top two bits set
            high_band += 1
        elif val & 0b00100000:
            mid_band += 1
        else:
            low_band += 1
    return (low_band << 2) | (mid_band >> 1) | (high_band << 1)

# Set-based interference pattern detection
def detect_interference_signatures(raw_data):
    unique_bytes = set(raw_data)
    suspicious = set()
    for b in unique_bytes:
        if bin(b).count('1') == 4 and b % 7 == 0:
            suspicious.add(b)
    baseline = {x for x in range(100, 150) if x % 3 == 0}
    rare_patterns = {x for x in unique_bytes if x < 30 or x > 220}
    overlap_count = len(suspicious.intersection(baseline)) + len(rare_patterns.difference(baseline))
    return overlap_count * 2

# Core signal quality analyzer
def validate_sample_range(samples, min_val=0, max_val=255):
    return all(min_val <= s <= max_val for s in samples)

# Main diagnostic engine
def analyze_signal_quality(samples, noise_filter):
    if not validate_sample_range(samples):
        return -1
    
    # Distractor: unused statistical moments
    mean_val = sum(samples) / len(samples)
    variance = sum((x - mean_val) ** 2 for x in samples) / len(samples)
    skew_hint = sum((x - mean_val) ** 3 for x in samples) / (len(samples) * variance ** 1.5) if variance > 0 else 0
    
    # Real computation begins: frequency band metric
    freq_metric = extract_frequency_bands(samples)
    
    # Interference detection via sets
    interference_score = detect_interference_signatures(samples)
    
    # Decoy normalization (never used)
    normalized = [max(0, min(255, int((s - mean_val) * 1.25) + 128)) for s in samples]
    
    # Conditional logic chain with nesting depth 4
    adjustment_factor = 1.0
    if freq_metric > 50:
        if interference_score < 20:
            if mean_val < 100:
                adjustment_factor = 0.85
            elif mean_val > 180:
                adjustment_factor = 0.75
            else:
                adjustment_factor = 0.95
        else:
            adjustment_factor = 0.6
    else:
        if variance < 1500:
            adjustment_factor = 0.9
        else:
            if skew_hint > 0.5:
                adjustment_factor = 0.8
            else:
                adjustment_factor = 1.0
    
    # Primary result calculation
    base_score = len([s for s in samples if s in noise_filter])
    filtered_ratio = base_score / len(samples)
    
    # Final composition with bit manipulation
    raw_diagnostic = int((filtered_ratio * 1000) + freq_metric)
    final_diagnostic = raw_diagnostic ^ interference_score  # XOR fusion
    final_diagnostic = final_diagnostic + int(adjustment_factor * 100)
    
    # Red herring: geometric progression check (unused)
    geo_sum = 0
    for i in range(1, 10):
        geo_sum += 3 * (2 ** (i-1))
    
    return final_diagnostic

# Entry point
if __name__ == "__main__":
    raw_samples = collect_sensor_samples()
    
    # Distractor variables
    processed_image = rgb_to_grayscale(raw_samples)
    entropy_estimate = len(set(raw_samples)) * 0.75
    
    # Critical threshold definition
    threshold_set = {n for n in range(50, 200) if n % 4 == 2}
    
    # Signal envelope (computed but unused)
    envelope = compute_envelope(raw_samples)
    
    # Key execution point
    final_diagnostic = analyze_signal_quality(raw_samples, threshold_set)
    
    # Output result
    print(f"Target result: {final_diagnostic}")