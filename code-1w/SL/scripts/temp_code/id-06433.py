import math

# Irrelevant helper function (dead code path)
def unused_signal_filter(x):
    return [val * 0.95 for val in x if val > 0]

# Misleading data transformation chain
temp_buffer = [i ** 2 for i in range(15) if i % 3 != 0]
decoy_matrix = [[math.sin(i + j) for j in range(4)] for i in range(4)]
offset_lookup = {i: temp_buffer[i] % 7 for i in range(len(temp_buffer)) if i % 2 == 0}

# Core computation setup
baseline_metrics = [0.88, 0.91, 0.76, 0.94, 0.85]
weight_vector = list(reversed([0.1, 0.15, 0.2, 0.25, 0.3]))

# Distractor: complex but unused bitwise scaling
scaling_factor = 0
for i in range(len(weight_vector)):
    scaling_factor ^= int(weight_vector[i] * 100) << 1

# Real data pipeline begins
raw_inputs = [85, 90, 78, 92, 88]
adjusted_inputs = [x * 1.05 if x < 80 else x * 1.02 for x in raw_inputs]

# Conditional normalization branch
if sum(adjusted_inputs) / len(adjusted_inputs) > 85:
    normalized = [x / 100.0 for x in adjusted_inputs]
else:
    normalized = [x / 120.0 for x in adjusted_inputs]

# Red herring: unused recursive function
def recursive_distractor(n):
    if n <= 1:
        return 1
    return n * recursive_distractor(n - 2) + 0.1

# Data alignment via slicing and filtering
aligned_data = normalized[1:4]  # Middle three values

# Simulated benchmark with decoy operations
correction_map = {}
for idx, val in enumerate(aligned_data):
    correction_map[idx] = math.log(val * 10 + 1, 2) if val > 0.8 else math.sqrt(val * 5)

# Actual metric calculation starts here
efficiency_score = sum(aligned_data) * 100
accuracy_bonus = 0
if all(x > 0.82 for x in aligned_data):
    accuracy_bonus = 15.5
elif any(x > 0.88 for x in aligned_data):
    accuracy_bonus = 7.2

# Complex conditional with lambda abstraction
penalty_function = lambda x: 5.0 if x < 0.8 else (2.5 if x < 0.85 else 0)
performance_penalty = sum(penalty_function(x) for x in aligned_data)

# Secondary distraction: bit manipulation on floats (unused)
coded_flags = 0
for val in baseline_metrics:
    coded_flags |= int(val * 100) & 0xFF

class PerformanceModel:
    def __init__(self, weights):
        self.weights = weights
        self.calibration = 1.0
    
    def apply_weights(self, data):
        return sum(d * w for d, w in zip(data, self.weights[:len(data)]))

# Instantiate but partially use model
model = PerformanceModel([0.4, 0.3, 0.3])
weighted_result = model.apply_weights(aligned_data)

# Benchmark data construction
benchmark_data = {
    'inputs': raw_inputs,
    'normalized': normalized,
    'metrics': baseline_metrics,
    'corrections': list(correction_map.values())
}

# Metric set with intentional redundancy
metric_set = [
    ('efficiency', efficiency_score),
    ('bonus', accuracy_bonus),
    ('penalty', performance_penalty),
    ('weighted', weighted_result)
]

# Final evaluation logic
aggregation_rules = {
    'efficiency': 0.4,
    'bonus': 0.2,
    'penalty': -0.3,
    'weighted': 0.7
}

# Critical execution point
final_score = 0.0
for name, value in metric_set:
    if name in aggregation_rules:
        contribution = value * aggregation_rules[name]
        final_score += contribution

# Apply hidden offset from earlier distractor structure (only relevant use)
if len(offset_lookup) % 2 == 0:
    final_score += 5.25
else:
    final_score -= 2.75

print(f"Result: {final_score}")