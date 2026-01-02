def analyze_frequency(data):
    # Irrelevant analysis function (dead end)
    magnitude = sum(x ** 2 for x in data) / len(data)
    peak = max(data)
    return magnitude * 0.707

# Calibration coefficients for sensor adjustment (some are decoys)
calibration_map = {
    'gain_a': 1.05,
    'offset_b': -0.3,
    'filter_c': 0.95,
    'unused_d': 2.1,  # red herring
    'scale_e': 1.2  # never used
}

# Raw signal chunks from satellite transmission (real data mixed with noise)
signal_chunks = [
    [1, 2, 3, 4, 5],
    [6, 7, 8],
    [9, 10, 11, 12, 13, 14],
    [15, 16],
    [17, 18, 19, 20, 21, 22, 23]
]

# Historical baseline (irrelevant)
historical_avg = 14.5
anomaly_threshold = 1.96

# Auxiliary function that looks important but isn't used
def validate_checksum(chunk):
    xor_sum = 0
    for val in chunk:
        xor_sum ^= val
    return xor_sum % 7

# Another decoy: simulate drift correction (not actually applied)
adjusted_chunks = []
for idx, chunk in enumerate(signal_chunks):
    adjusted = [x + 0.1 * idx for x in chunk]  # fake correction
    adjusted_chunks.append(adjusted)

# Real processing begins here — core logic hidden among distractions
def extract_key_segment(sequence):
    length = len(sequence)
    mid = length // 2
    if length > 4:
        # Use slice to get middle portion
        return sequence[mid - 2:mid + 2]
    return sequence

def apply_calibration(segment, calib):
    # Only uses two keys; others are distractions
    gain = calib['gain_a']
    offset = calib['offset_b']
    return [(val * gain) + offset for val in segment]

def compute_coherence(signal_part):
    total = 0
    for i in range(len(signal_part)):
        total += signal_part[i] * (i + 1)
    return total / len(signal_part)

def process_transmission(chunks, calib_map):
    results = []
    for chunk in chunks:
        # Extract meaningful part using slicing
        core = extract_key_segment(chunk)
        
        # Apply real transformation
        calibrated = apply_calibration(core, calib_map)
        
        # Compute weighted coherence score
        score = compute_coherence(calibrated)
        
        # Accumulate only this value
        results.append(score)
    
    # Aggregate final result through weighted sum
    final_weighted_sum = 0
    for i, res in enumerate(results):
        weight = 1 + (i * 0.5)
        final_weighted_sum += res * weight
    
    # Final adjustment based on system constant (hidden in plain sight)
    system_constant = 2  # not in calibration_map to avoid confusion
    final_output = final_weighted_sum * system_constant
    
    # Dead code below — looks like it does something
    if final_output < 0:
        final_output = abs(final_output)
    elif final_output == 0:
        final_output = 999
    
    return int(round(final_output))

# Execution point of interest
final_signal = process_transmission(signal_chunks, calibration_map)

# Print result as required
print(f"Target result: {final_signal}")