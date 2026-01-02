def preprocess_sensors(raw_readings):
    calibrated = []
    offset = 0.023
    for idx, val in enumerate(raw_readings):
        corrected = val * 0.987 + offset
        if idx % 3 == 0:
            corrected += 0.005
        calibrated.append(round(corrected, 6))
    return calibrated


def validate_stability(readings):
    variance = sum((x - sum(readings)/len(readings))**2 for x in readings) / len(readings)
    return variance < 0.05


def filter_outliers(data, threshold=2.5):
    mean_val = sum(data) / len(data)
    stdev = (sum((x - mean_val)**2 for x in data) / len(data)) ** 0.5
    filtered = [x for x in data if abs(x - mean_val) <= threshold * stdev]
    return filtered


def accumulate_segments(values):
    accumulation = [0]
    for v in values:
        accumulation.append(accumulation[-1] + v * 0.1)
    return accumulation


def calculate_gradient(elevations, temps):
    # Real logic starts here
    paired = list(zip(elevations, temps))
    slope_components = []
    
    temp_sum = sum(temps)
    elev_sum = sum(elevations)
    temp_elev_product = sum(e * t for e, t in paired)
    elev_squared = sum(e*e for e in elevations)
    n = len(paired)
    
    # Linear regression: gradient = (n*Σxy - ΣxΣy) / (n*Σx² - (Σx)²)
    numerator = n * temp_elev_product - elev_sum * temp_sum
    denominator = n * elev_squared - elev_sum ** 2
    
    if denominator == 0:
        return 0.0
    
    gradient = numerator / denominator
    
    # Irrelevant transformation (distraction)
    normalized = [abs(t - gradient) for t in temps]
    sorted_norm = sorted(normalized, reverse=True)
    mid_vals = sorted_norm[1:-1] if len(sorted_norm) > 2 else sorted_norm
    avg_mid = sum(mid_vals) / len(mid_vals) if mid_vals else 0
    
    # More distractions
    checksum = 0
    for i, v in enumerate(mid_vals):
        checksum ^= int(v * 1000) % 256
    
    # Decoy function call (no effect)
    _ = accumulate_segments([avg_mid] * 5)
    
    # Final result is based only on gradient
    return round(gradient * 1000, 6)  # Scale up for precision

# Simulated sensor input (irrelevant naming to distract)
altitude_readings = [300, 600, 900, 1200, 1500, 1800, 2100]
temp_readings_raw = [24.2, 21.5, 18.8, 16.0, 13.3, 10.5, 7.8]

# Irrelevant preprocessing chain
raw_calibrated = preprocess_sensors(temp_readings_raw)
if validate_stability(raw_calibrated):
    stable_temps = raw_calibrated
else:
    stable_temps = temp_readings_raw

# Filtering that doesn't change outcome due to low variance
filtered_temps = filter_outliers(stable_temps, threshold=3.0)

# Mismatched length handling (distraction - not triggered)
if len(filtered_temps) != len(altitude_readings):
    padded_temps = filtered_temps + [filtered_temps[-1]] * (len(altitude_readings) - len(filtered_temps))
else:
    padded_temps = filtered_temps

# Actual computation
thermal_gradient = calculate_gradient(altitude_readings, padded_temps)

# Dead code paths
final_checksum = 0
for i in range(len(padded_temps)):
    if i % 2 == 0:
        final_checksum += int(padded_temps[i])
    else:
        final_checksum -= int(padded_temps[i])

# Unused derived variables
summary_stats = {
    'range': max(padded_temps) - min(padded_temps),
    'median': sorted(padded_temps)[len(padded_temps)//2],
    'mode': max(set(padded_temps), key=padded_temps.count)
}

# Output target result
print(f"Result: {thermal_gradient}")