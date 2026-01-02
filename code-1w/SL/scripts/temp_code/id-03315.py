def analyze_signal(x, threshold=50):
    if x < 0:
        return (x ** 2) % 17
    elif x > threshold:
        return (x // 3) ^ 5
    else:
        return (x + 10) * 2


def validate_checksum(data):
    checksum = 0
    for val in data:
        checksum ^= val
    return checksum % 13 == 0

# Irrelevant helper function (dead code path)
def legacy_calibrate(v):
    return round((v * 0.87) + 3.14159, 2)

# Misleading transformation chain
def transform_sequence(seq):
    temp_result = []
    for item in seq:
        processed = item
        processed = (processed * 2) + 1
        processed = processed if processed % 2 == 0 else processed + 1
        processed = abs(processed - 100)
        temp_result.append(processed)
    return sorted(temp_result, reverse=True)

# String-based distractor logic
def extract_flags(config_str):
    flags = config_str.upper().replace('-', '_').split('_')
    enabled = [f for f in flags if len(f) % 2 == 0]
    return len(enabled) > 2

# Core processing function with early returns and red herrings
def process_readings(raw):
    temp_storage = []
    accumulator = 0
    decoy_sum = 0  # Distractor variable
    
    for reading in raw:
        # Apply non-linear transformation
        transformed = analyze_signal(reading)
        temp_storage.append(transformed)
        
        # Decoy accumulation path
        if transformed > 40:
            decoy_sum += transformed * 0.5
        elif transformed < 15:
            decoy_sum -= transformed
            break  # Early exit that may never trigger

    # Real logic continues regardless of break
    filtered = [x for x in temp_storage if x % 4 == 2]
    
    # Red herring: complex-looking but unused bitwise cascade
    magic_key = 0
    for i in range(len(temp_storage)):
        magic_key ^= (temp_storage[i] << 1) | (i & 3)
    magic_key = (magic_key ^ 0xFF) & 0xFFFF
    
    # Critical counting logic masked by noise
    count_valid = 0
    for val in filtered:
        if val > 20:
            count_valid += 1
    
    # Final computation buried in string distraction
    mode_indicator = "NORMAL_MODE_ACTIVE"
    mode_code = len(mode_indicator.lower().split('_')) * 100
    
    # Actual answer derivation
    base_score = sum(filtered) + count_valid * 10
    adjustment = len(raw) - len(filtered)
    final_diagnostic = base_score - adjustment * 3
    
    # Unrelated string manipulation (distractor)
    metadata_tag = "sensor_v2-debug-log"
    tag_parts = metadata_tag.split('-')
    tag_parts = [part.upper() for part in tag_parts]
    reconstructed = '_'.join(tag_parts)
    
    return final_diagnostic

# Simulated sensor input (deterministic)
sensor_data = [12, 65, 3, 88, 42, 7, 103]

# Execute main logic
final_diagnostic = process_readings(sensor_data)
print(f"Result: {final_diagnostic}")