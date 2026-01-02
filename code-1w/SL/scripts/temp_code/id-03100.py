import math

def analyze_sensor_array(raw_readings, threshold, mode='strict'):
    # Irrelevant preprocessing (distractor)
    normalized = [x * 1.005 for x in raw_readings if x > -50]
    outliers = [x for x in normalized if x > 100 or x < 0]
    sanitized = [x for x in normalized if x <= 100 and x >= 0]

    # Core logic disguised among distractions
    temp_buffer = []
    for idx, val in enumerate(sanitized):
        if idx % 2 == 0:
            temp_buffer.append(val * 0.95)
        else:
            temp_buffer.append(val * 1.05)

    # Red herring: unused transformation
    inverted_map = {i: round(100 / (v + 1), 3) for i, v in enumerate(temp_buffer)}

    # Real processing path begins here
    cumulative = 0
    for i in range(len(temp_buffer)):
        if temp_buffer[i] > threshold:
            cumulative += math.sin(temp_buffer[i] * math.pi / 180) * 100

    return int(round(cumulative))


def extract_metadata(header_str):
    # Decoy function with string methods (irrelevant)
    parts = header_str.split('|')
    tags = [p.strip().upper() for p in parts]
    tag_stats = {t: len(t) for t in tags}
    return tag_stats


def validate_checksum(data_seq):
    # Unused validation logic (dead code path)
    checksum = 0
    for i, d in enumerate(data_seq):
        checksum ^= (d + i) % 256
    return checksum == 0


def process_readings(data_list, factor):
    # Critical data transformation using dictionary and zip
    base_values = [d * factor for d in data_list]
    indices = list(range(len(base_values)))
    
    # Distractor: complex but unused structure
    aux_lookup = dict(zip(indices, [(i**2, math.log(i+1)) for i in range(len(base_values))]))
    
    # Real calculation buried here
    paired = list(enumerate(base_values))
    adjusted = []
    for i, val in paired:
        if i % 3 == 0:
            adjusted.append(val * 1.1)
        elif i % 3 == 1:
            adjusted.append(val * 0.9)
        else:
            adjusted.append(val)

    # Final aggregation with modular arithmetic
    total = 0
    for j, a in enumerate(adjusted):
        total += (a * j) % 89

    # Key result
    final_diagnostic = int(total) % 100000
    return final_diagnostic

# Simulated sensor input (real data)
raw_input = [23, 45, 67, 89, 12, 34, 56, 78, 91, 11]
header_info = "HDR|sensor_v3|diagnostic|2024|calib"
calibration_factor = 1.08

# Unused metadata extraction (distractor)
meta = extract_metadata(header_info)

# Filtering based on threshold (part of real flow)
threshold_value = 30
filtered_data = [x for x in raw_input if x > threshold_value]

# First-stage analysis (intermediate red herring)
diag_code = analyze_sensor_array(raw_input, threshold=25, mode='loose')

# Checksum never called (dead path)
# validate_checksum(raw_input)

# Actual critical execution point
final_diagnostic = process_readings(filtered_data, calibration_factor)

# Output result as required
print(f"Result: {final_diagnostic}")