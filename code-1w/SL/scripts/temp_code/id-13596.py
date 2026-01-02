def analyze_component(x, threshold=5):
    if x < threshold:
        return (x ** 2) + 3
    else:
        return (x // 2) - 1

# Irrelevant helper function (dead path)
def deprecated_calculator(a, b):
    return (a + b) * 2  # Never used

# Distractor variables
temp_buffer = [i * 1.5 for i in range(8)]
scaling_factor = 0.95
offset_correction = sum([1 if i % 2 == 0 else 0 for i in temp_buffer])

# Real data path
raw_inputs = [4, 7, 6, 3, 8]
processed = [analyze_component(x) for x in raw_inputs]

# Bit manipulation red herring
bitmask = 0b10101
masked_values = [v ^ bitmask for v in processed]  # Unused

# Weighting system with decoy logic
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

# Fake normalization (never applied)
normalized = [val / max(processed) for val in processed]  # Computed but unused

# Another distraction: recursive countdown (no side effects)
def countdown(n):
    if n <= 0:
        return 0
    return n - countdown(n - 1)

_ = countdown(5)  # Called but result ignored

# Core logic buried in noise
metrics = []
for idx, val in enumerate(processed):
    adjustment = 1
    if idx % 2 == 0:
        adjustment += 0.1
    if val > 10:
        adjustment *= 1.05
    metrics.append(val * adjustment)

# Decoy aggregation
mean_metric = sum(metrics) / len(metrics)
median_metric = sorted(metrics)[len(metrics)//2]

# Actual evaluation function
def evaluate_performance(mets, wts):
    total = 0
    for i in range(len(mets)):
        contribution = mets[i] * wts[i]
        if contribution > 5:
            total += contribution * 0.9  # Apply penalty
        else:
            total += contribution * 1.1  # Bonus for low values
    return int(total * 1.02)  # Final scaling and cast

# Critical assignment
final_score = evaluate_performance(metrics, weights)

print(f"Result: {final_score}")