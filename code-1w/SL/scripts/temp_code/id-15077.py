from collections import defaultdict
from itertools import combinations

# Simulated benchmark data across multiple test phases
test_phases = ['arithmetic', 'logic', 'assignment', 'control_flow']
raw_scores = [87, 92, 78, 85]
execution_times = [120, 95, 145, 110]
error_counts = [3, 1, 6, 4]

# Misleading auxiliary metrics (distractors)
stress_factor = 1.15
penalty_weights = {'latency': 0.3, 'errors': 0.7, 'consistency': 0.1}
consistency_metrics = defaultdict(lambda: 0.95)
for phase in test_phases:
    consistency_metrics[phase] += 0.01 * (100 - raw_scores[test_phases.index(phase)])

# Auxiliary function that seems important but is only partially used
def compute_adjusted_time(time, errors):
    adjustment = 1 + (errors * 0.05)
    return time * adjustment

# Another distractor: unused helper function
def analyze_phase_variability(scores):
    mean = sum(scores) / len(scores)
    variance = sum((x - mean) ** 2 for x in scores) / len(scores)
    return variance  # never actually used

# Key transformation pipeline
scaled_scores = []
for i, score in enumerate(raw_scores):
    normalized = (score / 100) * 100  # redundant but realistic
    time_penalty = (execution_times[i] - 100) * 0.1 if execution_times[i] > 100 else 0
    error_penalty = error_counts[i] * 2.5
    adjusted_score = normalized - time_penalty - error_penalty
    scaled_scores.append(max(adjusted_score, 0))

# Complex aggregation using lambda and itertools
pairwise_improvements = list(combinations(scaled_scores, 2))
boost_factor = sum(
    1 for a, b in pairwise_improvements if b > a
) / len(pairwise_improvements) if pairwise_improvements else 0

# Core calculation logic
baseline_efficiency = sum(scaled_scores) / len(scaled_scores)

# Final performance model
modifiers = {
    'speed_mod': max(0, 1 - sum(execution_times) * 0.001),
    'error_mod': 1 - (sum(error_counts) * 0.01),
    'balance_mod': 0.9 + (min(scaled_scores) * 0.005)
}

# Unused modifier path (dead code path - adds interference)
if stress_factor > 1.1:
    modifiers['stress_impact'] = 0.95

# Actual formula uses only subset of modifiers
active_modifiers = [modifiers['speed_mod'], modifiers['error_mod']]
efficiency_rating = baseline_efficiency * (sum(active_modifiers) / len(active_modifiers))

# Secondary scoring dimension: growth potential (semi-relevant)
growth_potential = 0
for i in range(1, len(scaled_scores)):
    diff = scaled_scores[i] - scaled_scores[i-1]
    if diff > 0:
        growth_potential += diff * 0.5

# Main entry point: what we're evaluating
def calculate_performance(data):
    base = efficiency_rating
    bonus = growth_potential * 0.3
    penalty = (6 - len(data.get('missing_phases', []))) * 0.2  # irrelevant key
    result = base + bonus - penalty
    return round(result, 2)

# Execution context
benchmark_data = {
    'phases': test_phases,
    'scores': raw_scores,
    'times': execution_times,
    'errors': error_counts
}

# Critical statement
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")