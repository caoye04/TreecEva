def analyze_component(reading, threshold=50):
    return reading * 1.2 if reading > threshold else reading * 0.8

# Simulated sensor readings from different system components
temperature_readings = [45, 67, 89, 34]
pressure_readings = [55, 62, 47, 70]
humidity_readings = [30, 85, 60, 40]

# Process each component with conditional scaling
temp_scaled = [analyze_component(x) for x in temperature_readings]
pressure_scaled = [analyze_component(x, 55) for x in pressure_readings]
humidity_scaled = [analyze_component(x) for x in humidity_readings]

# Irrelevant transformation: frequency analysis (dead-end computation)
frequency_weights = [0.1, 0.3, 0.2, 0.4]
weighted_freq = sum(f * w for f, w in zip([220, 440, 880, 1760], frequency_weights))  # unused later

# Extract peak and baseline values (some used, some not)
peak_temp = max(temp_scaled)
baseline_temp = min(temp_scaled)

peak_pressure = max(pressure_scaled)  # unused
average_humidity = sum(humidity_scaled) / len(humidity_scaled)

# System health metrics derived from scaled sensor data
metric_a = sum(temp_scaled) / 100.0  # normalized total temperature response
metric_b = (max(humidity_scaled) - average_humidity) * 1.5
metric_c = (sum(pressure_scaled) + peak_temp) // 10  # combined pressure and thermal load

# Dummy metrics for distraction
metric_x = (baseline_temp + 100) * 0.5  # irrelevant
metric_y = len(pressure_readings) ** 2  # red herring

# Weight coefficients for performance aggregation
weights = [0.4, 0.35, 0.25]  # metric_a, metric_b, metric_c respectively

# Unused alternate weighting scheme
alt_weights = [0.2, 0.5, 0.3]  # decoy

# Core function to compute final system score
def aggregate_performance(metrics, coeffs):
    temp_metric = metrics[0] * coeffs[0]
    humid_metric = metrics[1] * coeffs[1]
    pressure_metric = metrics[2] * coeffs[2]
    
    # Conditional adjustment based on interaction effect
    adjustment = 1.1 if metrics[0] > 30 and metrics[1] < 50 else 0.9
    
    raw_sum = temp_metric + humid_metric + pressure_metric
    return raw_sum * adjustment

# Compile relevant metrics into list
metrics = [metric_a, metric_b, metric_c]

# Dead code path: simulation override (never executed)
if False:
    metrics = [m * 0.1 for m in metrics]
    weights = alt_weights

# Critical execution point
final_score = aggregate_performance(metrics, weights)

# Additional misleading calculation
phantom_score = (metric_x + metric_y) * 0.75  # never used

# Print result as required
print(f"Result: {final_score}")