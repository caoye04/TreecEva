import math

# Simulated sensor array data from environmental monitoring station
def fetch_sensor_data():
    raw_values = [256, 192, 128, 64, 32, 16, 8, 4, 2, 1]
    offset_correction = 0.75
    adjusted = [x + offset_correction for x in raw_values]
    return adjusted

# Legacy calibration function (partially deprecated)
def legacy_calibrate(x):
    if x < 50:
        return x * 1.2
    elif x < 200:
        return x * 1.1
    else:
        return x * 1.05

# Signal processing pipeline
def preprocess_signal(signal_list):
    filtered = []
    noise_floor = 3.5
    for val in signal_list:
        if val > noise_floor:
            # Apply logarithmic compression
            compressed = math.log(val) * 10
            filtered.append(round(compressed, 2))
    return filtered

# Secondary transformation - applies windowing function
def apply_hamming_window(data):
    size = len(data)
    windowed = []
    for i in range(size):
        coefficient = 0.54 - 0.46 * math.cos((2 * math.pi * i) / (size - 1))
        windowed.append(data[i] * coefficient)
    return windowed

# Checksum validation (distractor - not used in final result)
def compute_checksum(arr):
    checksum = 0
    for item in arr:
        checksum ^= int(item)  # Bitwise XOR hash
    return checksum

# Data integrity verification (unused path)
def verify_integrity(trace):
    if len(trace) == 0:
        return False
    unique_count = len(set(trace))
    total_count = len(trace)
    return unique_count / total_count > 0.7

# Main analysis engine
def analyze_readings(readings):
    # Irrelevant intermediate transformation (red herring)
    temp_snapshot = readings[::2]  # Every other reading
    snapshot_sum = sum(temp_snapshot)
    
    # Decoy statistical calculation
    mean_val = sum(readings) / len(readings)
    variance_proxy = sum([(x - mean_val) ** 2 for x in readings]) / len(readings)
    stability_index = 1 / (1 + variance_proxy)  # Looks important, unused

    # Critical processing branch
    threshold_filtered = [x for x in readings if x > 15.0]
    if len(threshold_filtered) == 0:
        return -1
    
    # Transform via modular reduction and bit manipulation
    processed = []
    for x in threshold_filtered:
        truncated = int(x)
        # Combine arithmetic and bitwise ops
        modded = (truncated % 7) ^ 5  # XOR with prime
        processed.append(modded)
    
    # Final aggregation using set operations to remove duplicates
    unique_results = list(set(processed))
    sorted_results = sorted(unique_results, reverse=True)
    
    # Key computation: weighted sum based on position
    final_value = 0
    for idx, num in enumerate(sorted_results):
        final_value += num * (3 ** idx)  # Exponential weighting
    
    return final_value

# Unused diagnostic routine (dead code path)
def generate_report(data):
    report_lines = []
    for i, val in enumerate(data):
        hex_rep = hex(int(val))
        report_lines.append(f"Sample{i}: {val} ({hex_rep})")
    return '\n'.join(report_lines)

# Execution flow
if __name__ == "__main__":
    # Step 1: Fetch raw sensor input
    raw_signals = fetch_sensor_data()
    
    # Step 2: Apply legacy calibration (irrelevant but plausible)
    calibrated_signals = [legacy_calibrate(x) for x in raw_signals]
    
    # Step 3: Preprocess signal chain
    processed_signals = preprocess_signal(calibrated_signals)
    
    # Step 4: Apply hamming window (distraction - not used later)
    windowed_signals = apply_hamming_window(processed_signals)
    
    # Step 5: Compute unused checksum
    dummy_checksum = compute_checksum(processed_signals)
    
    # Step 6: Perform actual analysis on processed_signals (bypassing windowed)
    final_diagnostic = analyze_readings(processed_signals)
    
    # Output target result
    print(f"Target result: {final_diagnostic}")