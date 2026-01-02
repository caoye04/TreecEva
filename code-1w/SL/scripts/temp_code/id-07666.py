from itertools import combinations

# Simulate sensor data validation and anomaly scoring
def analyze_sensor_readings(readings):
    n = len(readings)
    valid_pairs = 0
    anomaly_count = 0
    temp_accumulator = 0
    parity_tracker = []

    # Real logic: count valid adjacent pairs with magnitude constraint
    for i in range(n - 1):
        if abs(readings[i]) > 0 and abs(readings[i + 1]) > 0:
            if (readings[i] + readings[i + 1]) % 2 == 0:
                valid_pairs += 1

        # Distractor: parity tracking not used later
        parity_tracker.append(readings[i] % 2)

    # Real logic: detect anomalies (outliers beyond threshold)
    threshold = sum(abs(x) for x in readings) / len(readings) if readings else 0
    for val in readings:
        if abs(val) > 2.5 * threshold:
            anomaly_count += 1

    # Intermediate score calculation
    base_score = valid_pairs * 7
    anomaly_penalty = anomaly_count * 12

    # Distractor: complex but unused combinatorial analysis
    redundant_combos = 0
    if n >= 3:
        for combo in combinations(range(n), 3):
            a, b, c = combo
            if a < b < c:
                # Useless computation
                redundant_combos += (readings[a] ^ readings[b]) & readings[c]

    # Real logic: secondary adjustment based on index patterns
    index_sum = 0
    for idx, value in enumerate(readings):
        if value < 0 and idx % 2 == 1:
            index_sum += idx

    temporal_weight = index_sum * 3

    # Distractor: dead code path (never executed due to fixed input)
    fallback_value = 0
    if all(x == 0 for x in readings):
        fallback_value = 999

    # Real aggregation
    aggregate_result = base_score - anomaly_penalty + temporal_weight

    # Real penalty adjustment using bitwise logic
    severity_flag = anomaly_count > 2
    volatility = (valid_pairs ^ anomaly_count) & 7
    penalty_adjustment = -volatility if severity_flag else volatility

    # Key statement
    final_score = aggregate_result + penalty_adjustment

    # Irrelevant transformation chain
    dummy_chain = final_score
    for _ in range(3):
        dummy_chain = (dummy_chain * 2) ^ 5
        dummy_chain = max(dummy_chain, 1)

    return final_score

# Input data
sensor_data = [4, -5, 0, 8, -3, 11, -7]

result = analyze_sensor_readings(sensor_data)
print(f"Target result: {result}")