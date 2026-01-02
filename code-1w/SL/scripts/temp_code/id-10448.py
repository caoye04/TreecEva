import itertools

# Simulated sensor array data from environmental monitoring system
def fetch_sensor_data():
    base_values = [12, 15, 22, 18, 30, 25, 40]
    noise_offsets = [0.7, -1.2, 0.5, 0.3, -0.8, 1.1, -0.4]
    return [base_values[i] + noise_offsets[i] for i in range(len(base_values))]

# Legacy calibration function (partially deprecated)
def calibrate_legacy(signal, factor=1.03):
    return [x * factor for x in signal]

# Advanced signal processor with harmonic filtering
def filter_harmonics(signal_sequence):
    filtered = []
    for i, val in enumerate(signal_sequence):
        if i % 2 == 0:
            filtered.append(val * 0.95)
        else:
            filtered.append(val * 1.05)
    return filtered

# Signal normalizer using z-score (not used in final path)
def normalize_zscore(data):
    mean_val = sum(data) / len(data)
    std_dev = (sum((x - mean_val) ** 2 for x in data) / len(data)) ** 0.5
    return [(x - mean_val) / std_dev for x in data]

# Irrelevant auxiliary computation: atmospheric pressure estimate (red herring)
def estimate_pressure_elevation(elevation):
    pressure = 101.3 * (1 - elevation / 44330) ** 5.255
    adjustment = 0
    for step in range(5):
        adjustment += (elevation % 10) * 0.1
        elevation //= 2
    return pressure + adjustment

# Unused recursive checksum (decoy function)
def recursive_checksum(values, depth=0):
    if depth >= 3 or len(values) == 1:
        return values[0] % 7
    split = len(values) // 2
    left = recursive_checksum(values[:split], depth + 1)
    right = recursive_checksum(values[split:], depth + 1)
    return (left + right) * 2 % 9

# Core transformation pipeline
sensor_readings = fetch_sensor_data()
adjusted_readings = calibrate_legacy(sensor_readings, factor=1.03)
refined_signal = filter_harmonics(adjusted_readings)

# Generate synthetic secondary channels (distractor)
synthetic_channels = []
for phase in [0.5, 1.0, 1.5]:
    channel = [refined_signal[i] * (i + phase) / 4 for i in range(len(refined_signal))]
    synthetic_channels.append(channel)

# Apply windowing function to refined signal (actual preprocessing)
def apply_window(signal):
    n = len(signal)
    windowed = [
        signal[i] * (0.54 - 0.46 * __import__('math').cos(2 * __import__('math').pi * i / (n - 1)))
        for i in range(n)
    ]
    return windowed

processed_signals = apply_window(refined_signal)

# Secondary unused transformation path (dead code branch)
temp_buffers = []
for idx, ch in enumerate(synthetic_channels):
    temp_buf = [x * idx for x in ch]
    temp_buffers.append(temp_buf)

# Diagnostic analyzer that computes final result
def analyze_readings(cleaned_data):
    # Compute moving average of squared deviations
    baseline = sum(cleaned_data) / len(cleaned_data)
    squared_devs = [(x - baseline) ** 2 for x in cleaned_data]
    
    # Use itertools to generate overlapping triplets (key operation)
    triplet_averages = [
        sum(triplet) / 3 for triplet in itertools.zip_longest(
            squared_devs, 
            squared_devs[1:], 
            squared_devs[2:],
            fillvalue=0
        )
    ]
    
    # Misleading intermediate calculation (looks important but unused)
    entropy_approx = 0
    for x in triplet_averages:
        if x > 0:
            entropy_approx += x * __import__('math').log(x)
    
    # Actual final computation: weighted sum of first four triplet averages
    weights = [0.4, 0.3, 0.2, 0.1]
    final_score = sum(triplet_averages[i] * weights[i] for i in range(4))
    
    # Additional scaling based on data length (relevant)
    final_score *= len(cleaned_data)
    
    return final_score

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Print result as required
print(f"Target result: {final_diagnostic}")