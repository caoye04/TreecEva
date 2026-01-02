import itertools

def analyze_pattern(sequence, depth):
    if depth == 0:
        return sum(sequence) % 7
    transformed = [(x * 2 + 1) % 13 for x in sequence]
    return analyze_pattern(transformed, depth - 1)


def compute_legacy_metric(data):
    accumulator = 0
    for i in range(len(data)):
        accumulator += (data[i] * (i + 1)) % 9
    return accumulator

# Irrelevant helper function (dead code path)
def deprecated_normalizer(val):
    return (val % 65536) / 65535.0

# Unused constant
tuning_factor_zeta = 0.876

# Simulated telemetry data from a distributed system
node_metrics = [12, 18, 24, 36, 48, 54, 60, 72]
base_threshold = 25
scaling_window = 4

# Misleading intermediate calculation
buffer_load = sum([(n % 5) * 3 for n in node_metrics])

# Decoy list transformation
shifted_values = [((x + 3) // 2) for x in node_metrics if x > 30]

# Real processing begins here
filtered_active = [x for x in node_metrics if x >= base_threshold]

# Apply non-linear weighting using cycle from itertools
cycles = list(itertools.islice(itertools.cycle([1, -1, 2]), len(filtered_active)))
weighted_scores = [val * weight for val, weight in zip(filtered_active, cycles)]

# Secondary transformation with conditional adjustment
adjusted_scores = []
for score in weighted_scores:
    if score > 0:
        adjusted_scores.append(score + 5)
    else:
        adjusted_scores.append(score - 3)

# Simulate historical comparison (irrelevant branch)
if len(adjusted_scores) > 10:
    historical_delta = compute_legacy_metric(adjusted_scores)
else:
    historical_delta = None  # Dead end

# Core logic disguised among distractions
metric_data = [
    analyze_pattern([x, x+2, x-1], 2) for x in filtered_active
]

# Key statement
final_score = evaluate_performance(metric_data, base_threshold)

# Actual implementation of the required function
def evaluate_performance(metrics, threshold):
    total = 0
    for m in metrics:
        if m > (threshold % 10):  # threshold % 10 = 5
            total += m * 2
        else:
            total -= m
    return total + len(metrics)

# Print final result
print(f"Target result: {final_score}")