def main():
    # Simulate student assessment scoring with adaptive weighting
    raw_scores = [88, 92, 76, 85, 94]
    max_possible = 100
    weights = [0.1, 0.2, 0.15, 0.25, 0.3]

    # Irrelevant normalization (distractor)
    normalized = [(s / max_possible) * 100 for s in raw_scores]
    adjusted_scores = [min(s + 5, 100) for s in raw_scores]  # Curve adjustment (semi-relevant)

    # Historical data (dead code path - distractor)
    historical_averages = [85, 87, 83, 86, 88]
    trend_analysis = list(map(lambda x: x[0] - x[1], zip(adjusted_scores, historical_averages)))

    # Difficulty scaling factors per test (relevant)
    difficulty_curve = [1.1, 0.95, 1.05, 0.9, 1.2]

    # Apply dynamic difficulty compensation
    def apply_difficulty_adjustment(scores, curve):
        return [scores[i] * (1 + (curve[i] - 1) * 0.5) for i in range(len(scores))]

    assessments = apply_difficulty_adjustment(raw_scores, difficulty_curve)

    # Compute performance entropy (distractor)
    import math
    total = sum(assessments)
    entropy = -sum((s/total) * math.log(s/total) for s in assessments if s > 0)

    # Aggregate function using weighted average and conditional boost
    def aggregate_performance(results, curve):
        base_weighted = sum(results[i] * weights[i] for i in range(len(results)))
        volatility = max(curve) - min(curve)
        boost_factor = 1.05 if volatility > 0.3 else 1.0
        penalty = 0.98 if any(s < 80 for s in raw_scores) else 1.0  # Uses outer scope
        
        # Complex conditional expression incorporating lambda
        modifier = (lambda x: x * 1.1 if x > 85 else x * 0.95)(base_weighted / len(results))
        
        # Multiple nested operations with set logic
        high_performers = {i for i, s in enumerate(results) if s >= 90}
        consistency_bonus = 1.02 if len(high_performers) >= 2 and abs(len(high_performers) - 2) < 2 else 1.0
        
        intermediate_result = base_weighted * boost_factor * penalty * consistency_bonus
        final_component = intermediate_result * (modifier / 85)  # Arbitrary scaling
        
        # Final computation
        return int(round(final_component))

    final_score = aggregate_performance(assessments, difficulty_curve)
    
    # Redundant diagnostic print (irrelevant)
    diagnostics = {"count": len([s for s in raw_scores if s >= 90]), "peak": max(raw_scores), "floor": min(raw_scores)}
    
    # Key output
    print(f"Result: {final_score}")

if __name__ == "__main__":
    main()