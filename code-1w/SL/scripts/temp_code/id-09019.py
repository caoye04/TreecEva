def calculate_final_score(performances, multipliers):
    # Initialize tracking variables
    total_points = 0
    bonus_awarded = False
    performance_log = []

    # Misleading pre-processing: normalizing multipliers (not actually used)
    normalized = [w / sum(multipliers) for w in multipliers]
    temp_result = 0
    
    for i, (perf, mult) in enumerate(zip(performances, multipliers)):
        # Real computation path
        base_score = perf * mult
        adjustment = 0
        
        # Conditional adjustments based on performance rank
        if perf > 85:
            adjustment += 10
        elif perf > 70:
            adjustment += 5
        else:
            adjustment -= 3
            
        # Accumulate score with adjustment
        total_points += base_score + adjustment
        performance_log.append((i, base_score, adjustment))

    # Secondary loop: checks for consecutive high performers (unused heuristic)
    streak_count = 0
    for p in performances:
        if p > 90:
            streak_count += 1
        else:
            streak_count = 0  # Reset
    
    # Simulated bonus logic (never triggers in this input)
    if streak_count >= 3:
        bonus_awarded = True
        total_points += 25

    # Dead code: irrelevant aggregation
    avg_performance = sum(performances) / len(performances)
    max_single_contribution = max(p * m for p, m in zip(performances, multipliers))

    # Final non-linear scaling (distractor calculation)
    scaling_factor = 1.0
    if avg_performance > 80:
        scaling_factor = 1.1
    elif avg_performance > 70:
        scaling_factor = 1.05

    # ACTUAL final score computation (scaling not applied)
    final_raw = total_points  # Scaling intentionally omitted

    return int(final_raw)

# Main execution context
if __name__ == "__main__":
    # Dataset: student test rankings and criterion weights
    rankings = [88, 92, 76, 81, 95]
    weights = [0.2, 0.25, 0.15, 0.1, 0.3]

    # Irrelevant auxiliary data
    student_ids = [101, 102, 103, 104, 105]
    subject_codes = ['MATH', 'PHYS', 'CHEM', 'BIO', 'COMP']
    id_map = {sid: code for sid, code in zip(student_ids, subject_codes)}

    # Unused transformation
    ranked_pairs = list(enumerate(zip(rankings, weights)))
    sorted_by_rank = sorted(ranked_pairs, key=lambda x: x[1][0], reverse=True)

    # Key statement
    final_score = calculate_final_score(rankings, weights)
    
    # Print result as required
    print(f"Target result: {final_score}")