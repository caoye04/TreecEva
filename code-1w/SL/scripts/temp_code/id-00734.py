import math

# Simulated sensor data processing with embedded diagnostics
def collect_sensor_readings():
    raw_samples = [127, 255, 192, 64, 224, 32, 160, 96]
    scale_factor = 0.75
    adjusted = [x * scale_factor for x in raw_samples]
    return adjusted

# Irrelevant transformation: color space simulation (red herring)
def rgb_to_grayscale(pixels):
    return [int(0.299 * r + 0.587 * g + 0.114 * b) for r, g, b in pixels]

# Unused helper: frequency binning (dead code path)
def bin_frequencies(signal, bins=8):
    min_val, max_val = min(signal), max(signal)
    width = (max_val - min_val) / bins
    return [int((x - min_val) // width) for x in signal]

# Core data transformation pipeline
def preprocess_signal(data):
    shifted = [x - 64 for x in data]  # Normalize around baseline
    amplified = [x * 1.5 for x in shifted]
    filtered = [x for x in amplified if x > 0]  # Remove negative noise
    return filtered

# Bit manipulation for checksum (distractor with partial relevance)
def compute_checksum(values):
    checksum = 0
    for v in values:
        truncated = int(v) & 0xFF
        checksum ^= truncated
        checksum = (checksum << 1) | (checksum >> 7)
        checksum &= 0xFF
    return checksum

# Main analysis function with lambda-based reduction
def analyze_signal(data):
    # Compute statistical features
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    
    # Redundant feature extraction (distractor)
    peak = max(data)
    entropy_proxy = -sum((x / peak) * math.log(x / peak) for x in data if x > 0)
    
    # Critical calculation chain
    quality_score = len(data) * std_dev / (mean_val + 1e-8)
    adjustment_factor = (lambda x: x ** 0.25)(quality_score)  # Use of lambda
    normalized_index = (mean_val + std_dev) * adjustment_factor
    
    # Complex conditional weighting (nested logic)
    if std_dev > 50:
        weight = 0.8
    elif mean_val < 30:
        weight = 1.2
    else:
        weight = 1.0
        secondary_weight = 0.9 if entropy_proxy > 10 else 1.1  # Unused branch
        
    final_index = normalized_index * weight
    
    # Decoy operation: matrix-like transformation (irrelevant)
    matrix_rep = [[x * 0.1 for _ in range(3)] for x in data[:3]]
    determinant_proxy = matrix_rep[0][0] * matrix_rep[1][1] - matrix_rep[0][1] * matrix_rep[1][0]
    
    # Final diagnostic computation (answer point)
    final_diagnostic = int(final_index + determinant_proxy - 5)
    return final_diagnostic

# Orchestration with unused branches
def main_pipeline():
    temp_calibration = [22.5, 23.1, 21.9]  # Environmental sensor (distractor)
    humidity_data = {"morning": 45, "afternoon": 38, "night": 52}  # Unused
    
    raw_data = collect_sensor_readings()
    processed_data = preprocess_signal(raw_data)
    
    # Spurious control flow
    mode = 'diagnostic'
    if mode == 'debug':
        debug_view = [hex(int(x)) for x in processed_data]
    elif mode == 'trace':
        trace_log = ','.join(map(str, processed_data))
    
    # Key execution point
    final_diagnostic = analyze_signal(processed_data)
    
    # Print required output
    print(f"Result: {final_diagnostic}")
    
    # Dead return paths
    if len(processed_data) > 100:
        return compute_checksum(processed_data)
    
    return final_diagnostic

# Execute main logic
result = main_pipeline()