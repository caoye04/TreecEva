from collections import defaultdict
import math

# Irrelevant helper function (decoy)
def analyze_sentiment(text):
    return sum(ord(c) % 3 for c in text) * 0.1

def generate_noise(n):
    # Dead code path - never used in final computation
    noise = [0] * n
    for i in range(n):
        noise[i] = (i ** 2 + 3 * i + 7) % 100
    return noise

def transform_value(x, mode='basic'):
    if mode == 'advanced':
        return int((x ^ 245) / 7)  # Bitwise XOR red herring
    return (x * 2) + 1

# Unused but plausible-looking metric computation
def compute_bias_factor(items):
    count_map = defaultdict(int)
    for item in items:
        count_map[item % 5] += 1
    return max(count_map.values()) - min(count_map.values())

# Core logic disguised among distractors
data = [84, 93, 76, 88, 91]
weights = [0.2, 0.1, 0.3, 0.15, 0.25]

# Distractor variables
scaling_factor = 1.05
offset_correction = -0.02
normalization_constant = sum(w ** 2 for w in weights)  # Misleading normalization

# Real processing buried in abstraction
dataset_stats = {
    'mean': sum(data) / len(data),
    'range': max(data) - min(data)
}

# Red herring: complex-looking but unused transformation chain
temp_data = list(map(lambda x: transform_value(x % 25), data))
processed_pairs = list(enumerate(zip(temp_data, [w*100 for w in weights])))

# Actual core logic
mask = [1 if d > 85 else 0 for d in data]
effective_weights = [w * (1 + 0.1 * m) for w, m in zip(weights, mask)]

# Weighted sum with conditional boosting
weighted_sum = 0
for i, val in enumerate(data):
    boosted_val = val * (1.1 if mask[i] else 1.0)
    weighted_sum += boosted_val * effective_weights[i]

# Secondary adjustment based on distribution skew
skew_metric = (sum(1 for d in data if d >= 85) - 2) * 0.05  # Baseline at 2 high performers

# Final aggregation
raw_score = weighted_sum * (1 + skew_metric)

# Irrelevant rounding pipeline
decoy_rounding_steps = []
for step in range(3):
    decoy_rounding_steps.append(round(raw_score, 3 - step))

# Key statement
final_score = math.floor(raw_score + 0.5)  # Equivalent to round to nearest int

print(f"Result: {final_score}")