import math

# Simulated sensor data from environmental monitoring stations
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.6, 23.9, 22.7]
humidity_readings = [45, 47, 50, 52, 58, 60, 55, 53, 51, 49]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015, 1014, 1013]

# Irrelevant backup arrays (distractor)
temp_backup = temperature_readings[:]
hum_backup = humidity_readings[:]
press_backup = pressure_readings[:]

# Misleading transformation - not used in final calculation
def corrupt_data(arr):
    return [x * 1.02 + 0.5 for x in arr]

corrupted_temps = corrupt_data(temperature_readings)  # Dead end

# Data segmentation and windowing
window_size = 3
divided_segments = []
for i in range(0, len(temperature_readings), window_size):
    segment = temperature_readings[i:i+window_size]
    if len(segment) == window_size:
        divided_segments.append(segment)

# Unused alternate grouping (red herring)
even_segments = [s for s in divided_segments if sum(s) % 2 == 0]
odd_segments = [s for s in divided_segments if sum(s) % 2 == 1]

# Signal processing: calculate moving RMS deviation
rms_values = []
baseline_avg = sum(temperature_readings) / len(temperature_readings)
for seg in divided_segments:
    squared_diffs = [(x - baseline_avg) ** 2 for x in seg]
    rms = math.sqrt(sum(squared_diffs) / len(squared_diffs))
    rms_values.append(rms)

# Bit manipulation mask based on humidity thresholds (distractor logic)
humidity_flags = 0
for h in humidity_readings:
    if h > 55:
        humidity_flags |= 1
    humidity_flags <<= 1
humidity_flags >>= 1  # Correct alignment after loop

# Pressure trend analysis - unused complex function (decoy)
def compute_pressure_gradient(data):
    gradients = []
    for i in range(1, len(data)):
        gradients.append(data[i] - data[i-1])
    return gradients

pressure_grads = compute_pressure_gradient(pressure_readings)  # Not used

# Primary processing path begins here
processed_segments = []
for idx, seg in enumerate(divided_segments):
    # Apply exponential smoothing
    smoothed = []
    alpha = 0.3
    smoothed.append(seg[0])
    for i in range(1, len(seg)):
        smoothed.append(alpha * seg[i] + (1 - alpha) * smoothed[i-1])
    processed_segments.append(smoothed)

# Secondary transformation: frequency domain approximation (distraction)
freq_peaks = []
for seg in processed_segments:
    peak = max(seg) - min(seg)
    freq_peaks.append(peak * 2 * math.pi)  # Simulated frequency magnitude

# Real computation begins: entropy-based stability metric
entropy_values = []
for seg in processed_segments:
    mean_seg = sum(seg) / len(seg)
    var = sum((x - mean_seg) ** 2 for x in seg) / len(seg)
    if var > 0:
        entropy = 0.5 * math.log(2 * math.pi * math.e * var)
    else:
        entropy = 0
    entropy_values.append(entropy)

# Auxiliary calculation with slicing (required Python feature)
recent_entropy = entropy_values[-2:]  # Last two segments
historical_entropy = entropy_values[:-2]

# Conditional adjustment based on entropy trend
adjustment_factor = 1.0
if len(recent_entropy) >= 2:
    if recent_entropy[0] < recent_entropy[1]:
        adjustment_factor = 1.2

# Final diagnostic computation
steady_count = sum(1 for e in entropy_values if e < 1.8)
fluctuation_score = sum(entropy_values) * adjustment_factor
stability_index = (steady_count / len(entropy_values)) * 100

# Critical statement
final_diagnostic = analyze_readings(processed_segments)

# Function definition placed AFTER usage (misleading)
def analyze_readings(segments):
    # This function computes a composite index based on segment variance
    total_weighted_var = 0
    total_length = 0
    
    for seg in segments:
        mean_val = sum(seg) / len(seg)
        variance = sum((x - mean_val) ** 2 for x in seg) / len(seg)
        weight = len(seg)
        total_weighted_var += variance * weight
        total_length += weight
    
    if total_length == 0:
        return 0
    
    avg_variance = total_weighted_var / total_length
    
    # Incorporate bit count from humidity flags as noise floor
    noise_floor = bin(humidity_flags).count('1')
    adjusted_diagnostic = (avg_variance * 50) - noise_floor
    
    # Additional distraction: unused rounding logic
    temp_rounded = [round(x) for x in temperature_readings]
    hum_rounded = [round(x/5)*5 for x in humidity_readings]
    
    return round(adjusted_diagnostic, 4)

# Print result as required
print(f"Target result: {final_diagnostic}")