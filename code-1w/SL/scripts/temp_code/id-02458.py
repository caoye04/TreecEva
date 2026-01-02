def analyze_productivity(values):
    base = sum(v ** 0.5 for v in values if v > 0)
    penalty = len([v for v in values if v < 5]) * 0.5
    return base - penalty

# Simulate employee performance metrics across departments
team_a = [8, 12, 4, 16, 3]
team_b = [9, 7, 11, 6, 14]

# Irrelevant intermediate calculation (distractor)
avg_team_a = sum(team_a) / len(team_a)
max_team_b = max(team_b)
dropped_calc = (avg_team_a + max_team_b) / 2 * 0.3  # Not used later

# Adjustment factors using dictionary and lambda
corrections = {'late': 0.92, 'overtime': 1.15, 'bonus': 1.08}
apply_adjust = lambda x, cond: x * corrections[cond] if cond in corrections else x

# Complex data structure with nested logic
metrics = {
    'efficiency': analyze_productivity(team_a),
    'output': sum(team_b),
    'consistency': len(team_a) if sum(team_b) > 40 else 0
}

# Multiple conditional expressions and distractors
status = 'high' if metrics['output'] > 45 else 'medium' if metrics['consistency'] else 'low'
threshold = 10 if status == 'high' else 15

# Unused variables to increase interference (dead code paths)
temp_factor = threshold * 1.2 if status == 'medium' else 0
dummy_map = {i: apply_adjust(v, 'bonus') for i, v in enumerate(team_a)}

# Real adjustment computation
adjustments = [
    apply_adjust(metrics['efficiency'], 'overtime'),
    apply_adjust(metrics['output'], 'bonus')
]

# Core logic with distractors embedded
intermediate = metrics['consistency'] * 2.5 if metrics['efficiency'] > 10 else 0
fallback = sum([x for x in adjustments if x > 20]) // 2

# Key statement
final_score = process_performance(metrics, adjustments) if 'efficiency' in metrics else fallback

# Helper function defined late to obscure flow
def process_performance(data, adj):
    raw = data['efficiency'] + data['output'] * 0.1
    bonus = adj[0] * 0.05 if adj else 0
    return int(raw + bonus + data.get('consistency', 0))

# Print result for evaluation
Result: {final_score}