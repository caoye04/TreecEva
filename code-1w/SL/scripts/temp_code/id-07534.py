from collections import Counter

# Simulate daily task tracking for a software developer over a week
tasks_completed = [8, 6, 9, 7, 10]
errors_per_day = [2, 1, 3, 0, 4]
distractions_log = ['email', 'meeting', 'phone', 'none', 'interruption', 'meeting', 'email']

# Auxiliary data - not all used directly
daily_hours = [7.5, 6.0, 8.0, 7.0, 9.0]
breaks_taken = [3, 2, 4, 1, 5]

# Compute productivity score with diminishing returns
def compute_productivity(tasks):
    base = sum(tasks)
    penalty = 0
    for t in tasks:
        if t > 8:
            penalty += (t - 8) * 0.5  # Effort quality degrades after 8 tasks
    return base - penalty

# Count distraction types (distractor: looks relevant but isn't used in final logic)
distraction_counter = Counter(distractions_log)
most_common_distraction = distraction_counter.most_common(1)

# Evaluate error severity with tiered weights
def compute_error_cost(errors):
    cost = 0
    for e in errors:
        if e <= 1:
            cost += e * 1.0
        elif e <= 3:
            cost += e * 1.5
        else:
            cost += e * 2.0  # High errors heavily penalized
    return cost

# Core evaluation function
def evaluate_performance(task_list, error_list, threshold=7.0):
    productivity = compute_productivity(task_list)
    total_errors = sum(error_list)
    error_cost = compute_error_cost(error_list)
    
    # Normalize productivity to 0-10 scale
    max_possible = len(task_list) * 10
    normalized_productivity = (productivity / max_possible) * 10
    
    # Apply error adjustment
    adjusted_score = normalized_productivity - (error_cost / 5)
    
    # Additional irrelevant computation (distractor)
    efficiency_ratio = productivity / (sum(daily_hours) + 1e-5) if daily_hours else 0
    
    # Threshold-based bonus/penalty
    if adjusted_score >= threshold:
        final = adjusted_score + 1.5
    else:
        final = adjusted_score - 1.0
    
    return round(final, 4)

# Misleading conditional - appears important but doesn't affect outcome
if len(breaks_taken) == len(tasks_completed):
    baseline_efficiency = sum(tasks_completed) / sum(breaks_taken)

# Key statement
final_score = evaluate_performance(tasks_completed, errors_per_day, threshold=7.0)

# Irrelevant string processing (uses string method as per requirement)
distraction_summary = ''.join([d[0] for d in distractions_log]).upper()
summary_checksum = len(distraction_summary) + sum([ord(c) for c in distraction_summary]) % 100

print(f"Result: {final_score}")