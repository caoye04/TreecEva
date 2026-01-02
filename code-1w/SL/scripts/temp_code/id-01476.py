import math

# Irrelevant helper function (dead code path)
def deprecated_normalization(data):
    return [x / max(data) for x in data]

# Unused transformation lambdas (distractors)
smooth_data = lambda x: [i + 0.1 for i in x if i % 2 == 0]
drop_noise = lambda x: [i for i in x if abs(i) > 0.5]

# Real but obfuscated constants
THRESHOLD = 0.78
PENALTY_FACTOR = 0.3
WEIGHT_A = 0.4
WEIGHT_B = 0.6
OFFSET = -1.1

# Simulated sensor metrics with noise (mixed relevance)
raw_metrics = [0.81, 0.74, 0.89, 0.62, 0.91, 0.55, 0.77, 0.83]
filtered_metrics = [x for x in raw_metrics if x > 0.6]  # Filtering relevant values

# Decoy statistical computation
mean_value = sum(raw_metrics) / len(raw_metrics)
variance = sum((x - mean_value) ** 2 for x in raw_metrics) / len(raw_metrics)
std_dev = math.sqrt(variance)

# Misleading normalization branch
if std_dev > 0.1:
    normalized = [(x - mean_value) / std_dev for x in raw_metrics]
else:
    normalized = raw_metrics

# Actual processing begins here — buried under distractions
baseline = {"ref": 0.75, "tolerance": 0.05, "boost": 1.2}
efficiency_set = {x for x in filtered_metrics if x > THRESHOLD}  # Set operation (relevant)
penalty_set = {x for x in filtered_metrics if x < THRESHOLD}   # Another set (partially relevant)

# Composite score using lambda and conditional expressions
evaluate_component = lambda val, ref: 1.0 if val >= ref else (val / ref) * 0.5

def calculate_weighted_score(vals, base):
    score = 0.0
    for v in vals:
        comp = evaluate_component(v, base["ref"])
        if comp >= 0.9:
            score += WEIGHT_A * comp
        elif comp >= 0.7:
            score += WEIGHT_B * comp * base["boost"]
        else:
            score += comp * (1 - PENALTY_FACTOR)
    return score

# Red herring: unused recursive function
def recursive_distractor(n):
    if n <= 1:
        return 1
    return n * recursive_distractor(n - 2)  # Never called

# String manipulation decoy (simulating log parsing)
sim_log = "METRIC:VAL=0.81|STATUS:OK METRIC:VAL=0.74|STATUS:LOW"
log_entries = sim_log.split(' ')
status_map = {}
for entry in log_entries:
    parts = entry.split('|')
    if len(parts) == 2:
        metric_part = parts[0].split('=')[1]
        status_part = parts[1].split(':')[1]
        status_map[float(metric_part)] = status_part

# Dictionary used for side tracking (semi-relevant)
metric_analysis = {}
for m in filtered_metrics:
    category = 'high' if m >= THRESHOLD else 'low'
    metric_analysis[m] = {
        'category': category,
        'adjusted': m * (1.2 if category == 'high' else 0.8),
        'flagged': False
    }

# Conditional branch with early exit red herring
exit_early = False
bypass_value = 0.0
if len(efficiency_set) == 0:
    final_result = 0.0
    exit_early = True
elif len(penalty_set) > 4:
    bypass_value = -1.0
    exit_early = True

# Main evaluation logic hidden in complexity
composite_list = []
for k, v in metric_analysis.items():
    if v['category'] == 'high':
        composite_list.append(v['adjusted'])
    else:
        composite_list.append(k)  # unadjusted for low

# Core calculation buried in abstraction
def evaluate_performance(data, base):
    raw_score = calculate_weighted_score(data, base)
    adjustment = len(efficiency_set) * 0.05 - len(penalty_set) * 0.03
    bonus = 0.1 if len(efficiency_set) >= 3 else 0.0
    # Final formula combining arithmetic, sets, and conditionals
    result = (raw_score + adjustment + bonus + OFFSET) * 100
    # Apply artificial ceiling
    if result > 95:
        result = 95 + (result - 95) * 0.1  # dampen excessive scores
    return round(result, 6)

# Key execution point
final_score = evaluate_performance(composite_list, baseline)

# Output as required
print(f"Result: {final_score}")