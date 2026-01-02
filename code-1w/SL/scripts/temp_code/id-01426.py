import itertools

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.9, 25.3, 26.0, 24.8, 23.7]
humidity_readings = [56, 58, 61, 55, 52, 59, 60]
pressure_readings = [1013, 1015, 1012, 1016, 1018, 1014, 1011]

# Irrelevant auxiliary data (distractor)
sound_levels = [45, 47, 50, 44, 42, 48, 51]  # Not used in final calculation
light_intensity = [800, 820, 780, 850, 870, 830, 790]  # Dead end

# Weight configuration for data fusion (some weights are decoys)
weights = {
    'temp': 0.4,
    'humidity': 0.3,
    'pressure': 0.2,
    'vibration': 0.1  # Unused weight - red herring
}

# Historical baselines (partially relevant)
baseline_temp = 24.0
baseline_humidity = 57
baseline_pressure = 1014

# Distractor function - looks important but unused
def calculate_acoustic_index(levels):
    return sum(x ** 0.5 for x in levels) / len(levels)

# Auxiliary transformation (used indirectly)
def normalize_deviation(value, base):
    return round((value - base) / base * 100, 2)

# Core processing with lambda and itertools
shifted_pairs = list(itertools.pairwise(temperature_readings))  # Consecutive differences
rate_of_change = [b - a for a, b in shifted_pairs]  # Temporal gradient

# Misleading intermediate metric (not part of final result)
average_fluctuation = sum(abs(x) for x in rate_of_change) / len(rate_of_change)

# Real signal: detect sustained anomaly windows
temp_anomalies = [
    normalize_deviation(t, baseline_temp) for t in temperature_readings
]
humi_anomalies = [
    normalize_deviation(h, baseline_humidity) for h in humidity_readings
]

# Pressure anomalies with integer division twist
pres_anomalies = [
    (p - baseline_pressure) // 2 for p in pressure_readings  # Integer division effect
]

# Composite anomaly scoring using weighted combination
anomaly_vectors = zip(temp_anomalies, humi_anomalies, pres_anomalies)

# Key processing function with distractors inside
def process_metrics(anomalies, weight_map):
    composite_scores = []
    
    # Red herring initialization
    debug_trace = []
    temp_cache = []
    
    for i, (t, h, p) in enumerate(anomalies):
        # Seemingly complex transformation (only some matter)
        severity = 0
        severity += abs(t) * weight_map['temp']
        severity += abs(h) * weight_map['humidity']
        severity += abs(p) * weight_map['pressure']
        
        # Decoy logic path
        if i % 5 == 0:
            fake_correction = t * weight_map.get('vibration', 0)  # Uses dummy weight
            debug_trace.append(fake_correction)
        
        # Real contribution
        composite_scores.append(severity)
        
        # Useless caching
        temp_cache.append((i, severity * 0.1))  # Never accessed
    
    # Final aggregation: median of top quartile
    sorted_scores = sorted(composite_scores)
    quartile_index = len(sorted_scores) // 4
    top_quartile = sorted_scores[-quartile_index:]
    
    # Median of top quartile
    mid = len(top_quartile) // 2
    if len(top_quartile) % 2 == 0:
        final_magnitude = (top_quartile[mid-1] + top_quartile[mid]) / 2
    else:
        final_magnitude = top_quartile[mid]
    
    # Final scaling with rounding
    return round(final_magnitude * 100)  # Amplify for reporting

# Trigger computation
data = zip(temp_anomalies, humi_anomalies, pres_anomalies)
final_score = process_metrics(data, weights)

# Output result as required
print(f"Result: {final_score}")