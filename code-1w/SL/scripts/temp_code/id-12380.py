def process_feedback(feedback_str):
    """Clean and normalize feedback string."""
    cleaned = feedback_str.strip().lower()
    words = cleaned.split()
    word_count = len(words)
    
    # Distractor: irrelevant transformation
    reversed_words = [word[::-1] for word in words]
    palindrome_check = [w == w[::-1] for w in words]
    
    # Actual logic contribution
    positive_indicators = ['good', 'excellent', 'great', 'well']
    negative_indicators = ['poor', 'bad', 'terrible', 'awful']
    
    pos_count = sum(1 for word in words if word in positive_indicators)
    neg_count = sum(1 for word in words if word in negative_indicators)
    
    return {'pos': pos_count, 'neg': neg_count, 'length': word_count}


def build_feedback_map(survey_list):
    """Build mapping from survey responses to processed scores."""
    feedback_map = {}
    temp_aggregates = []  # Semi-relevant: used only for logging
    
    for i, entry in enumerate(survey_list):
        result = process_feedback(entry)
        key = f"response_{i}"
        feedback_map[key] = result
        
        # Distractor: unused intermediate calculation
        avg_sentiment = (result['pos'] - result['neg']) / (result['length'] + 1)
        temp_aggregates.append(avg_sentiment if avg_sentiment > 0 else 0)
    
    # Distractor: dead code path (never accessed)
    if False:
        fallback = sum(temp_aggregates) * 1e-5
        feedback_map['fallback'] = {'value': fallback}
    
    return feedback_map


def calculate_adjustment_factor(data):
    """Calculate multiplier based on distribution of feedback."""
    total_pos = sum(item['pos'] for item in data.values())
    total_neg = sum(item['neg'] for item in data.values())
    total_entries = len(data)
    
    # Distractor: complex but unused metric
    rare_word_ratio = 0.789
    hypothetical_score = (total_pos * 2.1) - (total_neg * 1.3) + (total_entries * rare_word_ratio)
    
    # Relevant logic
    net_sentiment = total_pos - total_neg
    adjustment = 1.0 + (net_sentiment / (total_entries * 4))
    return round(adjustment, 4)


def evaluate_performance(feedback_summary, base_factor):
    """Final evaluation using summary and base multiplier."""
    # Use dictionary operations and conditional logic
    adjustments = {}
    for k, v in feedback_summary.items():
        if 'pos' in v and 'neg' in v:
            adjustments[k] = v['pos'] * 2 - v['neg']
    
    total_adjustment = sum(adjustments.values())
    
    # Case conversion as part of meaningful logic (real usage)
    scaling_key = "base_scale".upper()  # Simulate config lookup
    scale_factors = {"BASE_SCALE": 1.5, "DEFAULT": 1.0}
    scaling = scale_factors.get(scaling_key, 1.0)
    
    # Final computation
    raw_score = (total_adjustment * base_factor) * scaling
    final_score = int(abs(raw_score) + 0.5)  # Round to nearest integer
    
    # Irrelevant side computation
    outlier_detection = [v for v in adjustments.values() if v > 5]
    if len(outlier_detection) > 2:
        final_score += 10
    
    return final_score

# Main execution
if __name__ == "__main__":
    survey_responses = [
        "Excellent work well done great effort",
        "Poor execution bad style terrible formatting",
        "Good job good logic excellent clarity",
        "Awful performance poor structure"
    ]
    
    # Key variables
    feedback_dict = build_feedback_map(survey_responses)
    base_multiplier = calculate_adjustment_factor(feedback_dict)
    
    # Critical statement
    final_score = evaluate_performance(feedback_dict, base_multiplier)
    
    print(f"Result: {final_score}")