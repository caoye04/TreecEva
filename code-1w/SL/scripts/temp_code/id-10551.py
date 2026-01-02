from itertools import groupby

# Simulate user feedback analysis for a code education platform
user_responses = [
    (85, 'correct', 'loop'),
    (72, 'incorrect', 'condition'),
    (90, 'correct', 'function'),
    (68, 'incorrect', 'loop'),
    (77, 'correct', 'condition'),
    (88, 'correct', 'function'),
    (61, 'incorrect', 'condition'),
    (94, 'correct', 'loop')
]

# Extract performance by category using lambda
performance_by_type = lambda data, typ: [entry[0] for entry in data if entry[2] == typ]

# Calculate average score for a given category
def avg_score(scores):
    return round(sum(scores) / len(scores), 2) if scores else 0

# Categorize proficiency level based on average
def get_level(avg):
    if avg >= 85:
        return 'expert'
    elif avg >= 75:
        return 'intermediate'
    else:
        return 'beginner'

# Misleading auxiliary computation - not used in final result
total_incorrect = sum(1 for r in user_responses if r[1] == 'incorrect')
dummy_aggregates = {cat: avg_score(performance_by_type(user_responses, cat)) 
                        for cat in ['loop', 'condition', 'function']}
baseline_shift = 0.5 * total_incorrect  # Distractor variable

# Group responses by correctness first (irrelevant grouping)
sorted_by_correctness = sorted(user_responses, key=lambda x: x[1])
grouped_responses = {k: list(v) for k, v in groupby(sorted_by_correctness, key=lambda x: x[1])}

# Compute category averages - this will be used later
loop_scores = performance_by_type(user_responses, 'loop')
condition_scores = performance_by_type(user_responses, 'condition')
function_scores = performance_by_type(user_responses, 'function')

# Calculate proficiency levels for each category
category_avgs = {
    'loop': avg_score(loop_scores),
    'condition': avg_score(condition_scores),
    'function': avg_score(function_scores)
}

feedback_levels = []
for cat, avg in category_avgs.items():
    level = get_level(avg)
    # Inject extra logic with no impact
    adjustment = 0
    if level == 'expert':
        adjustment = 2.5
    elif level == 'beginner':
        adjustment = -1.0
    # Adjustment not applied - red herring
    feedback_levels.append((cat, level, avg))

# Unused transformation - dead code path
enhance = lambda item: (item[0], item[1].upper(), item[2])
uppercase_levels = [enhance(f) for f in feedback_levels]

# Core logic: aggregate performance based on number of 'expert' categories
expert_count = sum(1 for _, lvl, _ in feedback_levels if lvl == 'expert')
stability_factor = len([s for s in category_avgs.values() if s > 70])

# Final scoring formula
base_score = sum(category_avgs.values())
penalty = 3 * (3 - stability_factor)  # penalty if less than 3 stable categories

# Critical statement
final_score = aggregate_performance = lambda fs: int(base_score - penalty + 10 * expert_count)
final_score = aggregate_performance(feedback_levels)

print(f"Result: {final_score}")