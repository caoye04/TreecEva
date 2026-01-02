import itertools

def analyze_sensor_network():
    # Real data parameters (relevant)
    raw_readings = [14, 28, 19, 42, 35, 56, 47, 63]
    calibration_factor = 0.85
    base_offset = 3
    
    # Irrelevant sensor metadata (distractor)
    sensor_names = ['S1', 'S2', 'S3', 'S4']
    installation_dates = ['2022-01-05', '2022-02-17', '2022-03-09', '2022-04-21']
    location_grid = [(0,0), (0,1), (1,0), (1,1)]
    
    # Decoy transformation (dead path)
    def transform_legacy(x):
        return (x >> 2) ^ 7

    # Unused recursive function (red herring)
    def calculate_depth(n):
        if n <= 1:
            return 1
        return n + calculate_depth(n-2)

    # Actual processing begins
    adjusted_readings = [int(r * calibration_factor) + base_offset for r in raw_readings]
    
    # Filter logic (relevant)
    valid_range = lambda x: 20 <= x <= 60
    filtered_data = [r for r in adjusted_readings if valid_range(r)]

    # Complex distractor: irrelevant combinatorics (misleading)
    permutations = list(itertools.permutations([1, 2, 3]))
    combination_pairs = list(itertools.combinations_with_replacement('AB', 2))
    shuffle_weights = [sum(p) % 4 for p in permutations]  # unused

    # Real threshold logic (relevant)
    critical_levels = {'low': 25, 'high': 45}
    threshold_map = {**critical_levels, 'buffer': 5}  # used later

    # Fake diagnostic (decoy output)
    preliminary_diag = sum([r // 10 for r in adjusted_readings]) * 2 - 7

    # Real processing function embedded
    def process_readings(data, limits):
        acc = 0
        for val in data:
            if val < limits['low']:
                acc += val * 0.5
            elif val > limits['high']:
                acc += val * 1.2 - 10
            else:
                acc += val
        
        # Nested correction (relevant)
        if acc > 100:
            temp = acc
            for i in range(2):
                temp = (temp // (i+2)) + 3
            acc = temp
        
        # Redundant bit manipulation (distraction)
        decoy_mask = 0b1101
        shadow_op = (int(acc) & decoy_mask) ^ 0b1010  # computed but unused
        
        # Final adjustment (relevant)
        final_shift = int(acc + (acc * 0.1))
        return final_shift if final_shift != 0 else 1
    
    # Unused statistical block (dead code path)
    stats_summary = {}
    if len(filtered_data) > 10:
        avg = sum(filtered_data) / len(filtered_data)
        variance = sum((x - avg)**2 for x in filtered_data)
        stats_summary['mean'] = avg
        stats_summary['var'] = variance

    # Key execution point
    final_diagnostic = process_readings(filtered_data, threshold_map)
    
    # Print required result
    print(f"Result: {final_diagnostic}")

analyze_sensor_network()