import itertools

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.0, 23.2]
humidity_readings = [45, 47, 50, 44, 46, 48, 43, 51]
pressure_readings = [1013, 1015, 1012, 1010, 1014, 1016, 1009, 1011]

# Irrelevant backup readings (distractor)
backup_temp = [23.4, 24.2, 22.7, 25.1, 23.8, 24.5, 26.1, 23.1]
backup_humid = [46, 48, 49, 45, 47, 49, 42, 52]

# Preprocessing: Normalize sensor data using z-score
mean_temp = sum(temperature_readings) / len(temperature_readings)
std_temp = (sum((x - mean_temp) ** 2 for x in temperature_readings) / len(temperature_readings)) ** 0.5
normalized_temp = [(t - mean_temp) / std_temp for t in temperature_readings]

mean_humid = sum(humidity_readings) / len(humidity_readings)
normalized_humid = [(h - mean_humid) / 10 for h in humidity_readings]  # Simplified scaling

# Misleading transformation on pressure (not actually used later)
log_pressure = [round(2.302585 * (p - 1000), 4) for p in pressure_readings]  # log10(p-1000)*ln(10)
declining_trend = [log_pressure[i] > log_pressure[i+1] for i in range(len(log_pressure)-1)]
pressure_alerts = sum(declining_trend)

# Combine normalized data element-wise (only temp and humid used)
combined_readings = [[t, h] for t, h in zip(normalized_temp, normalized_humid)]

# Weight matrix for multi-factor index (real weights)
weights = [0.65, 0.35]  # Temperature weighted higher due to sensitivity

# Decoy weight sets (irrelevant)
alt_weights_v1 = [0.5, 0.5]
alt_weights_v2 = [0.7, 0.3]
dummy_weights = [0.1, 0.9]

# Auxiliary function that appears important but is never called
def calculate_air_quality_index(data):
    # Complex polynomial transform (dead code)
    aqi_components = []
    for entry in data:
        poly = 1.2 * entry[0]**2 - 0.8 * entry[1] + 0.05 * entry[0]*entry[1]
        aqi_components.append(max(poly, 0))
    return sum(aqi_components) / len(aqi_components)

# Another unused helper with bit manipulation red herring
def shift_diagnostic(code, level):
    if level < 0:
        return (code << abs(level)) & 0xFF
    else:
        return (code >> level) & 0xFF

# Real processing function
def process_metrics(metrics, w):
    scores = []
    for m in metrics:
        # Dot product simulation
        score = sum(m[i] * w[i] for i in range(len(w)))
        scores.append(round(score, 6))
    
    # Aggregate with outlier suppression
    sorted_scores = sorted(scores)
    trimmed = sorted_scores[1:-1] if len(sorted_scores) > 2 else sorted_scores
    
    # Hidden logic: only even-indexed original readings contribute
    indexed_contributions = [scores[i] for i in range(len(scores)) if i % 2 == 0]
    
    # Final integration uses the indexed contributions, not trimmed
    raw_final = sum(indexed_contributions) * 100
    
    # Additional distraction: unused correction factor
    season_factor = 1.07
    calibration_offset = -0.03
    
    return int(round(raw_final, 0))

# Data reshaping through itertools (partially relevant)
grouped_by_pair = list(itertools.zip_longest(*[iter(normalized_humid)]*2))
flat_pairs_sum = [sum(g) if g[1] is not None else g[0] for g in grouped_by_pair]

# Key execution point
final_score = process_metrics(combined_readings, weights)

# Irrelevant diagnostic print (commented out)
# print(f'Diagnostics: {shift_diagnostic(255, -3)}, Trends: {pressure_alerts}')

# Unused dictionary aggregations (red herring)
data_summary = {
    'max_normalized_temp': max(normalized_temp),
    'min_humidity': min(humidity_readings),
    'stable_pressures': sum(1 for p in itertools.pairwise(pressure_readings) if abs(p[0]-p[1]) <= 1),
    'readings_count': len(temperature_readings)
}

# Output result as required
print(f"Result: {final_score}")