from collections import Counter, defaultdict

# Simulate team contribution tracking in a collaborative coding project
def analyze_contributions(logs):
    user_activity = Counter()
    file_edits = defaultdict(int)
    edit_types = ['add', 'delete', 'modify']
    total_actions = 0

    for entry in logs:
        user, action, filename, lines = entry
        user_activity[user] += 1
        file_edits[filename] += lines
        total_actions += 1

    # Distractor: unused computation
    avg_per_file = len(file_edits) / (sum(file_edits.values()) + 1) if file_edits else 0
    
    return user_activity, file_edits

def compute_engagement_score(activity, weights=None):
    if not weights:
        weights = {'low': 1, 'medium': 3, 'high': 5}
    
    score = 0
    magnitude = sum(activity.values())
    level = 'low'
    
    if magnitude > 10:
        level = 'medium'
    if magnitude > 20:
        level = 'high'
    
    # Irrelevant scaling
    scaling_factor = 1.0
    if level == 'medium':
        scaling_factor = 1.2
    elif level == 'high':
        scaling_factor = 1.5

    base_score = weights[level] * len(activity)
    adjusted = base_score * scaling_factor
    
    # Dead code path (never reached due to logic)
    if scaling_factor > 2.0:
        adjusted *= 0.8
        
    return adjusted

def evaluate_performance(contributions, thresholds):
    # Core logic: calculate compliance ratio and weight by engagement
    compliant_users = 0
    total_users = len(contributions)
    min_threshold, max_threshold = thresholds
    
    for user, count in contributions.items():
        if min_threshold <= count <= max_threshold:
            compliant_users += 1
    
    compliance_rate = compliant_users / total_users if total_users else 0
    
    # Secondary metric: distribution balance
    counts = list(contributions.values())
    spread = max(counts) - min(counts) if counts else 0
    balance_penalty = 0
    if spread > 15:
        balance_penalty = spread * 0.1
    
    # Final scoring with distractor variables
    raw_compliance_score = compliance_rate * 100
    stability_adj = raw_compliance_score - balance_penalty
    final_score = int(stability_adj + 5)  # Add constant offset
    
    temp_debug = f'Score breakdown: {raw_compliance_score=}, {balance_penalty=}'  # unused
    
    return final_score

# Simulated activity log: (user, action, filename, lines_changed)
activity_log = [
    ('alice', 'add', 'main.py', 4),
    ('bob', 'modify', 'utils.py', 7),
    ('alice', 'delete', 'main.py', 2),
    ('carol', 'add', 'tests.py', 12),
    ('bob', 'add', 'docs.md', 3),
    ('alice', 'modify', 'main.py', 5),
    ('dave', 'add', 'config.json', 1),
    ('carol', 'modify', 'tests.py', 4),
    ('bob', 'delete', 'utils.py', 6),
    ('alice', 'add', 'main.py', 8),
    ('carol', 'add', 'tests.py', 9),
    ('dave', 'modify', 'config.json', 1),
    ('eve', 'add', 'README.md', 5),
    ('alice', 'add', 'main.py', 6),
    ('bob', 'add', 'utils.py', 10),
    ('carol', 'modify', 'tests.py', 3),
    ('alice', 'add', 'main.py', 7),
]

# Extract contributions
user_contributions, _ = analyze_contributions(activity_log)
engagement = compute_engagement_score(user_contributions)
enhanced_weight = engagement * 0.1  # unused in final logic

# Evaluate performance against expected thresholds (5-10 contributions)
target_thresholds = (5, 10)
final_score = evaluate_performance(user_contributions, target_thresholds)

print(f"Result: {final_score}")