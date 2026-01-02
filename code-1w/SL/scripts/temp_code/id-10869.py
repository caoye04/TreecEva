def analyze_metrics(data):
    base = len(data)
    temp_sum = sum(x ** 2 for x in data if x % 2 == 0)
    ignored_calc = [x for x in data if x > 10]  # dead-end list, not used later
    offset = 5 if base > 6 else 3
    return temp_sum + offset

benchmark_data = [3, 8, 12, 7, 4, 9, 14]

# Extraneous helper with misleading name
def predict_efficiency(arr):
    peak = max(arr)
    floor = min(arr)
    dummy_score = (peak - floor) * len(arr)
    return dummy_score  # never actually used

# Simulate intermediate diagnostics
diag_flags = [True if x % 3 == 0 else False for x in benchmark_data]
trigger_count = sum(1 for flag in diag_flags if flag)

# Conditional expression used appropriately
core_value = sum(benchmark_data) // len(benchmark_data) if benchmark_data else 0

# Distractor: irrelevant transformation
transformed = tuple((x * 2 + 1) % 5 for x in benchmark_data)
unused_total = sum(transformed)

# Actual computation path
raw_analysis = analyze_metrics(benchmark_data)
adjustment = 10 if trigger_count >= 2 else 5

# Key logic chain
base_metric = core_value * adjustment
secondary_boost = len([x for x in benchmark_data if x > core_value])

# Final calculation involving multiple steps and conditions
final_score = base_metric + secondary_boost * 3.5

# Output result as required
print(f"Result: {final_score}")