import itertools

# Simulated sensor data stream for a diagnostic system
temperature_readings = [36.1, 37.5, 38.2, 37.0, 36.8, 39.1, 37.3]
blood_pressure_systolic = [120, 125, 130, 118, 142, 124, 131]
oxygen_levels = [98, 96, 94, 95, 97, 93, 92]
heart_rate = [70, 75, 80, 85, 90, 95, 100]

# Irrelevant auxiliary data (distractor)
legacy_codes = ['A1', 'B2', 'C3', 'D4']
encoding_map = {code: idx for idx, code in enumerate(legacy_codes)}
encoded_sequence = list(map(lambda x: encoding_map[x] * 2, legacy_codes))

# Noise filter parameters (partially irrelevant)
smoothing_window = 3
noise_floor = 0.5

# Signal processing helper (red herring function)
def apply_smoothing(signal, window=smoothing_window):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Unused complex transformation (dead path)
def fourier_approximation(series, terms=3):
    from math import sin, pi
    result = [0.0] * len(series)
    n = len(series)
    for t in range(n):
        for k in range(1, terms + 1):
            result[t] += (2 / n) * series[t] * sin(2 * pi * k * t / n)
    return result

# Real-time anomaly detection (core logic buried in noise)
critical_thresholds = {
    'fever': 38.0,
    'hypertension': 140,
    'low_oxygen': 94,
    'tachycardia': 90
}

# Misleading intermediate aggregations (distractor variables)
avg_temp = sum(temperature_readings) / len(temperature_readings)
avg_pressure = sum(blood_pressure_systolic) / len(blood_pressure_systolic)
composite_risk_score = (avg_temp * 1.5 + avg_pressure * 0.5) / 100  # Not used later

# Data alignment via zip (relevant but obscured)
vitals_stream = list(zip(temperature_readings, blood_pressure_systolic, oxygen_levels, heart_rate))

# Diagnostic engine
abnormalities = []
for temp, pressure, o2, hr in vitals_stream:
    episode_flags = []
    if temp >= critical_thresholds['fever']:
        episode_flags.append('fever')
    if pressure >= critical_thresholds['hypertension']:
        episode_flags.append('hypertension')
    if o2 < critical_thresholds['low_oxygen']:
        episode_flags.append('low_oxygen')
    if hr > critical_thresholds['tachycardia']:
        episode_flags.append('tachycardia')
    abnormalities.append(episode_flags)

# Generate flag counts (relevant)
flag_counts = [len(flags) for flags in abnormalities]

# Decoy statistical analysis (irrelevant)
from itertools import combinations
all_pairs = list(combinations([avg_temp, avg_pressure, composite_risk_score], 2))
correlation_hints = [abs(a - b) < 5 for a, b in all_pairs]

# Core diagnostic logic
health_indicators = [
    readings[0] >= 37.5 or readings[2] < 95 or readings[3] > 85
    for readings in vitals_stream
]

thresholds = [False, True, True, False, True, True, True]

# Critical processing function with lambda and itertools
process_metrics = lambda data, refs: sum([
    int(d ^ r) for d, r in itertools.zip_longest(data, refs, fillvalue=False)
]) * 2 - 5

# Final computation
final_diagnostic = process_metrics(health_indicators, thresholds)

# Output result as required
print(f"Target result: {final_diagnostic}")