def analyze_component(x, factor=1.0):
    # Irrelevant computation path (dead function)
    return (x ** 2 + 3 * x + factor) / (factor + 1)

# Misleading global variables
temp_buffer = [0] * 15
offset_correction = 7.2
counter_log = {'reads': 0, 'writes': 0}

# Distractor: unused recursive function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Real logic begins: system performance evaluation
metrics = [85, 92, 78, 96, 88]
weights = [0.2, 0.3, 0.15, 0.25, 0.1]

# Simulated preprocessing with enumerate and zip (relevant)
normalized = []
for i, val in enumerate(metrics):
    adjusted = val * (1 + 0.01 * (i % 3))
    normalized.append(adjusted)

# Decoy transformation (not used in final result)
transformed_metrics = []
for x in metrics:
    transformed = (x + 10) * 0.9
    transformed_metrics.append(transformed)

# Bit manipulation red herring
decoys = []
for i in range(len(metrics)):
    decoy_val = i ^ 5 | 3
    decoys.append(decoy_val * 0.01)

# Core weighted evaluation using zip
weighted_sum = 0.0
for m, w in zip(normalized, weights):
    weighted_sum += m * w

# Conditional adjustment based on threshold logic
if weighted_sum > 85:
    adjustment = 5.0
elif weighted_sum > 75:
    adjustment = 2.5
else:
    adjustment = 0.0

# Additional distractor: sorting unrelated data
sorted_decoys = sorted(decoys, reverse=True)

# Unused dictionary mapping
category_map = {i: f'cat_{chr(65+i)}' for i in range(5)}

# Critical data structure: history log (partially relevant)
history = [{'step': j, 'value': weighted_sum - j * 0.3} for j in range(3)]

# Simulate short-circuit logic distraction
flag_trigger = False
status_code = (len(metrics) > 4) and (weights[0] < 0.25) or flag_trigger

# Actual key function
def evaluate_performance(mets, wts):
    total = 0.0
    for idx, (metric, weight) in enumerate(zip(mets, wts)):
        # Re-normalize using position
        factor = 1 + (idx % 2) * 0.05
        total += metric * factor * weight
    return total

# Final score calculation — KEY STATEMENT
final_score = evaluate_performance(metrics, weights)

# Red herring: modifying a variable not used later
final_score_temp = final_score + offset_correction

# Output the target result
print(f"Result: {final_score}")