import math

def preprocess_readings(sensor_log):
    # Irrelevant preprocessing with red herring logic
    filtered = []
    for idx, val in enumerate(sensor_log):
        if idx % 3 == 0:
            adjusted = val * 1.05 + 2.1
        else:
            adjusted = val * 0.98 - 1.3
        if abs(adjusted) > 50:
            adjusted = 50 if adjusted > 0 else -50
        filtered.append(round(adjusted, 2))
    return filtered

def compute_frequencies(data):
    # Dead code path - never actually used in final computation
    freq_map = {}
    for item in data:
        bin_idx = int(item // 10)
        freq_map[bin_idx] = freq_map.get(bin_idx, 0) + 1
    return freq_map

def validate_checksum(sequence):
    # Distractor function: looks important but unused
    checksum = 0
    for i, x in enumerate(sequence):
        checksum += x * (i + 1)
    return checksum % 17

def rotate_key(matrix):
    # Complex-looking but irrelevant bit manipulation
    shifted = []
    for row in matrix:
        temp = 0
        for val in row:
            temp ^= int(val * 7) & 255
            temp = ((temp << 3) | (temp >> 5)) & 255
        shifted.append(temp)
    return shifted

def extract_signatures(dataset):
    # Another decoy transformation
    signatures = []
    for i, group in enumerate(zip(*dataset)):
        sig = 0
        for j, val in enumerate(group):
            sig += int(math.sin(val) * 100) * (j + 1)
        signatures.append(abs(sig) % 100)
    return signatures

def aggregate_metrics(turbine_data, calibration_sequence):
    # Core logic embedded within distractions
    base_score = 0
    
    # Real processing begins here
    normalized = [x / max(turbine_data) for x in turbine_data]
    
    # Bitwise interference mask (only some bits matter)
    mask = 0
    for i, c in enumerate(calibration_sequence):
        mask ^= (c * (i + 1)) % 16
    
    # Key calculation chain
    intermediate = 0
    for i, (norm, raw) in enumerate(zip(normalized, turbine_data)):
        if i % 2 == 0:
            contribution = norm * math.log(raw + 10)
        else:
            contribution = norm * math.sqrt(raw)
        intermediate += contribution
    
    # Modular arithmetic integration
    mod_factor = len(calibration_sequence) % 7
    if mod_factor == 0:
        mod_factor = 3
    
    # Combine with masked offset
    masked_offset = (mask ^ 197) & 255  # Only lower 8 bits relevant
    scaled_offset = masked_offset / 100.0
    
    # Final composition
    raw_result = (intermediate * 42.5) + scaled_offset
    final_diagnostic = int((raw_result * mod_factor) - 312.7)  # Critical assignment
    
    # Redundant transformations below (dead computations)
    diagnostics_log = []
    for k in range(5):
        fake_entry = (final_diagnostic >> k) ^ (k * 13)
        diagnostics_log.append(hex(fake_entry))
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Input data with domain-specific meaning
    turbine_data = [87, 102, 95, 118, 93, 107, 115]
    calibration_sequence = [3, 7, 2, 8, 5, 9, 4, 6]
    
    # Call preprocessing (result unused - red herring)
    processed = preprocess_readings(turbine_data)
    
    # Compute frequencies (unused)
    freqs = compute_frequencies(turbine_data)
    
    # Validate checksum (computed but not used)
    chk = validate_checksum(calibration_sequence)
    
    # Rotate key on dummy matrix (decoy operation)
    dummy_matrix = [[1, 2], [3, 4], [5, 6]]
    rotated = rotate_key(dummy_matrix)
    
    # Extract signatures from transposed data (irrelevant)
    transposed_data = list(zip(*[turbine_data, processed]))
    sigs = extract_signatures(transposed_data)
    
    # Actual target computation
    final_diagnostic = aggregate_metrics(turbine_data, calibration_sequence)
    
    # Output required result
    print(f"Target result: {final_diagnostic}")