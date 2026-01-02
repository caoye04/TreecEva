from collections import defaultdict, Counter

# Simulate student responses to a logic-based quiz with multiple sections
def analyze_responses():
    # Raw response data: question_id -> list of student answers
    raw_data = {
        'Q1': ['A', 'B', 'A', 'C', 'A', 'B'],
        'Q2': ['B', 'B', 'C', 'B', 'A', 'B'],
        'Q3': ['C', 'C', 'C', 'A', 'B', 'C'],
        'Q4': ['D', 'A', 'D', 'D', 'D', 'A'],
        'Q5': ['E', 'E', 'D', 'E', 'E', 'E']
    }

    # Correct answers for each question
    key_answers = {'Q1': 'A', 'Q2': 'B', 'Q3': 'C', 'Q4': 'D', 'Q5': 'E'}

    # Track correct counts per student (index)
    student_correct = [0] * 6

    # Distractor: unused frequency tracker
    question_popularity = defaultdict(int)
    for q_id, answers in raw_data.items():
        for ans in answers:
            question_popularity[ans] += 1  # Not used later

    # Evaluate each student's performance
    for q_id, answers in raw_data.items():
        correct_answer = key_answers[q_id]
        for i, ans in enumerate(answers):
            if ans == correct_answer:
                student_correct[i] += 1

    # Compute individual accuracy rates
    accuracy_rates = [correct / len(raw_data) for correct in student_correct]

    # Distractor: compute median (not used)
    sorted_accuracies = sorted(accuracy_rates)
    n = len(sorted_accuracies)
    median_accuracy = (sorted_accuracies[n//2] + sorted_accuracies[-(n//2 + 1)]) / 2

    # Weighted scoring: extra credit for consistent performers
    consistency_bonus = 0
    for rate in accuracy_rates:
        if rate >= 0.8:
            consistency_bonus += 1

    # Base score is average correct answers
    base_score = sum(student_correct) / len(student_correct)

    # Apply non-linear transformation for final evaluation
    def evaluate_performance(base, bonus, rates):
        # Complex adjustment using distribution skew
        count_high = sum(1 for r in rates if r > 0.6)
        boost_factor = 1.2 if count_high >= 4 else 1.0
        
        # Irrelevant set operation (distractor)
        unique_scores = set(student_correct)
        redundant_calc = len(unique_scores) * 0.1  # Not used
        
        # Final nonlinear aggregation
        adjusted = (base ** 1.1) * boost_factor + (bonus * 0.5)
        return round(adjusted, 4)

    final_score = evaluate_performance(base_score, consistency_bonus, accuracy_rates)
    
    # Debug print removed
    # Final output
    print(f"Result: {final_score}")
    
    return final_score

# Execute and capture result
def main():
    result = analyze_responses()
    return result

main()