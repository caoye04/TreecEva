from itertools import combinations

# Simulate a competitive coding event with partial scoring and penalty tracking
def evaluate_submissions(scores, attempts):
    base_points = sum([s for s in scores if s > 0])
    failed_attempts = len([a for a in attempts if not a])
    adjustment_factor = 0.95 ** failed_attempts

    # Irrelevant computation: count digit occurrences in attempt indices
    digit_count = 0
    for idx in range(len(attempts)):
        digit_count += len(str(idx))

    adjusted_points = base_points * adjustment_factor
    return round(adjusted_points, 2)

# Process team qualification rounds
def generate_pairwise_metrics(team_data):
    metrics = []
    for pair in combinations(team_data.keys(), 2):
        score_diff = abs(team_data[pair[0]] - team_data[pair[1]])
        metrics.append(score_diff)
    
    # Distractor: unused statistical moment calculation
    mean_metric = sum(metrics) / len(metrics) if metrics else 0
    variance_proxy = sum([(m - mean_metric) ** 2 for m in metrics]) / len(metrics) if metrics else 0

    return metrics

# Main evaluation pipeline
def compute_ranking(raw_points, infractions):
    # Apply per-problem bonuses
    enhanced = [p + (2 if i % 3 == 0 else 0) for i, p in enumerate(raw_points)]
    
    # Penalty processing
    deduction = sum([inf * 5 for inf in infractions])
    temp_result = sum(enhanced) - deduction
    
    # State tracking variables (some irrelevant)
    snapshot_log = []
    for step in range(3):
        snapshot_log.append(f'Step_{step}: {temp_result - step * 2}')
    
    # Core ranking logic
    multiplier = 1.1 if temp_result > 80 else 1.05
    final_value = temp_result * multiplier
    
    # Dead code path: debugging trace (never accessed in normal execution)
    debug_mode = False
    if debug_mode:
        print('Trace:', snapshot_log)
        
    return int(round(final_value))

# Input data
problem_scores = [12, 15, 0, 20, 8, 18]
attempt_outcomes = [True, True, False, True, True, False]
team_ranks = {'Alpha': 85, 'Beta': 72, 'Gamma': 88}
penalty_flags = [1, 0, 2, 1]

# Execution pipeline
points = evaluate_submissions(problem_scores, attempt_outcomes)
intermediate_analysis = generate_pairwise_metrics(team_ranks)
final_score = compute_ranking(problem_scores, penalty_flags)

print(f"Target result: {final_score}")