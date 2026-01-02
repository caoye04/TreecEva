from itertools import combinations

# Recruitment data for technical roles
candidates = ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan']
min_years_experience = 3
required_skills = {'Python', 'SQL', 'Testing'}
application_scores = [85, 70, 90, 75, 80]
years_experience = [5, 2, 7, 3, 4]
skills_portfolio = [
    {'Python', 'SQL', 'Testing', 'DevOps'},
    {'Python', 'Frontend'},
    {'Python', 'SQL', 'Testing', 'ML'},
    {'SQL', 'Testing', 'CI/CD'},
    {'Python', 'Testing'}
]

# Evaluate which candidates meet minimum criteria
qualified_candidates = []
for i in range(len(candidates)):
    has_min_exp = years_experience[i] >= min_years_experience
    has_required_skills = required_skills.issubset(skills_portfolio[i])
    if has_min_exp and has_required_skills:
        qualified_candidates.append(candidates[i])

# Further filter based on score threshold
high_scorers = [score for score in application_scores if score >= 75]

# Find candidates who are both qualified and high scorers (approximation)
passed_candidates = qualified_candidates[:len(high_scorers) // 2]

# Compute final evaluation score
bonus_factor = 1.5
final_score = len(passed_candidates) * bonus_factor
print(f"Result: {final_score}")