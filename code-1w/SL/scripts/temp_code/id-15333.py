import itertools

def main():
    # Simulate sensor data from three monitoring stations
    station_a = [104, 95, 110, 98, 102]
    station_b = [205, 198, 210, 200, 195]
    station_c = [310, 305, 315, 300, 312]

    # Irrelevant transformation (distractor)
    transformed_b = [x * 0.98 + 2 for x in station_b]
    offset_correction = sum(transformed_b) / len(transformed_b) - 200

    # Normalize data using min-max scaling (relevant preprocessing)
    def normalize(series):
        min_val, max_val = min(series), max(series)
        return [(x - min_val) / (max_val - min_val) for x in series]

    normalized_a = normalize(station_a)
    normalized_b = normalize(station_b)
    normalized_c = normalize(station_c)

    # Combine all normalized data into a single list of tuples
    normalized_data = list(itertools.zip_longest(normalized_a, normalized_b, normalized_c, fillvalue=0))

    # Weight configuration for performance metric
    base_weights = [0.25, 0.35, 0.4]
    adjustment_factor = 0.05

    # Apply cyclic shift based on length (semi-relevant but misleading complexity)
    shifted_weights = base_weights[-len(normalized_data) % 3:] + base_weights[:-len(normalized_data) % 3]
    metric_weights = [w + adjustment_factor * 0.1 for w in shifted_weights]  # Minor tweak

    # Dead code path (distractor)
    if len(normalized_data) > 10:
        metric_weights = [w * 1.1 for w in metric_weights]

    # Core evaluation logic
    def calculate_stability(series):
        diffs = [abs(series[i+1] - series[i]) for i in range(len(series)-1)]
        return 1 - sum(diffs) / len(diffs) if diffs else 1

    stability_scores = [
        calculate_stability([row[i] for row in normalized_data if row[i]]) 
        for i in range(3)
    ]

    # Final performance score calculation
    raw_contributions = [
        metric_weights[i] * stability_scores[i] if i < len(stability_scores) else 0 
        for i in range(3)
    ]

    # Misleading intermediate: average without purpose
    avg_contribution = sum(raw_contributions) / len(raw_contributions) if raw_contributions else 0

    # Key statement
    final_score = evaluate_performance(metric_weights, normalized_data)

    print(f"Result: {final_score}")


def evaluate_performance(weights, data_matrix):
    # Extract each sensor's time series
    series_0 = [row[0] for row in data_matrix]
    series_1 = [row[1] for row in data_matrix]
    series_2 = [row[2] for row in data_matrix]

    # Calculate consistency score (inverse of variance)
    def consistency(series):
        mean_val = sum(series) / len(series)
        variance = sum((x - mean_val) ** 2 for x in series) / len(series)
        return 1 / (1 + variance)

    # Actual weights used (ignore distractor shifts)
    true_weights = [0.25, 0.35, 0.4]
    scores = [consistency(series_0), consistency(series_1), consistency(series_2)]
    
    # Final weighted score
    result = sum(true_weights[i] * scores[i] for i in range(3))
    
    return round(result, 4)

if __name__ == "__main__":
    main()