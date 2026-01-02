from collections import defaultdict

# Simulate sensor data processing with noise filtering and performance scoring
def main():
    baseline = [0.8, 1.2, 0.9, 1.1, 1.0]
    raw_data = "1.1,1.3,0.7;1.0,1.5,0.8;1.2,1.1,0.9"

    # Parse and normalize sensor readings
    segments = raw_data.split(';')
    normalized = []
    temp_store = defaultdict(float)

    for i, segment in enumerate(segments):
        values = list(map(float, segment.split(',')))
        avg_val = sum(values) / len(values)
        normalized.append(round(avg_val, 2))
        temp_store[f'segment_{i}'] = avg_val

    readings = [x for x in normalized if abs(x - 1.0) <= 0.5]  # Filter outliers

    # Irrelevant transformation - red herring
    transformed = []
    for val in readings:
        if val > 0.95:
            transformed.append(val ** 1.1)
        else:
            transformed.append(val ** 0.9)

    # Dummy counters for state tracking (not used in final logic)
    high_count = 0
    low_count = 0
    for r in readings:
        if r >= 1.0:
            high_count += 1
        else:
            low_count += 1

    # Misleading intermediate calculation
    volatility_index = max(readings) - min(readings) if readings else 0.0
    adjustment_factor = volatility_index * 0.1 if volatility_index > 0.2 else 0.05

    # Core logic wrapped in a conditional expression
    use_enhanced = len(readings) > 2
    scaling = 1.25 if use_enhanced else 1.0

    def calculate_performance(base, obs):
        base_avg = sum(base) / len(base)
        obs_avg = sum(obs) / len(obs) if obs else 0

        # Weighted difference with scaling
        deviation = abs(obs_avg - base_avg)
        penalty = deviation * 10

        # Final score computation
        raw_score = 100 - penalty
        adjusted_score = raw_score * scaling

        # Dead code branch - never executed due to prior filtering
        if False and len(obs) == 0:
            return -1

        return int(adjusted_score)

    final_score = calculate_performance(baseline, readings)
    print(f"Result: {final_score}")

main()