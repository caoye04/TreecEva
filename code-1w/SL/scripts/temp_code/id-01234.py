def evaluate_performance(skills, feedback):
    base = len(skills)
    bonus = 0
    
    # Analyze proficiency levels
    proficient_count = sum(1 for level in skills.values() if level >= 7)
    
    # Use lambda to filter constructive feedback
    is_constructive = lambda fb: 'improve' in fb or 'suggest' in fb
    constructive_feedback = set(filter(is_constructive, feedback))
    
    # Award bonus for each constructive point addressed
    for skill in skills:
        if skill.lower() in ' '.join(constructive_feedback).lower():
            bonus += 2
    
    # Additional reward if all high-level skills are covered in feedback
    high_skills = {k for k, v in skills.items() if v >= 8}
    if high_skills.issubset({word for fb in feedback for word in fb.split()}):
        bonus += 3
    
    final_score = base * 2 + bonus + proficient_count
    
    return final_score

# Main execution
skill_levels = {
    'debugging': 9,
    'optimization': 8,
    'testing': 7,
    'documentation': 6
}

feedback_set = {
    'good logic flow',
    'suggest adding error handling',
    'improve documentation clarity',
    'excellent optimization techniques'
}

final_score = evaluate_performance(skill_levels, feedback_set)
print(f"Result: {final_score}")