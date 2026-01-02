def filter_anomalies(data):
    # Irrelevant transformation (distractor)
    temp_adjusted = [x * 1.05 for x in data if x > 0]
    valid_readings = []
    for val in data:
        if 10 <= val <= 100:  # Only consider normal range
            valid_readings.append(val)
    # Dead code path - never used
    if len(valid_readings) > 100:
        return sorted(valid_readings)[:100]
    return valid_readings


def rolling_average(values, window=3):
    # Unused helper function - red herring
    averages = []
    for i in range(len(values) - window + 1):
        averages.append(sum(values[i:i+window]) / window)
    return averages


def extract_metadata(header_str):
    # Distractor: processes string but not used in final calculation
    parts = header_str.split('|')
    metadata_map = {}
    for part in parts:
        if '=' in part:
            k, v = part.split('=', 1)
            metadata_map[k.strip()] = v.strip()
    # Extract version using slicing
    version = metadata_map.get('VER', '')[1:] if 'VER' in metadata_map else ''
    try:
        return int(version)
    except ValueError:
        return -1


def compute_checksum(nums):
    # Seemingly important but unused security feature
    checksum = 0
    for i, num in enumerate(nums):
        checksum ^= (int(num) << (i % 4))  # Bit manipulation red herring
    return checksum & 0xFFFF


def normalize_readings(raw_vals):
    # Another distractor function that isn't used
    min_val, max_val = min(raw_vals), max(raw_vals)
    if max_val == min_val:
        return [0.5] * len(raw_vals)
    return [(x - min_val) / (max_val - min_val) for x in raw_vals]


def process_readings(valid_sensors):
    # Core logic buried among noise
    base_threshold = 42
    adjusted = [x + 1 for x in valid_sensors]  # Step 1: increment all
    
    # Conditional filtering based on bitwise property (relevant)
    filtered_by_mode = []
    for x in adjusted:
        if (x & 1) == 0:  # Keep only even numbers
            filtered_by_mode.append(x)
    
    # Accumulate every third element (key step)
    accumulated = 0
    for i, val in enumerate(filtered_by_mode):
        if (i + 1) % 3 == 0:  # Every third index (1-based)
            accumulated += val * 2
    
    # Secondary adjustment with modulo arithmetic
    mod_adjusted = accumulated % 97
    
    # Use of string slicing to derive offset (subtle but relevant)
    code_key = 'XJ9KLM8NPQRS7TUVW6YZ'
    offset_char = code_key[mod_adjusted % len(code_key)]  # Pick char
    offset_value = ord(offset_char) - ord('A')  # Map to number
    
    # Final computation chain
    intermediate = mod_adjusted + offset_value
    correction_factor = len(valid_sensors) - len(filtered_by_mode)
    result = intermediate - correction_factor
    
    # Decoy operation (looks important but unused)
    if result > 50:
        result = result ^ 255
    
    return result

# Simulated sensor input (mixed valid and invalid)
sensor_data = [5, 15, 22, 33, 40, 41, 42, 50, 60, 75, 88, 92, 101, 110, 120]

# Metadata string with embedded version (unused but plausible)
header_info = 'LOC=Z45|DATE=2023-11-07|VER=B3|MODE=NORMAL'

# Trigger irrelevant functions (to add noise)
version_num = extract_metadata(header_info)
checksum_value = compute_checksum(sensor_data)

# Main processing pipeline
filtered_data = filter_anomalies(sensor_data)
normalized = normalize_readings(sensor_data)  # Computed but not used

# Key execution point
final_diagnostic = process_readings(filtered_data)

# Output result
print(f"Result: {final_diagnostic}")