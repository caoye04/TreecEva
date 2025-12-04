def calculate_bonus(performance_rating, seniority):
    # Irrelevant bonus calculation - not used in final logic
    base_bonus = performance_rating * 100
    multiplier = seniority // 2
    irrelevant_result = base_bonus + multiplier * 50
    return base_bonus + multiplier * 25

def filter_candidates_by_skills(candidate_data, required_skills):
    # Misleading function that appears important but isn't used
    qualified = []
    for candidate in candidate_data:
        skill_match = sum(1 for skill in candidate['skills'] if skill in required_skills)
        if skill_match >= 2:
            qualified.append(candidate)
    return qualified

def compute_final_score(candidates, threshold):
    total_candidates = len(candidates)
    processed_scores = []
    
    # Main logic using enumerate and zip
    for idx, candidate in enumerate(candidates):
        technical_score = candidate['technical']
        behavioral_score = candidate['behavioral']
        
        # Complex scoring logic
        if technical_score >= 80 and behavioral_score >= 70:
            base_score = (technical_score + behavioral_score) // 2
            
            # Bonus logic that's actually relevant
            if idx % 2 == 0:
                bonus = 5
            else:
                bonus = 3
                
            final_candidate_score = base_score + bonus
            processed_scores.append(final_candidate_score)
    
    # Using zip with enumerate for additional processing
    weighted_scores = []
    scores_and_indices = list(enumerate(processed_scores))
    pairs = list(zip(scores_and_indices, [x * 2 for x in processed_scores]))
    
    for (idx, score), double_score in pairs:
        if score > threshold:
            weighted_score = score + (idx % 3)
            weighted_scores.append(weighted_score)
    
    # Dead code path - misleading calculation
    if len(weighted_scores) == 0:
        backup_calculation = sum(processed_scores) * 2 - 15
        # This path is never taken but adds confusion
        return backup_calculation
    
    # Final score calculation
    if weighted_scores:
        max_score = max(weighted_scores)
        min_score = min(weighted_scores)
        final_score = (max_score + min_score) // 2
    else:
        final_score = 0
    
    return final_score

# Candidate data
candidates = [
    {'technical': 85, 'behavioral': 75, 'skills': ['python', 'sql', 'git']},
    {'technical': 78, 'behavioral': 82, 'skills': ['java', 'c++', 'python']},
    {'technical': 92, 'behavioral': 68, 'skills': ['python', 'javascript', 'react']},
    {'technical': 88, 'behavioral': 79, 'skills': ['python', 'aws', 'docker']},
    {'technical': 95, 'behavioral': 85, 'skills': ['python', 'ml', 'stats']}
]

threshold = 75

# Irrelevant intermediate calculations
temp_result = calculate_bonus(8, 3)
unused_data = filter_candidates_by_skills(candidates, ['python', 'java'])
misleading_value = temp_result * 2 - 50

# The key execution
final_score = compute_final_score(candidates, threshold)

print(f"Result: {final_score}")