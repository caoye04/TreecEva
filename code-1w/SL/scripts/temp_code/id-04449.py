import math

# Simulate atmospheric pressure transformation in a layered environmental model
def compute_layered_pressure(altitude, temperature, humidity):
    base_pressure = 101.325
    lapse_rate = 0.0065
    pressure_drop = base_pressure * math.exp(-lapse_rate * altitude / (temperature + 273.15))
    humidity_correction = 1 + (humidity * 0.003)
    return pressure_drop * humidity_correction

# Analyze spectral frequency shifts due to thermal drift (red herring function)
def calculate_doppler_shift(frequency, velocity, medium_speed=343):
    shifted = frequency * (1 + velocity / medium_speed)
    normalized_shift = shifted % 100
    return normalized_shift

# Irrelevant signal processing for noise filtering
def apply_kalman_filter(signal_data, process_noise=0.01, measurement_noise=0.03):
    estimate = 0.0
    error_estimate = 1.0
    filtered = []
    for z in signal_data:
        kalman_gain = error_estimate / (error_estimate + measurement_noise)
        estimate = estimate + kalman_gain * (z - estimate)
        error_estimate = (1 - kalman_gain) * error_estimate + process_noise
        filtered.append(estimate)
    return filtered

# Main data set: sensor readings from drone flight at different altitudes
altitudes = [120, 250, 380, 500, 620]
temperatures = [22, 18, 15, 10, 6]
humidities = [0.45, 0.52, 0.61, 0.73, 0.82]
frequencies = [440, 880, 1760, 3520]  # Unused in final computation

# Process each layer's pressure with enumerate and zip (required python features)
pressure_readings = []
for i, (alt, temp, hum) in enumerate(zip(altitudes, temperatures, humidities)):
    p = compute_layered_pressure(alt, temp, hum)
    if i % 2 == 0:
        p *= 1.02  # minor calibration for even-indexed layers
    pressure_readings.append(p)

# Distractor: Doppler analysis on irrelevant frequencies
doppler_results = []
for freq in frequencies:
    shift_val = calculate_doppler_shift(freq, velocity=25)
    if shift_val > 50:
        doppler_results.append(shift_val * 0.75)

# Secondary transformation: extract critical pressure band using slicing
working_slice = pressure_readings[1:4]  # middle three layers only
smoothed_slice = [p * 0.98 for p in working_slice]

# Compute derived metrics (some are decoys)
avg_smoothed = sum(smoothed_slice) / len(smoothed_slice)
max_pressure = max(pressure_readings)
min_pressure = min(pressure_readings)
pressure_range = max_pressure - min_pressure  # unused

# Hidden logic path: equilibrium determined by geometric mean of smoothed slice
cumulative_product = 1.0
for val in smoothed_slice:
    cumulative_product *= val
geometric_mean = cumulative_product ** (1 / len(smoothed_slice))

# Adjustment factor based on temperature gradient (decoy calculation below)
temp_gradient = []
for j in range(1, len(temperatures)):
    temp_gradient.append(temperatures[j] - temperatures[j-1])
steepness_index = sum(abs(g) for g in temp_gradient)  # looks important but unused

# Real adjustment uses only the number of valid high-humidity layers
high_humidity_count = sum(1 for h in humidities if h > 0.6)
adjustment_factor = 1 + (high_humidity_count * 0.05)

# Critical execution point
final_pressure = geometric_mean
equilibrium_score = final_pressure * adjustment_factor

# Dead code path: entropy calculation never used
if equilibrium_score > 100:
    entropy = 0
    for p in pressure_readings:
        if p > 0:
            entropy -= (p / 1000) * math.log(p / 1000)

# Another red herring: attempt to correlate with doppler (never executed)
doppler_pressure_correlation = 0
dummy_weights = [0.1, 0.2, 0.15, 0.3]

# Output the target result
Result: {equilibrium_score}