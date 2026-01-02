import itertools

# Simulated sensor array data from environmental monitoring station
temperature_readings = [23.5, 24.1, 19.8, 25.3, 22.7, 26.0, 20.2, 24.8]
humidity_readings = [45, 52, 61, 48, 55, 43, 59, 50]
pressure_readings = [1013, 1015, 1012, 1018, 1014, 1010, 1016, 1017]

# Irrelevant auxiliary arrays (distractors)
sound_levels = [32, 41, 38, 45, 36, 34, 40, 39]  # Unused in final calculation
light_intensity = [8700, 9100, 8500, 9200, 8800, 8600, 9000, 8900]  # Dead code path

# Calibration coefficients (some irrelevant)
baseline_offset = 0.87
scaling_factor = 1.03
normalization_constant = 0.995
phase_shift = 0.12  # Unused

# Preprocessing: filter out unstable readings using rolling window logic
def extract_stable_segments(data, threshold=1.5):
    segments = []
    current_segment = []
    for i in range(1, len(data)):
        if abs(data[i] - data[i-1]) < threshold:
            if not current_segment:
                current_segment.append(data[i-1])
            current_segment.append(data[i])
        else:
            if len(current_segment) > 1:
                segments.append(current_segment[:])
                current_segment = []
    if len(current_segment) > 1:
        segments.append(current_segment)
    return segments[0] if segments else [data[0]]

# Misleading transformation function (partially unused)
def apply_noise_correction(values, strength=0.9):
    corrected = []
    for v in values:
        adjusted = v * (1 + (0.1 * strength))
        normalized = adjusted - 0.05 * strength
        corrected.append(round(normalized, 2))
    return corrected

# Core processing with multiple concepts
filtered_temps = extract_stable_segments(temperature_readings, 1.2)

# Bit manipulation red herring
def compute_checksum(values):
    checksum = 0
    for v in values:
        scaled = int(v * 10)
        checksum ^= scaled  # XOR into checksum
        checksum = (checksum << 1) & 0xFFFF | (checksum >> 15)  # Rotate left
    return checksum & 0x7FFF

temp_checksum = compute_checksum(filtered_temps)  # Distractor value

# Decoy function using string methods (irrelevant)
def generate_status_report(code, level):
    status_map = {0: 'OK', 1: 'WARN', 2: 'ERROR'}
    prefix = f"SYS-{level}"
    suffix = "[COMPLETE]" if level > 0 else "[PENDING]"
    message = prefix + ": Status check " + status_map.get(code % 3, 'UNKNOWN')
    return message.lower().replace(' ', '_').strip() + ' -> ' + suffix

report = generate_status_report(temp_checksum, 5)  # Dead end

# Real processing begins here — combines tuple unpacking, filtering, and scaling
calibration_factor = (scaling_factor * normalization_constant) + baseline_offset

# Data fusion using zip and itertools.chain
fused_readings = list(itertools.chain.from_iterable(
    zip(filtered_temps, humidity_readings[:len(filtered_temps)])
))

# Extract only temperature components (every odd index was temp, but this is misleading)
# Actually, every even index is temp due to zip order
reconstructed_temps = [fused_readings[i] for i in range(0, len(fused_readings), 2)]

# Secondary filter based on auxiliary condition (uses set for uniqueness)
valid_indices = set(range(0, len(reconstructed_temps), 2))  # Artificial constraint
trimmed_temps = [t for i, t in enumerate(reconstructed_temps) if i in valid_indices or t > 22.0]

# Final processing function
def process_readings(readings, calib):
    if not readings:
        return 0.0
    
    # Apply calibration
    calibrated = [temp * calib for temp in readings]
    
    # Aggregate with weighted contributions
    total_weight = 0
    weighted_sum = 0
    
    for i, val in enumerate(calibrated):
        weight = 1.0 + (0.1 * (i + 1))  # Increasing importance over time
        weighted_sum += val * weight
        total_weight += weight
    
    # Use of tuple unpacking in loop (real usage)
    diagnostics = []
    for item in calibrated:
        category = 'HIGH' if item > 25 else 'NORMAL'
        code = 1 if category == 'HIGH' else 0
        diagnostics.append((item, category, code))
    
    # Only use the first diagnostic code for final result
    primary_code = diagnostics[0][2] if diagnostics else 0
    
    # Final computation
    average_calibrated = weighted_sum / total_weight
    final_score = average_calibrated * 100 + primary_code * 5
    
    # This break is inside a non-loop, so it's dead code (misleading)
    # break  # Invalid syntax if uncommented — but commented as distractor
    
    return round(final_score, 4)

# Key execution point
final_diagnostic = process_readings(trimmed_temps, calibration_factor)

# Output result
print(f"Result: {final_diagnostic}")