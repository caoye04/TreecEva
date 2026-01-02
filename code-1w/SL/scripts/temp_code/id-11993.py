def analyze_signal_strength(readings):
    filtered = [x for x in readings if x > 30]
    avg = sum(filtered) / len(filtered) if filtered else 0
    return avg * 1.5

readings_data = [25, 35, 45, 20, 50, 60, 10, 40]
signal_outcome = analyze_signal_strength(readings_data)

# Irrelevant transformation chain (distractor)
decoy_sequence = [signal_outcome + i for i in range(5)]
temp_offset = sum(decoy_sequence) / 100
offset_adjusted = temp_offset * 2.5 if temp_offset > 1 else temp_offset * 0.8

# Unused function meant to mislead (dead code path)
def compute_payload_capacity(items, limit):
    total_weight = 0
    count = 0
    for item in sorted(items, reverse=True):
        if total_weight + item <= limit:
            total_weight += item
            count += 1
    return count

item_weights = [15, 23, 12, 8, 40]
capacity_result = None  # Never actually used

# Real data path begins here
baseline_metrics = [88, 76, 92, 81, 79]
benchmark_weights = [0.2, 0.15, 0.3, 0.25, 0.1]

# Misleading intermediate calculation
weighted_sum = sum(a * b for a, b in zip(baseline_metrics, benchmark_weights))

# Another distraction: set operations with no impact
evaluated_indices = {i for i, val in enumerate(baseline_metrics) if val > 80}
complement_set = {0,1,2,3,4} - evaluated_indices
penalty_factor = len(complement_set) * 0.05

# Simulated noise injection (unused)
noise_profile = [abs((i - weighted_sum) % 7) for i in range(len(benchmark_weights))]
smoothed_noise = [n * 0.1 for n in noise_profile]

# Core logic disguised among distractions
adjusted_metrics = []
for idx, (metric, weight) in enumerate(zip(baseline_metrics, benchmark_weights)):
    adjustment = 0.0
    if idx in evaluated_indices:
        adjustment = signal_outcome * 0.01
    adjusted_value = metric * (1 + adjustment)
    adjusted_metrics.append(adjusted_value)

# Secondary irrelevant loop
for i, val in enumerate(adjusted_metrics):
    if i % 2 == 0:
        val *= 0.99  # This doesn't update the list!

# Actual evaluation function with nested logic
def evaluate_performance(metrics, weights):
    result = 0.0
    for i, (m, w) in enumerate(zip(metrics, weights)):
        if m >= 85:
            contribution = m * w * 1.1
        elif m >= 75:
            contribution = m * w
        else:
            contribution = m * w * 0.9
        result += contribution
    
    # Final adjustment based on signal (only place signal_outcome is actually used)
    if signal_outcome > 60:
        result *= 1.05
    return int(round(result))

final_score = evaluate_performance(adjusted_metrics, benchmark_weights)
print(f"Result: {final_score}")