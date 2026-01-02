import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 25.3, 22.7, 26.0, 25.8, 24.5, 23.9, 26.2, 27.1, 25.0]
humidity_readings = [45, 47, 50, 52, 49, 54, 58, 51, 48, 60, 53]
pressure_readings = [1013, 1012, 1015, 1010, 1008, 1014, 1016, 1009, 1007, 1018, 1011]

# Irrelevant calibration coefficients (distractor)
calibration_a = 0.987
adjustment_factor = 1.023
normalization_constant = 0.005
offset_matrix = [[1.1, 0.9], [1.05, 0.95]]

# Data preprocessing with slicing and filtering
recent_temps = temperature_readings[-7:]  # Last 7 temperature readings
smoothed_temps = []
for i in range(len(recent_temps)):
    window = recent_temps[max(0, i-2):i+1]
    smoothed_temps.append(sum(window) / len(window))

# Misleading secondary processing path (dead code path)
def deprecated_analysis(data):
    return sum(x ** 0.5 for x in data if x > 24) * 0.75

# Unused transformation (distractor)
transformed_humidity = [h * 1.05 - 3 for h in humidity_readings]
avg_transformed = sum(transformed_humidity) / len(transformed_humidity)

# Real-time anomaly detection thresholds (dictionary usage)
threshold_map = {
    'temp_high': 26.0,
    'temp_low': 24.0,
    'humidity_critical': 55,
    'pressure_trend': -5
}

# Historical baseline (irrelevant data)
historical_avg_temp = 24.8
historical_seasonal_adjustment = 1.2
baseline_deviations = [abs(t - historical_avg_temp) for t in temperature_readings]

# Process pressure trends with bit manipulation (bitwise distraction)
pressure_deltas = [pressure_readings[i] - pressure_readings[i-1] for i in range(1, len(pressure_readings))]
encoded_trends = []
for delta in pressure_deltas:
    encoded = (abs(delta) << 2) ^ 0x0F  # Bit shift and XOR (mostly irrelevant)
    encoded_trends.append(encoded)

# Actual signal extraction (key logic buried)
valid_temp_range = [t for t in smoothed_temps if threshold_map['temp_low'] <= t <= threshold_map['temp_high']]
outlier_count = len(smoothed_temps) - len(valid_temp_range)

# Conditional accumulation based on multiple criteria
alert_level = 0
if len(valid_temp_range) < 5:
    alert_level += 3
if outlier_count > 2:
    alert_level += 2
if pressure_deltas[-3:].count(0) == 0 and pressure_readings[-1] > pressure_readings[0]:
    alert_level += 1

# Decoy function that's never called (red herring)
def compute_stability_index(seq, weight=0.8):
    stability = 0
    for i in range(1, len(seq)):
        stability += weight * abs(seq[i] - seq[i-1])
    return 100 - stability

# Core analysis function with dictionary and slicing
def analyze_readings(temp_data, limits):
    high_temp_events = [t for t in temp_data if t > limits['temp_high']]
    stable_period = temp_data[1:-1]  # Exclude first and last (slicing)
    drift = temp_data[-1] - temp_data[0]
    
    # Secondary metrics (some irrelevant)
    variance_proxy = sum((x - sum(temp_data)/len(temp_data))**2 for x in temp_data) / len(temp_data)
    trend_consistency = 0
    for i in range(1, len(temp_data)):
        if (temp_data[i] - temp_data[i-1]) > 0:
            trend_consistency += 1
    
    # Final diagnostic calculation (actual answer source)
    diagnostic_score = len(high_temp_events) * 100
    diagnostic_score -= outlier_count * 15
    diagnostic_score += alert_level * 25
    
    # This line determines the final answer
    return int(diagnostic_score)

# Additional red herring: unused statistical analysis
mean_pressure = sum(pressure_readings) / len(pressure_readings)
pressure_variance = sum((p - mean_pressure) ** 2 for p in pressure_readings)
theoretical_max = math.log(mean_pressure) * 10

# Main processing pipeline
processed_data = smoothed_temps.copy()

# Critical execution point
final_diagnostic = analyze_readings(processed_data, threshold_map)

# Output result
print(f"Result: {final_diagnostic}")