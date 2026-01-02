import math

# Sensor simulation and health monitoring system for industrial turbines
def generate_raw_readings():
    return [23.5, 24.1, 22.9, 25.3, 19.8, 26.7, 21.0, 20.4]

# Irrelevant helper - simulates temperature drift (not used in final calculation)
def simulate_drift(values):
    return [v + 0.1 * i for i, v in enumerate(values)]

# Decoy function: appears useful but is never called
def deprecated_normalization(data):
    mean_val = sum(data) / len(data)
    return [math.sin(x - mean_val) for x in data]

# Core processing pipeline
raw_data = generate_raw_readings()

# Misleading intermediate transformation - looks important but unused
smoothed_data = [raw_data[i] * (1 + 0.02 ** i) for i in range(len(raw_data))]

# Actual relevant processing starts here
filtered_readings = [x for x in raw_data if 20 <= x <= 25]  # Only valid operational range

# Dead code path - assigned but never used
redundant_copy = filtered_readings.copy()
offset_correction = 0.0  # Placeholder for calibration (zero effect)

calibrated = [x + offset_correction for x in filtered_readings]

# Bit manipulation red herring: process index positions in binary
binary_flags = []
for i in range(len(calibrated)):
    flag = (i << 2) | 1  # Arbitrary bit shift + OR
    if flag & 4:  # Conditional that never triggers
        binary_flags.append(flag)

# Distractor: complex-looking but unused statistical computation
skew_estimate = 0.0
if len(calibrated) > 1:
    mean_x = sum(calibrated) / len(calibrated)
    variance = sum((x - mean_x) ** 2 for x in calibrated) / len(calibrated)
    skew_estimate = sum((x - mean_x) ** 3 for x in calibrated) / (len(calibrated) * variance ** 1.5)

# Another decoy list comprehension with no downstream use
derived_weights = [round(math.log(5 + i) * (1.1 ** i), 3) for i in range(len(calibrated))]

# Key conditional expression chain using logical operations
valid_count = len(calibrated)
threshold_met = valid_count >= 4
signal_strength = sum(calibrated) / len(calibrated) if calibrated else 0.0
consistency_check = all(abs(calibrated[i] - calibrated[i-1]) < 2.0 for i in range(1, len(calibrated))) if calibrated else False

# Logical combination with short-circuit evaluation (appears critical)
diagnostic_flag = threshold_met and (signal_strength > 21.5 or consistency_check)

# Unused alternate diagnostic path (dead branch)
if not diagnostic_flag and valid_count > 2:
    backup_analysis = min(calibrated) > 18.0
    diagnostic_flag = backup_analysis  # Never reached

# Main analysis function with nested logic
def analyze_readings(readings):
    if not readings:
        return -999.0

    base_score = sum(math.sqrt(x) for x in readings)

    # Multi-level nesting with conditional expressions
    adjustment = 0.0
    for x in readings:
        if x < 22.0:
            adjustment -= 0.5
        elif x > 24.0:
            adjustment += 0.3
        else:
            if int(x) % 2 == 0:  # Even integer part
                adjustment += 0.1
            else:
                adjustment -= 0.05

    # Complex composite score with irrelevant trigonometric distraction
    trig_factor = sum(math.cos(math.pi * x / 100) for x in readings)  # Near-constant values
    final_adjustment = adjustment + trig_factor * 0.01  # Negligible contribution

    return round(base_score + final_adjustment, 4)

# Secondary processing function (only some outputs matter)
def process_metrics(raw):
    # List comprehension with filtering and transformation
    processed = [val * 1.05 for val in raw if val >= 19.5]
    
    # Redundant validation step
    for p in processed:
        assert p > 0, "Negative reading encountered"
    
    # Return transformed data
    return processed

# Execute processing steps
processed_metrics = process_metrics(raw_data)

# Critical execution point
final_diagnostic = analyze_readings(processed_metrics)

# Output result as required
print(f"Target result: {final_diagnostic}")