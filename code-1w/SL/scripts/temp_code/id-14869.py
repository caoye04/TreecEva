import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.6]
humidity_readings = [45, 48, 50, 55, 60, 62, 58, 53]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1007, 1009, 1011]

# Irrelevant calibration offset (distractor)
calibration_offset = sum([math.sin(i * 0.1) for i in range(100)]) / 100

# Misleading preprocessing: normalizing with no real effect (dead transformation)
def normalize(lst):
    min_val, max_val = min(lst), max(lst)
    return [(x - min_val) / (max_val - min_val) for x in lst]

normalized_temps = normalize(temperature_readings)
normalized_humid = normalize(humidity_readings)

# Unused function: decoy for signal filtering (dead code path)
def filter_noise(signal, threshold=0.5):
    return [x for x in signal if abs(x - sum(signal)/len(signal)) < threshold]

# Another red herring: spurious correlation index that isn't used later
spurious_correlation = sum(
    t * h for t, h in zip(temperature_readings, humidity_readings)
) / len(temperature_readings)

# Real processing begins here — actual signal fusion logic
combined_raw = [
    round(t * (h / 100) * (1013 / p), 3)
    for t, h, p in zip(temperature_readings, humidity_readings, pressure_readings)
]

# Apply moving average filter (relevant)
def smooth_signal(signal, window=2):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window)
        smoothed.append(sum(signal[start:i+1]) / (i - start + 1))
    return smoothed

smoothed_fusion = smooth_signal(combined_raw)

# Introduce irrelevant frequency domain analysis (distraction)
frequency_components = [
    sum(smoothed_fusion[j] * math.cos(2 * math.pi * i * j / len(smoothed_fusion))
    for j in range(len(smoothed_fusion))) for i in range(3)
]

# Actual key processing: detect anomalies above dynamic threshold
baseline = sum(smoothed_fusion) / len(smoothed_fusion)
anomaly_threshold = baseline * 1.15
anomalies_detected = [x for x in smoothed_fusion if x > anomaly_threshold]

# Bit manipulation decoy — looks important but unused (bit-level red herring)
bit_encoded = 0
for val in anomalies_detected:
    shifted = int(val * 10) & 0xFF
    bit_encoded ^= shifted << (int(val) % 8)

# Destructuring assignment distraction (irrelevant tuple unpacking)
(*_, last_temp, second_last_temp) = temperature_readings
(*first_humid, *_rest) = humidity_readings

# Real processing step: count significant deviations
significant_deviation_count = len([x for x in smoothed_fusion if x > baseline * 1.2])

# Dictionary-based mapping of severity levels (partially relevant)
severity_map = {
    'normal': 0,
    'warning': 1,
    'alert': 2,
    'critical': 3
}

# Determine severity based on anomaly duration and magnitude
exceedance_duration = len([x for x in smoothed_fusion if x > anomaly_threshold])
magnitude_factor = sum(anomalies_detected) / len(anomalies_detected) if anomalies_detected else 0

# Compute weighted diagnostic score (this will be overridden — misleading intermediate)
diagnostic_score = exceedance_duration * magnitude_factor * 10

diagnostic_score = 0  # Reset — previous calculation was a red herring

# Correct path: use character counting from station codes as salt (unusual but valid)
station_codes = ['STN_A', 'STN_B', 'STN_C', 'STN_D', 'STN_E', 'STN_F', 'STN_G', 'STN_H']
char_count_salt = sum(len(code.replace('_', '')) for code in station_codes)  # = 24

# Incorporate salt into final computation
adjusted_anomaly_count = len(anomalies_detected) + (char_count_salt % 5)

# Final processing pipeline
processed_signals = []
for idx, (val, temp) in enumerate(zip(smoothed_fusion, temperature_readings)):
    # Inject index-based modulation
    modulated = val * (1 + (idx % 3) * 0.05)
    # Conditional adjustment based on temperature band
    if 24 <= temp <= 25.5:
        modulated *= 1.08
    processed_signals.append(round(modulated, 3))

# Core analysis function (uses enumerate and zip as required)
def analyze_readings(signals):
    total_energy = 0.0
    for i, signal in enumerate(signals):
        contribution = signal
        # Nested conditional with distractor branch
        if i % 4 == 0:
            contribution *= 1.1
        elif i % 4 == 1:
            # Dead logic: never affects final due to override below
            temp_debug = contribution * 0.95
            contribution = contribution  # No-op distraction
        else:
            contribution *= 0.98
        
        # Use of enumerate and zip together (required feature)
        indices = list(range(len(signals)))
        for j, (ix, sig) in enumerate(zip(indices, signals)):
            if ix == i and j == i:  # Only true on diagonal
                total_energy += contribution * (0.99 ** j)
                break
    
    # Final transformation using adjusted_anomaly_count from earlier
    # This creates cross-scope dependency (key complexity)
    final_scalar = total_energy * (adjusted_anomaly_count / len(signals))
    
    # Decoy rounding — looks like precision adjustment but actually necessary
    return round(final_scalar, 3)

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Target result: {final_diagnostic}")