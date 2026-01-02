from itertools import combinations
from functools import reduce

# Simulate sensor data quality assessment in an environmental monitoring system
def analyze_sensor_metrics(raw_readings):
    n = len(raw_readings)
    valid_count = sum(1 for x in raw_readings if 10 <= x <= 90)
    outlier_ratio = (n - valid_count) / n if n > 0 else 0

    # Irrelevant transformation (distractor)
    normalized = [max(0, min(100, x)) for x in raw_readings]
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0

    # Semi-relevant processing: count fluctuation patterns
    fluctuations = 0
    for i in range(1, len(normalized)):
        if abs(normalized[i] - normalized[i-1]) > 15:
            fluctuations += 1

    stability_score = 100 - (fluctuations * 5)

    # Core metric computation
    base_quality = valid_count * 2
    precision_bonus = sum(1 for x in raw_readings if x % 5 == 0) // 2
    
    return {
        'quality': base_quality,
        'precision': precision_bonus,
        'stability': max(0, stability_score),
        'outlier_ratio': outlier_ratio
    }


def generate_diagnostic_flags(metrics):
    flags = []
    if metrics['outlier_ratio'] > 0.3:
        flags.append('HIGH_NOISE')
    if metrics['stability'] < 40:
        flags.append('UNSTABLE_SIGNAL')
    if metrics['precision'] < 3:
        flags.append('LOW_RESOLUTION')
    return set(flags)

# Helper function using lambda and set operations
evaluate_dimension = lambda m, w: m['quality'] * w[0] + m['precision'] * w[1] + m['stability'] * w[2]

metric_weights = (0.4, 0.3, 0.3)

# Complex evaluation with distractors
def evaluate_performance(metrix, weights):
    # Note: intentional typo in parameter name to include dead code path
    if not metrix or 'quality' not in metrix:
        # Dead code - never reached due to how it's called
        fallback = {'quality': 50, 'precision': 5, 'stability': 50, 'outlier_ratio': 0.1}
        return evaluate_dimension(fallback, weights)

    primary_score = evaluate_dimension(metrix, weights)

    # Distractor: complex but unused calculation involving combinations
    samples = [metrix['quality'], metrix['precision'], metrix['stability']]
    combo_values = []
    for r in range(2, len(samples)+1):
        for combo in combinations(samples, r):
            combo_values.append(reduce(lambda x, y: x * y // (x + y + 1), combo, 1))
    
    # Another distractor: character counting from flag names (semi-relevant)
    dummy_flag_analysis = ''.join(sorted(generate_diagnostic_flags(metrix)))
    phantom_weight = len(dummy_flag_analysis) % 7  # Not used in final score

    # Actual answer computation
    adjustment_factor = 0
    if metrix['outlier_ratio'] < 0.15:
        adjustment_factor += 8
    if metrix['precision'] >= 6:
        adjustment_factor += 5
    
    final_result = primary_score + adjustment_factor
    
    return int(final_result)

# Main execution flow
sensor_data = [85, 42, 76, 38, 91, 45, 88, 23, 77, 40, 82]

# Process the sensor readings
processed_metrics = analyze_sensor_metrics(sensor_data)

# Generate diagnostic context (distractor usage)
diag_flags = generate_diagnostic_flags(processed_metrics)

# Key statement
final_score = evaluate_performance(processed_metrics, metric_weights)

print(f"Result: {final_score}")