import math

# Simulated sensor metrics from a distributed system
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
humidity_readings = [45, 47, 50, 44, 46]
pressure_readings = [1013, 1012, 1015, 1011, 1014]

# Irrelevant auxiliary data (distractor)
legacy_system_flags = [0x1A, 0x2C, 0x3E, 0x0F]
unused_buffer = list(map(lambda x: (x << 2) ^ 0xFF, legacy_system_flags))

# Derived health indicators (some relevant, some not)
avg_temp = sum(temperature_readings) / len(temperature_readings)
avg_humidity = sum(humidity_readings) / len(humidity_readings))
variance_pressure = sum((p - sum(pressure_readings)/len(pressure_readings))**2 for p in pressure_readings) / len(pressure_readings)

# Noise threshold calculation (dead path - never used)
effective_range = max(pressure_readings) - min(pressure_readings)
noise_floor = math.log(effective_range + 1, 2) if effective_range > 0 else 0

# System state classification (mixed relevance)
def classify_stability(temp, humidity):
    if temp < 23 or temp > 25:
        return 1
    elif humidity < 40 or humidity > 55:
        return 2
    else:
        return 0

# Misleading intermediate scores (red herring)
raw_stability = [classify_stability(t, h) for t, h in zip(temperature_readings, humidity_readings)]
baseline_risk_score = sum(raw_stability) * 0.75

# Core metric computation (relevant)
normalized_temp = abs(avg_temp - 23.5) * -1.5
normalized_variance = (1 - min(1, variance_pressure / 2.0)) * 10

def calculate_response_time_factor(readings):
    diffs = [abs(readings[i+1] - readings[i]) for i in range(len(readings)-1)]
    return 10 - sum(diffs) * 0.5

response_factor = calculate_response_time_factor(temperature_readings)

# Decoy function with unused logic
def deprecated_normalization(data, factor=0.9):
    return [x * factor for x in sorted(data, reverse=True)]

# Weighted metrics framework
metrics = {
    'thermal': normalized_temp,
    'stability': normalized_variance,
    'responsiveness': response_factor,
    'legacy_compatibility': 5.0,  # Hardcoded placeholder (distractor)
    'data_integrity': 7.2        # Fake metric (irrelevant)
}

# Actual weights (only some affect final result)
weights = {
    'thermal': 0.3,
    'stability': 0.4,
    'responsiveness': 0.3,
    'legacy_compatibility': 0.0,  # Zero weight - irrelevant
    'data_integrity': 0.0        # Zero weight - irrelevant
}

# Aggregation function with conditional expression and list comprehension
def aggregate_performance(mets, wts):
    valid_keys = [k for k in mets.keys() if wts.get(k, 0) > 0]
    if not valid_keys:
        return 0.0
    weighted_sum = sum(mets[k] * wts[k] for k in valid_keys)
    total_weight = sum(wts[k] for k in valid_keys)
    return round(weighted_sum / total_weight, 6) if total_weight > 0 else 0.0

# Critical execution point
final_score = aggregate_performance(metrics, weights)

# Spurious post-processing (dead code path)
adjusted_final = final_score * 1.05 if baseline_risk_score < 2 else final_score * 0.95
flagged_anomalies = [i for i, s in enumerate(raw_stability) if s > 0]

# Output the target result
print(f"Result: {final_score}")