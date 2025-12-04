def calculate_overlap_ratio(skills_a, skills_b):
    # Convert to sets for intersection operations
    set_a = set(s.lower() for s in skills_a)
    set_b = set(s.lower() for s in skills_b)
    
    # Calculate overlap metrics
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    
    # Metrics that won't be used but look important
    jaccard = len(intersection) / len(union) if union else 0
    containment = len(intersection) / len(set_a) if set_a else 0
    
    # The actual metric we'll use
    overlap_ratio = len(intersection) / len(set_b) if set_b else 0
    
    return overlap_ratio

def analyze_experience(years_experience, complexity_factors):
    # Base score calculation
    base_score = min(years_experience * 1.5, 10)
    
    # Apply complexity factors that seem important
    for factor, weight in complexity_factors.items():
        if factor == 'international':
            base_score += weight * 0.8
        elif factor == 'team_size':
            # This looks important but isn't used
            team_factor = min(weight / 10, 1.5)
    
    # Normalize to 0-10 scale
    normalized_score = min(base_score, 10)
    return normalized_score

def parse_education_level(education):
    education_map = {
        'high school': 1,
        'associate': 2,
        'bachelor': 3,
        'master': 4,
        'phd': 5,
        'post-doctoral': 5
    }
    
    # Look for keywords in the education string
    for level, score in education_map.items():
        if level in education.lower():
            return score
    return 0

def calculate_candidate_score(candidate, requirements):
    # Initialize tracking variables
    potential_score = 0
    leadership_bonus = 0
    tech_depth_score = 0
    
    # Calculate skill match - this is relevant
    skill_match = calculate_overlap_ratio(candidate['skills'], requirements['required_skills'])
    skill_score = skill_match * 35
    
    # Experience calculation - this is relevant
    experience_factors = {'international': 2, 'team_size': candidate['team_led_size']}
    experience_score = analyze_experience(candidate['years_experience'], experience_factors)
    
    # Education score calculation - this is relevant
    education_level = parse_education_level(candidate['education'])
    education_score = education_level * 3
    
    # Calculate various metrics that look important
    for project in candidate['projects']:
        if project['complexity'] > 7:
            tech_depth_score += 1.5
        
        # This is a distraction
        if project['role'].lower() == 'lead':
            leadership_bonus += 2
    
    # Misleading intermediate calculation
    initial_score = skill_score + experience_score + education_score + tech_depth_score
    adjusted_score = initial_score * 0.8
    
    # The actual calculation we care about
    relevant_score = skill_score + (experience_score * 2) + education_score
    
    # More distractions
    if candidate['certifications']:
        cert_bonus = len(candidate['certifications']) * 2
        potential_score = relevant_score + cert_bonus
    
    # Normalize to 0-100 scale
    normalized_score = min(relevant_score, 100)
    
    # Apply a position-specific multiplier - this is relevant
    if requirements['position_level'] == 'senior':
        normalized_score *= 1.1
    elif requirements['position_level'] == 'mid':
        normalized_score *= 1.0
    else:
        normalized_score *= 0.9
    
    # Final rounding to integer
    final_score = int(normalized_score)
    return final_score

# Candidate profile data
candidate_profile = {
    'name': 'Alex Johnson',
    'years_experience': 6,
    'education': 'Master in Computer Science',
    'skills': ['Python', 'SQL', 'Data Analysis', 'Machine Learning', 'Cloud Computing'],
    'certifications': ['AWS Certified Developer', 'Scrum Master'],
    'projects': [
        {'name': 'E-commerce Platform', 'role': 'Lead', 'complexity': 8},
        {'name': 'Data Pipeline', 'role': 'Developer', 'complexity': 7},
        {'name': 'ML Recommendation System', 'role': 'Data Scientist', 'complexity': 9}
    ],
    'team_led_size': 6
}

# Position requirements
position_requirements = {
    'position_level': 'senior',
    'required_skills': ['python', 'data analysis', 'machine learning', 'statistics'],
    'min_years_experience': 5,
    'preferred_education': 'Master'
}

# Calculate the candidate's score
final_score = calculate_candidate_score(candidate_profile, position_requirements)
print(f"Result: {final_score}")