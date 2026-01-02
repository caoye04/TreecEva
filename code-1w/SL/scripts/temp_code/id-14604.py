def evaluate_performance(skills, threshold):
    # Precompute redundant metrics (distractor)
    peak_skill = max(skills)
    skill_range = peak_skill - min(skills)
    normalized_total = sum(x / peak_skill for x in skills if x > 0)

    # Irrelevant filtering (dead computation path)
    advanced_skills = [s for s in skills if s >= threshold * 0.75]
    proficiency_set = set(advanced_skills)
    overlap_count = len(proficiency_set.intersection({threshold, threshold + 1, threshold - 1}))

    # Actual logic begins: count how many skills meet or exceed threshold
    qualified = [skill for skill in skills if skill >= threshold]
    base_score = len(qualified) * threshold

    # Apply bonus based on distribution (real contribution)
    if len(qualified) >= 3:
        sorted_skills = sorted(qualified, reverse=True)
        top_three_contribution = sum(sorted_skills[:3])
        bonus = top_three_contribution // 4
        base_score += bonus

    # More distractions: analyze gaps (unused)
    gaps = []
    for i in range(1, len(skills)):
        if skills[i] < skills[i-1]:
            gaps.append(skills[i-1] - skills[i])
    avg_drop = sum(gaps) / len(gaps) if gaps else 0

    # Final adjustment: apply penalty if low consistency
    stability_factor = 1
    if skill_range > threshold * 2:
        stability_factor = 0.9

    adjusted_score = base_score * stability_factor

    # Additional red herring: unused transformation
    transformed = [((x ** 0.5) * 10) for x in skills]
    complexity_metric = sum(transformed[i] * (i+1) for i in range(len(transformed))) / 100

    return int(adjusted_score)


# Main execution context
skill_levels = [85, 90, 78, 92, 88, 76, 95]
challenge_threshold = 85

# Distractor variables and operations
baseline_avg = sum(skill_levels) / len(skill_levels)
data_slice = skill_levels[2:5]
shifted_data = [x - 70 for x in skill_levels]
dummy_set = {x % 10 for x in shifted_data}
useless_sum = sum(dummy_set)

# Key statement
final_score = evaluate_performance(skill_levels, challenge_threshold)

# Print result as required
print(f"Result: {final_score}")