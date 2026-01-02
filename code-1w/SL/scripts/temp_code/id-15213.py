import math

def analyze_metrics(raw_values, thresholds):
    counts = {key: 0 for key in thresholds}
    temp_results = []
    total_sum = 0
    outlier_count = 0

    for val in raw_values:
        if val > thresholds['high']:
            counts['high'] += 1
            total_sum += val * 0.9
        elif val < thresholds['low']:
            counts['low'] += 1
            outlier_count += 1
            adjusted = val - (val * 0.1)
            temp_results.append(adjusted)
        else:
            counts['medium'] += 1
            total_sum += val
            temp_results.append(val ** 0.5)

    # Irrelevant aggregation
    avg_temp = sum(temp_results) / len(temp_results) if temp_results else 0
    decay_factor = math.exp(-0.1 * outlier_count)
    return total_sum, counts, avg_temp, decay_factor


def normalize_dataset(data_list):
    mean_val = sum(data_list) / len(data_list)
    variance = sum((x - mean_val) ** 2 for x in data_list) / len(data_list)
    std_dev = variance ** 0.5
    normalized = [(x - mean_val) / std_dev for x in data_list]
    return normalized


def calculate_final_score(metrics_dict):
    base = metrics_dict['sum_valid']
    penalty = 0

    if metrics_dict['anomalies'] > 5:
        penalty += metrics_dict['anomalies'] * 1.5
    if metrics_dict['coverage'] < 0.7:
        penalty += 10

    bonus = 0
    if metrics_dict['consistency'] > 0.9:
        bonus += 25

    score = base - penalty + bonus
    return int(score)

# Main execution
raw_data = [120, 45, 67, 89, 134, 23, 78, 91, 150, 60, 40, 88, 95, 102, 30]
config_thresholds = {'low': 50, 'medium': 75, 'high': 100}

# Step 1: Analyze raw metrics
total_contribution, category_breakdown, average_sqrt, dampening = analyze_metrics(raw_data, config_thresholds)

# Step 2: Normalize subset for irrelevant trend analysis
subset_for_trend = [raw_data[i] for i in range(0, len(raw_data), 3)]
normalized_trend = normalize_dataset(subset_for_trend)
drift_metric = sum(abs(normalized_trend[i] - normalized_trend[i-1]) for i in range(1, len(normalized_trend)))

# Step 3: Process summary statistics
valid_entries = len(raw_data) - category_breakdown['low']
effective_coverage = valid_entries / len(raw_data)
consistency_ratio = (category_breakdown['medium'] + category_breakdown['high']) / len(raw_data)

# Simulated cache for unused optimization trace
cache_log = {}
for i, val in enumerate(raw_data):
    if val > 100:
        cache_log[f'entry_{i}'] = {'flagged': True, 'weight': val * 0.01}

# Misleading intermediate calculation
dummy_aggregate = 0
for k in range(5):
    dummy_aggregate += (k + 1) * 3

# Prepare final input dictionary
processed_data = {
    'sum_valid': total_contribution,
    'anomalies': category_breakdown['low'],
    'coverage': effective_coverage,
    'consistency': consistency_ratio
}

# Critical execution point
final_score = calculate_final_score(processed_data)

Result: {final_score}