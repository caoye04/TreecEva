from collections import defaultdict

# Simulate developer contribution analysis with noise and distractions
def analyze_developer_metrics(contributions):
    total_lines = sum(contributions.values())
    commit_count = len(contributions)
    avg_per_commit = total_lines / commit_count if commit_count else 0

    # Distractor: irrelevant stats
    max_commit = max(contributions.values(), default=0)
    min_commit = min(contributions.values(), default=0)
    range_spread = max_commit - min_commit
    size_metric = len([v for v in contributions.values() if v > 50])

    # Semi-relevant transformation
    weighted_tally = 0
    for k, v in contributions.items():
        if 'refactor' in k:
            weighted_tally += v * 1.2
        elif 'bugfix' in k:
            weighted_tally += v * 1.5
        else:
            weighted_tally += v * 0.8

    return weighted_tally, avg_per_commit, size_metric

# Secondary distractor function
def compute_entropy(data):
    from math import log
    total = sum(data)
    if total == 0:
        return 0.0
    entropy = 0.0
    for x in data:
        p = x / total
        if p > 0:
            entropy -= p * log(p, 2)
    return round(entropy, 4)

# Main processing pipeline
contributions = {
    'feat_login': 120,
    'refactor_auth': 85,
    'bugfix_session': 40,
    'docs_update': 30,
    'perf_optimize': 90
}

# Irrelevant intermediate calculations
lines_by_type = defaultdict(int)
for k, v in contributions.items():
    prefix = k.split('_')[0]
    lines_by_type[prefix] += v

# Unused entropy computation (distractor)
entropy_value = compute_entropy(list(contributions.values()))

# Real logic begins
base_weighted, average_lines, large_commits = analyze_developer_metrics(contributions)

# Apply conditional adjustment based on project phase
project_phase = 'maintenance'
phase_multiplier = 1.0
if project_phase == 'initial':
    phase_multiplier = 0.7
elif project_phase == 'maintenance':
    phase_multiplier = 1.3

adjusted_base = base_weighted * phase_multiplier

# Penalty system for low productivity signals
total_contrib = sum(contributions.values())
penalty_factor = 1.0
if average_lines < 50:
    penalty_factor *= 0.9
if 'docs' in str(contributions) and total_contrib > 200:
    penalty_factor *= 0.95

# Core rating calculation — this is where final_score is determined
def calculate_rating(raw_score, penalty):
    initial = raw_score * 0.85
    deduction = initial * (1 - penalty)
    return int(initial - deduction)

final_score = calculate_rating(adjusted_base, penalty_factor)

# Additional red herring computations
snapshot = {k.upper(): v * 0.1 for k, v in contributions.items()}
scaled_entropy = entropy_value * 10
buffer_zone = [scaled_entropy * i for i in range(3)]

# Critical output
print(f"Result: {final_score}")