import math

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 22.8, 25.0, 26.3, 27.1, 25.8, 24.7, 23.9]
humidity_readings = [45, 48, 50, 55, 60, 62, 58, 54, 51]
pressure_readings = [1013, 1012, 1014, 1015, 1016, 1018, 1017, 1015, 1014]

# Irrelevant calibration constants (distractor)
CALIBRATION_OFFSET_A = 0.037
CALIBRATION_OFFSET_B = -0.021
REFERENCE_VOLTAGE = 3.3

# Decoy processing function that's never called
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [x - mean_val for x in data]

# Unused signal filtering (dead code path)
def apply_low_pass(signal, alpha=0.2):
    filtered = [signal[0]]
    for i in range(1, len(signal)):
        filtered.append(alpha * signal[i] + (1 - alpha) * filtered[-1])
    return filtered

# Auxiliary transformation - actually used
transform_sensor = lambda x: round(math.log(x) * 100, 2)

# Step 1: Preprocess temperature with logarithmic scaling
scaled_temps = [transform_sensor(temp + 273.15) for temp in temperature_readings]  # Kelvin conversion

# Step 2: Compute humidity trends with list comprehension and conditional logic
trend_analysis = [
    1 if humidity_readings[i] > humidity_readings[i-1] else -1
    for i in range(1, len(humidity_readings))
]

# Step 3: Compute rolling average of pressure (window size 3)
rolling_pressure = [
    sum(pressure_readings[i:i+3]) / 3
    for i in range(len(pressure_readings) - 2)
]

# Irrelevant derived metrics (distractors)
virtual_index_a = sum(scaled_temps[:5]) * 0.07
virtual_index_b = math.sqrt(abs(virtual_index_a - 150))
phantom_metric = (virtual_index_a + virtual_index_b) % 47

# Step 4: Correlation analysis between scaled temp and humidity
# Only odd-indexed readings are valid due to sensor sync issue
valid_temp_humidity_pairs = [
    (scaled_temps[i], humidity_readings[i])
    for i in range(len(scaled_temps))
    if i % 2 == 1  # Only odd indices are synchronized
]

correlation_score = sum(
    (pair[0] - sum(scaled_temps[1::2]) / len(scaled_temps[1::2])) *
    (pair[1] - sum(humidity_readings[1::2]) / len(humidity_readings[1::2]))
    for pair in valid_temp_humidity_pairs
)

# Step 5: Signal validation mask based on pressure stability
def generate_stability_mask(rolling_pressures):
    avg_pressure = sum(rolling_pressures) / len(rolling_pressures)
    return [1 if abs(p - avg_pressure) < 2 else 0 for p in rolling_pressures]

stability_mask = generate_stability_mask(rolling_pressure)

# Step 6: Masked integration of correlation with stability
masked_integration = 0
for i, score in enumerate([correlation_score] * len(stability_mask)):
    if i < len(stability_mask):  # Safety check
        masked_integration += score * stability_mask[i]

# Step 7: Process signals through multi-stage pipeline
processed_signals = []
for idx, val in enumerate(scaled_temps):
    if idx % 3 == 0:
        processed_signals.append(val * 1.1)
    elif idx % 3 == 1:
        processed_signals.append(val * 0.95)
    else:
        processed_signals.append(val * 1.05 + 2.0)

# Step 8: Analyze final diagnostic from processed signals
def analyze_readings(signals):
    # Nested logic with multiple conditions
    threshold = sum(signals) / len(signals) + 10
    extreme_count = 0
    for s in signals:
        if s > threshold:
            extreme_count += 1
            if s > threshold + 5:  # Second-level filter
                extreme_count += 1  # Double count for severe deviations

    # Bit manipulation stage (simulated fault detection)
    fault_code = extreme_count ^ 15
    fault_code = fault_code << 2
    fault_code = fault_code & 255

    # Final computation combining multiple factors
    base_diagnostic = int(fault_code) + int(correlation_score % 50)

    # Red herring: unused adjustment
    temporal_drift = math.sin(len(signals) * 0.1) * 3.7

    # Critical line - this determines the answer
    final_diagnostic = base_diagnostic * 3 - 17

    return final_diagnostic

# Execution point of interest
final_diagnostic = analyze_readings(processed_signals)

# Output result as required
print(f"Result: {final_diagnostic}")