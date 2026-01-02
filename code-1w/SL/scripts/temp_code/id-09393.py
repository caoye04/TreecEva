import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.6, 26.7, 24.3, 23.9, 25.1]
humidity_readings = [56, 61, 59, 62, 58, 55, 60, 63]
pressure_readings = [1013, 1015, 1012, 1010, 1009, 1014, 1016, 1011]

# Irrelevant calibration offset (distractor)
calibration_bias = sum([0.1 * math.sin(i) for i in range(len(temperature_readings))])

# Misleading intermediate transformation (dead path)
def adjust_for_altitude(values, altitude=150):
    return [v * (1 - altitude / 10000) for v in values]

adjusted_temps = adjust_for_altitude(temperature_readings)  # Unused

# Signal processing pipeline
smoothing_factor = 0.85
def smooth_signal(signal):
    smoothed = [signal[0]]
    for i in range(1, len(signal)):
        smoothed.append(smoothing_factor * signal[i] + (1 - smoothing_factor) * smoothed[-1])
    return smoothed

# Process relevant signals
temp_trend = [t - 22 for t in temperature_readings]  # Baseline adjustment
smoothed_trend = smooth_signal(temp_trend)

# Humidity outlier detection (irrelevant but plausible)
mean_humidity = sum(humidity_readings) / len(humidity_readings)
humidity_devs = [(h - mean_humidity) ** 2 for h in humidity_readings]
humidity_variance = sum(humidity_devs) / len(humidity_devs)
outlier_threshold = mean_humidity + 2 * math.sqrt(humidity_variance)
humidity_outliers = [h for h in humidity_readings if h > outlier_threshold]  # Unused

# Pressure normalization (distractor)
normalized_pressure = [(p - 1012) / 10 for p in pressure_readings]

# Composite index calculation (core logic buried)
weighted_temp_index = sum([t * 1.5 for t in smoothed_trend])
fluctuation_penalty = 0
for i in range(1, len(smoothed_trend)):
    change = abs(smoothed_trend[i] - smoothed_trend[i-1])
    if change > 1.0:
        fluctuation_penalty += change * 0.5

raw_stability_score = weighted_temp_index - fluctuation_penalty

# Decoy function with plausible name
def compute_thermal_mass(temps, material='air'):
    factors = {'air': 0.24, 'water': 1.0, 'steel': 0.12}
    return sum(temps) * factors.get(material, 0.24)

# Unused but realistic call
device_thermal_capacity = compute_thermal_mass(temperature_readings, 'air')

# Real processing begins here: detect sustained anomalies
anomaly_window = []
for val in smoothed_trend:
    anomaly_window.append(abs(val) > 2.0)

# Count consecutive high deviations
max_consecutive = 0
current_streak = 0
for is_anomalous in anomaly_window:
    if is_anomalous:
        current_streak += 1
        max_consecutive = max(max_consecutive, current_streak)
    else:
        current_streak = 0

# Secondary metric: trend direction consistency
positive_trend = [t > 0 for t in smoothed_trend]
consistent_runs = []
current_run = 0
prev = None
for curr in positive_trend:
    if prev is not None and curr == prev:
        current_run += 1
    else:
        if current_run > 0:
            consistent_runs.append(current_run)
        current_run = 1
    prev = curr
if current_run > 0:
    consistent_runs.append(current_run)
long_consistent_segments = len([r for r in consistent_runs if r >= 3])

# Data structure cross-reference (plausible complexity)
signal_summary = {
    'stability': raw_stability_score,
    'max_anomaly_streak': max_consecutive,
    'consistency_bands': long_consistent_segments,
    'size_hint': len(smoothed_trend)
}

# Final diagnostic computation
processed_signals = list(zip(
    [signal_summary['stability']],
    [signal_summary['max_anomaly_streak']],
    [signal_summary['consistency_bands']]
))

def analyze_readings(data):
    total = 0
    for entry in data:
        a, b, c = entry
        total += int(a) + (b * 100) + (c * 10)
    return abs(total)  # Ensure positive result

final_diagnostic = analyze_readings(processed_signals)
print(f"Result: {final_diagnostic}")