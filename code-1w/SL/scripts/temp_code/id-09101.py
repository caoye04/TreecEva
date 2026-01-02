import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 25.3, 26.0, 24.8, 23.9, 22.7, 25.6, 26.2, 27.1, 26.8, 25.9]
humidity_readings = [55.2, 57.8, 60.1, 62.3, 61.5, 59.4, 56.7, 63.2, 64.0, 65.5, 63.8, 62.9]
pressure_readings = [1013.2, 1012.8, 1011.9, 1010.5, 1009.7, 1010.3, 1011.0, 1008.9, 1007.6, 1006.8, 1008.1, 1009.4]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.037
CALIBRATION_OFFSET_B = -0.021
REFERENCE_VOLTAGE = 3.3
NOISE_FLOOR_DB = 42.5

# Misleading intermediate computations (red herring)
def compute_power_spectral_density(signal):
    n = len(signal)
    psd = [0] * n
    for i in range(n):
        psd[i] = (signal[i] ** 2) / n
    return psd

power_density = compute_power_spectral_density(temperature_readings)  # unused

# Data alignment and windowing (partially relevant but overcomplicated)
def align_and_window(data, window_size=4):
    padded = [data[0]] * (window_size - 1) + data
    windows = []
    for i in range(len(padded) - window_size + 1):
        windows.append(padded[i:i + window_size])
    return windows

aligned_temp = align_and_window(temperature_readings)
aligned_humid = align_and_window(humidity_readings)

# Decoy function with unused logic
def calculate_thermal_index_v1(temp, humid):
    index = temp * (humid / 100) * 0.65
    adjustment = math.log(temp + 1) if temp > 0 else 0
    return index + adjustment

# Real processing begins here
rolling_avg_temp = []
for i in range(len(temperature_readings) - 2):
    avg = sum(temperature_readings[i:i+3]) / 3
    rolling_avg_temp.append(round(avg, 2))

# Humidity trend detection (distractor)
humidity_trend = []
for i in range(1, len(humidity_readings)):
    trend_val = humidity_readings[i] - humidity_readings[i-1]
    humidity_trend.append(trend_val)

# Pressure normalization (irrelevant path)
normalized_pressure = []
baseline_p = pressure_readings[0]
for p in pressure_readings:
    normalized_pressure.append(p - baseline_p)

# Key transformation: extract significant fluctuations
def extract_anomalies(series, tolerance=1.0):
    anomalies = []
    for i in range(1, len(series)):
        diff = abs(series[i] - series[i-1])
        if diff > tolerance:
            anomalies.append((i, diff))
    return anomalies

# Apply to temperature fluctuations above 1.0°C
temp_anomalies = extract_anomalies(temperature_readings, tolerance=1.0)

# Process humidity spikes (misleading branch)
humidity_spikes = extract_anomalies(humidity_readings, tolerance=2.0)

# Unused statistical summary (dead code path)
class DataSummary:
    def __init__(self, values):
        self.mean = sum(values) / len(values)
        self.min = min(values)
        self.max = max(values)
        self.variance = sum((x - self.mean) ** 2 for x in values) / len(values)
        self.skew = 0  # placeholder

summary_temp = DataSummary(temperature_readings)
summary_humid = DataSummary(humidity_readings)

# Actual signal processing pipeline
processed_data = {
    'smoothed': rolling_avg_temp,
    'spike_indices': [idx for idx, _ in temp_anomalies],
    'magnitude': [round(mag, 2) for _, mag in temp_anomalies]
}

# Threshold configuration map (critical for final decision)
threshold_map = {
    'low_risk': 1.2,
    'moderate_risk': 1.8,
    'high_risk': 2.5
}

# Diagnostic engine with multiple evaluation layers
def evaluate_risk_level(magnitude, thresholds):
    if magnitude < thresholds['low_risk']:
        return 1
    elif magnitude < thresholds['moderate_risk']:
        return 2
    elif magnitude < thresholds['high_risk']:
        return 3
    else:
        return 4

# Auxiliary transformation (slicing operation used here - required feature)
def slice_stable_segments(data, window=2):
    segments = []
    i = 0
    while i < len(data) - window + 1:
        segment = data[i:i+window]
        if max(segment) - min(segment) < 0.5:
            segments.append(segment)
        i += 1
    return segments

stable_windows = slice_stable_segments(rolling_avg_temp)

# Final analysis combining spike magnitudes and risk classification
def analyze_readings(diagnostic_input, thresholds):
    spike_magnitudes = diagnostic_input['magnitude']
    classifications = [evaluate_risk_level(mag, thresholds) for mag in spike_magnitudes]
    
    # Compute weighted diagnostic score
    weight_map = {1: 0.1, 2: 0.4, 3: 1.2, 4: 2.5}
    total_score = 0.0
    for mag, cls in zip(spike_magnitudes, classifications):
        contribution = mag * weight_map[cls]
        total_score += contribution
    
    # Additional correction based on spike count density
    time_span_days = 12  # one reading per day
    spike_count = len(spike_magnitudes)
    density_factor = spike_count / time_span_days
    
    # Final diagnostic is integer-rounded total score adjusted by density
    final_score = int(total_score * (1 + density_factor))
    
    # Introduce irrelevant bit manipulation (distractor)
    masked_score = final_score ^ 0xFF  # XOR with 255
    shifted = (masked_score << 2) >> 1  # shift left then right (no net effect beyond multiply by 2)
    
    # But we ignore all that and return original adjusted score
    return final_score

# Execute key statement
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Print result as required
print(f"Target result: {final_diagnostic}")