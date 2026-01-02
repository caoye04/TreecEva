def evaluate_performance(output_count, defect_count, review_notes):
    base_efficiency = output_count * 1.5
    penalty = defect_count * 10
    
    # Analyze feedback string for key indicators
    positive_indicators = ['exceeds', 'great', 'efficient', 'reliable']
    negative_indicators = ['concern', 'error-prone', 'delay', 'issue']
    
    praise_count = sum(1 for word in positive_indicators if word in review_notes.lower())
    concern_count = sum(1 for word in negative_indicators if word in review_notes.lower())
    
    sentiment_bonus = praise_count * 5 - concern_count * 3
    
    # Distractor: irrelevant string processing
    padded_notes = review_notes.strip().upper()
    char_frequency = {c: padded_notes.count(c) for c in set(padded_notes) if c.isalpha()}
    rare_letter_bonus = sum(1 for count in char_frequency.values() if count == 1)
    
    # Another distractor: unused function call simulation
    audit_trail = []
    audit_trail.append(f"Review processed at level 2")
    
    # Bitwise operation on derived values (relevant)
    efficiency_class = int(base_efficiency) & int(sentiment_bonus)
    adjustment_factor = (efficiency_class >> 2) if efficiency_class > 0 else 0
    
    # Final score computation (depends only on certain components)
    raw_score = base_efficiency - penalty + sentiment_bonus + adjustment_factor
    
    # Irrelevant transformation
    normalized = raw_score / max(1, len(review_notes))
    capped_score = min(normalized, 100)
    
    # Final assignment — this is the key statement
    final_score = int(raw_score)  # Only raw_score matters here
    return final_score

# Simulated data
productivity = 80
errors = 7
feedback_string = "Great job overall, exceeds expectations, but some concerns about error-prone sections and delays in delivery."

# Key statement
final_score = evaluate_performance(productivity, errors, feedback_string)
print(f"Result: {final_score}")