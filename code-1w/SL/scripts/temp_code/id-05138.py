from collections import defaultdict, Counter

# Simulated sensor network data processing with red herrings
def process_diagnostics():
    raw_readings = [187, 205, 198, 213, 176, 192, 201, 184]
    calibration_map = {i: val * 0.91 for i, val in enumerate(raw_readings)}
    
    # Irrelevant transformation - dead code path
    temp_offsets = []
    for x in raw_readings:
        if x > 200:
            temp_offsets.append(x // 7)
        else:
            temp_offsets.append(x % 11)
    
    # Distractor: unused frequency analysis
    reading_frequencies = Counter(raw_readings)
    rare_values = [k for k, v in reading_frequencies.items() if v == 1]

    # Real computation begins
    adjusted = [int(v * 1.08) for v in calibration_map.values()]
    outliers = [v for v in adjusted if v < 180 or v > 220]
    
    # Masked summation logic
    base_total = 0
    for i, val in enumerate(adjusted):
        if i % 2 == 0:
            base_total += val >> 2  # Bit shift red herring
        else:
            base_total += val // 3
    
    # Decoy accumulation
    phantom_sum = 0
    for val in adjusted:
        phantom_sum += val ^ 255  # Bitwise XOR distraction

    # Conditional expression chain with actual relevance
    aggregate_score = sum(adjusted) if len(outliers) < 5 else sum(adjusted) // 2
    
    # Actual correction factor buried in logic
    status_flags = [1 if x > 195 else 0 for x in adjusted]
    flag_count = sum(status_flags)
    
    intermediate = (flag_count * 37) & 0xFF  # Bitwise AND red herring
    
    # Correction factor derived from tuple unpacking and conditional logic
    codes = [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D')]
    lookup = defaultdict(lambda: 10)
    for idx, label in codes:
        if idx % 2 == 0:
            lookup[label] = idx * 12
        else:
            lookup[label] = idx * 8
    
    # Meaningless list comprehensions
    _ = [x * x for x in range(len(codes)) if x % 2 == 1]
    _ = ['processed' for _ in range(4) if False]  # Dead code

    # Real correction logic hidden among distractors
    if flag_count in [3, 4]:
        _, primary_code = zip(*codes)  # Unpacking usage
        if 'C' in primary_code:
            correction_factor = lookup['C']
        else:
            correction_factor = 55
    else:
        correction_factor = 44

    # Key assignment - target execution point
    final_diagnostic = aggregate_score + correction_factor
    
    # Final red herring: unused bitwise mix
    security_hash = 0
    for val in adjusted + [correction_factor]:
        security_hash ^= (val << 1) | 1
    
    return final_diagnostic

result = process_diagnostics()
print(f"Result: {result}")