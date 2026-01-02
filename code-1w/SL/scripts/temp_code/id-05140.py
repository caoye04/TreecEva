def monitor_sensor_drift(readings):
    drift = 0
    for i, val in enumerate(readings):
        if i > 0 and abs(val - readings[i-1]) > 0.5:
            drift += 0.1
    return drift

def compute_phase_coherence(sequence):
    coherence = 0
    for a, b in zip(sequence, sequence[1:]):
        if a == b:
            coherence += 1
    return coherence / len(sequence) if sequence else 0

def encrypt_sequence(ids):
    encrypted = []
    for i, num in enumerate(ids):
        shifted = (num << 2) ^ 255
        encrypted.append(shifted)
    return encrypted

def validate_calibration_points(points):
    valid_count = 0
    for p in points:
        x, y = p
        if x >= 0 and y >= 0 and (x + y) % 2 == 0:
            valid_count += 1
    return valid_count

def decode_operational_mode(mode_code):
    mode_map = {1: 'idle', 2: 'active', 3: 'standby', 4: 'diagnostic'}
    return mode_map.get(mode_code, 'unknown')

def analyze_system_state(phases):
    total_weight = 0
    for i, phase in enumerate(phases):
        mode_str = decode_operational_mode(phase['mode'])
        if mode_str == 'diagnostic':
            sensor_drift = monitor_sensor_drift(phase['sensors'])
            coherence = compute_phase_coherence(phase['sequence'])
            calibration_valid = validate_calibration_points(phase['calibration'])
            
            # Irrelevant encryption call (distractor)
            _ = encrypt_sequence([10, 20, 30])
            
            # Misleading intermediate that looks important
            temp_score = (coherence * 100) + calibration_valid
            if temp_score > 75:
                total_weight += phase['weight']
            
            # Dead code path - never executed due to logic
            anomaly_flag = False
            if sensor_drift < 0:
                anomaly_flag = True  # Unreachable
                for _ in range(10):
                    anomaly_flag = not anomaly_flag  # Decoy loop

    # Key computation
    adjustment_factor = 0.85
    raw_diagnostic = int(total_weight * adjustment_factor)
    
    # Multiple assignments with distractors
    base_offset = 17
    padding = base_offset // 3  # 5
    final_diagnostic = raw_diagnostic + padding
    
    # Unused but plausible-looking transformation
    _ = [(x.upper(), y*2) for x, y in zip(['a','b'], [1,2])]  # List comp red herring
    
    return final_diagnostic

# Main execution data
operational_phases = [
    {
        'mode': 1,
        'sensors': [1.0, 1.1, 1.6, 2.2],
        'sequence': [1, 1, 0, 1],
        'calibration': [(0,0), (1,1), (2,2)],
        'weight': 50
    },
    {
        'mode': 4,
        'sensors': [0.5, 0.6, 1.2, 1.3],
        'sequence': [1, 1, 1, 0],
        'calibration': [(0,2), (2,4), (3,5), (4,4)],
        'weight': 80
    },
    {
        'mode': 4,
        'sensors': [2.0, 2.1, 2.7, 3.3],
        'sequence': [0, 0, 0, 0],
        'calibration': [(1,1), (3,3)],
        'weight': 120
    }
]

# Execute key statement
final_diagnostic = analyze_system_state(operational_phases)
print(f"Target result: {final_diagnostic}")