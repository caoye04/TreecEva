import math

# Simulated sensor data from satellite subsystems
def collect_thermal_readings():
    readings = [
        [23.4, 25.1, 24.8, 26.0, 27.3],
        [28.1, 29.5, 30.2, 28.9, 27.6],
        [30.5, 32.4, 31.8, 33.0, 32.1],
        [26.7, 25.9, 24.4, 23.8, 22.9],
        [24.1, 25.5, 26.7, 25.9, 27.2]
    ]
    return readings

# Legacy function for deprecated calibration (red herring)
def apply_legacy_calibration(data):
    calibrated = []
    for row in data:
        calibrated.append([x * 0.92 + 1.2 for x in row])
    return calibrated

# Misleading diagnostic that appears relevant but is unused
def calculate_anomaly_index(matrix):
    anomalies = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 30.0 or matrix[i][j] < 25.0:
                anomalies += 1
    return anomalies * 0.7

# Irrelevant string processing to simulate log parsing
def parse_system_logs(log_lines):
    keyword_stats = {}
    all_text = " ".join(log_lines).lower()
    words = all_text.split()
    for word in ['error', 'warning', 'fault', 'reset']:
        keyword_stats[word] = all_text.count(word)
    # Unused transformation
    normalized = {k: v / (sum(keyword_stats.values()) + 1e-8) for k, v in keyword_stats.items()}
    return sum(keyword_stats.values())  # Only total count used

# Bit manipulation decoy for 'security check'
def validate_signature(bits):
    checksum = 0
    for b in bits:
        checksum ^= b
        checksum = (checksum << 1) & 0xFF | (checksum >> 7)
    return checksum % 13 == 0

# Real core logic: detect thermal asymmetry patterns
def compute_gradient_flow(matrix):
    gradients = []
    for i in range(len(matrix) - 1):
        row_grad = []
        for j in range(len(matrix[i]) - 1):
            dx = matrix[i][j+1] - matrix[i][j]
            dy = matrix[i+1][j] - matrix[i][j]
            magnitude = math.sqrt(dx*dx + dy*dy)
            row_grad.append(magnitude)
        gradients.append(row_grad)
    return gradients

# Main integrity computation
def compute_integrity_score(matrix, flags):
    # Step 1: Compute actual gradient field
    flow = compute_gradient_flow(matrix)
    
    # Step 2: Flatten and analyze statistical properties
    flat_flow = [item for row in flow for item in row]
    mean_flow = sum(flat_flow) / len(flat_flow)
    variance = sum((x - mean_flow) ** 2 for x in flat_flow) / len(flat_flow)
    std_dev = math.sqrt(variance)
    
    # Step 3: Apply physical constraint model
    stability_ratio = 0
    for row in flow:
        for g in row:
            if g < mean_flow + 2 * std_dev:
                stability_ratio += 1
    stability_ratio /= len(flat_flow)
    
    # Step 4: Incorporate system flags using bit logic
    flag_value = 0
    for f in flags:
        if f == 'OVERHEAT':
            flag_value |= 0x01
        elif f == 'PRESSURE_LOSS':
            flag_value |= 0x02
        elif f == 'VIBRATION_ALERT':
            flag_value |= 0x04
    
    # Step 5: Critical calculation path
    base_score = 1000 * stability_ratio
    if flag_value & 0x01:
        base_score *= 0.6
    if flag_value & 0x02:
        base_score *= 0.8
    if flag_value & 0x04:
        base_score *= 0.9
    
    # Step 6: Final nonlinear transformation
    final_score = int(base_score * (1 + math.sin(math.pi * stability_ratio / 2)))
    
    # Decoy dictionary operations (unused)
    diagnostics = {
        'readings_processed': len(matrix),
        'gradient_rows': len(flow),
        'max_gradient': max(flat_flow),
        'flag_code': format(flag_value, '03b'),
        'calibration_offset': 1.22  # Unused
    }
    
    # Dead code branch (never executed due to flag structure)
    if 'CRITICAL_FAILURE' in flags:
        final_score = -999  # This will not trigger
    
    return final_score

# Execution begins here
if __name__ == '__main__':
    # Collect primary sensor data
    raw_readings = collect_thermal_readings()
    
    # Apply fake calibration (result not used)
    _ = apply_legacy_calibration(raw_readings)
    
    # Parse logs for distraction
    logs = [
        'System boot OK',
        'Sensor array online',
        'No errors detected',
        'Thermal regulation active'
    ]
    log_severity = parse_system_logs(logs)
    
    # Generate decoy anomaly index
    _ = calculate_anomaly_index(raw_readings)
    
    # Create bit signature for irrelevant validation
    signature_bits = [72, 69, 65, 84, 72, 69, 82]  # 'HEATHER' in ASCII
    _ = validate_signature(signature_bits)
    
    # Actual system flags (only these affect result)
    system_alerts = ['OVERHEAT', 'VIBRATION_ALERT']
    
    # Core computation
    thermal_matrix = raw_readings
    final_diagnostic = compute_integrity_score(thermal_matrix, system_alerts)
    
    # Output target variable
    print(f"Result: {final_diagnostic}")