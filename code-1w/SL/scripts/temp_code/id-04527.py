def evaluate_performance(skills, threshold):
    # Normalize skill levels using min-max scaling (irrelevant for final logic but adds distraction)
    min_skill = min(skills)
    max_skill = max(skills)
    normalized = [(s - min_skill) / (max_skill - min_skill + 1e-8) for s in skills]

    # Calculate weighted mastery index (semi-relevant transformation)
    weights = [1, 2, 1.5, 3, 2.5]  # Weight per skill domain
    weighted_sum = sum(w * s for w, s in zip(weights, skills))
    total_weight = sum(weights)
    mastery_index = weighted_sum / total_weight

    # Determine proficiency set (using set operations)
    high_skills = {i for i, s in enumerate(skills) if s >= threshold}
    mid_skills = {i for i, s in enumerate(skills) if threshold * 0.7 <= s < threshold}
    cross_domain_synergy = len(high_skills.intersection({0, 2, 4})) > 1  # Checks synergy between strategic domains

    # Simulate training adaptation (distractor computation)
    adaptation_rate = 0.85
    projected_growth = [s * adaptation_rate for s in skills]
    avg_projected = sum(projected_growth) / len(projected_growth)

    # Evaluate combinatorial problem-solving capacity
    valid_combinations = 0
    n = len(skills)
    for i in range(n):
        for j in range(i + 1, n):
            if skills[i] + skills[j] >= 2 * threshold:
                valid_combinations += 1

    # Final scoring with conditional boosts
    base_score = len(high_skills) * 10
    combo_bonus = valid_combinations * 2 if cross_domain_synergy else valid_combinations
    penalty = 5 if len(mid_skills) > 2 else 0

    # String-based status determination (uses string method)
    performance_class = "excellent" if base_score >= 30 else "adequate" if base_score >= 20 else "poor"
    multiplier = 1.25 if "ex" in performance_class else 1.0

    final_score = int((base_score + combo_bonus - penalty) * multiplier)
    return final_score


# Main execution
skill_levels = [8, 6, 9, 5, 7]  # Skill ratings in five domains
challenge_threshold = 7.5
final_score = evaluate_performance(skill_levels, challenge_threshold)
print(f"Result: {final_score}")