def analyze_data_points(values):
    filtered = [v for v in values if v > 0]
    adjusted = [x * 1.5 for x in filtered if x < 100]
    return sum(adjusted) // len(filtered) if filtered else 0


def validate_checksum(data):
    checksum = 0
    for d in data:
        checksum ^= d % 256
    return checksum == 42


def extract_metadata(record_str):
    parts = record_str.split('|')
    timestamp_str = parts[0].strip()
    location_code = parts[1].strip()
    status_flag = parts[2].strip().upper()
    
    # Irrelevant string processing (distractor)
    clean_location = location_code.strip('LX').lower()
    is_active = 'ACTIVE' in status_flag
    
    return {
        'year': int(timestamp_str[:4]),
        'month': int(timestamp_str[4:6]),
        'valid': is_active and len(location_code) > 2
    }

# Simulated sensor readings
readings = [12, -5, 45, 0, 98, 203, 67, -44, 11]

# Extraneous data structure (semi-relevant)
data_log = "20231201|LX789|active"

# Intermediate calculations with some distractions
base_metric = sum(readings) // len([r for r in readings if r != 0])
eval_factor = base_metric % 17

# Conditional adjustment based on dummy condition
if eval_factor > 10:
    eval_factor -= 5
else:
    temp_shift = eval_factor << 1
    eval_factor = temp_shift ^ 3  # Bitwise red herring

# Checksum validation (not actually used, distractor)
validation_data = [10, 20, 30, 40, 50]
valid_checksum = validate_checksum(validation_data)

# Metadata extraction (partially irrelevant)
meta = extract_metadata(data_log)

# Core logic chain begins
aggregated = analyze_data_points(readings)

# Multiple assignment distraction
weight_a, weight_b = 0.6, 0.4

# Logical expression with short-circuiting (distractor)
override_flag = (weight_a > 1.0) or (False and meta['year'] > 2020)

# Main scoring logic
raw_score = aggregated + eval_factor

# Complex conditional with nested structure
if raw_score >= 80:
    if meta['month'] == 12:
        final_score = raw_score * 1.2
    else:
        final_score = raw_score * 1.1
elif raw_score >= 50:
    final_score = raw_score * 1.05
else:
    final_score = max(raw_score - 10, 0)

# Redundant reassignment (dead code path - not executed)
if False:
    final_score = 999

# Final adjustment using string-based logic (irrelevant but plausible)
day_str = "15"
buffer_value = int(day_str.lstrip('0')) if day_str.isdigit() else 1

# Final score output
Result: {final_score}