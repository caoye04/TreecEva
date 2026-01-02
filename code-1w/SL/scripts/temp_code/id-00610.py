import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_values = [127, 255, 192, 64, 80]
    timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800]
    metadata = {'unit': 'lux', 'version': '2.1', 'mode': 'auto'}
    
    # Irrelevant intermediate transformation (distractor)
    temp_map = {i: val ** 0.5 for i, val in enumerate(raw_values) if val > 100}
    norm_factor = sum(temp_map.values()) / len(temp_map) if temp_map else 1.0
    
    # Actual relevant data structure
    return [{'id': i, 'val': v, 'ts': t} for i, (v, t) in enumerate(zip(raw_values, timestamps))]


def generate_calibration_matrix(seed=42):
    # Generate a 5x5 calibration matrix using modular arithmetic and bit shifts
    matrix = [[0]*5 for _ in range(5)]
    val = seed
    for i in range(5):
        for j in range(5):
            val = (val * 1103515245 + 12345) & 0x7FFFFFFF
            matrix[i][j] = (val % 17) - 8  # Range: -8 to 8
    
    # Dead code path - never used (red herring)
    if any(x > 5 for row in matrix for x in row):
        alternate = [[x * 0.5 for x in row] for row in matrix]
        return alternate  # This branch is logically unreachable due to modulo
    
    return matrix

# Unused helper function (decoy)
def validate_checksum(data):
    chk = 0
    for item in data:
        chk ^= item.get('val', 0) << 2
    return chk % 100 == 42

# Auxiliary transformation with partial relevance
def apply_noise_filter(signal):
    filtered = []
    for i, s in enumerate(signal):
        adjusted = s['val']
        if i % 2 == 0:
            adjusted = int(adjusted * 0.9)
        else:
            adjusted = int(adjusted * 1.1)
        filtered.append({**s, 'val': adjusted})
    
    # Distractor: irrelevant aggregation
    avg_post = sum(f['val'] for f in filtered) / len(filtered)
    outlier_count = len([f for f in filtered if abs(f['val'] - avg_post) > 50])
    
    return filtered

# Core processing logic with conditional expressions and dictionary ops
def compute_entropy(readings):
    counts = {}
    total = 0
    for r in readings:
        bucket = r['val'] // 32
        counts[bucket] = counts.get(bucket, 0) + 1
        total += 1
    
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p) if p > 0 else 0
    
    return entropy

# Main processing with zip, enumerate, and complex control flow
def process_readings(data, matrix):
    # Apply calibration using matrix multiplication (only first 5 elements)
    calibrated = []
    for i, entry in enumerate(data[:5]):
        raw_val = entry['val']
        correction = 0
        for j in range(5):
            if i < len(matrix) and j < len(matrix[i]):
                correction += matrix[i][j] * ((raw_val >> j) & 1)  # Bitwise contribution
        calibrated.append(raw_val + correction)
    
    # Irrelevant secondary processing chain (distraction)
    derived_signals = []
    for c in calibrated:
        signal = {}
        signal['raw'] = c
        signal['squared'] = c ** 2
        signal['mod7'] = c % 7
        signal['is_peak'] = True if c > 200 and c % 2 == 0 else False
        derived_signals.append(signal)
    
    # Real computation embedded within noise
    weighted_sum = 0
    weights = [0.1, 0.2, 0.4, 0.2, 0.1]
    for idx, (val, w) in enumerate(zip(calibrated, weights)):
        weighted_sum += val * w
    
    # Use of enumerate and zip in filtering (actually used)
    status_flags = [1 if d['val'] > 100 else 0 for d in data]
    paired = list(zip(calibrated, status_flags))
    active_calibrated = [c for c, f in paired if f == 1]
    
    # Conditional expression determining final output
    base_metric = weighted_sum if len(active_calibrated) >= 3 else compute_entropy(data)
    
    # Final transformation involving dictionary operations
    config = {'scale': 1.75, 'offset': -12, 'active': True}
    final_value = base_metric * config.get('scale', 1.0) + config.get('offset', 0)
    
    # Key result variable
    final_diagnostic = int(round(final_value))
    
    # Multiple unused intermediate variables (distractors)
    summary_stats = {
        'max_raw': max(d['val'] for d in data),
        'min_cal': min(calibrated),
        'range': max(calibrated) - min(calibrated),
        'count_even': len([c for c in calibrated if c % 2 == 0]),
        'flag_density': sum(status_flags) / len(status_flags)
    }
    
    # Red herring: complex but unused calculation
    if summary_stats['flag_density'] > 0.5:
        hypothetical = 0
        for k, v in sorted(config.items()):
            if isinstance(v, (int, float)):
                hypothetical += abs(v) * 100
        summary_stats['hypothetical_score'] = hypothetical
    
    return final_diagnostic

# Execution sequence
sensor_data = collect_sensor_data()
sensor_data = apply_noise_filter(sensor_data)  # Note: this modifies values but original path still works
calibration_matrix = generate_calibration_matrix()
final_diagnostic = process_readings(sensor_data, calibration_matrix)
print(f"Result: {final_diagnostic}")