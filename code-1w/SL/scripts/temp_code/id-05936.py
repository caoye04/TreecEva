import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.3, 26.0, 24.7, 23.9]
humidity_readings = [56, 58, 61, 55, 52, 59, 60]
pressure_readings = [1013, 1015, 1012, 1010, 1008, 1014, 1016]

# Irrelevant auxiliary data (distractor)
legacy_system_flags = [0b1010, 0b1100, 0b0110, 0b1111, 0b0001]
redundant_checksums = [sum(pressure_readings[:i]) % 256 for i in range(1, 4)]
placeholder_matrix = [[i * j for j in range(3)] for i in range(3)]

# Signal processing constants
denoising_factor = 0.87
amplification_threshold = 24.0
baseline_correction = 1.2

# Step 1: Normalize temperature readings
corrected_temps = [t + baseline_correction for t in temperature_readings]

# Step 2: Detect anomalous spikes above threshold
spike_indices = []
for i, temp in enumerate(corrected_temps):
    if temp > amplification_threshold:
        spike_indices.append(i)

# Irrelevant bit manipulation (red herring)
masked_flags = []
for flag in legacy_system_flags:
    masked = (flag << 2) ^ 0b1101
    masked_flags.append(masked & 0b1111)

# Step 3: Compute rolling average over 3-point window
rolling_avg = []
for i in range(2, len(corrected_temps)):
    window_avg = sum(corrected_temps[i-2:i+1]) / 3
    rolling_avg.append(round(window_avg, 2))

# Step 4: Fuse multiple sensor streams into composite signal
composite_signal = []
for i in range(len(temperature_readings)):
    norm_temp = corrected_temps[i] / max(corrected_temps)
    norm_humidity = humidity_readings[i] / 100.0
    fused_value = denoising_factor * (0.7 * norm_temp + 0.3 * norm_humidity)
    composite_signal.append(fused_value)

# Step 5: Process signals using non-linear transformation
processed_signals = []
def process_segment(segment):
    return math.log(1 + segment ** 2) if segment > 0.5 else segment * 0.9

for val in composite_signal:
    processed_signals.append(process_segment(val))

# Dead code path - never called (distractor)
def deprecated_analysis(data):
    magnitude = sum([x**2 for x in data]) ** 0.5
    return magnitude * 0.1

# Unused intermediate calculation (misleading)
average_power = sum([x**2 for x in processed_signals]) / len(processed_signals)
spectral_entropy = -sum([p * math.log(p) for p in processed_signals if p > 0])

# Step 6: Analyze processed signals to generate diagnostic
valid_detections = [p for p in processed_signals if p > 0.45]

def analyze_readings(readings):
    if not readings:
        return -1
    
    # Complex multi-step logic
    squared_sum = sum([r**2 for r in readings])
    mean_square = squared_sum / len(readings)
    rms_value = math.sqrt(mean_square)
    
    # Apply corrective scaling based on detection count
    correction_factor = len(valid_detections) / len(readings)
    adjusted_rms = rms_value * (1 + correction_factor)
    
    # Final transformation with floor constraint
    diagnostic_score = max(adjusted_rms * 100, 10)
    
    # Integer quantization
    return int(round(diagnostic_score))

# Critical execution point
final_diagnostic = analyze_readings(processed_signals)

# Output result
print(f"Target result: {final_diagnostic}")