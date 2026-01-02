from collections import defaultdict, Counter

# Simulate system benchmark data with noise
def generate_noisy_data():
    raw = [10, 15, 20, 25, 30]
    noise = [i % 3 for i in range(len(raw))]
    return [raw[i] + noise[i] for i in range(len(raw))]

def analyze_trends(data):
    trends = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trends.append('up')
        elif data[i] < data[i-1]:
            trends.append('down')
        else:
            trends.append('stable')
    counter = Counter(trends)
    return counter['up'] - counter['down']

def calculate_stability_index(seq):
    diffs = [abs(seq[i] - seq[i-1]) for i in range(1, len(seq))]
    avg_diff = sum(diffs) / len(diffs) if diffs else 0
    # Distractor: unused stability metric
    peak_variation = max(diffs) - min(diffs) if len(diffs) > 1 else 0
    return avg_diff

def calculate_performance(metrics):
    # Core logic starts here
    base = sum(metrics)
    trend_weight = analyze_trends(metrics)
    
    # Irrelevant transformation (distractor)
    temp_shift = [x * 0.95 for x in metrics if x > 15]
    adjustment_factor = 1.0
    if len(temp_shift) > 2:
        adjustment_factor = 0.98
    
    # Actual computation path
    stability = calculate_stability_index(metrics)
    if stability < 5:
        adjustment_factor += 0.05
    
    # Multiple assignment distractor
    initial, *rest = metrics
    offset = len(rest) % 4
    
    # Key calculation
    raw_score = base + (trend_weight * 10)
    penalty = 0
    for val in metrics:
        if val % 5 == 0:
            penalty += 2
    final_score = int((raw_score - penalty) * adjustment_factor)
    
    # Dead code branch (distractor)
    if False:
        fallback = sum(metrics) // len(metrics)
        final_score = fallback
    
    return final_score

# Main execution
benchmark_data = generate_noisy_data()

# Extraneous analysis (not used in final score)
data_slice = benchmark_data[1:4]
summary_stats = defaultdict(int)
for x in data_slice:
    summary_stats['total'] += x
    summary_stats['count'] += 1

# This is the key statement
final_score = calculate_performance(benchmark_data)

print(f"Result: {final_score}")