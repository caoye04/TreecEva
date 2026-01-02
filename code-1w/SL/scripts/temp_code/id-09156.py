import math

# Simulated sensor array data from environmental monitoring system
def acquire_samples():
    raw_readings = [14.2, 18.7, 22.5, 19.3, 25.1, 20.4, 17.8, 23.6]
    calibration_offset = 0.8
    adjusted = [r + calibration_offset for r in raw_readings]
    filtered = [val for val in adjusted if val > 18.0]  # Only significant readings
    return filtered

# Signal processing with multiple transformation stages
def preprocess(signal_chunk):
    windowed = signal_chunk[1:-1]  # Remove edge noise
    normalized = [x / max(windowed) for x in windowed]
    squared_energy = [val ** 2 for val in normalized]
    return squared_energy

# Legacy diagnostic function (partially deprecated)
def legacy_evaluate(data):
    avg = sum(data) / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    return avg * 0.7 + variance * 0.3

# Decoy function – appears relevant but unused in final computation
def compute_redundancy_score(sequence):
    if not sequence:
        return 0
    unique_vals = set(sequence)
    duplicate_count = len(sequence) - len(unique_vals)
    score = len(sequence) / (duplicate_count + 1)
    adjustment = math.sin(len(unique_vals))
    return score * adjustment

# Auxiliary transformation: frequency domain approximation
def estimate_dominant_frequency(samples):
    n = len(samples)
    fft_magnitude = [abs(math.sin(2 * math.pi * k / n)) for k in range(n)]
    total_power = sum(fft_magnitude)
    weighted_sum = sum(i * fft_magnitude[i] for i in range(n))
    centroid = weighted_sum / (total_power + 1e-8)
    return centroid * 1.5

# Main analysis pipeline combining statistical and set-based logic
def analyze_signal(processed):
    if len(processed) < 3:
        return -1
    
    # Compute statistical descriptors
    mean_val = sum(processed) / len(processed)
    std_dev = (sum((x - mean_val) ** 2 for x in processed) / len(processed)) ** 0.5
    z_scores = [abs((x - mean_val) / (std_dev + 1e-8)) for x in processed]
    outliers = {i for i, z in enumerate(z_scores) if z > 1.8}
    
    # Apply correction based on outlier presence
    corrected_values = [
        processed[i] * 0.9 if i in outliers else processed[i]
        for i in range(len(processed))
    ]
    
    # Secondary validation using moving window
    valid_windows = 0
    for i in range(len(corrected_values) - 2):
        window_avg = sum(corrected_values[i:i+3]) / 3
        if 0.4 <= window_avg <= 0.8:
            valid_windows += 1
    
    # Set-based interference: unrelated tracking variables
    observed_indices = set(range(len(processed)))
    excluded_indices = {0, len(processed)-1}
    active_set = observed_indices - excluded_indices
    temp_mismatch = len(active_set.difference(outliers)) % 7
    
    # Core decision logic
    base_score = sum(corrected_values) * 100
    window_bonus = valid_windows * 15
    penalty = len(outliers) * 10
    
    # Final diagnostic formula
    final_score = base_score + window_bonus - penalty + temp_mismatch
    return int(round(final_score))

# Irrelevant utility: network health monitor (dead code path)
def check_transmission_integrity(payload):
    checksum = 0
    for char in str(payload):
        checksum ^= ord(char)
    status_codes = {'healthy': 0, 'warning': 1, 'critical': 2}
    return status_codes.get('healthy')

# Orchestration with red herring operations
sample_data = acquire_samples()
processed_samples = preprocess(sample_data)

# Unused intermediate computations - misleading relevance
energy_summary = [math.log(x + 1) for x in processed_samples]
spectral_metric = estimate_dominant_frequency(processed_samples)
placeholder_diagnostic = legacy_evaluate(processed_samples)
redundancy_diagnostic = compute_redundancy_score(processed_samples)

# Key execution point
final_diagnostic = analyze_signal(processed_samples)

# Output target result
print(f"Result: {final_diagnostic}")