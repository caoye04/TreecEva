import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 24.9, 23.7, 22.9]
humidity_readings = [56, 58, 61, 54, 52, 57, 59, 60]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1014, 1016, 1011]

# Irrelevant calibration constants (distractor)
CALIBRATION_FACTOR_A = 0.987
CALIBRATION_FACTOR_B = 1.014
REFERENCE_OFFSET = 273.15

# Misleading intermediate processing (red herring)
def adjust_for_drift(values, factor):
    return [v * factor for v in values]

# Unused function - dead code path (distractor)
def legacy_normalization(data):
    max_val, min_val = max(data), min(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

# Fake diagnostic that looks important but isn't used (decoy)
class DiagnosticEngine:
    def __init__(self):
        self.thresholds = {'temp': 30, 'humid': 70}
        self.alert_mode = False

    def run_self_test(self):
        return True

# Auxiliary transformation with partial relevance
noise_floor = 0.05
def apply_noise_filter(signal):
    return [x for x in signal if abs(x) > noise_floor]

# Complex preprocessing chain with mixed relevance
def preprocess_sensor_data(raw_data):
    # Step 1: Smooth using moving average (relevant)
    smoothed = []
    window_size = 3
    for i in range(len(raw_data)):
        start = max(0, i - window_size + 1)
        end = i + 1
        window_avg = sum(raw_data[start:end]) / (end - start)
        smoothed.append(round(window_avg, 2))
    
    # Step 2: Normalize to baseline (partially relevant)
    baseline = sum(smoothed) / len(smoothed)
    normalized = [x - baseline for x in smoothed]
    
    # Step 3: Amplify small fluctuations (irrelevant but looks technical)
    amplified = [x * 1.25 for x in normalized]
    
    # Step 4: Filter out near-zero values (relevant)
    filtered = apply_noise_filter(amplified)
    
    # Step 5: Apply fake phase shift (completely irrelevant)
    shifted = [filtered[-i % len(filtered)] for i in range(len(filtered))] if len(filtered) > 0 else []
    
    # Return only the filtered component (shifted is a red herring)
    return filtered

# Another decoy function that computes something plausible but unused
def compute_entropy(data):
    total = sum(abs(x) for x in data)
    if total == 0:
        return 0.0
    probabilities = [abs(x) / total for x in data]
    return -sum(p * math.log(p) for p in probabilities if p > 0)

# Real processing pipeline
processed_temps = preprocess_sensor_data(temperature_readings)
processed_humid = preprocess_sensor_data(humidity_readings)
processed_pressure = preprocess_sensor_data(pressure_readings)

# Combine signals with weighted fusion (key logic)
combined_signal = []
max_len = max(len(processed_temps), len(processed_humid), len(processed_pressure))

# Extend shorter lists to match length (padding with last value)
for lst in [processed_temps, processed_humid, processed_pressure]:
    while len(lst) < max_len:
        lst.append(lst[-1] if lst else 0)

# Weighted combination: temp (40%), humid (30%), pressure (30%)
for i in range(max_len):
    fused = (
        0.4 * processed_temps[i] +
        0.3 * processed_humid[i] +
        0.3 * processed_pressure[i]
    )
    combined_signal.append(round(fused, 3))

# Analyze the fused signal (target computation)
def analyze_readings(signal):
    if not signal:
        return 0.0
    
    # Compute statistical moments (some are distractors)
    mean_val = sum(signal) / len(signal)
    variance = sum((x - mean_val) ** 2 for x in signal) / len(signal)
    std_dev = math.sqrt(variance)
    
    # Skewness calculation (looks complex but irrelevant)
    if std_dev > 0:
        skewness = sum(((x - mean_val) / std_dev) ** 3 for x in signal) / len(signal)
    else:
        skewness = 0
    
    # Kurtosis (another advanced stat - not used in result)
    if std_dev > 0:
        kurtosis = sum(((x - mean_val) / std_dev) ** 4 for x in signal) / len(signal)
    else:
        kurtosis = 0
    
    # Key insight: Count how many readings exceed 1 standard deviation from mean
    threshold = std_dev  # Use std_dev as dynamic threshold
    extreme_count = sum(1 for x in signal if abs(x - mean_val) > threshold)
    
    # Final diagnostic is based on pattern density, not the fancy stats
    if len(signal) > 0:
        pattern_density = extreme_count / len(signal)
        # Scale by 1000 and truncate to integer
        result = int(pattern_density * 1000)
    else:
        result = 0
    
    return result

# Execute main analysis
final_diagnostic = analyze_readings(processed_signals=combined_signal)

# Print result as required
print(f"Target result: {final_diagnostic}")