def evaluate_performance(skills, thresh):
    proficient = {k for k, v in skills.items() if v >= thresh}
    improvement_needed = {k for k, v in skills.items() if v < thresh}
    score = len(proficient) * 10
    
    # Irrelevant distraction: unused variable (minimal interference)
    backup_calc = [v for v in skills.values()]
    
    if 'python' in proficient:
        score += 5
    if 'math' in improvement_needed:
        score -= 2
    return score

# Main execution
data_science_skills = {
    'python': 9,
    'math': 7,
    'ml': 8,
    'sql': 6
}
threshold = 8
temp_result = sum(data_science_skills.values())  # Distractor: not used later
final_score = evaluate_performance(data_science_skills, threshold)
print(f"Result: {final_score}")