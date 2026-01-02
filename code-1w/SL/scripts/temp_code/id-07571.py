from itertools import combinations

def compute_filtration_efficiency():
    raw_sequence = [101, 203, 305, 407, 509, 611]
    offset = 2
    generated_pairs = list(combinations(raw_sequence, 2))
    
    # Compute expected checksums for validation
    checksums = set()
    for a, b in generated_pairs:
        if (a + b) % 7 == 0:
            checksums.add(a + b)
    
    # Simulate sensor readings with noise filtering
    sensor_readings = [x * 2 for x in raw_sequence]
    filtered_readings = [r for r in sensor_readings if r < 1000]
    
    # Define valid and target code sets based on system specs
    valid_codes = {x % 100 for x in raw_sequence}
    target_codes = {x % 50 for x in filtered_readings}
    
    # Key statement
    filtration_score = len(valid_codes.intersection(target_codes))
    
    # Irrelevant diagnostic log
    debug_flag = False
    if debug_flag:
        print(f'Debug: {len(checksums)} valid checksums found')
    
    print(f'Target result: {filtration_score}')

compute_filtration_efficiency()