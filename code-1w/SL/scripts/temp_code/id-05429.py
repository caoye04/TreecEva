from itertools import combinations

# Simulate sensor array readings with noise filtering
def process_sensor_data(raw_readings):
    filtered = [x for x in raw_readings if 10 <= x <= 100]
    sorted_readings = sorted(filtered, reverse=True)
    top_quartile = sorted_readings[:len(sorted_readings)//4+1]

    # Distractor: energy calculation (not used in final result)
    total_energy = sum(x**2 for x in raw_readings if x > 0)
    energy_threshold = total_energy / len(raw_readings) if raw_readings else 0

    # Valid computation path
    baseline = sum(top_quartile) / len(top_quartile) if top_quartile else 0
    deviation_scores = [abs(baseline - x) for x in top_quartile]
    avg_deviation = sum(deviation_scores) / len(deviation_scores) if deviation_scores else 0

    # Secondary distractor: pattern analysis with slicing (unused)
    patterns = [top_quartile[i:i+2] for i in range(len(top_quartile)-1)]
    symmetry_checks = [p == p[::-1] for p in patterns if len(p) == 2]

    # Core logic step 1: generate candidate correction factors
    candidates = []
    for a, b in combinations([int(baseline), int(avg_deviation)+1, 5], 2):
        if a > b:
            candidates.append(a - b)
        else:
            candidates.append(b - a)

    # Core logic step 2: select stable correction
    valid_corrections = [c for c in candidates if c % 2 == 0 and c < 20]
    final_tally = min(valid_corrections) if valid_corrections else 10

    # Distractor: historical trend simulation (unused)
    mock_history = [final_tally * (1.0 + i/10) for i in range(-3, 0)]
    predicted_drift = sum(mock_history) / len(mock_history) if mock_history else 0

    # Core logic step 3: compute adjustment based on baseline properties
    adjustment_factor = 0
    baseline_int = int(baseline)
    digit_sum = sum(int(d) for d in str(baseline_int))
    if digit_sum % 3 == 0:
        adjustment_factor = 4
    elif baseline_int % 2 == 0:
        adjustment_factor = 2
    else:
        adjustment_factor = 1

    # Key assignment statement
    result_score = final_tally + adjustment_factor

    # Red herring: unused transformation chain
    transformed = ''.join(chr(97 + (ord(c) - 97 + 3) % 26) for c in 'debug')
    metadata_flag = len(transformed) > 4

    return result_score

# Input data
sensor_input = [12, 95, 88, 45, 103, 91, 7, 89, 95, -5, 42]

# Execute and print result
result = process_sensor_data(sensor_input)
print(f"Result: {result}")