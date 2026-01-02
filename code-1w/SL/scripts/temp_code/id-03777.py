import math

# Irrelevant helper function (decoy)
def compute_entropy(values):
    return sum(-p * math.log2(p) for p in values if p > 0)

# Misleading data structures
temp_log = [0.1, 0.5, 0.3, 0.9]
backup_registry = {'a': 10, 'b': 20, 'c': 30}
shadow_cache = {x: x**2 for x in range(5)}

# Real computation inputs
metric_weights = [0.4, 0.3, 0.2, 0.1]
raw_outcomes = [85, 90, 78, 92]

# Distractor: unused transformation chain
def transform_data(data):
    processed = [x + 10 for x in data]
    normalized = [x / max(processed) for x in processed]
    scaled = [int(x * 100) for x in normalized]
    return scaled

# Dead code path (never called)
class DataProcessor:
    def __init__(self, weights):
        self.weights = weights
        self.history = []

    def apply_filter(self, values):
        return [v * w for v, w in zip(values, self.weights)]

# Another red herring: complex but unused bitwise operation
def scramble_bits(x):
    x ^= (x << 3) & 0xFF
    x ^= (x >> 2)
    x ^= (x << 5)
    return x % 100

# Real logic hidden among distractions
def analyze_trend(sequence):
    diffs = [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    pos_count = len([d for d in diffs if d > 0])
    neg_count = len([d for d in diffs if d < 0])
    return 'upward' if pos_count > neg_count else 'downward'

# Auxiliary calculation with plausible but irrelevant intermediate
event_risk_profile = set()
for val in raw_outcomes:
    if val < 80:
        event_risk_profile.add('low')
    elif val < 90:
        event_risk_profile.add('medium')
    else:
        event_risk_profile.add('high')

# More distraction: fake aggregation
temporary_aggregate = 0
for k, v in backup_registry.items():
    temporary_aggregate += v * 0.1

# Core evaluation logic (non-obvious due to context noise)
def evaluate_performance(weights, outcomes):
    # Step 1: Apply exponential scaling to emphasize higher scores
    exp_scaled = [math.exp(outcome / 100) for outcome in outcomes]
    
    # Step 2: Normalize the exponential scores
    max_scaled = max(exp_scaled)
    normalized_scores = [s / max_scaled for s in exp_scaled]
    
    # Step 3: Weighted sum using metric weights
    weighted_sum = sum(w * s for w, s in zip(weights, normalized_scores))
    
    # Step 4: Adjust based on trend analysis (calls analyze_trend)
    trend = analyze_trend(outcomes)
    adjustment_factor = 1.05 if trend == 'upward' else 0.95
    
    # Step 5: Final adjustment and scaling to integer score
    adjusted_score = weighted_sum * adjustment_factor * 100
    
    # Step 6: Cap at maximum possible performance
    capped_score = min(adjusted_score, 100)
    
    # Step 7: Add bonus if all outcomes above threshold (not triggered here)
    bonus = 5 if all(o >= 85 for o in outcomes) else 0
    
    # Step 8: Compute final score
    final = round(capped_score + bonus)
    
    return final

# Additional noise: unused list comprehension with side effects
_ = [print(f"Processing item {i}") for i in range(2) if i > 5]  # Never executes

# Critical execution point
final_score = evaluate_performance(metric_weights, raw_outcomes)

# Print result as required
print(f"Result: {final_score}")