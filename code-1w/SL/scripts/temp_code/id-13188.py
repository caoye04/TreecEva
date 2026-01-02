from collections import defaultdict, Counter

# Simulate student responses to a logic-based quiz with distractors
def evaluate_performance(responses, answer_key, time_spent_per_question):
    correct_count = 0
    penalty_points = 0
    time_bonus = 0.0
    response_frequency = Counter(responses)
    
    # Distractor: Count how many times each option was selected (not directly used)
    option_analysis = {option: count for option, count in response_frequency.items()}
    
    # Logical evaluation of answers
    for i, response in enumerate(responses):
        if i >= len(answer_key):  # Handle overflow
            penalty_points += 2
            continue
        
        # Core comparison logic
        is_correct = response == answer_key[i]
        time_on_question = time_spent_per_question[i]
        
        # Time-based bonus calculation (semi-relevant)
        if time_on_question < 15:
            time_bonus += 0.5 if is_correct else -0.2
        elif time_on_question > 60:
            time_bonus -= 0.3  # Penalty for excessive time

        # Main scoring
        if is_correct:
            correct_count += 1
        else:
            penalty_points += 1

    # Distractor: Analyze response patterns (computed but not fully used)
    rare_answers = [opt for opt, cnt in response_frequency.items() if cnt == 1]
    unusual_pattern_bonus = 2 if len(rare_answers) > 3 else 0

    # Intermediate score transformations (mix of relevant and red herring)
    raw_score = correct_count * 4 - penalty_points
    adjusted_score = raw_score + int(time_bonus)
    
    # Final nonlinear adjustment based on logical consistency
    consistency_factor = 1
    for i in range(1, len(responses)):
        if responses[i] == responses[i-1]:  # Repetition check
            consistency_factor *= 0.95
    
    # Distractor: Unused helper computation
    def compute_entropy(freqs):
        from math import log
        total = sum(freqs.values())
        entropy = 0
        for count in freqs.values():
            p = count / total
            entropy -= p * log(p)
        return entropy
    
    entropy_estimate = compute_entropy(response_frequency)  # Computed but unused

    # Final score using only select components
    final_score = int(adjusted_score * consistency_factor)
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
student_responses = ['A', 'B', 'B', 'C', 'D', 'A', 'B', 'B', 'C', 'C']
answer_key =           ['A', 'B', 'C', 'C', 'D', 'B', 'B', 'A', 'C', 'D']
time_spent =           [12, 45, 67, 23, 10, 75, 30, 18, 40, 80]

# Execute
final_score = evaluate_performance(student_responses, answer_key, time_spent)