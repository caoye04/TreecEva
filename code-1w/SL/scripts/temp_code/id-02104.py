import math

# Simulated sensor data from a thermal regulation system
temperature_readings = [23.5, 24.1, 25.0, 26.8, 27.3, 28.0, 27.9, 27.1, 26.4, 25.7]
humidity_readings = [45, 47, 50, 55, 60, 63, 65, 62, 58, 53]

def preprocess(data_list):
    """Apply moving average filter (window size 3) with edge padding."""
    if len(data_list) < 3:
        return data_list
    smoothed = []
    for i in range(len(data_list)):
        if i == 0:
            smoothed.append((data_list[0] + data_list[1]) / 2)
        elif i == len(data_list) - 1:
            smoothed.append((data_list[i-1] + data_list[i]) / 2)
        else:
            smoothed.append((data_list[i-1] + data_list[i] + data_list[i+1]) / 3)
    return smoothed

# Irrelevant transformation - decoy function
def transform_coordinates(x_vals, y_vals):
    """Convert Cartesian to polar (unused in final logic)."""
    magnitudes = []
    angles = []
    for x, y in zip(x_vals, y_vals):
        r = math.sqrt(x*x + y*y)
        theta = math.atan2(y, x)
        magnitudes.append(r)
        angles.append(theta)
    return magnitudes, angles

# Misleading intermediate analysis
def calculate_variance(data):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    return variance

variance_warning = calculate_variance(temperature_readings) > 2.0  # Red herring

# Signal processing chain
filtered_temps = preprocess(temperature_readings)
filtered_humidity = preprocess(humidity_readings)

# Combine signals using phase offset (simulated)
phase_shifted = []
for i, temp in enumerate(filtered_temps):
    shift = math.sin(math.pi * i / 4)  # Periodic influence
    phase_shifted.append(temp + shift * 0.5)

# Destructuring assignment - extract key samples
critical_points = phase_shifted[::3]  # Every third point
first_diag, *remaining_diagnostics, last_diag = critical_points

# Tuple unpacking with enumerate - relevant step
indexed_diagnostics = list(enumerate(remaining_diagnostics, start=1))

eval_sum = 0
for idx, val in indexed_diagnostics:
    # Weighted contribution based on position and magnitude
    weight = (idx + 1) ** 0.5
    eval_sum += val * weight

# Decoy string processing - irrelevant but plausible
log_entry = "THERMAL_DIAG_2023"
split_parts = log_entry.split('_')
level_code = split_parts[1] if len(split_parts) > 1 else "UNKNOWN"
valid_chars = sum(1 for c in level_code if c.isalpha())  # Distraction

# Modular arithmetic masking pattern (distractor)
mask_sequence = []
for i in range(len(phase_shifted)):
    mask = (i * 17) % 13
    masked_val = round(phase_shifted[i]) % mask if mask != 0 else 0
    mask_sequence.append(masked_val)

# Core diagnostic logic (hidden among noise)
def compute_stability_index(vals):
    """Compute weighted stability metric from processed signal."""
    base_score = 0
    for i, v in enumerate(vals):
        contribution = v * math.cos(i * math.pi / 6)
        base_score += contribution
    return base_score * 1.25

stability_snapshot = compute_stability_index(filtered_temps)

# Final analysis incorporating boolean logic and thresholds
threshold_met = stability_snapshot > 25.0
amplitude_ok = max(phase_shifted) - min(phase_shifted) < 5.0

# Logical operations and short-circuit evaluation
diagnostic_flag = threshold_met and amplitude_ok or (variance_warning and False)

# Data restructuring - relevant only through side effect of length
processed_data = []
for t, h in zip(filtered_temps, filtered_humidity):
    entry = {
        't': round(t, 1),
        'h': int(h),
        'q': (round(t) % 3) + (int(h) % 4)
    }
    processed_data.append(entry)

# Key function that computes the answer
def analyze_signal(data_entries):
    total = 0
    for item in data_entries:
        # Extract and combine fields using modular arithmetic
        temp_part = item['t'] * 1.1
        humidity_part = item['h'] % 7
        quality_adj = item['q'] // 2
        # Critical calculation step
        total += temp_part - humidity_part + quality_adj
    # Final adjustment using bitwise manipulation (obscured relevance)
    total = total * 100
    total = int(total) ^ 456  # XOR with constant
    total = total & 1023  # Mask to 10 bits
    return total / 100.0

final_diagnostic = analyze_signal(processed_data)
print(f"Target result: {final_diagnostic}")