def analyze_metrics(data, threshold):
    if not data:
        return 0
    filtered = [x for x in data if x > threshold]
    return sum(filtered) // len(filtered) if filtered else 0

# Irrelevant utility function (decoy)
def compute_entropy(values):
    from math import log
    total = sum(values)
    entropy = 0
    for v in values:
        prob = v / total
        entropy -= prob * log(prob)
    return entropy

# Misleading performance indicator (dead path)
current_ranking = 12
temporal_weight = 0.85
baseline_offset = -7

# Real data pipeline
raw_feedback = [4.2, 3.8, 4.5, 4.0, 3.9, 4.3, 4.1, 3.7]
smoothing_factor = 1.05
adjusted_feedback = [round(x * smoothing_factor, 2) for x in raw_feedback]

# Simulate noise injection and filtering
noisy_data = adjusted_feedback + [2.1, 5.5, 1.9]  # outliers added
valid_range = (3.5, 5.0)
filtered_feedback = [score for score in noisy_data if valid_range[0] <= score <= valid_range[1]]

# Set operations: identify consistent performers
feedback_set = set(adjusted_feedback)
high_performers = {x for x in feedback_set if x >= 4.2}
outliers = {x for x in feedback_set if x < 3.8}
consistency_pool = feedback_set - outliers  # meaningful subset

# Dummy transformation chain (distractor)
scaling_register = [1.0]
for i in range(len(filtered_feedback)):
    scaling_register.append(scaling_register[-1] * 0.95 + 0.1)
decay_adjusted_sum = sum(filtered_feedback) * scaling_register[-1]

# Control flow with red herring variables
if len(high_performers) > 3:
    calibration_factor = 1.1
    shadow_modifier = 0.07  # unused
    reference_anchor = 4.0      # unused
else:
    calibration_factor = 0.95
    debug_trace = [0]*5         # dead code block
    for i in range(5):
        debug_trace[i] = i**3

# Core aggregation logic
performance_log = []
for val in consistency_pool:
    if val >= 4.0:
        performance_log.append(val ** 2)
    else:
        performance_log.append(val)

# Key computation with conditional expression
aggregate_performance = lambda s, c: c * (sum(s) / len(s)) if s else 0
intermediate_result = aggregate_performance(consistency_pool, 1.0)

# Final score calculation (answer point)
final_score = aggregate_performance(consistency_pool, calibration_factor)

# Redundant print statements (distractors)
print(f'Debug: {len(raw_feedback)} entries processed')
print(f'Filtered count: {len(filtered_feedback)}')
print(f'High performers: {len(high_performers)}')

# Critical output
Target result: {final_score}