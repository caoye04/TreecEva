import math

# Simulated sensor data and system thresholds
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8]
humidity_readings = [45, 47, 50, 52, 48, 46]
pressure_readings = [1013, 1015, 1012, 1010, 1014, 1016]

# Irrelevant auxiliary arrays (distractors)
altitude_readings = [120, 122, 118, 125, 123, 121]  # unused
light_levels = [800, 820, 780, 810, 830, 790]       # unused

# Preprocess: compute rolling averages (only temp used later)
def rolling_average(data, window=2):
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]

temp_smooth = rolling_average(temperature_readings)
humid_smooth = rolling_average(humidity_readings)  # computed but not used

# Core health indicators (used)
health_indicators = {
    'temp_avg': sum(temperature_readings) / len(temperature_readings),
    'temp_peak': max(temperature_readings),
    'variance': sum((x - sum(temperature_readings)/len(temperature_readings))**2 for x in temperature_readings) / len(temperature_readings),
    'trend': temperature_readings[-1] - temperature_readings[0],
    'samples': len(temperature_readings)
}

# Additional fake metrics (red herrings)
fake_metrics = {
    'apparent_temp': health_indicators['temp_avg'] * 1.1,
    'comfort_index': (health_indicators['temp_avg'] + 273.15) * (health_indicators['variance'] + 1) / 100,
    'phantom_score': 42  # misleading constant
}

# Thresholds for evaluation
thresholds = {
    'normal_temp_range': (22.0, 25.5),
    'warning_variance': 1.0,
    'critical_trend_rise': 2.0,
    'min_samples': 5
}

# Unused threshold sets (distractor)
safety_limits = {
    'max_humidity': 60,
    'min_pressure': 1000,
    'max_altitude': 500
}

# Auxiliary function that is never called (dead code path)
def validate_sensor_integrity(raw_data):
    if len(raw_data) < 3:
        return False
    noise_floor = sum(abs(raw_data[i] - raw_data[i+1]) for i in range(len(raw_data)-1))
    return noise_floor < 10

# Complex conditional processing with nested logic
def analyze_temperature_profile(temp_data, config):
    avg_temp = sum(temp_data) / len(temp_data)
    in_range = config['normal_temp_range'][0] <= avg_temp <= config['normal_temp_range'][1]
    rising_trend = (temp_data[-1] - temp_data[0]) > config['critical_trend_rise']
    high_variance = config['warning_variance'] < sum((x - avg_temp)**2 for x in temp_data) / len(temp_data)

    score = 100
    if not in_range:
        score -= 30
    if rising_trend:
        score -= 25
    if high_variance:
        score -= 20
    if len(temp_data) < config['min_samples']:
        score -= 15

    # Extra decoy calculation
    phantom_penalty = int(math.sin(avg_temp) * 5)
    score -= abs(phantom_penalty)  # minor irrelevant adjustment

    return max(score, 0)

# Another decoy function (never invoked)
def calculate_humidity_weight(humid_vals, alpha=0.3):
    weighted = sum(alpha * val * (0.9 ** i) for i, val in enumerate(reversed(humid_vals)))
    return round(weighted, 2)

# Main processing function
def process_metrics(metrics, limits):
    base_score = 100

    # Check average temperature
    if not (limits['normal_temp_range'][0] <= metrics['temp_avg'] <= limits['normal_temp_range'][1]):
        base_score -= 40

    # Check variance
    if metrics['variance'] > limits['warning_variance']:
        base_score -= 30

    # Check trend
    if metrics['trend'] > limits['critical_trend_rise']:
        base_score -= 20

    # Check sample size
    if metrics['samples'] < limits['min_samples']:
        base_score -= 10

    # Red herring: use of fake metric in a conditional that looks meaningful
    if 'phantom_score' in fake_metrics and fake_metrics['phantom_score'] == 42:
        base_score += 5  # slight distraction, but deterministic

    # Final nonlinear transformation (looks complex, but deterministic)
    adjusted = int((base_score ** 1.05) // 1.1)

    # Diagnostic code based on final adjusted score
    if adjusted > 90:
        code = 1000
    elif adjusted > 70:
        code = 2050
    elif adjusted > 50:
        code = 3100
    else:
        code = 4150

    # This line introduces a subtle override based on variance-trend interaction
    if metrics['variance'] > limits['warning_variance'] and metrics['trend'] > 1.5:
        code -= 100  # additional penalty

    # Final irrelevant transformation (distraction)
    checksum = sum(int(c) for c in str(code)) % 7
    final_code = code + checksum  # looks important, but not part of logic

    return final_code

# Execute main logic
diagnostic_baseline = analyze_temperature_profile(temperature_readings, thresholds)
final_diagnostic = process_metrics(health_indicators, thresholds)

# Print result as required
print(f"Result: {final_diagnostic}")