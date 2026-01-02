from collections import defaultdict, Counter

# Simulate user interaction logs with various actions
def simulate_user_actions():
    actions = [
        'click:start', 'hover:menu', 'click:settings', 'type:input',
        'click:submit', 'drag:slider', 'click:confirm', 'hover:tooltip',
        'click:start', 'type:search', 'click:result', 'click:purchase'
    ]
    return actions

# Extract action types and count frequency
def analyze_actions(logs):
    counts = defaultdict(int)
    for entry in logs:
        action = entry.split(':')[0]
        counts[action] += 1

    # Irrelevant transformation (distractor)
    temp_data = {k: v * 1.5 for k, v in counts.items()}
    normalized = {k: int(v) for k, v in temp_data.items()}  # Truncate decimals

    return dict(counts), normalized

# Legacy function - unused but looks relevant (dead code path)
def calculate_legacy_score(data):
    score = 0
    for val in data.values():
        score += val ** 2
    return score * 0.75

# Core logic: map action frequency to rank category
def get_rank_category(frequency_map):
    total_actions = sum(frequency_map.values())
    unique_actions = len(frequency_map)

    # Compute derived metrics (some are red herrings)
    avg_per_action = total_actions / unique_actions if unique_actions else 0
    entropy_like_metric = 0
    for count in frequency_map.values():
        if count > 0:
            prob = count / total_actions
            entropy_like_metric -= prob * (prob ** 0.5)

    # Determine rank based on heuristic thresholds (actual relevant logic)
    if total_actions >= 8 and frequency_map.get('click', 0) >= 4:
        return 'A'
    elif total_actions >= 6 and avg_per_action >= 1.8:
        return 'B'
    else:
        return 'C'

# String-based risk heuristic (uses string method - relevant distractor)
def assess_risk_level(actions):
    all_text = ' '.join(actions)
    suspicious_keywords = ['admin', 'debug', 'override', 'backdoor']
    found = [word for word in suspicious_keywords if word in all_text]

    # This block does nothing for final result (misleading intermediate)
    if len(found) > 0:
        warning_flag = True
        quarantine_list = found.copy()
    else:
        warning_flag = False
        quarantine_list = []

    # Actual no-op return (diverts attention)
    return warning_flag

# Main evaluation logic (key computation)
def evaluate_performance(rank, base):
    multipliers = {'A': 2.5, 'B': 1.8, 'C': 1.2}
    adjustment = 0

    # Simulated complex adjustment chain (only one path matters)
    if rank == 'A':
        adjustment += 0.3
        adjustment *= 1.1
    elif rank == 'B':
        adjustment += 0.15
    else:
        adjustment -= 0.1

    # Final formula (correct path)
    raw_score = base * multipliers[rank]
    final = raw_score + (adjustment * 100)

    # Decoy operations (bit manipulation red herring)
    decoy_value = (int(final) << 2) ^ 0xFF
    decoy_value = decoy_value >> 1

    # Only this line matters
    return int(final)

# Unused recursive function (distractor - looks important)
def recursive_sum(n):
    if n <= 1:
        return n
    return n + recursive_sum(n - 2)

# Auxiliary counter analysis (partially irrelevant)
def compute_rarity_score(counts):
    counter = Counter(counts)
    rare_count = len([c for c in counter.values() if c == 1])
    return rare_count * 5

# Entry point
if __name__ == '__main__':
    # Step 1: Simulate logs
    logs = simulate_user_actions()

    # Step 2: Analyze actions
    freq_raw, freq_norm = analyze_actions(logs)

    # Step 3: Get rank
    rank = get_rank_category(freq_raw)

    # Step 4: Assess risk (no impact on final answer)
    risk_alert = assess_risk_level(logs)

    # Step 5: Compute auxiliary metrics (distraction)
    rarity_score = compute_rarity_score(freq_raw)
    legacy = calculate_legacy_score(freq_norm)

    # Step 6: Base points determined by fixed rule
    base_points = len(logs) * 10  # 120

    # Step 7: Evaluate performance (critical statement)
    final_score = evaluate_performance(rank, base_points)

    # Print result
    print(f"Result: {final_score}")