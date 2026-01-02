def analyze_trend(data, threshold=0.5):
    trend = []
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            trend.append(1)
        elif data[i] < data[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return sum(trend) / len(trend) if trend else 0

# Irrelevant helper function (decoy)
def normalize_values(arr):
    max_val = max(arr) if arr else 1
    return [x / max_val for x in arr]

# Unused transformation path
def transform_case(text):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(text)])

# Dead code path with misleading intermediate
class DataProcessor:
    def __init__(self, scale=1.0):
        self.scale = scale
        self.history = []

    def record(self, value):
        self.history.append(value * self.scale)

    def get_peak(self):
        return max(self.history) if self.history else 0

# Distractor: unused statistical computation
def entropy(probabilities):
    from math import log
    return -sum(p * log(p) for p in probabilities if p > 0)

# Real logic begins here
def compute_weighted_sum(values, weights):
    return sum(v * w for v, w in zip(values, weights))

baseline = [0.8, 0.6, 0.9, 0.7]
metrics = [0.85, 0.72, 0.88, 0.75]

# Red herring: complex but unused bit manipulation
bit_mask = 0b101010
shifted = (bit_mask << 3) & 0xFF
inverted = ~shifted & 0xFF

# Another distraction: string-based key generation
config_key = "A" + str(len(baseline)) + transform_case("xyz")
dummy_set = {len(config_key), shifted, inverted}

# Conditional expression with distractor branches
data_mode = 'advanced' if sum(baseline) > 2.5 else 'basic'
scaling_factor = 1.5 if data_mode == 'advanced' else 0.8

# Simulate unused data pipeline
temp_data = [0.1, 0.2, 0.3]
smoothed = normalize_values(temp_data)

# Real processing starts
weight_vector = [1.2, 0.8, 1.0, 0.9]
effective_metrics = compute_weighted_sum(metrics, weight_vector)
expected_baseline = compute_weighted_sum(baseline, weight_vector)

# Set operation as required feature (distractor usage)
valid_ranges = {0.5, 0.6, 0.7, 0.8, 0.9}
coverage = len(valid_ranges.intersection(set(round(m, 1) for m in metrics)))

# Dictionary operations (required feature)
performance_gaps = {f'metric_{i}': metrics[i] - baseline[i] for i in range(len(metrics))}
positive_improvements = {k: v for k, v in performance_gaps.items() if v > 0}

drift = analyze_trend(metrics)

# Conditional logic with early exit red herring
if drift < 0:
    adjustment = -0.1
elif drift > 0.1:
    adjustment = 0.15
else:
    adjustment = 0.05  # This will be taken

# Final evaluation with conditional expression
raw_score = effective_metrics - expected_baseline

# Key statement
final_score = evaluate_performance(metrics, baseline) if raw_score > 0 else -1

def evaluate_performance(m, b):
    improvement = sum(mi - bi for mi, bi in zip(m, b))
    penalty = 0.0
    
    # Nested logic with multiple steps
    for i in range(len(m)):
        if m[i] < b[i]:
            penalty += 0.05
        elif m[i] > b[i] + 0.1:
            penalty -= 0.02  # Reward overachievement
    
    # Additional arithmetic and set interaction
    unique_improved = len({i for i in range(len(m)) if m[i] > b[i]})
    bonus = 0.1 if unique_improved >= 3 else 0.05
    
    # Final composition
    result = improvement - penalty + bonus + adjustment
    return round(result * 1000, 4)

# Ensure function is defined before call (move to top in execution)
# We reassign here to simulate correct order
final_score = evaluate_performance(metrics, baseline)
print(f"Result: {final_score}")