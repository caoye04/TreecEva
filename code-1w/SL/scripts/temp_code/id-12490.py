from collections import defaultdict
from itertools import combinations

def analyze_productivity(logs):
    daily_count = defaultdict(int)
    for day, tasks in logs.items():
        completed = sum(1 for status in tasks if status == 'done')
        daily_count[day] = completed
    return daily_count

def calculate_rating(items, factor):
    base = sum(len(item) for item in items)
    adjustment = 0
    temp_result = 0
    
    # Irrelevant combinatorial check (distractor)
    for r in range(2, 4):
        combos = list(combinations(items, r))
        temp_result += len(combos)  # unused accumulation

    # Semi-relevant filtering
    filtered = [item for item in items if len(item) > 1]
    if len(filtered) > 2:
        adjustment = len(filtered) // 2
    
    # Critical distraction: unused scoring path
    alternate_score = 0
    for item in items:
        if 'x' in item:
            alternate_score += hash(item) % 5
    # This is never used, but looks important

    # Actual score computation
    raw_score = base * (1 - factor)
    final = int(raw_score + adjustment)
    
    # Dead code branch (misleading)
    if factor < 0:
        final *= -1
        placeholder = [i for i in range(1000)]  # heavy-looking but unreachable
    
    return final

# Main simulation data
project_logs = {
    'monday': ['done', 'pending', 'done', 'done'],
    'tuesday': ['done', 'review', 'done'],
    'wednesday': ['blocked', 'done', 'done', 'done', 'done']
}

# Extract meaningful metric
productivity = analyze_productivity(project_logs)
task_lengths = [str(v) for v in productivity.values()]

# Introduce noise variables
penalty_factor = 0.25
threshold_check = any(count >= 4 for count in productivity.values())
summary_stats = {k: (v, v**2) for k, v in productivity.items()}  # unused

# Core calculation with key statement
contributions = ['feat', 'fix', 'docs', 'style', 'refactor']
final_score = calculate_rating(contributions, penalty_factor)

# Output result as required
print(f"Result: {final_score}")