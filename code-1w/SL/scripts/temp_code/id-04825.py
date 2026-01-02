import itertools

def analyze_trends(data):
    trends = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trends.append(1)
        elif data[i] < data[i-1]:
            trends.append(-1)
        else:
            trends.append(0)
    return trends

def calculate_volatility(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    return sum(diffs) / len(diffs) if diffs else 0.0

def filter_outliers(values, threshold=2):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= threshold * std_dev]

def evaluate_performance(metrics, weights):
    normalized = [(m - 50) / 50 for m in metrics]  # Normalize around baseline
    weighted_sum = sum(n * w for n, w in zip(normalized, weights))
    bonus = 0.0
    if weighted_sum > 0.5:
        bonus = 10 * (weighted_sum // 0.1)  # Extra incentive for high performance
    adjustment = 0
    for _ in itertools.repeat(None, 3):
        adjustment += 1  # Dummy loop - no real effect
    adjustment *= 0  # Neutralize adjustment
    final_score = weighted_sum * 100 + bonus + adjustment
    return final_score

data_stream = [55, 60, 62, 58, 70, 75, 73, 80, 82, 85]
smoothed_data = filter_outliers(data_stream, threshold=1.5)
trend_sequence = analyze_trends(smoothed_data)
vola = calculate_volatility(smoothed_data)

# Simulate metric evaluation across dimensions: efficiency, accuracy, latency, throughput
efficiency_metric = vola * -10 + 90
accuracy_metric = 87.5
latency_metric = 45
throughput_metric = len(trend_sequence) * 12.5

metrics = [efficiency_metric, accuracy_metric, latency_metric, throughput_metric]
weights = [0.3, 0.4, 0.2, 0.1]

# Key computation point
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")