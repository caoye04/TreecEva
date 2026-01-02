from collections import defaultdict

# Simulate developer contribution analysis with noise and distractions
def analyze_developer_activity(logs):
    activity_count = defaultdict(int)
    temp_memo = {}  # Unused distractor
    total_lines = 0
    invalid_entries = 0

    for entry in logs:
        parts = entry.split(' | ')
        if len(parts) < 3:
            invalid_entries += 1
            continue
        
        timestamp, user, action = parts[0], parts[1], parts[2]
        activity_count[user] += 1
        total_lines += len(action)

        # Distractor computation - not used later
        if 'bug' in action.lower():
            temp_memo[user] = temp_memo.get(user, 0) + 1

    return dict(activity_count), total_lines

# Secondary helper - partially relevant
def extract_metrics(counts):
    ranked = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    top_user = ranked[0][0] if ranked else 'none'
    total_devs = len(counts)
    return top_user, total_devs

# Core calculation with embedded logic chain
def calculate_rating(contributions, penalty_factor):
    base_score = 0
    adjustment = 0.0
    debug_trace = []  # Dead variable - distraction

    for dev, commits in contributions.items():
        if commits > 10:
            base_score += 25
        elif commits > 5:
            base_score += 15
        else:
            base_score += 5

        # Complex but irrelevant branching
        if len(dev) % 2 == 0 and commits % 3 == 0:
            adjustment += 1.5
        elif commits > 20:
            adjustment -= 0.7

    # Real impact step
    raw_total = base_score * (1 - penalty_factor)

    # Distractor: unnecessary list creation
    summary_stats = [base_score, adjustment, raw_total]
    final_score = int(raw_total - adjustment)  # adjustment subtracted to offset red herring

    return final_score

# Main execution flow
if __name__ == '__main__':
    log_data = [
        '2023-08-01|alice|implemented feature X',
        '2023-08-02|bob|fixed bug in module Y',
        '2023-08-03|alice|updated docs',
        '2023-08-04|carol|refactored pipeline',
        '2023-08-05|bob|added test cases',
        '2023-08-06|alice|optimized query',
        '2023-08-07|dave|initial commit',
        '2023-08-08|eve|resolved race condition',
        '2023-08-09|alice|patched security issue',
        '2023-08-10|bob|improved logging'
    ]

    contributions, lines = analyze_developer_activity(log_data)
    _, dev_count = extract_metrics(contributions)

    scaling_factor = 0.15
    penalty_factor = scaling_factor if dev_count > 3 else 0.05

    final_score = calculate_rating(contributions, penalty_factor)
    print(f"Result: {final_score}")