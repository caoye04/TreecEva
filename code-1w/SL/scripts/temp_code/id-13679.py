from itertools import compress, cycle

def analyze_sensor_stream(raw_readings, config):
    # Irrelevant pre-processing: Normalize timestamps (not used in final result)
    base_time = raw_readings[0][0] if raw_readings else 0
    time_normalized = [(t - base_time, val) for t, val in raw_readings]

    # Distractor: Simulate calibration offset (unused)
    calibration_curve = [abs(val * 0.02) for t, val in time_normalized[:10]]
    offset_correction = sum(calibration_curve) / len(calibration_curve) if calibration_curve else 0.0

    # Relevant: Extract values and apply dynamic threshold mask
    values = [val for t, val in raw_readings]
    moving_avg = [sum(values[i:i+3]) / 3 for i in range(len(values)-2)]
    anomalies = [i+2 for i, v in enumerate(moving_avg) if abs(values[i+2] - v) > config['noise_floor']]

    # Mask generation using enumerate and zip (key python feature)
    mask = [False] * len(values)
    for idx, _ in enumerate(values):
        if idx in anomalies:
            mask[idx] = True

    filtered_data = list(compress(values, mask))  # Use of itertools

    # Dead code path: Unused smoothing function
    def smooth(x, factor=0.3):
        return [x[0]] + [factor * x[i] + (1-factor) * x[i-1] for i in range(1, len(x))]

    # Decoy data structure with misleading computations
    stats_summary = {
        'peak': max(values) if values else 0,
        'variance': sum((v - sum(values)/len(values))**2 for v in values)/len(values) if values else 0,
        'clipped_count': sum(1 for v in values if v > config.get('clip_limit', 999))
    }

    # Unused recursive helper (red herring)
    def integrate_signal(data, acc=0.0):
        if not data:
            return acc
        return integrate_signal(data[1:], acc + abs(data[0]))

    # Key mapping logic with dictionary operations
    level_map = {'low': 1, 'med': 2, 'high': 3}
    threshold_map = {level: config['base_threshold'] * mult for level, mult in level_map.items()}

    # Conditional override that looks important but is never triggered
    if config.get('safe_mode') and len(filtered_data) > 100:
        threshold_map = {k: v * 0.5 for k, v in threshold_map.items()}

    # Core processing function (appears complex but deterministic)
    def process_readings(data, limits):
        if not data:
            return -1
        
        # Use of enumerate and zip to pair indices and categorized levels
        categorize = lambda x: 'low' if x < limits['low'] else 'med' if x < limits['high'] else 'high'
        categories = [categorize(x) for x in data]
        indexed_pairs = list(enumerate(categories))
        
        # Simulated multi-pass analysis (only last pass matters)
        scores = []
        for i, cat in indexed_pairs:
            base_score = level_map[cat] * (i % 4 + 1)
            if i % 7 == 0:
                base_score *= -1  # occasional inversion
            scores.append(base_score)
        
        # Final aggregation with bitwise manipulation (looks cryptic)
        aggregate = 0
        for s in scores:
            aggregate ^= s  # XOR accumulation
            aggregate = (aggregate + len(categories)) % 9997
        
        # One-time adjustment based on data length parity
        if len(data) % 2 == 1:
            aggregate += 13
        
        return aggregate

    # Execution point of interest
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Distractor: Unused signal reconstruction
    pattern_cycle = cycle([1, -1, 0])
    reconstructed = [v * next(pattern_cycle) for v in filtered_data]

    # Print required output
    print(f"Result: {final_diagnostic}")
    return final_diagnostic

# Input data and configuration
readings = [
    (100, 15), (101, 18), (102, 100), (103, 22), (104, 19),
    (105, 25), (106, 95), (107, 20), (108, 18), (109, 211),
    (110, 17), (111, 23), (112, 88), (113, 19), (114, 20)
]

config_params = {
    'noise_floor': 70,
    'base_threshold': 12,
    'clip_limit': 200,
    'safe_mode': False  # Prevents unused branch
}

# Execute
analyze_sensor_stream(readings, config_params)