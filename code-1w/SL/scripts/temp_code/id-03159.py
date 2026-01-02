def analyze_system_load(usage_log):
    peak_load = max(usage_log)
    avg_load = sum(usage_log) / len(usage_log)
    normalized_peaks = [x / peak_load for x in usage_log]
    volatility = sum(abs(normalized_peaks[i] - normalized_peaks[i-1]) for i in range(1, len(normalized_peaks)))
    return {'peak': peak_load, 'average': avg_load, 'volatility': volatility}


def preprocess_metrics(raw_data):
    cleaned = [x for x in raw_data if 0 <= x <= 100]
    sorted_data = sorted(cleaned, reverse=True)
    top_quartile = sorted_data[:len(sorted_data)//4]
    enhancement_factor = 1.2 if sum(top_quartile) > 150 else 1.0
    adjusted = [x * enhancement_factor for x in cleaned]
    return adjusted


def calculate_efficiency_index(values):
    if not values:
        return 0.0
    mean_val = sum(values) / len(values)
    variance = sum((x - mean_val) ** 2 for x in values) / len(values)
    efficiency = mean_val / (1 + variance ** 0.5)
    return round(efficiency, 4)


def simulate_failure_modes(status_codes):
    failure_count = 0
    for code in status_codes:
        if code in [500, 502, 503]:
            failure_count += 1
    recovery_rate = (len(status_codes) - failure_count) / len(status_codes)
    risk_score = failure_count * 10 + (1 - recovery_rate) * 20
    return risk_score  # unused in final computation


def filter_outliers(data_stream):
    median_val = sorted(data_stream)[len(data_stream)//2]
    filtered = [x for x in data_stream if abs(x - median_val) < 25]
    return filtered  # used indirectly via preprocessing


def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    for key, weight in weights.items():
        if key == 'efficiency':
            weighted_sum += metrics['efficiency'] * weight
        elif key == 'stability':
            weighted_sum += metrics['stability'] * weight
        elif key == 'consistency':
            weighted_sum += metrics['consistency'] * weight
    bonus = 10 if metrics['efficiency'] > 70 else 0
    penalty = 5 if metrics['stability'] < 40 else 0
    return int(weighted_sum + bonus - penalty)

# Simulated telemetry input
raw_telemetry = [88, 92, 76, 105, -3, 85, 90, 83, 77, 110, 89, 94, 73]
status_codes = [200, 200, 500, 200, 200, 200, 502, 200, 200, 200]
load_log = [67, 72, 70, 80, 75, 85, 78, 74, 69, 82]
benchmark_weights = {
    'efficiency': 2.5,
    'stability': 1.8,
    'consistency': 2.0
}

# Irrelevant intermediate computations
_ = simulate_failure_modes(status_codes)
system_load = analyze_system_load(load_log)
noise_floor = sum(x ** 0.5 for x in load_log if x % 2 == 0) / 3

# Core processing chain
filtered_metrics = filter_outliers(raw_telemetry)
processed_data = preprocess_metrics(filtered_metrics)
efficiency = calculate_efficiency_index(processed_data)
volatility_index = system_load['volatility']
stability_score = 100 - int(volatility_index * 5)
consistency_metric = len([x for x in processed_data if x > 75])

# Final aggregation
metrics_summary = {
    'efficiency': efficiency,
    'stability': stability_score,
    'consistency': consistency_metric
}

# Key execution point
final_score = evaluate_performance(metrics_summary, benchmark_weights)
print(f"Result: {final_score}")