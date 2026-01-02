from itertools import combinations

# Simulate ranking-based scoring with noise filtering and conditional bonuses
def process_leaderboard(entries):
    filtered = [e for e in entries if e[1] > 75]  # Only top performers
    sorted_entries = sorted(filtered, key=lambda x: x[1], reverse=True)
    return [name for name, score in sorted_entries]

# Misleading helper: appears useful but not used in final logic
def legacy_ranking_adjustment(data):
    adjusted = []
    for item in data:
        temp_val = item[1] * 0.95 + 10
        if temp_val > 100:
            temp_val = 100
        adjusted.append((item[0], temp_val))
    return adjusted

# Auxiliary calculation: computes pair consistency (distractor)
def compute_pair_consistency(names):
    pairs = list(combinations(names, 2))
    count = 0
    for a, b in pairs:
        if abs(hash(a) % 100 - hash(b) % 100) < 10:
            count += 1
    return count  # Unused in final result

# Core scoring logic
def calculate_base_points(rank_index):
    base = 100 - rank_index * 5
    penalty = 0
    if rank_index % 3 == 0:
        penalty = 10
    return base - penalty

def calculate_final_score(ranks, multiplier):
    total = 0
    for i, name in enumerate(ranks):
        points = calculate_base_points(i)
        if i < 3:
            points += multiplier  # Bonus for top three
        total += points
    
    # Red herring computation
    shadow_total = 0
    for i in range(len(ranks)):
        shadow_total += (i + 1) * 7 % 4
    
    # Another distraction: irrelevant transformation
    temp_scores = [total + i * 0.1 for i in range(5)]
    smoothed = sum(temp_scores) / len(temp_scores)
    
    # Final adjustment based on deterministic rule
    if len(ranks) % 2 == 1:
        total -= 5
    
    return int(smoothed)  # smoothing doesn't affect integer cast

# Main execution
if __name__ == "__main__":
    raw_data = [
        ('Alice', 88), ('Bob', 92), ('Charlie', 70),
        ('Diana', 95), ('Eve', 60), ('Frank', 83),
        ('Grace', 91), ('Henry', 77)
    ]
    
    # Step 1: Filter and rank participants
    leaderboard_names = process_leaderboard(raw_data)
    
    # Step 2: Compute fake consistency metric (not used)
    _ = compute_pair_consistency(leaderboard_names)
    
    # Step 3: Define bonus (based on number of high scorers)
    high_scorer_count = len([s for _, s in raw_data if s >= 85])
    bonus_multiplier = 8 if high_scorer_count >= 3 else 5
    
    # Step 4: Calculate final score
    final_score = calculate_final_score(leaderboard_names, bonus_multiplier)
    
    # Print result as required
    print(f"Result: {final_score}")