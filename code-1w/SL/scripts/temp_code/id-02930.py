import math

def analyze_signal(x):
    # Irrelevant signal processing function (dead code path)
    return sum(math.sin(x[i] * 0.1) for i in range(len(x)))

def generate_checksum(data):
    # Unused checksum logic (distractor)
    chk = 0
    for d in data:
        chk ^= int(d * 3.14) & 0xFF
    return chk

def decode_sequence(seq):
    # Complex but irrelevant decoding (red herring)
    decoded = []
    for s in seq:
        if s % 3 == 0:
            decoded.append(s // 3)
        elif s % 5 == 0:
            decoded.append(s * 2)
    return [x for x in decoded if x < 100]

def transform_coordinates(coords):
    # Distractor: coordinate transformation not used in final result
    lat_offset = 0.001
    lon_factor = 1.005
    return [(c[0] + lat_offset, c[1] * lon_factor) for c in coords]

def calculate_entropy(values):
    # Misleading advanced computation (not part of final answer)
    total = sum(values)
    if total == 0:
        return 0.0
    probs = [v / total for v in values if v > 0]
    return -sum(p * math.log2(p) for p in probs)

def validate_readings(readings):
    # Partially used but mostly distracting validation
    valid = []
    thresholds = {'low': 10, 'high': 100}
    for r in readings:
        if thresholds['low'] < r < thresholds['high']:
            valid.append(r)
    outlier_count = len(readings) - len(valid)
    status_flag = 'CLEAN' if outlier_count == 0 else 'FLAGGED'
    return valid, status_flag  # Only 'valid' is semi-relevant

def compute_aggregate_score(items):
    # Completely irrelevant scoring function (decoy)
    base = sum(items) * 0.85
    bonus = len([x for x in items if x > 50]) * 2.5
    penalty = sum(1 for x in items if x < 5) * 1.75
    return round(base + bonus - penalty, 3)

def process_readings(data, calib):
    # Core relevant function with embedded logic chain
    filtered, _ = validate_readings(data)
    
    # Step 1: Apply calibration using matrix diagonal
    calibrated = [filtered[i] * calib[i % len(calib)] for i in range(len(filtered))]
    
    # Step 2: Normalize to baseline
    baseline = sum(calibrated) / len(calibrated)
    normalized = [x / baseline for x in calibrated]
    
    # Step 3: Detect rising trends
    trend_scores = []
    for i in range(1, len(normalized)):
        if normalized[i] > normalized[i-1]:
            trend_scores.append(1)
        elif normalized[i] < normalized[i-1]:
            trend_scores.append(-1)
    
    # Step 4: Accumulate directional bias
    net_trend = sum(trend_scores)
    
    # Step 5: Apply asymmetric correction based on string-encoded rule
    rule_str = 'UpWeightHighTrend'
    adjustment_factor = 1.0
    if 'High' in rule_str and net_trend > 0:
        adjustment_factor = 1.25
    elif 'Down' in rule_str:
        adjustment_factor = 0.75
    
    adjusted_trend = net_trend * adjustment_factor
    
    # Step 6: Fuse with entropy-like dispersion metric (simplified)
    dispersion = sum(abs(x - 1.0) for x in normalized)
    
    # Step 7: Final diagnostic as weighted combination
    raw_diagnostic = (adjusted_trend * 100) + (dispersion * 10)
    
    # Step 8: Clamp to meaningful range and round
    final_diagnostic = int(max(-1000000, min(1000000, raw_diagnostic)))
    
    return final_diagnostic

# Main execution block
if __name__ == '__main__':
    # Simulated sensor inputs (some out of range to trigger filtering)
    sensor_data = [5, 12, 15, 8, 99, 105, 18, 22, 25, 30, 40, 60, 55]
    
    # Calibration coefficients (only diagonal effect matters)
    calibration_matrix = [1.1, 0.9, 1.05, 1.0, 0.95]
    
    # Decoy data structures (distractors)
    gps_coordinates = [(40.7128, -74.0060), (34.0522, -118.2437), (41.8781, -87.6298)]
    system_flags = {
        'debug_mode': False,
        'encrypt_output': False,
        'log_level': 'VERBOSE',
        'buffer_size': 4096
    }
    processing_pipeline = ['ingest', 'filter', 'calibrate', 'analyze', 'report']
    version_info = 'v2.3.1-beta'.upper().replace('-', '_')
    
    # Dead code paths with misleading computations
    temp_analysis = analyze_signal(sensor_data)
    checksum = generate_checksum(sensor_data)
    decoded_seq = decode_sequence([15, 30, 45, 60])
    geo_adjusted = transform_coordinates(gps_coordinates)
    entropy_metric = calculate_entropy(sensor_data)
    aggregate_score = compute_aggregate_score(sensor_data)
    
    # Key execution point
    final_diagnostic = process_readings(sensor_data, calibration_matrix)
    
    # Output result
    print(f"Result: {final_diagnostic}")