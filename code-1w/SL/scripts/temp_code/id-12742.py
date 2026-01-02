from collections import defaultdict, Counter
import math

# Simulate system telemetry data (irrelevant but plausible)
telemetry = defaultdict(lambda: 0)
telemetry['boot_count'] = 12
for i in range(5):
    telemetry[f'sensor_{i}'] = (i ** 3) % 7

def analyze_signal_strength(signal_log):
    # Irrelevant recursive analysis with no impact on final result
    if len(signal_log) <= 1:
        return 0
    mid = len(signal_log) // 2
    return signal_log[mid] + analyze_signal_strength(signal_log[:mid])

# Dummy signal processing
log_data = [3, 6, 9, 12, 15, 18]
signal_value = analyze_signal_strength(log_data)

# Core task: performance evaluation with distractors
base_metrics = [85, 90, 78, 92, 88]
adjustment_factors = [0.95, 1.02, 0.99, 1.01, 0.97]

# Apply adjustments (some irrelevant)
adjusted = []
for i in range(len(base_metrics)):
    val = base_metrics[i] * adjustment_factors[i]
    if val > 90:
        val += 2  # Minor boost for high performers (distractor)
    adjusted.append(round(val, 2))

# Weighted scoring setup
weights = [0.2, 0.3, 0.1, 0.25, 0.15]
metrics = [m + 5 for m in adjusted]  # Artificial inflation (partially relevant)

# Decoy transformation using bitwise and modular arithmetic
transformed = []
for x in metrics:
    temp = int(x) ^ 255  # Bit-flip lower byte (irrelevant)
    temp = (temp % 100) * 1.05  # Wrap and scale (red herring)
    transformed.append(temp)

# Conditional logic with misleading branches
penalty_mode = False
if sum(metrics) / len(metrics) > 100:
    penalty_mode = True
    for i in range(len(metrics)):
        metrics[i] *= 0.9  # This block never executes (dead path)

# Another decoy: frequency counting of irrelevant values
counter = Counter()
for t in transformed:
    bucket = int(t // 10)
    counter[bucket] += 1

# Real calculation buried among distractions
effective_values = []
for i in range(len(metrics)):
    raw = metrics[i]
    w = weights[i]
    # Key computation: exponential decay weighting based on position
    decay = math.exp(-0.2 * i)
    contribution = raw * w * decay
    effective_values.append(contribution)

# Secondary adjustment using conditional expression
total_base = sum(effective_values)
bonus_applied = 1.05 if total_base > 40 else 1.0
adjusted_total = total_base * bonus_applied

# Final nonlinear transformation
final_score = int(adjusted_total) & 0xFFFF  # Clamp to 16-bit (but within range)

# Print required output
print(f"Result: {final_score}")