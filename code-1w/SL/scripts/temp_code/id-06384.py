import itertools

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.0, 23.9, 24.4, 26.1]
humidity_readings = [45, 47, 50, 44, 48, 52, 46]
co2_levels = [410, 415, 420, 405, 430, 425, 418]

# Irrelevant auxiliary arrays (distractors)
pressure_readings = [1013, 1015, 1012, 1010, 1014, 1016, 1011]
solar_radiation = [800, 820, 780, 840, 810, 830, 790]
wind_speeds = [3.2, 3.5, 2.8, 4.1, 3.7, 3.0, 3.9]

# Misleading preprocessing steps
offset_correction = sum([abs(t - 24) for t in temperature_readings]) / len(temperature_readings)
normalized_co2 = [c - 400 for c in co2_levels]  # Scale to baseline

# Unused transformation function (dead code path)
def smooth_signal(signal):
    return [sum(signal[i:i+3])/3 if i+2 < len(signal) else signal[i] for i in range(len(signal))]

# Weight configuration for multi-sensor fusion
weights = {
    'temp': 0.4,
    'humidity': 0.3,
    'co2': 0.3
}

# Auxiliary lookup table with red herring values
index_map = dict(enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
reversed_indices = {v: k for k, v in index_map.items()}

# Complex data packaging using zip and enumerate (relevant + distractor mix)
data_packets = []
for idx, (t, h, c) in enumerate(zip(temperature_readings, humidity_readings, co2_levels)):
    packet = {
        'id': f'SENSOR-{idx+1}',
        'temp_c': t,
        'humidity_pct': h,
        'co2_ppm': c,
        'quality_flag': 'VALID' if t > 23 and h < 50 else 'CALIB',
        'timestamp': f'2023-07-01T{12+idx}:00:00Z'
    }
    data_packets.append(packet)

# Extract core values using list comprehensions and itertools.chain
flat_data = list(itertools.chain(*[
    [p['temp_c'], p['humidity_pct'], p['co2_ppm']] for p in data_packets
]))

data = [temperature_readings, humidity_readings, co2_levels]

# Decoy statistical analysis (irrelevant computations)
mean_temp = sum(temperature_readings) / len(temperature_readings)
median_humidity = sorted(humidity_readings)[len(humidity_readings)//2]
max_co2_spike = max(co2_levels) - min(co2_levels)

# Real processing begins here — complex weighted metric pipeline
def calculate_stability_index(values):
    mean_val = sum(values) / len(values)
    variance = sum((v - mean_val) ** 2 for v in values) / len(values)
    return 100 / (1 + variance)  # Higher stability = lower variance

def apply_weighted_transform(vals, weight):
    # Emphasize trend consistency using lambda-based smoothing
    pairwise_diffs = list(map(lambda x: abs(x[1] - x[0]), 
                              zip(vals[:-1], vals[1:])))
    avg_change = sum(pairwise_diffs) / len(pairwise_diffs) if pairwise_diffs else 0
    trend_score = 50 * (1 - min(avg_change / 10, 1))
    base_score = calculate_stability_index(vals)
    return weight * (0.7 * base_score + 0.3 * trend_score)

def process_metrics(sensor_arrays, importance_weights):
    # Unpack with meaningful names
    temps, humids, co2s = sensor_arrays
    
    # Secondary distraction: spurious correlation check
    correlated_pairs = 0
    for i in range(len(temps)):
        if temps[i] > 24 and humids[i] < 48 and co2s[i] > 415:
            correlated_pairs += 1  # Not actually used in final score
    
    # Key computation branches
    temp_contribution = apply_weighted_transform(temps, importance_weights['temp'])
    humid_contribution = apply_weighted_transform(humids, importance_weights['humidity'])
    co2_contribution = apply_weighted_transform(co2s, importance_weights['co2'])
    
    # Composite score with hidden offset
    raw_composite = temp_contribution + humid_contribution + co2_contribution
    
    # Final nonlinear calibration (critical step)
    calibration_factor = 1.0 + (0.05 * sum(1 for t in temps if t >= 25))
    final_score = raw_composite * calibration_factor
    
    # DEAD CODE: this would override but is never reached due to logic gate
    if False and len(temps) > 10:
        backup_weights = [0.5, 0.25, 0.25]
        fallback = sum(apply_weighted_transform(arr, w) for arr, w in 
                      zip(sensor_arrays, backup_weights))
        final_score = fallback  # unreachable
    
    return final_score

# Execute main processing
final_score = process_metrics(data, weights)

# Print result as required
Target result: {final_score}