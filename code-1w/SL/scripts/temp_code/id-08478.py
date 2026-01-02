import math

# Simulated sensor data processing with diagnostic analysis
raw_readings = [3.2, 1.8, 4.5, 2.7, 5.1, 3.6, 2.9, 4.0, 3.8]
noise_floor = 1.5
calibration_factor = 0.87

# Irrelevant constants (distractors)
system_id = "DIAG-9X"
max_iterations = 150
version_code = 202311

# Preprocessing: remove noise and calibrate
filtered_readings = [x - noise_floor for x in raw_readings if x > noise_floor]
calibrated_signals = [round(x * calibration_factor, 3) for x in filtered_readings]

# Generate frequency spectrum (partially irrelevant)
frequencies = [math.sin(2 * math.pi * i * 0.1) for i in range(len(calibrated_signals))]
fft_magnitude_estimate = sum(f * f for f in frequencies[:len(calibrated_signals)//2])

# Threshold configuration map (used later)
threshold_map = {
    'low': 1.0,
    'medium': 2.2,
    'high': 3.5
}

# Signal state classification with decoy logic
state_counter = {'stable': 0, 'fluctuating': 0, 'critical': 0}
previous = calibrated_signals[0]
for val in calibrated_signals[1:]:
    diff = abs(val - previous)
    if diff < 0.3:
        state_counter['stable'] += 1
    elif diff < 0.8:
        state_counter['fluctuating'] += 1
    else:
        state_counter['critical'] += 1
    previous = val

# Dead code path - never executed but looks important
legacy_mode = False
if legacy_mode:
    adjustment = 0.0
    for i in range(len(calibrated_signals)):
        calibrated_signals[i] *= (1 + adjustment)

# Decoy function that's defined but not used
def deprecated_analysis(data):
    return sum(d**2 for d in data) / len(data)

# Real processing begins: group signals by ranges
processed_data = []
for sig in calibrated_signals:
    category = 'low'
    if sig >= threshold_map['high']:
        category = 'high'
    elif sig >= threshold_map['medium']:
        category = 'medium'
    
    # Apply conditional transformation
    adjusted_value = sig * 1.1 if category == 'high' else (sig * 0.95 if category == 'medium' else sig)
    processed_data.append(round(adjusted_value, 3))

# Another irrelevant computation (misleading intermediate result)
avg_power_estimation = sum(p**2 for p in processed_data) / len(processed_data)
diagnostic_shadow = avg_power_estimation * 0.735  # Looks important but unused

# Core diagnostic algorithm
healthy_count = sum(1 for p in processed_data if p > threshold_map['medium'])
anomaly_score = len(processed_data) - healthy_count

# Bit manipulation red herring (unused)
bit_encoded = 0
for p in processed_data[:4]:
    bit_encoded ^= int(p * 10) & 0xFF

# Final diagnostic decision tree
primary_weight = 0.6
secondary_weight = 0.4

baseline_metric = sum(processed_data) / len(processed_data)
boost_factor = 1.25 if state_counter['critical'] == 0 else 0.8

interim_result = baseline_metric * boost_factor

# Conditional expression determining final outcome
final_diagnostic = int(interim_result * primary_weight * 100) + int(anomaly_score * secondary_weight * 25)

# Output the target result
print(f"Result: {final_diagnostic}")