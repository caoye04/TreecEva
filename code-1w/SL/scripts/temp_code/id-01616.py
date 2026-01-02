def process_combinations(skill_set):
    combinations = set()
    for s1 in skill_set:
        for s2 in skill_set:
            if s1 != s2:
                pair = tuple(sorted([s1, s2]))
                combinations.add(pair)
    return len(combinations)

# Irrelevant utility function (minor distraction)
def format_skills(skill_list):
    return [skill.capitalize() for skill in skill_list]

# Main execution
skills = ['python', 'java', 'cpp', 'javascript']
skills_set = set(skills)

# Additional irrelevant variable
recommended_pathways = format_skills(skills)

result = process_combinations(skills_set)
print(f"Target result: {result}")