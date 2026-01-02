def analyze_metrics(data):
    baseline = sum(data) / len(data)
    variance = sum((x - baseline) ** 2 for x in data) / len(data)
    adjusted_values = [x * 0.9 + 0.1 for x in data if x > baseline]
    return adjusted_values

benchmark_data = [85, 90, 78, 92, 88, 76, 95]

# Irrelevant preprocessing (distractor)
shadow_copy = [x * 2 for x in benchmark_data]
duplicate_check = list(set(shadow_copy))
normalization_factor = max(duplicate_check) / 100

# Semi-relevant transformation
filtered_data = [x for x in benchmark_data if x >= 80]
scaled_data = [x * 1.1 for x in filtered_data]

# Core logic embedded with noise
status_flags = {i: 'active' if x > 85 else 'pending' for i, x in enumerate(benchmark_data)}
activation_count = sum(1 for flag in status_flags.values() if flag == 'active')

intermediate_result = sum(scaled_data) / (activation_count or 1)

# Misleading statistical computation (dead end)
median_val = sorted(benchmark_data)[len(benchmark_data)//2]
deviation_sum = sum(abs(x - median_val) for x in benchmark_data)

# Actual performance model
def compute_performance(logs):
    raw_total = sum(logs)
    bonus = 5 if len(logs) > 6 else 0
    penalty = 2 * (90 - min(logs)) if min(logs) < 90 else 0
    
    # Secondary adjustment based on distribution
    high_performers = len([x for x in logs if x >= 90])
    excellence_bonus = 10 if high_performers >= 3 else 0
    
    # Distractor: unused helper calculation
    def get_entropy(arr):
        from math import log
        total = sum(arr)
        probs = [x/total for x in arr]
        return -sum(p * log(p) for p in probs if p > 0)
    
    # Final score computation
    base_score = raw_total * 0.8
    final_modifier = bonus - penalty + excellence_bonus
    return int(base_score + final_modifier)

# Trigger point
final_score = compute_performance(benchmark_data)
print(f"Result: {final_score}")