from collections import defaultdict

# Simulate system performance metrics with auxiliary tracking
def analyze_workload(inputs):
    stats = defaultdict(int)
    temp_cache = []
    for item in inputs:
        if item % 3 == 0:
            stats['divisible_by_3'] += 1
        if item > 5:
            stats['greater_than_5'] += 1
            temp_cache.append(item * 0.1)
    scaling_factor = sum(temp_cache) if temp_cache else 0.5
    return dict(stats), scaling_factor

def evaluate_conditions(flags):
    # Some flags trigger side behaviors, but only 'X' contributes to score
    result_set = {k: v for k, v in flags.items() if v > 0}
    extra_noise = [i**2 for i in range(len(result_set)) if i % 2 == 0]  # Irrelevant computation
    activation = 10 if 'X' in result_set else 0
    return activation + len(extra_noise)  # len(extra_noise) is distraction

# Core scoring logic
def compute_performance(flag_data, base):
    base_value = sum(base.values())
    adjustment = evaluate_conditions(flag_data)
    multiplier = 1.5 if flag_data.get('enhanced', False) else 1.0
    return int((base_value + adjustment) * multiplier)

# Setup: synthetic telemetry data
raw_inputs = [2, 3, 6, 7, 9, 10, 12]
base_metrics = {'latency': 12, 'throughput': 18, 'reliability': 4}
bonus_flags = {'X': 5, 'Y': 0, 'Z': -1, 'enhanced': True}

# Step 1: Analyze input workload (produces intermediate stats and unused factor)
metrics_summary, influence = analyze_workload(raw_inputs)

# Step 2: Introduce misleading branch based on unrelated condition
if influence > 0.7:
    fallback_mode = True
    buffer_offset = 200
else:
    fallback_mode = False
    buffer_offset = 50  # Not used later

# Step 3: Compute final score — this is the critical execution point
final_score = compute_performance(bonus_flags, base_metrics)

# Print result as required
print(f"Target result: {final_score}")