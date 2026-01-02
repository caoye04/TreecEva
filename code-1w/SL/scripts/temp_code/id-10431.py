from itertools import combinations

# Simulate sensor fusion from redundant environmental sensors
def analyze_readings(temps, humids):
    n = len(temps)
    valid_pairs = 0
    temp_sum = sum(t for t in temps if -40 <= t <= 85)  # Filter invalid temperature readings
    humid_product = 1
    for h in humids:
        if 0 <= h <= 100:
            humid_product *= (h + 1)  # Avoid zeroing on 0%

    # Generate all possible dual-sensor pairs to assess consistency
    for pair in combinations(range(n), 2):
        i, j = pair
        if abs(temps[i] - temps[j]) < 5 and abs(humids[i] - humids[j]) < 10:
            valid_pairs += 1

    # Compute stability metric based on pair consistency
    stability = valid_pairs / max(1, n * (n - 1) / 2)

    # Dummy computations to increase cognitive load (distractors)
    avg_temp = temp_sum / len([t for t in temps if -40 <= t <= 85]) if temps else 0
    geometric_humid = humid_product ** (1.0 / len(humids)) if humids else 0
    noise_floor = sum(1 for h in humids if h > 90) * 0.01
    adjustment_factor = (stability * 1.5) % 1.0

    # Core logic: score depends only on stability and filtered temp sum
    base_score = int(stability * 100)
    temp_offset = temp_sum // 10 if temp_sum >= 0 else 0
    final_score = base_score + temp_offset

    # Irrelevant secondary processing (dead path)
    if False:
        fallback = 0
        for t in temps:
            fallback += abs(t) // 3
        final_score = max(final_score, fallback)

    return final_score


def compute_aggregate(sensors):
    temperatures = [s[0] for s in sensors]
    humidities = [s[1] for s in sensors]

    # Preprocess: inject dummy smoothing (unused)
    smoothed_temps = [temperatures[0]]
    for i in range(1, len(temperatures)):
        smoothed_temps.append(int(0.7 * temperatures[i] + 0.3 * smoothed_temps[i-1]))

    # Unused statistical measures
    mean_temp = sum(temperatures) / len(temperatures)
    variance = sum((t - mean_temp) ** 2 for t in temperatures) / len(temperatures)
    peak_humidity = max(humidities) if humidities else 0

    # Actual computation uses only raw temps and humids through analyze_readings
    result = analyze_readings(temperatures, humidities)

    # Final scaling (no-op for this input)
    scaling = 1.0
    if peak_humidity > 95:
        scaling = 0.9

    return int(result * scaling)

# Input data from 6 sensor nodes
sensor_data = [
    (23, 45), (25, 50), (22, 47), (24, 55), (1000, 30), (-50, 60)
]

# Execute main computation
final_score = compute_aggregate(sensor_data)
print(f"Result: {final_score}")