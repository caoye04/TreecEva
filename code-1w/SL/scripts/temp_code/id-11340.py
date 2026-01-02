def analyze_signal(data, threshold=0.75):
    filtered = [x for x in data if x > threshold]
    return len(filtered) / len(data) if data else 0

# Irrelevant signal processing function (dead code path)
def process_frequency_spectrum(spectrum):
    magnitude = sum([abs(x) for x in spectrum])
    normalized = [x / magnitude for x in spectrum if magnitude != 0]
    return normalized[::-1]

# Unused helper function (distractor)
def calculate_entropy(values):
    from math import log
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count/total) * log(count/total) for count in freq.values())
    return entropy

# Simulated system metrics (some irrelevant)
system_load = [0.21, 0.34, 0.67, 0.89, 0.45, 0.72, 0.79, 0.91]
cpu_spikes = [x for x in system_load if x > 0.7]
idle_periods = len([x for x in system_load if x < 0.3])

# Benchmark weights with red herring entries
dummy_weights = {'latency': 0.1, 'throughput': 0.2, 'redundancy': 0.05, 'jitter': 0.0}
benchmark_weights = {'latency': 0.3, 'throughput': 0.4, 'accuracy': 0.3}  # real weights

# Performance metrics with decoy and actual values
metrics = {
    'latency': 0.12,
    'throughput': 850,
    'accuracy': 0.98,
    'debug_flag': True,
    'version': '2.1.3',
    'timestamp': 1712345678
}

# Fake transformation (misleading intermediate result)
transformed_metrics = {k: v*100 if isinstance(v, float) and k != 'latency' else v for k, v in metrics.items()}

# Phantom normalization using slicing (irrelevant)
normalized_slice = system_load[1:6:2]
avg_slice = sum(normalized_slice) / len(normalized_slice)

# Core logic buried among distractions
def adjust_for_outliers(values, factor=1.5):
    sorted_vals = sorted(values)
    q1 = sorted_vals[len(sorted_vals)//4]
    q3 = sorted_vals[3*len(sorted_vals)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return [v for v in values if lower <= v <= upper]

# Another unused function (decoy)
def generate_report_header(title):
    line = "=" * (len(title) + 4)
    return f"{line}\n| {title} |\n{line}"  

# Real evaluation logic hidden in complexity
def evaluate_performance(met, weights):
    score_components = []
    
    # Latency: convert to score (lower is better)
    latency_score = max(0, (0.2 - met['latency']) * 5)  # capped at 0.2s
    
    # Throughput: scale to 0-1 range based on ideal 1000 ops/sec
    throughput_score = min(1, met['throughput'] / 1000)
    
    # Accuracy: already in 0-1 range
    accuracy_score = met['accuracy']
    
    # Weighted combination
    total_score = (
        latency_score * weights['latency'] +
        throughput_score * weights['throughput'] +
        accuracy_score * weights['accuracy']
    )
    
    # Apply outlier-adjusted bonus only if all metrics are high
    adjusted_load = adjust_for_outliers(system_load)
    stability_ratio = len(adjusted_load) / len(system_load)
    bonus = 0.05 if stability_ratio > 0.8 and accuracy_score > 0.95 else 0
    
    return total_score + bonus

# Dead code assignment (distractor)
intermediate_result = analyze_signal(system_load, 0.5) * 1000

# Critical execution point
final_score = evaluate_performance(metrics, benchmark_weights)

# Print required output
print(f"Target result: {final_score}")