def preprocess_metrics(raw):    
    # Irrelevant preprocessing
    temp = [x * 1.05 for x in raw if x > 0]
    adjusted = [t + 2 for t in temp]
    norm = sum(adjusted) / len(adjusted)
    return [v / norm for v in adjusted]

# Misleading data
irrelevant_logs = [
    {'type': 'latency', 'value': 120},
    {'type': 'timeout', 'value': 300},
    {'type': 'retries', 'value': 3}
]

stats_cache = {
    'avg_latency': 95,
    'peak_memory': 4800,
    'cache_hit_ratio': 0.87
}

bonus_factor = 1.75

# Real input data
base_metrics = [88, 92, 76, 85, 94]

# Distractor: unused function
def calculate_robustness(data):
    return sum(d ** 0.5 for d in data if d % 2 == 0)

# Distractor: fake aggregation
shadow_sum = 0
for val in base_metrics:
    if val > 90:
        shadow_sum += val * 0.1

# Unused transformation
shifted = list(map(lambda x: x + 5, [n//2 for n in base_metrics]))

# Real logic begins
metric_data = {}
for i, val in enumerate(preprocess_metrics(base_metrics)):
    metric_data[f'step_{i}'] = round(val * 100, 3)

# Decoy dictionary update
metric_data['diagnostic'] = 'nominal'

# Actual weight map (used later)
weights = {key: 0.1 + idx*0.05 for idx, key in enumerate(metric_data) if 'step_' in key}

# Fake filter that does nothing
filtered_steps = {k: v for k, v in metric_data.items() if isinstance(v, (int, float)) and v > 50}

# Dummy conditional with no effect
threshold_flag = False
if sum(filtered_steps.values()) > 300:
    threshold_flag = True
    extra_weight = 0.05

# Critical distraction: recursive decoy
def useless_recurse(n):
    if n <= 1:
        return 1
    return n * useless_recurse(n-2) + 2

# Irrelevant call
junk_result = useless_recurse(7)

# Core evaluation logic
running_total = 0.0
weight_sum = 0.0
for label in metric_data:
    if 'step_' in label:
        score = metric_data[label]
        weight = weights[label]
        running_total += score * weight
        weight_sum += weight

# Misleading normalization
fake_norm = running_total / len(weights)

# Real weighted average
true_avg = running_total / weight_sum

# Bonus application (depends on true_avg)
efficiency_class = 'high' if true_avg > 85 else 'standard'

# Final computation chain
if efficiency_class == 'high':
    applied_bonus = bonus_factor
else:
    applied_bonus = 1.0

# Final score calculation
final_score = (true_avg * 0.7) + (true_avg * applied_bonus * 0.3)

# Print result as required
print(f"Result: {final_score}")