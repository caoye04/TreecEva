import itertools

# Simulated environmental sensor fusion system
# Combines temperature, pressure, and humidity with noise filtering

def collect_sensor_data(base_temp, elevation):
    raw_readings = []
    for i in range(5):
        temp_offset = (i ^ 3) * 0.5
        pressure = (base_temp + 273.15) * 2.1 - (elevation // 100)
        humidity = 40 + (i % 4) * 15
        raw_readings.append({
            'temp': round(base_temp + temp_offset, 2),
            'pressure': pressure,
            'humidity': humidity,
            'sensor_id': f'TH{i}{elevation}'
        })
    return raw_readings

# Irrelevant helper - simulates calibration drift (not used in final path)
def apply_drift_correction(data_list):
    for entry in data_list:
        entry['temp'] *= 0.98
        entry['pressure'] *= 1.02
    return data_list

# Red herring function: looks important but unused in critical path
def validate_checksum(record_str):
    checksum = 0
    for char in record_str:
        if char.isdigit():
            checksum ^= int(char)
        else:
            checksum += ord(char) % 7
    return checksum % 13 == 0

# Distractor: complex string transformation with no impact
def generate_report_header(category, level):
    prefix = category.upper()[:3]
    code = ''.join([chr((ord(c) + level) % 26 + 65) for c in prefix])
    suffix = str(level * 7).zfill(3)
    return f'{code}-{suffix}-REV2'

# Unused recursive validation (dead path)
def recursive_integrity_check(value, depth=0):
    if depth >= 3 or value < 10:
        return value == 7
    return recursive_integrity_check(value // 2, depth + 1)

# Real processing begins here — filters anomalous readings
def filter_outliers(readings):
    temps = [r['temp'] for r in readings]
    mean_temp = sum(temps) / len(temps)
    filtered = [r for r in readings if abs(r['temp'] - mean_temp) <= 1.0]
    return filtered

# Transforms multiple sensor inputs using bitwise fusion
def fuse_sensors(filtered_data):
    fused_values = []
    for r in filtered_data:
        # Bit manipulation: pack pressure and humidity into composite signal
        p_val = int(r['pressure']) & 0xFF  # Use lower byte
        h_val = int(r['humidity']) << 2  # Shift to avoid overlap
        fused_signal = p_val ^ h_val  # XOR fusion
        fused_values.append(fused_signal)
    return fused_values

# Main analysis: computes diagnostic from fused signals
def analyze_fusion_pattern(fused_list):
    if not fused_list:
        return 0
    
    # Use itertools to generate pairwise differences
    pairs = list(itertools.combinations(fused_list, 2))
    diffs = [abs(a - b) for a, b in pairs]
    
    # Compute statistical fingerprint
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    max_fused = max(fused_list) if fused_list else 0
    
    # Diagnostic formula: combination of spread and magnitude
    diagnostic_raw = (avg_diff * 1.7) + (max_fused * 0.3)
    
    # Final adjustment based on count parity
    adjustment = len(fused_list) % 4
    return int(diagnostic_raw + adjustment)

# Orchestration function — only this one matters
def process_readings(data_src):
    # Step 1: Filter temperature outliers
    clean_data = filter_outliers(data_src)
    
    # Step 2: Fuse remaining sensor signals
    fused_signals = fuse_sensors(clean_data)
    
    # Step 3: Analyze pattern and produce diagnostic code
    result_code = analyze_fusion_pattern(fused_signals)
    
    # Dead code branch — looks like it updates something, but doesn't affect output
    if result_code > 100:
        for item in clean_data:
            item['flag'] = 'HIGH_RISK'
            item['timestamp'] = 'N/A'
    
    # Key computation happens here — final diagnostic
    final_diagnostic = result_code + 10  # Final offset
    return final_diagnostic

# Irrelevant global constants (distractors)
CALIBRATION_MODE = False
MAX_BUFFER_SIZE = 2048
RETRY_LIMIT = 3

# Simulate real-world input
sensor_data = collect_sensor_data(base_temp=22.5, elevation=750)

# Apply irrelevant string operations on sensor IDs
ids = [s['sensor_id'] for s in sensor_data]
reversed_parts = [part[::-1] for part in ids]
header_tag = generate_report_header('environment', 5)

# Execute main logic
final_diagnostic = process_readings(sensor_data)
print(f"Result: {final_diagnostic}")