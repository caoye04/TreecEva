import math

# Simulated sensor data processing with diagnostic analysis
def collect_samples(base_freq, duration, sample_rate):
    samples = []
    for t in range(0, int(duration * sample_rate)):
        time_point = t / sample_rate
        # Signal composed of multiple harmonics
        signal = (math.sin(2 * math.pi * base_freq * time_point) + 
                  0.5 * math.sin(2 * math.pi * 3 * base_freq * time_point))
        samples.append(signal)
    return samples

# Irrelevant helper - dead code path
def deprecated_filter(x):
    return [val for val in x if abs(val) > 0.1]

# Noise injection function - misleading distraction
def add_noise(data, intensity=0.02):
    return [val + intensity * math.sin(i) for i, val in enumerate(data)]

# Main transformation: apply windowing and FFT-like magnitude estimation
def apply_hamming_window(data):
    N = len(data)
    windowed = [data[i] * (0.54 - 0.46 * math.cos(2 * math.pi * i / (N - 1))) for i in range(N)]
    return windowed

# Simulate frequency bin energy aggregation (simplified)
def compute_spectral_energy(windowed_data):
    N = len(windowed_data)
    energies = []
    for k in range(5):  # Analyze first 5 bins
        real = sum(windowed_data[n] * math.cos(2 * math.pi * k * n / N) for n in range(N))
        imag = sum(windowed_data[n] * math.sin(2 * math.pi * k * n / N) for n in range(N))
        magnitude = math.sqrt(real**2 + imag**2)
        energies.append(magnitude)
    return energies

# Determine active bands based on thresholds
def identify_active_bands(spectral_energies, config_map):
    bands = []
    for i, energy in enumerate(spectral_energies):
        if energy > config_map['threshold'] * (i + 1):
            bands.append(i)
    return set(bands)

# Recursive harmonic validation (unused but plausible)
def validate_harmonic_chain(band_list, current=1):
    if current > max(band_list):
        return True
    if current in band_list:
        return validate_harmonic_chain(band_list, current + 1)
    return False

# Decoy function - looks important but unused
def generate_report(data_summary):
    report = {"integrity": "valid", "checksum": sum(data_summary) % 17}
    return report

# Core diagnostic logic
def analyze_signal(data_vector, critical_thresholds):
    # Step 1: Preprocess with conditional expression
    cleaned = [x if abs(x) > 0.01 else 0.0 for x in data_vector]
    
    # Step 2: Count significant components
    significant_count = sum(1 for x in cleaned if x != 0.0)
    
    # Step 3: Apply conditional scaling
    scale_factor = 2.5 if significant_count > 100 else 1.8
    scaled = [x * scale_factor for x in cleaned]
    
    # Step 4: Compute aggregate metrics
    total_power = sum(x**2 for x in scaled)
    avg_magnitude = math.sqrt(total_power / len(scaled)) if scaled else 0
    
    # Step 5: Determine modulation index using set intersection
    reference_bands = {1, 3, 4}
    detected_bands = critical_thresholds.intersection({1, 2, 3, 4, 5})
    overlap = len(reference_bands & detected_bands)
    
    # Step 6: Conditional diagnostic path
    if overlap >= 2 and avg_magnitude > 0.45:
        diagnostic_code = 3
    elif overlap == 1 and total_power > 15:
        diagnostic_code = 2
    else:
        diagnostic_code = 1
    
    # Step 7: Final computation with modular arithmetic
    checksum = sum(int(100 * x) for x in scaled[:10]) % 89
    final_score = (diagnostic_code * 1000) + checksum
    
    # Step 8: Red herring transformation (no effect)
    temp_analysis = {"data": [math.tanh(x) for x in scaled], "version": "legacy"}
    legacy_flag = temp_analysis.get("version") == "current"
    
    # Final result
    return final_score

# Misleading initialization block
initial_config = {
    "threshold": 0.35,
    "sample_rate": 1000,
    "duration": 2.0,
    "base_frequency": 5
}

# Generate raw data
raw_sensor_data = collect_samples(
    base_freq=initial_config["base_frequency"],
    duration=initial_config["duration"],
    sample_rate=initial_config["sample_rate"]
)

# Add noise (distraction)
noisy_data = add_noise(raw_sensor_data, intensity=0.03)

# Apply main processing window
windowed_signal = apply_hamming_window(noisy_data)

# Compute spectral characteristics
spectral_profile = compute_spectral_energy(windowed_signal)

# Build threshold set from spectral data (only some used)
thresh_elements = []
for i, energy in enumerate(spectral_profile):
    if energy > 0.1:
        thresh_elements.append(i + 2)
thresh_elements.extend([7, 8, 10])
threshold_set = set(thresh_elements)

# Dead code - unused parameter map
auxiliary_params = {
    "bands": identify_active_bands(spectral_profile, initial_config),
    "harmonics_valid": validate_harmonic_chain([]),  # never called
    "fallback_mode": False
}

# Processed data for analysis (key input)
processed_data = windowed_signal.copy()

# Modify based on conditional expression
processed_data = processed_data[::-1] if len(processed_data) % 2 == 1 else processed_data

# CRITICAL EXECUTION POINT
final_diagnostic = analyze_signal(processed_data, threshold_set)

# Output result
print(f"Result: {final_diagnostic}")