from itertools import combinations

# Simulate a scenario where we evaluate a candidate's performance across multiple dimensions
def analyze_candidate_performance(test_scores, interview_rounds, coding_challenges):
    # Irrelevant preprocessing: normalize scores (not actually used in final logic)
    normalized_scores = [round((score - min(test_scores)) / (max(test_scores) - min(test_scores)) * 100, 2) for score in test_scores]
    
    # Distractor: unused variable tracking interview difficulty levels
    interview_difficulty_trend = [len(round_data) * 1.5 for round_data in interview_rounds]

    # Core logic begins: filter valid coding challenges
    successful_submissions = [ch for ch in coding_challenges if ch['passed'] and ch['time_taken'] < 60]
    
    # Compute base score from test scores above 85
    high_performers = list(filter(lambda x: x > 85, test_scores))
    base_score = sum(high_performers) if high_performers else 50

    # Use itertools to find all possible pairs of strong performers (distractor computation)
    potential_pairs = list(combinations(high_performers, 2))
    pair_count_indicator = len(potential_pairs)  # Semi-relevant but not critical

    # Bonus logic: if more than one successful submission, add bonus
    submission_count = len(successful_submissions)
    bonus = 15 if submission_count > 1 else 5

    # Additional condition using conditional expression
    experience_weight = 2 if any(ch['complexity'] == 'hard' for ch in successful_submissions) else 1

    # Intermediate distractor: compute average challenge time (not used)
    avg_time_wasted = sum(ch['time_taken'] for ch in coding_challenges) / len(coding_challenges)

    # Final calculation with nested dependency
    raw_final = base_score + bonus * experience_weight
    
    # Apply ceiling cap based on number of interview rounds passed
    max_allowed = 100 + len(interview_rounds)  # slight dynamic cap
    final_score = min(raw_final, max_allowed)
    
    # Print result as required
    print(f"Result: {final_score}")
    
    # Return for clarity (though printed already)
    return final_score

# Input data
test_scores = [78, 92, 88, 95, 82]
interview_rounds = [
    ['behavioral', 'technical'],
    ['system_design', 'problem_solving', 'follow_up'],
    ['HR', 'culture_fit']
]
coding_challenges = [
    {'passed': True, 'time_taken': 45, 'complexity': 'medium'},
    {'passed': True, 'time_taken': 55, 'complexity': 'hard'},
    {'passed': False, 'time_taken': 70, 'complexity': 'hard'}
]

# Execute function
calculate_final_score = analyze_candidate_performance
target_result = calculate_final_score(test_scores, interview_rounds, coding_challenges)