import itertools

def analyze_noise_patterns(logs):
    # Irrelevant function: analyzes noise but not used in main logic
    return sum(len(log) for log in logs if 'ERR' in log)

def preprocess_sensor_input(raw):
    # Distractor: looks important but unused in critical path
    filtered = [x for x in raw if x > 0]
    return [x ** 0.5 for x in filtered if x % 2 == 1]

def validate_checksum(sequence):
    # Decoy function with misleading relevance
    chk = 0
    for i, val in enumerate(sequence):
        chk ^= (val + i) % 7
    return chk == 5

def transform_coordinates(coords):
    # Dead code path — never called
    return [(y * 2, x // 3) for x, y in coords]

def calculate_harvest_efficiency(config, readings):
    # Core logic buried under distractions
    base_yield = 0
    adjustment_factor = 0.87
    
    # Unrelated temporary variables
    temp_log = ['SYS_OK', 'INIT_DONE']
    debug_flag = len(temp_log) > 1
    
    # Real logic begins
    flat_readings = list(itertools.chain.from_iterable(readings))
    valid_sensors = [r for r in flat_readings if r < 1000 and r % 3 != 0]
    
    # Misleading intermediate calculation
    outlier_score = sum(1 for r in flat_readings if r > 950) * 17
    
    for section in config:
        width, height, crop_type = section
        area = width * height
        
        # Conditional branching with red herring
        if crop_type == 'WHEAT':
            base_yield += area * 2.3
        elif crop_type == 'CORN':
            base_yield += area * 1.9
        else:
            base_yield += area * 1.5  # Default case actually used
    
    # Another decoy variable
    calibration_offset = ''.join([str(int(adjustment_factor * 100))])
    
    # Key transformation using string method
    tag = "yield_adjust_{}".format(calibration_offset).strip('_')
    if 'adjust' in tag:
        base_yield *= adjustment_factor
    
    # Final computation
    efficiency_ratio = len(valid_sensors) / (len(flat_readings) + 1e-6)
    final_output = base_yield * efficiency_ratio
    
    # This line produces the answer
    final_output = int(final_output + 0.5)  # Round to nearest integer
    
    return final_output

# Main execution block
if __name__ == '__main__':
    # Input data setup
    area_config = [
        (12, 8, 'BARLEY'),
        (15, 6, 'OATS'),
        (10, 10, 'RYE')
    ]

    sensor_data = [
        [200, 305, 1001, 700],
        [150, 980, 310],
        [420, 960, 777, 1010]
    ]

    # Unused variables - red herrings
    system_logs = ['BOOT_OK', 'ERR_SENSOR_3', 'SYNC_FAIL', 'ERR_SENSOR_5']
    checksum_valid = validate_checksum([2, 4, 6, 8])
    processed = preprocess_sensor_input([10, 25, 36, 49])
    coordinate_map = [(x*2, x+1) for x in range(5)]

    # Critical statement
    final_yield = calculate_harvest_efficiency(area_config, sensor_data)

    # Output result
    print(f"Result: {final_yield}")