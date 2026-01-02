import math

# Simulated industrial batch processing with noise filtering and quality validation
def analyze_sensor_data(raw_readings):
    filtered_readings = []
    for val in raw_readings:
        if val < 0:  # Invalid reading
            continue
        if val > 1000:  # Sensor overload, discard
            continue
        if int(val) % 7 == 0:  # Noise pattern filter (empirical)
            continue
        filtered_readings.append(val * 0.87)
    return filtered_readings

# Irrelevant helper - decoy function (dead path)
def compute_thermal_gradient(temp_log):
    return [t2 - t1 for t1, t2 in zip(temp_log, temp_log[1:])]

# Batch metadata (distractors)
equipment_id = "RX-9000"
operator_shift = "night"
batch_timestamp = 1712345678
target_purity = 99.2

# Raw sensor input with anomalies
raw_batch_data = [
    105.4, 210.8, 140.2, 35.1, 70.3,  # Normal values
    1050.0, -45.6, 560.7,  # Invalid: overload and negative
    49.0, 98.0, 196.0, 392.0,  # Divisible by 7 (noise)
    80.5, 161.0, 322.5, 645.0   # Valid signal chain
]

# Signal processing pipeline
smoothed_signal = [round(x + 0.05, 1) for x in raw_batch_data]  # Minor correction (irrelevant now)

# Real processing begins here
validated_readings = analyze_sensor_data(raw_batch_data)

# Apply time-decay weighting (simulated stabilization)
weighted_readings = [
    val * math.exp(-i * 0.05) for i, val in enumerate(validated_readings)
]

# Normalize using moving average baseline (distractor computation)
baseline = sum(weighted_readings[:5]) / 5 if len(weighted_readings) >= 5 else 0
normalized_output = [val - baseline for val in weighted_readings]

# Artifact from another system - irrelevant data structure
legacy_diagnostic_codes = {"E1", "W2", "I9", "E1", "C4"}
diagnostic_flags = set()
for code in legacy_diagnostic_codes:
    if code.startswith("E"):
        diagnostic_flags.add("error")
    elif code.startswith("W"):
        diagnostic_flags.add("warning")

# Critical processing step: batch segmentation by phase
phase_markers = [0, len(normalized_output) // 3, 2 * len(normalized_output) // 3, len(normalized_output)]
phase_integrals = []
for i in range(3):
    segment = normalized_output[phase_markers[i]:phase_markers[i+1]]
    integral = sum(segment) * 1.1  # Energy approximation
    phase_integrals.append(round(integral, 2))

# Final purification pass: remove residual negatives
processed_batch = [max(0, x) for x in normalized_output]

# Key statement - target execution point
filtration_yield = sum(processed_batch)

# Output must be printed exactly like this
print(f"Result: {filtration_yield}")