def calculate_harmonic_influence():
    values = [3, 7, -2, 5, 8]
    weights = [10, 20, 30, 40, 50]
    total_harmonic_weight = 0.0
    base_offset = sum([v for v in values if v > 0]) // len(values)
    
    for i, (val, w) in enumerate(zip(values, weights)):
        if val <= 0:
            continue
        total_harmonic_weight += weights[i] * (1 / (i + 1))
    
    temp = [x for x in range(3)]  # Irrelevant computation
    unused_flag = False
    
    print(f"Result: {total_harmonic_weight}")

calculate_harmonic_influence()