from collections import defaultdict, Counter
from itertools import combinations, chain

# Simulated dataset: user activity logs with various actions
def generate_activity_logs():
    logs = [
        {'user': 'alice', 'action': 'login', 'duration': 30},
        {'user': 'bob', 'action': 'edit', 'duration': 45},
        {'user': 'alice', 'action': 'export', 'duration': 60},
        {'user': 'carol', 'action': 'login', 'duration': 20},
        {'user': 'bob', 'action': 'print', 'duration': 15},
        {'user': 'alice', 'action': 'edit', 'duration': 50},
        {'user': 'dave', 'action': 'login', 'duration': 10},
        {'user': 'carol', 'action': 'edit', 'duration': 40}
    ]
    return logs

# Irrelevant helper: computes pairwise combinations of users (not used in final score)
def compute_user_pairs(users):
    return list(combinations(users, 2))

# Misleading aggregation: total duration per action (looks important but unused)
def aggregate_by_action(logs):
    agg = defaultdict(int)
    for log in logs:
        agg[log['action']] += log['duration']
    return agg

# Decoy function: calculates frequency of actions (never called)
def count_action_frequency(logs):
    return Counter([log['action'] for log in logs])

# Core processing: group by user and compute weighted engagement
# Weight = duration + 10 if action is 'edit' or 'export'
def process_user_engagement(logs):
    user_scores = defaultdict(float)
    action_weights = {'edit': 1.5, 'export': 2.0}  # bonus multipliers

    for log in logs:
        base = log['duration']
        action = log['action']
        weight = action_weights.get(action, 1.0)
        user_scores[log['user']] += base * weight
    
    return user_scores

# Secondary transformation: normalize scores to 0-100 scale
def normalize_scores(scores):
    if not scores:
        return {}
    max_score = max(scores.values())
    min_score = min(scores.values())
    if max_score == min_score:
        return {k: 50.0 for k in scores}
    
    normalized = {}
    for k, v in scores.items():
        normalized[k] = (v - min_score) / (max_score - min_score) * 100
    
    return normalized

# Another red herring: finds long sessions (duration > 40), but result unused
def extract_long_sessions(logs):
    long_ones = []
    for log in logs:
        if log['duration'] > 40:
            long_ones.append(log)
    return long_ones

# Bit manipulation decoy: scrambles user ID lengths (irrelevant)
def obfuscate_user_lengths(users):
    result = 0
    for user in users:
        length = len(user)
        result ^= (length << 2) | (length >> 1)  # arbitrary bit juggling
    return result

# Main scoring logic: combines normalized engagement with fixed bonus
# Bonus awarded only if at least 3 users have score > 60
def calculate_final_score(normalized):
    bonus = 0
    high_performers = [u for u, s in normalized.items() if s > 60]
    
    if len(high_performers) >= 3:
        bonus = 25
    
    base_total = sum(normalized.values())
    return int(base_total + bonus)

# Dead code path: clustering by duration ranges (never invoked)
def cluster_durations(logs):
    clusters = defaultdict(list)
    for log in logs:
        d = log['duration']
        if d < 25:
            clusters['short'].append(log)
        elif d < 50:
            clusters['medium'].append(log)
        else:
            clusters['long'].append(log)
    return clusters

# Orchestrator with multiple distractions
if __name__ == '__main__':
    # Step 1: Load raw data
    raw_logs = generate_activity_logs()
    
    # Step 2: Extract users (used later)
    users = list(set(log['user'] for log in raw_logs))
    
    # Step 3: Compute irrelevant pairings
    user_pairs = compute_user_pairs(users)  # dead end
    
    # Step 4: Aggregate by action (misleading metric)
    action_totals = aggregate_by_action(raw_logs)
    
    # Step 5: Process core engagement scores
    raw_engagement = process_user_engagement(raw_logs)
    
    # Step 6: Normalize the scores
    normalized_engagement = normalize_scores(raw_engagement)
    
    # Step 7: Extract long sessions (unused)
    long_sessions = extract_long_sessions(raw_logs)
    
    # Step 8: Obfuscate user lengths (completely irrelevant)
    obfuscated_key = obfuscate_user_lengths(users)
    
    # Step 9: Cluster durations (dead code, never used)
    duration_clusters = cluster_durations(raw_logs)
    
    # Step 10: Calculate final score from normalized values
    final_score = calculate_final_score(normalized_engagement)
    
    # Output the target result
    print(f"Result: {final_score}")