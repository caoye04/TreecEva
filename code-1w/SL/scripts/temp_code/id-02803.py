import math

# Sensor calibration constants (used in decoy function)
CALIBRATION_OFFSET = 0.87
REFERENCE_VOLTAGE = 3.3
TEMP_CORRECTION_FACTOR = 1.02

# Irrelevant sensor simulation data
raw_signals = [0.45, 0.67, 0.91, 1.23, 0.88, 0.54, 1.01, 1.33, 0.76, 0.65]
noise_floor = [0.02 * i + 0.1 for i in range(10)]
filtered_data = [raw_signals[i] - noise_floor[i] for i in range(len(raw_signals))]

def apply_calibration(signal):
    # Decoy function – not actually used in main logic
    return (signal * REFERENCE_VOLTAGE) + CALIBRATION_OFFSET

def generate_histogram(data):
    # Dead code path – never called
    bins = [0] * 5
    for val in data:
        idx = min(4, int(val // 0.2))
        bins[idx] += 1
    return bins

def compute_entropy(arr):
    # Unused advanced calculation – red herring
    total = sum(arr)
    if total == 0:
        return 0.0
    probabilities = [x / total for x in arr if x > 0]
    return -sum(p * math.log2(p) for p in probabilities)

# Real processing begins here
voltage_readings = [2.1, 3.4, 1.8, 4.5, 2.7, 3.0, 1.9, 4.1, 2.2, 3.8, 1.7, 4.4]
adjusted_readings = [v * 0.91 for v in voltage_readings]  # Scale down for load factor

# Extract critical phase window using slicing
phase_window = adjusted_readings[2:10]  # Focus on indices 2 to 9

# Apply non-linear transformation
transformed = []
for x in phase_window:
    if x < 2.5:
        transformed.append(x ** 1.8)
    elif x < 3.5:
        transformed.append(x * 1.6)
    else:
        transformed.append(math.sqrt(x) * 2.1)

# Compute statistical profile
mean_val = sum(transformed) / len(transformed)
squared_deviations = [(x - mean_val) ** 2 for x in transformed]
variance = sum(squared_deviations) / len(squared_deviations)
std_dev = math.sqrt(variance)

# Mask outliers and recompute (slicing again)
cleaned = [x for x in transformed if abs(x - mean_val) <= 2 * std_dev]
trimmed_mean = sum(cleaned) / len(cleaned)

# Simulate system load response curve
response_curve = []
for i in range(len(cleaned)):
    dampened = cleaned[i] * (0.85 ** i)
    shifted = dampened + (0.12 * (i % 3))
    response_curve.append(shifted)

# Aggregate final signal energy
energy_integral = sum(response_curve) * 0.76  # Time step multiplier

# Secondary validation check (unused but looks important)
consistency_score = len([x for x in response_curve if x > trimmed_mean])
threshold_flag = consistency_score >= 4

# Core thermal model function
previous_capacity = 0

def recursive_thermal_decay(level, depth):
    # Recursive red herring – not used
    global previous_capacity
    if depth == 0 or level < 0.5:
        return level
    decayed = level * 0.63
    next_val = recursive_thermal_decay(decayed, depth - 1)
    previous_capacity += next_val
    return next_val

# Actual thermal calculation
peak_reading = max(phase_window)
base_factor = math.log(peak_reading) * 1.45

def calculate_thermal_profile(data_slice):
    # Main relevant function
    length_factor = len(data_slice) * 0.33
    avg_signal = sum(data_slice) / len(data_slice)
    fluctuation_index = max(data_slice) - min(data_slice)
    stability_modifier = 1.0 if fluctuation_index < 1.5 else 0.85
    
    # Final composite computation
    capacity = (base_factor + length_factor + avg_signal) * stability_modifier
    
    # Extra obfuscation via unused intermediate
    hypothetical_max = (base_factor + 10) * 1.2  # Distractor
    normalization_ratio = capacity / hypothetical_max if hypothetical_max != 0 else 0  # Unused
    
    return capacity

# Trigger key statement
processed_readings = response_curve[1:7]  # Critical slice
thermal_capacity = calculate_thermal_profile(processed_readings)

# Print result as required
print(f"Result: {thermal_capacity}")