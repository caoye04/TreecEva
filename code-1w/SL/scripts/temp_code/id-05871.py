import itertools

# Sensor array simulation with noise and calibration data
def collect_sensor_data():
    raw_readings = [127, 255, 192, 64, 224, 32, 160, 96]
    timestamps = list(range(1000, 1008))
    sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
    
    # Misleading transformation: irrelevant frequency modulation
    modulated = [(x * 1.05) % 256 for x in raw_readings]
    paired_data = list(zip(timestamps, sensor_ids, raw_readings, modulated))
    
    # Dead code path: unused smoothing function
    def smooth_signal(signal):
        return [sum(signal[i:i+3]) / 3 for i in range(len(signal)-2)]
    
    return paired_data

# Auxiliary function: checksum validation (distractor)
def validate_checksum(data_seq):
    checksum = 0
    for val in data_seq:
        checksum = (checksum + val) & 0xFF
    return checksum == 0x7F  # Rare condition, not used in main logic

# Data filtering based on bit-pattern criteria
def filter_by_bit_criteria(raw_entries):
    result = []
    high_noise_floor = 200
    low_signal_threshold = 64
    
    for ts, sid, val, mod_val in raw_entries:
        # Irrelevant signal quality metric
        quality_score = (val ^ 0xFF) & (val >> 4)
        
        # Actual filtering: keep values where top two bits are different
        if ((val & 0x80) >> 7) ^ ((val & 0x40) >> 6):  # XOR of bit 7 and 6
            result.append((ts, sid, val))
    
    # Distractor: unused outlier detection
    outliers = [entry for entry in raw_entries if entry[2] > high_noise_floor]
    
    return result

# Core processing with arithmetic and set operations
def process_readings(entries, factor):
    base_values = [entry[2] for entry in entries]
    
    # Bit manipulation chain: invert, shift, mask
    transformed = []
    for v in base_values:
        inverted = v ^ 0xFF
        shifted = (inverted << 1) & 0xFF
        masked = shifted & ~(1 << 0)  # Clear LSB
        transformed.append(masked)
    
    # Use of enumerate and zip: index-aware pairing
    indexed = list(enumerate(transformed))
    paired_shifts = list(zip(transformed[:-1], transformed[1:]))
    
    # Set operations to find unique transition patterns
    diffs = set(abs(a - b) for a, b in paired_shifts)
    common_diffs = diffs.intersection({16, 32, 48})
    
    # Decoy aggregation: unused statistical measures
    mean_decoy = sum(base_values) / len(base_values) if base_values else 0
    variance_proxy = sum((x - mean_decoy) ** 2 for x in base_values)
    
    # Critical arithmetic chain
    accumulator = 0
    for i, t_val in indexed:
        if i % 2 == 0:
            accumulator += t_val * factor
        else:
            accumulator -= t_val // factor
    
    # Final transformation using itertools
    repeated_acc = list(itertools.accumulate([accumulator] * 3, lambda a, x: (a * 2) % 1000))
    final_value = repeated_acc[-1]
    
    # Secondary red herring: complex string-based encoding (unused)
    status_flags = ['OK' if x > 100 else 'LOW' for x in transformed]
    encoded_status = ''.join(f'{ord(f[0]):02x}' for f in status_flags)
    
    return int(final_value)

# Main execution flow
if __name__ == '__main__':
    # Calibration constant (critical but obscured)
    calibration_factor = 3
    
    # Unused alternate calibration table (distractor)
    alt_calibrations = {2: 'LO', 3: 'MED', 4: 'HIGH'}
    metadata_log = [{'version': 'A1', 'mode': 'DIAG'}, {'version': 'B2', 'mode': 'TEST'}]
    
    # Collect and filter sensor data
    all_entries = collect_sensor_data()
    filtered_data = filter_by_bit_criteria(all_entries)
    
    # Compute diagnostic result
    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")