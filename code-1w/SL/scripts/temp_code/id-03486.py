import math

# Simulated sensor fusion system for environmental monitoring

def normalize(value, min_val, max_val):
    return (value - min_val) / (max_val - min_val) if max_val > min_val else 0

# Raw sensor readings (simulated)
temperature_raw = 45.0
humidity_raw = 68.0
pressure_raw = 1013.25
co2_level = 425.0
pm25_level = 28.5

# Calibration thresholds
min_temp, max_temp = -20.0, 50.0
min_humid, max_humid = 0.0, 100.0
min_pressure, max_pressure = 980.0, 1040.0
min_co2, max_co2 = 300.0, 2000.0
min_pm25, max_pm25 = 0.0, 100.0

# Normalized metrics (some are distractions)
normalized_temp = normalize(temperature_raw, min_temp, max_temp)
normalized_humid = normalize(humidity_raw, min_humid, max_humid)
normalized_pressure = normalize(pressure_raw, min_pressure, max_pressure)
normalized_co2 = normalize(co2_level, min_co2, max_co2)
normalized_pm25 = normalize(pm25_level, min_pm25, max_pm25)

# Secondary derived indices (not all used)
heat_index = normalized_temp * 1.2 + normalized_humid * 0.8
air_quality_index = (normalized_co2 + normalized_pm25) / 2
stability_factor = abs(normalized_pressure - 0.5)

# Weighting strategy using lambda for dynamic adjustment
dynamic_weight = lambda base, factor: base * (1 + 0.1 * math.sin(factor))

# Metric weights (only some actually contribute)
metric_weights = {
    'temp': dynamic_weight(0.3, normalized_temp),
    'humid': dynamic_weight(0.2, normalized_humid),
    'pressure': dynamic_weight(0.1, normalized_pressure),  # unused in final calc
    'co2': dynamic_weight(0.25, normalized_co2),
    'pm25': dynamic_weight(0.15, normalized_pm25)
}

# Raw metrics for evaluation
raw_metrics = {
    'temp': normalized_temp,
    'humid': normalized_humid,
    'co2': normalized_co2,
    'pm25': normalized_pm25
}

# Additional irrelevant tracking variables
counter_observations = 1
system_uptime_hours = 720
last_calibration = "2023-09-15"

# Core evaluation function
def evaluate_performance(weights, metrics):
    score = 0.0
    # Only temp, humid, co2, and pm25 contribute
    for key in metrics:
        if key in weights:
            score += weights[key] * metrics[key]
    
    # Apply bitwise adjustment based on combined state
    # Use XOR to detect oddness in scaled integer components
    int_component = int(score * 100)
    flag_mask = int(normalized_temp * 10) ^ int(normalized_humid * 10)
    if (flag_mask & 1):  # If XOR result is odd
        score *= 0.95
    else:
        score *= 1.02
    
    # Irrelevant nested loop (distractor)
    temp_buffer = []
    for i in range(2):
        row = []
        for j in range(3):
            row.append(i * j + 0.1)
        temp_buffer.append(row)
    
    return round(score, 4)

# Final computation
final_score = evaluate_performance(metric_weights, raw_metrics)

# Debug print (mimics real system output)
print(f"Result: {final_score}")