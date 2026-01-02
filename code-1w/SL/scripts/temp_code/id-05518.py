from collections import defaultdict
import math

def analyze_trends(data, baseline):
    trends = []
    above_count = 0
    total_deviation = 0.0
    squared_errors = []
    temp_store = []

    for val in data:
        deviation = val - baseline
        total_deviation += abs(deviation)
        squared_errors.append(deviation ** 2)
        if val > baseline:
            above_count += 1
            trends.append('up')
        elif val < baseline:
            trends.append('down')
        else:
            trends.append('stable')

    avg_error = math.sqrt(sum(squared_errors) / len(squared_errors)) if squared_errors else 0
    temp_store.append(avg_error)
    return total_deviation, trends, above_count

def compute_aggregate(deviations, weights):
    weighted_sum = 0
    norm_factor = sum(weights) + 1e-8
    for i in range(len(deviations)):
        weighted_sum += deviations[i] * weights[i]
    normalized = weighted_sum / norm_factor
    penalty = 0
    for w in weights:
        if w > 0.5:
            penalty += w * 0.1
    final_value = normalized - penalty
    return round(final_value, 4)

def main():
    # Simulated sensor readings over time
    readings = [104, 97, 110, 95, 108, 102, 99]
    reference = 100

    # Irrelevant backup data (distractor)
    backup_readings = [x * 1.01 for x in readings]
    correction_factor = 0.99
    adjusted_backup = [b * correction_factor for b in backup_readings]

    # Core analysis
    total_dev, trend_labels, up_days = analyze_trends(readings, reference)

    # Compute daily absolute deviations (used in final calculation)
    deviations = [abs(x - reference) for x in readings]

    # Weight assignment based on day importance (hypothetical)
    weights = []
    for i, dev in enumerate(deviations):
        if i % 3 == 0:
            weights.append(0.8)
        elif dev > 5:
            weights.append(0.6)
        else:
            weights.append(0.3)

    # Unused statistical measures (distractor)
    mean_dev = sum(deviations) / len(deviations)
    variance = sum((d - mean_dev) ** 2 for d in deviations) / len(deviations)
    stdev = math.sqrt(variance)
    z_scores = [(d - mean_dev) / stdev for d in deviations]

    # Data aggregation for reporting (partially used)
    report_data = defaultdict(list)
    for i, label in enumerate(trend_labels):
        report_data[label].append(readings[i])

    # Final computation chain
    intermediate_metric = total_dev / len(readings)
    scaling_factor = 1 + (up_days / len(readings))
    enhanced_metric = intermediate_metric * scaling_factor

    # Key statement
    final_score = compute_aggregate(deviations, weights)

    # Print result as required
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()