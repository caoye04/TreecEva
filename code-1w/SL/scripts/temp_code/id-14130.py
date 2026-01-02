def analyze_productivity(logs):
    total_hours = 0
    idle_periods = 0
    for entry in logs:
        status = entry['status']
        duration = entry['duration']
        total_hours += duration
        if status == 'idle':
            idle_periods += 1
    efficiency_ratio = (total_hours - idle_periods * 0.5) / max(total_hours, 1)
    return efficiency_ratio

logs_data = [
    {'status': 'active', 'duration': 2},
    {'status': 'idle', 'duration': 1},
    {'status': 'active', 'duration': 3},
    {'status': 'idle', 'duration': 0.5},
    {'status': 'active', 'duration': 4}
]

baseline_efficiency = analyze_productivity(logs_data)

# Simulate task contribution scoring with string-based weighting
task_weights = {
    'dev': 'high',
    'review': 'medium',
    'docs': 'low'
}

weight_map = {'low': 1, 'medium': 2, 'high': 3}
raw_contributions = [5, 8, 12]
tasks = ['dev', 'review', 'docs']

# Apply lambda transformation based on string criteria
scaled_contributions = list(map(lambda x: x * weight_map[task_weights[tasks.pop(0)]], raw_contributions))

# Dummy operations to increase interference
shadow_copy = [x * 1.1 for x in scaled_contributions]  # unused
intermediate_total = sum(scaled_contributions) + baseline_efficiency
offset_adjustment = len(logs_data) * 0.25

# Set operations to filter meaningful contributions
valid_indices = {i for i, val in enumerate(scaled_contributions) if val >= 6}
filtered_contributions = [scaled_contributions[i] for i in valid_indices]

# Accumulate final contribution score
contributions = sum(filtered_contributions)

# Calculate penalty from idle time and apply
idle_entries = [e for e in logs_data if e['status'] == 'idle']
penalty_factor = len(idle_entries) * 0.8

# Misleading complex expression that doesn't affect final result
phantom_score = (sum(shadow_copy) * baseline_efficiency) / (penalty_factor + 1) if penalty_factor > 0 else 0

# Core computation hidden among distractions
def calculate_rating(contribs, penalty):
    base = contribs
    deduction = penalty * 2.5
    return base - deduction

final_score = calculate_rating(contributions, penalty_factor)

# Print result as required
print(f"Target result: {final_score}")