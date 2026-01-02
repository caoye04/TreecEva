from collections import defaultdict

# Simulate a coding competition ranking system with bonus logic
def main():
    participants = ['Alice', 'Bob', 'Charlie', 'Diana']
    raw_scores = [87, 91, 88, 95]
    penalty_points = [5, 3, 10, 7]
    difficulty_factors = [1.1, 1.05, 1.2, 1.15]
    
    # Irrelevant computation: average score (not used in final logic)
    total = 0
    for s in raw_scores:
        total += s
    avg_score = total / len(raw_scores)
    
    # Apply penalties and difficulty scaling
    adjusted_scores = {}
    for i, p in enumerate(participants):
        adjusted_scores[p] = (raw_scores[i] - penalty_points[i]) * difficulty_factors[i]
    
    # Misleading sort: sorts but doesn't use this order directly
    sorted_by_name = sorted(adjusted_scores.items(), key=lambda x: x[0])
    
    # Actual ranking based on adjusted scores
    rankings = sorted(adjusted_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Bonus system with conditional multiplier
    base_bonus = 100
    rank_map = {entry[0]: idx for idx, entry in enumerate(rankings)}
    
    # Unused dead code path (simulates alternate logic)
    if avg_score > 90:
        adjustment_factor = 0.9
    else:
        adjustment_factor = 1.1  # never used
    
    # Conditional bonus logic
    bonus_multiplier = 2 if rank_map['Diana'] == 0 else 1.5
    
    # Distractor: complex dictionary comprehension not affecting result
    score_summary = {
        k: {
            'base': round((raw_scores[i] - penalty_points[i])),
            'final': round(v, 2)
        } for i, (k, v) in enumerate(adjusted_scores.items())
    }
    
    # Key function call
    final_score = calculate_final_score(rankings, bonus_multiplier)
    
    # Another red herring: sorting summary (not used)
    sorted_summary = sorted(score_summary.items(), key=lambda x: x[1]['final'], reverse=True)
    
    print(f"Result: {final_score}")

# Helper function to compute final score
def calculate_final_score(rank_list, multiplier):
    top_three_contribution = 0
    for i in range(min(3, len(rank_list))):
        name, score = rank_list[i]
        if name in ['Alice', 'Diana']:
            top_three_contribution += score * 0.3
        else:
            top_three_contribution += score * 0.2
    
    # Add bonus pool
    bonus_pool = 50 * multiplier
    total_award = top_three_contribution + bonus_pool
    
    # Extra computation that looks important but isn't part of output
    normalized = total_award / 1.5
    capped = min(normalized, 100)
    
    return int(total_award)  # Final deterministic answer

if __name__ == "__main__":
    main()