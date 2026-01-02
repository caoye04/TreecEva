import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_streams = {
        'temp': [23.5, 24.1, 22.7, 25.3, 26.0, 23.9, 24.4],
        'humidity': [45, 47, 50, 44, 60, 55, 48],
        'co2': [400, 410, 395, 420, 430, 415, 405],
        'pressure': [1013, 1015, 1012, 1018, 1020, 1017, 1014]
    }
    return raw_streams

# Irrelevant preprocessing: spectrogram analysis (dead path)
def compute_spectrogram(signal):
    n = len(signal)
    spec = [0] * n
    for i in range(n):
        for j in range(n):
            spec[i] += signal[j] * math.sin(2 * math.pi * i * j / n)
    return [x / n for x in spec]

# Real processing: filter anomalies based on dynamic thresholds
def filter_anomalies(stream, baseline):
    cleaned = []
    for val in stream:
        deviation = abs(val - baseline)
        tolerance = baseline * 0.1
        if deviation <= tolerance:
            cleaned.append(val)
    return cleaned

# Distractor function: entropy calculation (unused later)
def shannon_entropy(values):
    total = sum(values)
    probabilities = [v / total for v in values if v > 0]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return round(entropy, 4)

# Core analysis engine
def analyze_readings(data, thresholds):
    results = {}
    
    # Compute rolling stats (distractor block)
    temp_run = [data['temp'][i:i+3] for i in range(len(data['temp'])-2)]
    avg_temps = [sum(window)/3 for window in temp_run]
    fluctuation = max(avg_temps) - min(avg_temps)
    
    # Real logic begins: assess each parameter
    normal_ranges = {
        'temp': (22.0, 26.0),
        'humidity': (40, 60),
        'co2': (390, 450),
        'pressure': (1010, 1025)
    }
    
    status_flags = []
    for param, readings in data.items():
        low_th, high_th = thresholds[param]
        critical_count = 0
        for r in readings:
            if r < low_th or r > high_th:
                critical_count += 1
        status_flags.append(critical_count)
    
    # Secondary evaluation using set operations
    alert_set_a = {i for i, x in enumerate(status_flags) if x >= 2}
    alert_set_b = {1, 3}  # fixed pattern
    cross_alerts = alert_set_a & alert_set_b
    
    # Tertiary processing with dictionary transforms
    flag_weights = {'temp': 1.2, 'humidity': 0.8, 'co2': 1.5, 'pressure': 0.5}
    weighted_score = 0
    for idx, param in enumerate(data.keys()):
        weighted_score += status_flags[idx] * flag_weights[param]
    
    # Final diagnostic with slicing influence
    history_buffer = [weighted_score * (0.9 ** i) for i in range(10)]
    recent_trend = history_buffer[::2]  # every other reading
    base_diagnostic = sum(recent_trend[:4])
    
    # Key red herring: complex but unused transformation
    transformed = []
    for x in history_buffer:
        try:
            transformed.append(math.tanh(math.log(abs(x) + 1e-5)) * 100)
        except:
            transformed.append(0)
    final_normalization = math.sqrt(sum([x*x for x in transformed[:3]]))
    
    # ACTUAL answer computation (non-obvious due to distractions)
    primary_causes = len(alert_set_a)
    secondary_effects = len(cross_alerts)
    final_diagnostic = int(base_diagnostic * 10 + primary_causes * 5 - secondary_effects * 3)
    
    return final_diagnostic

# Main execution flow
sensor_data = collect_sensor_data()

# Distractor: unused entropy analysis
humidity_entropy = shannon_entropy(sensor_data['humidity'])
co2_entropy = shannon_entropy(sensor_data['co2'])

# Threshold calibration (real use)
threshold_map = {
    'temp': (21.5, 26.5),
    'humidity': (38, 62),
    'co2': (380, 460),
    'pressure': (1008, 1028)
}

# Data filtering chain
filtered_data = {}
for key, readings in sensor_data.items():
    if key == 'temp':
        filtered_data[key] = filter_anomalies(readings, 24.0)
    elif key == 'humidity':
        filtered_data[key] = filter_anomalies(readings, 48.0)
    else:
        filtered_data[key] = readings  # no filtering for others

# Critical statement
final_diagnostic = analyze_readings(filtered_data, threshold_map)

# Print result
print(f"Result: {final_diagnostic}")