from collections import defaultdict

# Simulate a coding competition ranking system with bonus logic
def main():
    participants = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    raw_scores = [88, 92, 75, 96, 85]
    penalty_points = [5, 3, 10, 2, 8]
    submission_times = [120, 95, 145, 88, 110]  # in minutes

    # Irrelevant transformation: normalize times (not used later)
    max_time = max(submission_times)
    normalized_times = [round(t / max_time, 3) for t in submission_times]

    # Compute adjusted scores
    adjusted_scores = []
    for i in range(len(raw_scores)):
        score = raw_scores[i] - penalty_points[i]
        if submission_times[i] < 100:
            score += 5  # bonus for fast submission
        adjusted_scores.append(score)

    # Rank participants by adjusted score
    ranked_data = sorted(zip(participants, adjusted_scores), key=lambda x: -x[1])
    rankings = {p: idx + 1 for idx, (p, _) in enumerate(ranked_data)}

    # Distractor: count rank frequencies (not used)
    rank_counter = defaultdict(int)
    for rank in rankings.values():
        rank_counter[rank] += 1

    base_multiplier = 1.0
    if rankings['Alice'] < 3:
        base_multiplier += 0.2
    if rankings['Diana'] == 1:
        base_multiplier += 0.3

    # Bonus pool calculation (semi-relevant)
    total_bonus_pool = sum([100 // rank for rank in rankings.values()])
    average_bonus = total_bonus_pool / len(participants)
    rounded_bonus = round(average_bonus, 1)

    # Dead code path (never executed due to condition)
    debug_mode = False
    if debug_mode:
        print("Debug info:", rank_counter)
        extra_compensation = 0
        for p in participants:
            if p.startswith('C'):
                extra_compensation += 10

    # Actual multiplier logic
    bonus_multiplier = base_multiplier
    if rounded_bonus > 45:
        bonus_multiplier *= 1.15

    def calculate_final_score(ranks, mult):
        base_score = 0
        for participant, rank in ranks.items():
            if participant in ['Bob', 'Eve']:
                base_score += 10 // rank
            else:
                base_score += 15 // rank
        
        # Apply multiplier
        final = int(base_score * mult)
        
        # Red herring: unused adjustment
        potential_max = sum(15 // (i+1) for i in range(len(ranks)))
        efficiency_ratio = final / potential_max if potential_max > 0 else 0
        
        return final

    final_score = calculate_final_score(rankings, bonus_multiplier)
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()