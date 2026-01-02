from itertools import combinations

# Simulate sensor readings with noise and calibration offsets
def analyze_sensor_data():
    raw_readings = [12, 15, 10, 8, 20, 14]
    calibration_factor = 0.9
    adjusted_readings = [x * calibration_factor for x in raw_readings]

    # Compute moving average over window size 3 (with padding)
    padded_readings = [0] + adjusted_readings + [0]
    moving_averages = []
    for i in range(1, len(padded_readings) - 1):
        avg = (padded_readings[i-1] + padded_readings[i] + padded_readings[i+1]) / 3
        moving_averages.append(round(avg, 2))

    # Threshold filtering: only values above 10 are valid signals
    valid_signals = [val for val in moving_averages if val > 10]

    # Misleading distraction: entropy-like computation on signal distribution
    total_energy = sum([x**2 for x in valid_signals])
    normalized_entropy = 0
    if total_energy > 0:
        probs = [x**2 / total_energy for x in valid_signals]
        from math import log
        normalized_entropy = -sum(p * log(p) for p in probs if p > 0)

    # Real logic path: find all pairs of valid signals within tolerance
    tolerance = 1.5
    coherent_pairs = []
    for a, b in combinations(valid_signals, 2):
        if abs(a - b) <= tolerance:
            coherent_pairs.append((a, b))

    # Bonus distraction: unused recursive helper
    def useless_recursive(n):
        if n <= 1:
            return 1
        return n + useless_recursive(n - 2)

    dummy_trace = useless_recursive(7)  # Dead-end computation

    # Aggregate score based on pair count and average coherence
    pair_contributions = [abs(a - b) for a, b in coherent_pairs]
    base_count_score = len(coherent_pairs) * 10

    stability_penalty = 0
    if pair_contributions:
        avg_deviation = sum(pair_contributions) / len(pair_contributions)
        stability_penalty = int(avg_deviation * 5)

    final_score = base_count_score - stability_penalty

    # Irrelevant string processing (distraction)
    status_log = "Sensor analysis complete"
    tokens = status_log.split()
    reversed_tokens = [token[::-1] for token in tokens]
    joined_back = " ".join(reversed_tokens)

    # Final output
    print(f"Result: {final_score}")
    return final_score

analyze_sensor_data()