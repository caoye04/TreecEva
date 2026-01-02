import math

# Simulated sensor data processing with embedded diagnostics
def collect_samples(base_freq, duration, sample_rate):
    timesteps = [i / sample_rate for i in range(int(duration * sample_rate))]
    raw_samples = [math.sin(2 * math.pi * base_freq * t) + \
                  0.5 * math.cos(2 * math.pi * 3 * base_freq * t) \
                  for t in timesteps]
    return raw_samples

# Irrelevant auxiliary function (decoy)
def compute_entropy(data):
    histogram = {}
    for x in data:
        key = int(x * 10) % 5
        histogram[key] = histogram.get(key, 0) + 1
    total = len(data)
    entropy = 0
    for count in histogram.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 3)

# Signal preprocessing with red herrings
def preprocess_signal(samples, threshold=0.1, gain=1.2):
    amplified = [x * gain for x in samples]
    filtered = []
    spike_count = 0
    for val in amplified:
        if abs(val) > threshold:
            filtered.append(val)
            if val > 0.8:
                spike_count += 1  # Distraction: unused later
    # Distractor: dead code path
    normalization_factor = sum([abs(x) for x in amplified]) / len(amplified) if amplified else 1
    normalized = [x / normalization_factor for x in amplified]  # Not used
    return filtered  # Only this matters

# Data segmentation decoy
def segment_data(data, window_size=100):
    segments = []
    for i in range(0, len(data) - window_size + 1, window_size):
        segment = data[i:i+window_size]
        segments.append(segment)
    return segments  # Unused in main flow

# Core analysis with conditional logic and slicing
def analyze_signal(cleaned):
    n = len(cleaned)
    if n == 0:
        return 0
    
    # Use slicing to isolate mid-sequence behavior
    mid_section = cleaned[n//4 : 3*n//4]
    upper_quartile = sorted(mid_section)[len(mid_section)//2:]
    
    # Compute weighted diagnostic score
    signal_power = sum([x*x for x in mid_section])
    avg_amplitude = sum(abs(x) for x in mid_section) / len(mid_section)
    
    # Conditional expression based on distribution
    peak_ratio = len([x for x in upper_quartile if x > 0.5]) / len(upper_quartile) if upper_quartile else 0
    
    # Key logic step involving enumerate and zip
    trend_score = 0
    for i, (a, b) in enumerate(zip(mid_section, mid_section[1:])):
        if b > a and i % 2 == 0:  # Every even-indexed transition
            trend_score += 0.1
    
    # Final computation combining multiple concepts
    diagnostic_value = signal_power * avg_amplitude
    if peak_ratio > 0.3:
        diagnostic_value += trend_score * 100
    
    # Misleading transformation (not part of output)
    transformed = [math.atan(x) for x in cleaned]
    secondary_index = sum(transformed) * 0.01  # Decoy variable
    
    return int(diagnostic_value)  # Deterministic integer result

# Irrelevant constants (distractors)
CALIBRATION_OFFSET = -0.04
REFERENCE_VOLTAGE = 3.3
MAX_ITERATIONS = 500

# Main execution flow
if __name__ == "__main__":
    # Generate raw data
    raw_signal = collect_samples(base_freq=2.5, duration=4, sample_rate=50)
    
    # Extract entropy (unused - distraction)
    entropy_metric = compute_entropy(raw_signal)
    
    # Preprocess to get relevant samples
    processed_samples = preprocess_signal(raw_signal, threshold=0.15)
    
    # Perform segmentation (result not used - red herring)
    segments = segment_data(processed_samples, window_size=75)
    
    # Apply secondary filter (no effect - dead code)
    clipped = [x for x in processed_samples if x < 1.0]
    scaling_constant = math.sqrt(2) * CALIBRATION_OFFSET
    adjusted = [x + scaling_constant for x in clipped]  # Nowhere used
    
    # Critical statement
    final_diagnostic = analyze_signal(processed_samples)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")