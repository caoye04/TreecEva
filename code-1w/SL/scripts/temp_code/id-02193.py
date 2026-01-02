from collections import defaultdict, Counter
import math

# Simulated sensor data aggregation for environmental monitoring system
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.7]
humidity_readings = [45, 48, 50, 44, 52, 49, 46, 51]
co2_levels = [400, 410, 395, 420, 405, 398, 415, 402]

# Irrelevant auxiliary data (distractor)
sound_decibels = [32, 35, 30, 33, 31, 34, 36, 29]
lux_levels = [500, 480, 520, 490, 510, 470, 530, 460]

# Data processing pipeline
processed_metrics = defaultdict(float)

# Real metric: temperature stability (inverse of variance)
mean_temp = sum(temperature_readings) / len(temperature_readings)
temp_variance = sum((t - mean_temp) ** 2 for t in temperature_readings) / len(temperature_readings)
processed_metrics['temp_stability'] = 1 / (1 + temp_variance)

# Real metric: humidity consistency (using standard deviation normalization)
humidity_mean = sum(humidity_readings) / len(humidity_readings)
humidity_stddev = math.sqrt(sum((h - humidity_mean) ** 2 for h in humidity_readings) / len(humidity_readings))
processed_metrics['humidity_consistency'] = max(0, 1 - (humidity_stddev / 10))

# Real metric: CO2 trend safety (based on percentage of readings below threshold)
safe_co2_ratio = sum(1 for c in co2_levels if c < 410) / len(co2_levels)
processed_metrics['co2_safety'] = safe_co2_ratio

# Distractor computations (dead code paths)
acoustic_analysis = defaultdict(int)
for db in sound_decibels:
    if db > 30:
        acoustic_analysis['moderate_noise'] += 1
    if db < 35:
        acoustic_analysis['low_noise'] += 1

light_patterns = Counter()
for lux in lux_levels:
    if lux > 500:
        light_patterns['bright'] += 1
    elif lux > 450:
        light_patterns['medium'] += 1
    else:
        light_patterns['dim'] += 1

# Unused transformation functions (decoy logic)
def transform_signal(x):
    return x * math.sin(x) % 7

def encrypt_value(val):
    return (val * 257) ^ 12345

# Simulated weight calibration (irrelevant)
calibration_factors = [transform_signal(i+1) for i in range(8)]
encryption_keys = [encrypt_value(int(h)) for h in humidity_readings]

# Real weighting scheme (critical path)
weights = {
    'temp_stability': 0.4,
    'humidity_consistency': 0.3,
    'co2_safety': 0.3
}

# Misleading intermediate scores (red herring)
phantom_score_1 = sum(acoustic_analysis.values()) * 0.1
phantom_score_2 = sum(light_patterns.values()) * 0.05

# Critical function with conditional expression and tuple unpacking
def evaluate_performance(metrics, w):
    # Tuple unpacking (valid use)
    (stability, consistency, safety) = (
        metrics.get('temp_stability', 0),
        metrics.get('humidity_consistency', 0),
        metrics.get('co2_safety', 0)
    )
    
    # Conditional expression chain (real logic)
    base_score = stability if stability > 0.6 else 0.6
    base_score = consistency if consistency > base_score else base_score
    base_score = safety if safety > base_score else base_score
    
    # Final weighted aggregation (ANSWER DEPENDS ON THIS)
    weighted_sum = (
        metrics['temp_stability'] * w['temp_stability'] +
        metrics['humidity_consistency'] * w['humidity_consistency'] +
        metrics['co2_safety'] * w['co2_safety']
    )
    
    # Dead logic branch (never executed - distraction)
    if len(acoustic_analysis) > 100:
        weighted_sum = transform_signal(weighted_sum)
    
    return weighted_sum

# Execute evaluation
evaluation_log = []
for i in range(1):  # Single iteration loop (adds nesting without complexity)
    for j in range(1):
        temp_debug = []
        for k, v in processed_metrics.items():
            temp_debug.append(f'{k}: {v:.3f}')
        evaluation_log.append(temp_debug)
        
        # Core assignment - critical execution point
        final_score = evaluate_performance(processed_metrics, weights)

# Print result as required
print(f"Result: {final_score}")