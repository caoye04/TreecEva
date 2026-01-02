skills_required = {'python', 'sql', 'api', 'testing'}

applicants = [
    {'name': 'Alice', 'skills': ['python', 'sql', 'api']},
    {'name': 'Bob', 'skills': ['python', 'testing', 'devops']},
    {'name': 'Charlie', 'skills': ['python', 'sql', 'api', 'testing']},
    {'name': 'Diana', 'skills': ['python', 'api', 'frontend']}
]

passed_candidates = []
base_multiplier = 7
penalty_factor = 0.5

for applicant in applicants:
    skill_set = set(applicant['skills'])
    if skills_required.issubset(skill_set):
        passed_candidates.append(applicant['name'])

# Unrelated tracking variable (minor distraction)
processed_count = len(applicants)

penalty_set = {x for x in range(len(passed_candidates)) if x % 2 == 0}
penalty_set_size = len(penalty_set)

final_score = len(passed_candidates) * base_multiplier - penalty_set_size
print(f"Result: {final_score}")