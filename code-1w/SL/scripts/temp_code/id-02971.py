from collections import defaultdict, Counter

# Simulate student responses to a multi-section exam
def analyze_exam_performance():
    # Raw data: section-wise answers (1 = correct, 0 = incorrect)
    responses = [
        [1, 1, 0, 1, 1, 0, 1],  # Algebra
        [1, 0, 1, 1, 0, 1, 1],  # Geometry
        [0, 1, 1, 1, 1, 0, 0],  # Calculus
        [1, 1, 1, 0, 1, 1, 1]   # Statistics
    ]

    # Section weights
    weights = {'Algebra': 0.2, 'Geometry': 0.2, 'Calculus': 0.3, 'Statistics': 0.3}

    # Irrelevant distractor: count total attempts
    total_attempts = sum(len(section) for section in responses)
    avg_length = total_attempts / len(responses)  # Not used later

    # Compute raw scores per section
    raw_scores = []
    for i, section in enumerate(responses):
        correct = sum(section)
        max_items = len(section)
        percentage = correct / max_items
        raw_scores.append(percentage)

    # Misleading intermediate: normalize scores between 0 and 1 (already are)
    normalized = [score / max(raw_scores) for score in raw_scores]  # Redundant step

    # Distractor: frequency analysis of raw scores
    score_counter = Counter([round(s, 2) for s in raw_scores])
    mode_score = max(score_counter, key=score_counter.get)  # Computed but unused

    # Weighted scoring using ordered sections
    section_names = ['Algebra', 'Geometry', 'Calculus', 'Statistics']
    weighted_score = 0.0
    for i, name in enumerate(section_names):
        weighted_score += raw_scores[i] * weights[name]

    # Apply performance bonus if any section has perfect score
    perfect_section_bonus = 0.05 if any(score == 1.0 for score in raw_scores) else 0.0

    # Conditional expression for distinction threshold
    distinction_threshold = 0.85
    performance_level = 'Distinction' if weighted_score >= distinction_threshold else 'Pass'

    # Final adjustment based on improvement trend (last two sections only)
    recent_improvement = raw_scores[3] > raw_scores[2]  # Stats vs Calculus
    improvement_bonus = 0.02 if recent_improvement else 0.0

    # Final score calculation
    final_score = weighted_score + perfect_section_bonus + improvement_bonus

    # Distractor variables (dead computations)
    adjusted_total = final_score * 100
    ceiling_value = int(-(-adjusted_total // 1))  # Just here to distract

    # Output target result
    print(f"Result: {final_score}")
    return final_score

# Execute function
def calculate_final_score():
    return analyze_exam_performance()

final_score = calculate_final_score()