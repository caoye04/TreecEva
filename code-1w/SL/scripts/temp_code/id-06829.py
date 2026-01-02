import math

# Irrelevant helper function (dead code path)
def unused_diagnostic_check(data):
    return sum([x ** 2 for x in data if x > 5])

# Misleading preprocessing with decoy transformations
def decoy_normalize(values):
    adjusted = [(v - min(values)) / (max(values) - min(values) + 1e-8) for v in values]
    return [round(a * 100) for a in adjusted]  # Scaled but never used

# Distractor: complex bit manipulation with no real impact
def hidden_bit_flag(n):
    flag = (n ^ (n << 1)) & 0xF
    return flag >> 1 if flag else n | 7

# Unused statistical validation
validity_threshold = 0.95
def validate_consistency(logs):
    diffs = [abs(logs[i] - logs[i-1]) for i in range(1, len(logs))]
    return sum(d > 0.1 for d in diffs) / len(diffs) < validity_threshold

# Core logic disguised among noise
base_metrics = [3.2, 4.1, 2.7, 5.5, 4.8]
weights = [0.1, 0.2, 0.15, 0.3, 0.25]

# Irrelevant transformation chain
temp_scaled = [math.log(x + 10) for x in base_metrics]
decoy_ranks = sorted(temp_scaled, reverse=True)
rank_map = {val: idx for idx, val in enumerate(decoy_ranks)}

# Real computation buried in noise
adjusted_metrics = [
    m * (1.1 if i % 2 == 0 else 0.9)  # Conditional expression
    for i, m in enumerate(base_metrics)
]

# Fake aggregation
phantom_total = sum([w ** 2 * m for w, m in zip(weights, adjusted_metrics)])

# Another red herring: conditional branch that doesn't affect outcome
if sum(base_metrics) > 15:
    adjustment_factor = 1.05
else:
    adjustment_factor = 0.95  # Not actually applied below

# Real weighted score calculation (only this matters)
effective_weights = [w * (1.2 if w >= 0.2 else 0.8) for w in weights]
normalized_weights = [w / sum(effective_weights) for w in effective_weights]
weighted_sum = sum(m * w for m, w in zip(adjusted_metrics, normalized_weights))

divergence_penalty = 0.0
for i in range(len(adjusted_metrics) - 1):
    divergence_penalty += abs(adjusted_metrics[i] - adjusted_metrics[i+1])
divergence_penalty *= 0.05

# Key function containing the answer
def evaluate_performance(data):
    raw_score = weighted_sum  # Depends on prior closed-form calc
    noise_floor = math.sin(math.pi / 6)  # Constant: 0.5
    final_adjustment = raw_score - divergence_penalty + noise_floor
    
    # Decoy branching with conditional expression
    status_flag = 'optimal' if final_adjustment > 4.0 else 'suboptimal'
    
    # Final irrelevant bitwise check
    audit_id = 237
    flag_check = (audit_id ^ 0xAA) & 0x0F
    
    # Only this line contributes to meaningful output
    return round(final_adjustment * 100) / 100  # Precision clipping

# Trigger execution
temp_diag = unused_diagnostic_check(base_metrics)
metric_data = decoy_normalize(base_metrics)
validate_consistency(metric_data)  # Returns True but unused

# Critical statement
final_score = evaluate_performance(metric_data)

print(f"Result: {final_score}")