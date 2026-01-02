def analyze_feedback(surveys):
    word_counts = {}
    stop_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of'}
    total_length = 0
    
    for survey in surveys:
        words = survey.lower().split()
        filtered_words = [word for word in words if word.isalpha() and word not in stop_words]
        total_length += len(filtered_words)
        
        for word in filtered_words:
            word_counts[word] = word_counts.get(word, 0) + 1
    
    avg_length = total_length / len(surveys) if surveys else 0
    return word_counts, avg_length


def compute_weights(indices):
    weighted_sum = 0
    norm_factor = sum(i+1 for i in indices) or 1
    temp_vals = []
    
    for i, idx in enumerate(indices):
        temp = (idx * (i + 1)) / norm_factor
        temp_vals.append(temp)
        weighted_sum += temp * 0.9
    
    scale_factor = 1.5 if len(temp_vals) > 3 else 1.0
    return weighted_sum * scale_factor


def evaluate_performance(feedback, rankings):
    feedback_map = {k: v for k, v in feedback.items() if v > 2}
    rank_list = [r for r in rankings if r % 2 == 1]
    
    score_basis = 0
    bonus = 0
    
    # Irrelevant tracking
    change_log = []
    debug_state = {'processed': 0, 'skipped': 0}
    
    for key, val in feedback_map.items():
        if len(key) % 2 == 0:
            score_basis += val * 1.5
        else:
            score_basis += val * 0.8
        
        # Distractor logic
        if 'e' in key:
            bonus += 1.2
        elif 'a' in key:
            bonus -= 0.5
        
        debug_state['processed'] += 1
    
    # Unused normalization step
    if score_basis != 0:
        normalized = [x / score_basis for x in rank_list if score_basis > 10]
    
    weight_input = [len(k) for k in feedback_map.keys()]
    adjustment = compute_weights(weight_input)
    
    intermediate = score_basis + bonus
    final_score = int(intermediate - adjustment)  # Final computation
    
    return final_score

# Main execution
survey_data = [
    "Very good service and very professional",
    "Excellent support and fast response time",
    "The team was helpful but could improve",
    "Outstanding quality and attention to detail",
    "Satisfied with overall performance"
]

feedback_freq, avg_len = analyze_feedback(survey_data)
rankings = [10, 15, 22, 8, 14, 19]
final_score = evaluate_performance(feedback_freq, rankings)
print(f"Result: {final_score}")