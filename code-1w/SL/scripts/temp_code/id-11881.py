from collections import defaultdict

# Simulate developer contribution analysis with noise and distractions
def analyze_developer_activity(logs):
    activity_count = defaultdict(int)
    file_types = set()
    total_lines = 0
    distraction_counter = 0  # Irrelevant tracking

    for entry in logs:
        action, file_name, lines = entry.split('|')
        lines = int(lines)
        extension = file_name.split('.')[-1]
        
        activity_count[action] += 1
        file_types.add(extension)
        total_lines += abs(lines)  # Use absolute for consistency

        # Distracting logic: tracks something unused later
        if 'test' in file_name.lower():
            distraction_counter += 1

    return activity_count, len(file_types), total_lines

# Secondary helper with red herring output
def compute_temporal_bias(timestamps):
    weighted_sum = 0.0
    decay = 0.95
    for i, t in enumerate(timestamps):
        weighted_sum += t * (decay ** i)  # Older timestamps matter less
    return weighted_sum if weighted_sum > 0 else 0.1  # Avoid zero

# Core calculation buried among distractions
def calculate_rating(contribs, penalty):
    base = sum(contribs.values())
    bonus = 0
    
    # Meaningful branching
    if contribs.get('commit', 0) > 5:
        bonus += 10
    if contribs.get('push', 0) == 0:
        bonus -= 5

    # Real computation
    raw_score = base * 2 + bonus
    applied_penalty = raw_score * (1 - penalty)
    
    # Dead code branch (never reached due to structure, but looks active)
    if False:
        applied_penalty = max(applied_penalty, 5)  # Unused

    return int(applied_penalty)

# Simulated input data
log_entries = [
    'commit|app.py|45',
    'push|app.py|45',
    'edit|utils.js|23',
    'commit|utils.js|23',
    'edit|styles.css|12',
    'commit|docs.md|6',
    'review|app.py|0',
    'commit|tests.py|-10',  # Negative lines (deletion)
    'edit|config.json|8'
]

timestamp_sequence = [1672531200, 1672534800, 1672538400, 1672542000, 1672545600]

# Extract meaningful metrics
contribution_stats, unique_extensions, total_loc = analyze_developer_activity(log_entries)

# Compute irrelevant temporal bias (used nowhere critical)
temporal_influence = compute_temporal_bias(timestamp_sequence)

# Noise variables to increase cognitive load
average_commit_size = total_loc / contribution_stats.get('commit', 1)
duplicate_ratio = len(log_entries) / (unique_extensions + 1) if unique_extensions else 0

# Key statement
penalty_factor = 0.15
final_score = calculate_rating(contribution_stats, penalty_factor)

# Output result
print(f"Result: {final_score}")