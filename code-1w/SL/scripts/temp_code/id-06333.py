def process_feedback(raw_entries):
    cleaned = [entry.strip().lower() for entry in raw_entries if entry]
    word_count = sum(len(entry.split()) for entry in cleaned)
    
    # Irrelevant statistics
    avg_length = word_count / len(cleaned) if cleaned else 0
    caps_count = sum(1 for entry in raw_entries if entry.isupper())
    
    categorized = {}
    for entry in cleaned:
        category = 'positive' if 'good' in entry or 'excellent' in entry else 'negative'
        category = 'neutral' if 'average' in entry or 'okay' in entry else category
        categorized[entry] = category
    
    return categorized


def calculate_sentiment_tone(entries_map):
    pos_count = sum(1 for label in entries_map.values() if label == 'positive')
    neg_count = sum(1 for label in entries_map.values() if label == 'negative')
    net_tone = pos_count - neg_count
    
    # Dummy transformation
    adjusted_tone = net_tone * 1.5
    if adjusted_tone > 10:
        adjusted_tone = 10
    
    return adjusted_tone


def evaluate_performance(feedback_log):
    parsed_data = process_feedback(feedback_log)
    tone_score = calculate_sentiment_tone(parsed_data)
    
    # Secondary metric (unused but plausible)
    entry_lengths = [len(k) for k in parsed_data.keys()]
    length_factor = sum(entry_lengths) // len(entry_lengths) if entry_lengths else 0
    
    # Core logic disguised among distractions
    multiplier = 7
    if tone_score > 0:
        multiplier += 2
    elif tone_score == 0:
        multiplier += 0
    else:
        multiplier -= 1
    
    base_value = 8
    for i in range(abs(int(tone_score))):
        base_value = (base_value + i) % 11
    
    # Final computation
    final_score = int(tone_score * multiplier + base_value)
    
    # Red herring variables
    temp_result = final_score ** 0.5
    normalized = temp_result / 1.0 if temp_result > 0 else 0
    
    return final_score

# Input data
feedback_entries = [
    "  EXCELLENT WORK !!  ",
    "good effort shown",
    "needs improvement",
    "Okay performance, could be better",
    "Excellent and outstanding dedication",
    "average commitment level",
    ""
]

# Execution point of interest
result_map = process_feedback(feedback_entries)
tone_val = calculate_sentiment_tone(result_map)
final_score = evaluate_performance(feedback_entries)
print(f"Target result: {final_score}")