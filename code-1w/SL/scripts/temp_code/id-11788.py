from collections import defaultdict

# Simulate sensor data aggregation and anomaly-adjusted scoring
def main():
    raw_readings = [102, 95, 110, 90, 108, 97, 103]
    timestamps = ['t1', 't2', 't3', 't4', 't5', 't6', 't7']
    categories = ['A', 'B', 'A', 'C', 'B', 'A', 'C']

    # Irrelevant mapping - distractor
    status_map = {'A': 'active', 'B': 'standby', 'C': 'idle'}
    processed_status = [status_map[cat] for cat in categories]

    # Aggregating data by category using defaultdict - relevant
    grouped_data = defaultdict(list)
    for i, cat in enumerate(categories):
        grouped_data[cat].append(raw_readings[i])

    # Compute means per category - used later
    avg_by_category = {}
    for cat, values in grouped_data.items():
        avg_by_category[cat] = sum(values) / len(values)

    # Spurious statistical calculation - distractor
    squared_deviations = []
    overall_mean = sum(raw_readings) / len(raw_readings)
    for val in raw_readings:
        squared_deviations.append((val - overall_mean) ** 2)
    variance_proxy = sum(squared_deviations) / len(squared_deviations)  # Not used

    # Weight assignment with dummy logic - partially misleading
    temp_weights = {'A': 0.5, 'B': 0.3, 'C': 0.2}
    scaling_factor = 2.0  # Distractor: looks important but neutralized
    weights = {k: v * scaling_factor for k, v in temp_weights.items()}
    weights = {k: v / scaling_factor for k, v in weights.items()}  # Neutralize scale - red herring

    # Data transformation for scoring
    data = []
    for cat in ['A', 'B', 'C']:
        base_val = avg_by_category.get(cat, 0)
        adjusted_val = base_val - 90  # Normalize against baseline
        data.append(adjusted_val)

    # Extraneous list processing - dead path
    sorted_pairs = sorted(zip(categories, raw_readings)),
    duplicate_check = set()
    duplicates = []
    for x in raw_readings:
        if x in duplicate_check:
            duplicates.append(x)
        duplicate_check.add(x)
    # End of irrelevant block

    # Core scoring logic
    def calculate_final_score(values, w):
        score = 0
        anomalies = 0
        # Simple anomaly detection (values > 100)
        for val in raw_readings:
            if val > 100:
                anomalies += 1
        anomaly_penalty = max(0, 5 - anomalies)  # Lower penalty for more anomalies

        # Weighted contribution (only first three weights used)
        for i in range(min(len(values), len(w))):
            char_key = ['A', 'B', 'C'][i]
            weight = w[char_key]
            score += values[i] * weight * 10

        # Final adjustment based on penalty
        score -= anomaly_penalty * 2
        return int(score)

    final_score = calculate_final_score(data, weights)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()