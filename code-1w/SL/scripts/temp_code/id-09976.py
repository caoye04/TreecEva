import math

def analyze_sensor_array():
    # Simulated sensor readings (temperature in millidegrees)
    raw_readings = [23450, 25670, 22890, 24120, 26780, 21340, 27890, 20980]
    
    # Irrelevant auxiliary data (distraction)
    timestamps = ['t0', 't1', 't2', 't3', 't4', 't5', 't6', 't7']
    location_tags = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    metadata_map = dict(zip(location_tags, enumerate(timestamps)))
    
    # Calibration coefficients (some irrelevant)
    base_offset = 1000
    temp_coeff_a = 0.89
    temp_coeff_b = 1.02  # unused red herring
    adjustment_matrix = [1.01, 0.99, 1.03]  # misleading complex structure
    
    # Filtering valid range (22000 to 27000 millidegrees)
    filtered_data = []
    for val in raw_readings:
        if val >= 22000 and val <= 27000:
            filtered_data.append(val)
    
    # Dead code path - never executed (distractor)
    def legacy_correction(x):
        return x * 0.98 + 50  # obsolete algorithm
    
    # Unused lambda (red herring)
    outlier_penalty = lambda x: x * 1.5 if x > 30000 else x
    
    # Real processing begins here
    calibration_factor = math.log(2.71828) * temp_coeff_a  # effectively 0.89
    
    # Complex-looking but unused transformation
    transformed = list(map(lambda x: (x - base_offset) ** 0.5, raw_readings))
    normalized = [round((x - min(raw_readings)) / (max(raw_readings) - min(raw_readings)) * 100) for x in raw_readings]
    
    # Decoy statistical computation
    avg_normalized = sum(normalized) / len(normalized)
    deviation_score = sum(abs(n - avg_normalized) for n in normalized)
    
    # Actual key function with nested logic
    def process_readings(data, factor):
        result = 0
        for i, val in enumerate(data):
            # Apply calibration and convert to degrees
            adjusted = (val / 1000.0) * factor
            
            # Conditional weighting based on position
            if i % 2 == 0:
                adjusted *= 1.1
            else:
                adjusted *= 0.9
            
            # Accumulate with rounding drift simulation
            result += round(adjusted, 2)
            
            # Nested conditional with bit manipulation distraction
            if result > 100:
                # Bitwise ops that don't affect outcome (misleading)
                dummy = (int(result) & 255) ^ 16
                result -= 0.01  # minor correction, actually relevant
        
        # Final nonlinear adjustment
        if result > 200:
            result = math.sqrt(result) * 8
        return int(round(result))

    final_diagnostic = process_readings(filtered_data, calibration_factor)
    
    # Irrelevant post-processing (dead end)
    diagnostic_log = []
    for tag, (idx, ts) in metadata_map.items():
        if idx < len(filtered_data):
            diagnostic_log.append(f'{tag}:{ts}')
    
    # Unused sorting operation (distraction)
    sorted_pairs = sorted(zip(filtered_data, normalized), key=lambda x: x[1], reverse=True)
    
    # Output the target variable
    print(f'Target result: {final_diagnostic}')

analyze_sensor_array()