import math

# Simulated sensor fusion system for environmental monitoring
def collect_environmental_data():
    base_readings = [2.1, 3.5, 4.8, 5.2, 6.7]
    timestamps = [1623456780, 1623456790, 1623456800, 1623456810, 1623456820]
    
    # Irrelevant auxiliary data (distractor)
    location_codes = ['LOC-A', 'LOC-B', 'LOC-C', 'LOC-D', 'LOC-E']
    device_status = {code: 'ACTIVE' if i % 2 == 0 else 'STANDBY' for i, code in enumerate(location_codes)}
    
    # Real processing path
    processed = []
    for val in base_readings:
        adjusted = round(val * 1.08 + 0.3, 2)
        processed.append(adjusted)
    
    return list(zip(timestamps, processed))


def generate_calibration_reference():
    # Generate a 3x3 calibration matrix with dummy transformations
    base_factors = [0.98, 1.02, 0.99]
    calibration_matrix = [[f * 0.1 for _ in range(3)] for f in base_factors]
    
    # Fill actual values
    for i in range(3):
        for j in range(3):
            calibration_matrix[i][j] = base_factors[i] * (0.95 + j * 0.05)
    
    # Unused but misleading computation (red herring)
    temp_normalization = sum([sum(row) for row in calibration_matrix]) / 9
    threshold_map = {i: temp_normalization * (1.1 ** i) for i in range(5)}
    
    return calibration_matrix

# Legacy function - never called (dead code path)
def deprecated_analysis(data):
    cumulative_score = 0
    for item in data:
        if isinstance(item, tuple):
            cumulative_score += item[1] * 0.7
    return int(cumulative_score % 100)

# Auxiliary transformation not used in main flow
def transform_coordinates(x, y):
    radius = math.sqrt(x*x + y*y)
    angle = math.atan2(y, x)
    return (radius, angle)

# Bit manipulation decoy (irrelevant to final result)
def scramble_value(n):
    n = ((n << 3) & 0xFF) | (n >> 5)
    n ^= 0b10101010
    n = (n + 17) % 256
    return n

# Main processing pipeline
def extract_key_features(raw_data):
    features = []
    for ts, val in raw_data:
        # Extract time-based characteristics
        sec = ts % 100
        category = 'EVEN' if sec % 2 == 0 else 'ODD'
        
        # Compute derived metrics (some irrelevant)
        squared_dev = (val - 4.5) ** 2
        inverted = 1 / (1 + math.exp(-val))
        binned = int((val - 2) // 1)
        
        # Only 'val', 'binned', and 'category' are actually used later
        features.append({
            'raw': val,
            'bin': binned,
            'cat': category,
            'sq_dev': squared_dev,      # unused
            'sigmoid': inverted         # unused
        })
    return features


def apply_spatial_filter(features, kernel_size=3):
    padded = [features[0]] * (kernel_size // 2) + features + [features[-1]] * (kernel_size // 2)
    filtered = []
    
    for i in range(len(features)):
        window = padded[i:i+kernel_size]
        avg_bin = sum(pt['bin'] for pt in window) / len(window)
        # Only this transformed value is eventually used
        filtered.append({'smoothed_bin': avg_bin})
    
    # Decoy aggregation
    total_spread = sum(f['smoothed_bin'] for f in filtered)
    spread_factor = total_spread / len(filtered) if filtered else 0
    
    return filtered


def compute_integrity_check(processed_features):
    # Checksum based on internal consistency (not used in final output)
    checksum = 0
    for feat in processed_features:
        bin_val = feat.get('smoothed_bin', 0)
        checksum ^= int(bin_val * 100) & 0xFFFF
    return checksum


def process_readings(sensor_data, calibration_matrix):
    # Initial extraction
    extracted = extract_key_features(sensor_data)
    
    # Apply filter
    filtered = apply_spatial_filter(extracted)
    
    # Dummy integrity verification (side effect only)
    verify_code = compute_integrity_check(filtered)
    
    # Core calculation begins here
    total_impact = 0.0
    for i, entry in enumerate(filtered):
        smooth_val = entry['smoothed_bin']
        
        # Simulated matrix interaction (only first row used)
        if i < len(calibration_matrix[0]):
            factor = calibration_matrix[0][i]
            total_impact += smooth_val * factor
        
        # Red herring: complex conditional that never triggers due to data range
        special_flag = False
        if smooth_val > 10 and i % 4 == 0:
            special_flag = True
            aux = math.log(smooth_val) * 1000
            # This block is unreachable with current data

    # Final nonlinear transformation
    if total_impact > 0:
        final_diagnostic = math.floor((total_impact ** 1.5) * 100) / 100
    else:
        final_diagnostic = 0.0
    
    # Irrelevant bit manipulation on float (converted to int bits)
    raw_bits = scramble_value(int(abs(final_diagnostic) * 1000) % 256)
    
    # Critical print statement
    print(f"Result: {final_diagnostic}")
    return final_diagnostic


# Orchestration sequence
if __name__ == "__main__":
    # Initialize core data
    sensor_data = collect_environmental_data()
    calibration_matrix = generate_calibration_reference()
    
    # Phantom variables to distract
    audit_log = set()
    audit_log.add("INIT")
    system_uptime = 12745
    last_sync = 1623456000
    
    # Key execution point
    final_diagnostic = process_readings(sensor_data, calibration_matrix)