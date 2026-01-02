import math

# Sensor calibration constants (some are decoys)
CALIBRATION_A = 0.872
CALIBRATION_B = 1.045
CALIBRATION_C = 2.119  # Unused in final calculation
def calibrate_sensor(value, mode='A'):
    if mode == 'A':
        return value * CALIBRATION_A
    elif mode == 'B':
        return value * CALIBRATION_B
    else:
        return value

# Simulated raw sensor readings from thermal array
def get_raw_readings():
    return [127, 142, 135, 168, 153, 130, 145]

# Secondary system diagnostics (distractor function)
def run_diagnostics(data):
    avg = sum(data) / len(data)
    variance = sum((x - avg) ** 2 for x in data) / len(data)
    return {'average': avg, 'variance': variance, 'status': 'OK'}

# Signal processing pipeline
def preprocess_signal(signal_stream):
    filtered = []
    for i, val in enumerate(signal_stream):
        if i % 2 == 0:
            filtered.append(val * 0.95)
        else:
            filtered.append(val * 1.05)
    return filtered

# Frequency domain transformation (red herring)
def apply_fourier_transform(data):
    transformed = []
    for i in range(len(data)):
        real_part = sum(data[j] * math.cos(2 * math.pi * i * j / len(data)) for j in range(len(data)))
        imag_part = sum(-data[j] * math.sin(2 * math.pi * i * j / len(data)) for j in range(len(data)))
        magnitude = math.sqrt(real_part**2 + imag_part**2)
        transformed.append(magnitude)
    return transformed  # Never used in main logic

def enhance_resolution(data, factor=2):
    expanded = []
    for a, b in zip(data, data[1:]):
        expanded.append(a)
        expanded.append((a + b) / 2)
    expanded.append(data[-1])
    return expanded

def detect_anomalies(data):
    threshold = sum(data) / len(data) + 0.5 * (max(data) - min(data))
    anomalies = [i for i, x in enumerate(data) if x > threshold]
    return anomalies  # Computed but irrelevant

def calculate_thermal_output(calibrated_data):
    base_energy = 0
    for i, reading in enumerate(calibrated_data):
        if i % 3 == 0:
            base_energy += reading * 1.1
        elif i % 3 == 1:
            base_energy += reading * 0.9
        else:
            base_energy += reading * 1.05
    
    # Apply non-linear efficiency curve
    efficiency_factor = 0.85 + (len(calibrated_data) * 0.01)
    adjusted_energy = base_energy * efficiency_factor
    
    # Secondary correction based on position distribution
    position_weight = sum(i * v for i, v in enumerate(calibrated_data)) / sum(calibrated_data)
    final_output = adjusted_energy / (1 + math.exp(-0.1 * position_weight))
    
    return final_output

# Main execution sequence
raw_readings = get_raw_readings()
diag_report = run_diagnostics(raw_readings)  # Distractor call

# Begin actual signal processing chain
partial_correction = [calibrate_sensor(x, 'A') for x in raw_readings]
processed_signal = preprocess_signal(partial_correction)
anomaly_indices = detect_anomalies(processed_signal)  # Computed but unused
enhanced_data = enhance_resolution(processed_signal, factor=2)  # Elaborate distractor
fourier_magnitudes = apply_fourier_transform(processed_signal)  # Dead-end computation

# Critical processing step
final_calibrated = [calibrate_sensor(x, 'B') for x in processed_signal]

# Key statement
thermal_capacity = calculate_thermal_output(final_calibrated)

print(f"Result: {thermal_capacity}")