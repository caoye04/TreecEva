import itertools

# Simulated sensor data processing pipeline with diagnostic checks
def collect_sensor_readings():
    raw_readings = [18, 22, 37, 41, 25, 33, 29, 31]
    offset = 5
    calibrated = [x - offset for x in raw_readings]
    return calibrated

# Irrelevant backup function (dead code path)
def backup_calibrate(x):
    return x + 3 if x < 30 else x - 2

# Signal filtering using moving average (relevant)
def smooth_signal(data):
    window_size = 3
    smoothed = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i + window_size]
        smoothed.append(round(sum(window) / window_size, 2))
    return smoothed

# Red herring: unused noise detection
noise_threshold = 1.5
def detect_noise(pattern):
    differences = [abs(pattern[i] - pattern[i-1]) for i in range(1, len(pattern))]
    return [diff > noise_threshold for diff in differences]

# Data normalization (relevant but partially obscured)
def normalize(data):
    min_val, max_val = min(data), max(data)
    if max_val == min_val:
        return [0.5] * len(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Decoy statistical analysis (distractor)
def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count/total) * log2(count/total) for count in freq.values())
    return round(entropy, 4)

# Core transformation: frequency domain simulation via simple bit analysis (relevant)
def extract_frequency_signature(values):
    # Use bit manipulation to simulate spectral signature
    integral = 0
    for val in values:
        shifted = int(val * 100)
        integral ^= shifted  # XOR accumulation
        integral = (integral << 1) & 0xFFFF  # 16-bit wrap
    return integral

# Higher-order processing with lambda and set operations (mixed relevance)
def enhance_features(signal):
    # Generate feature combinations
    pairs = list(itertools.combinations(signal[:5], 2))
    diff_set = {round(abs(a - b), 2) for a, b in pairs}
    sum_set = {round(a + b, 2) for a, b in pairs}
    
    # Feature extraction using lambda
    feature_score = sum(map(lambda x: x**2, diff_set)) - len(sum_set)
    return feature_score

# Main analysis chain
processed_data = None
def analyze_signal(raw):
    global processed_data
    
    # Step 1: Smoothing
    step1 = smooth_signal(raw)
    
    # Step 2: Normalize
    step2 = normalize(step1)
    
    # Step 3: Enhance features (uses lambda and sets)
    enhancement_metric = enhance_features(step2)
    
    # Step 4: Simulate frequency signature (bitwise core)
    freq_code = extract_frequency_signature(step2)
    
    # Dead branch: never executed, misleading control flow
    debug_mode = False
    extra_adjustment = 0
    if debug_mode and len(step2) > 100:
        extra_adjustment = compute_entropy(step2)
    
    # Final integration
    processed_data = {
        'base': sum(step1),
        'enriched': enhancement_metric,
        'signature': freq_code,
        'aux': extra_adjustment
    }
    
    # Critical calculation
    result = int(processed_data['base'] + (processed_data['enriched'] / 100) + (processed_data['signature'] % 1000))
    return result

# Unused alternate workflow (red herring)
def legacy_analysis(seq):
    return sum(x * 2 for x in seq if x > 25)

# Entry point
readings = collect_sensor_readings()
interim_noise_check = detect_noise(readings)  # Dead usage
final_diagnostic = analyze_signal(readings)
print(f"Result: {final_diagnostic}")