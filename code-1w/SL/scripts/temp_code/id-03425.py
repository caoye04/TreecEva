def analyze_sentiment(text):
    if not text:
        return 0
    positive_words = ['good', 'excellent', 'great', 'outstanding']
    negative_words = ['bad', 'poor', 'terrible', 'awful']
    words = text.lower().split()
    score = 0
    for word in words:
        cleaned = word.strip('.,!?"')
        if cleaned in positive_words:
            score += 1
        elif cleaned in negative_words:
            score -= 2
    return score

status_flags = {'system_ok': True, 'debug_mode': False, 'maintenance': False}

historical_data = [
    {'input': 'The service was excellent and great', 'value': 85},
    {'input': 'Poor and bad experience', 'value': 45},
    {'input': 'It was good but not outstanding', 'value': 70}
]

aggregate = 0
for entry in historical_data:
    sentiment = analyze_sentiment(entry['input'])
    adjusted = entry['value'] + sentiment * 2
    aggregate += adjusted

base_metrics = {
    'baseline': 100,
    'tolerance': 5,
    'scaling_factor': 0.8
}

feedback = [
    'Great performance overall!',
    'Not bad, could improve.',
    'Terrible response time.',
    'Excellent results generated.'
]

sentiment_tally = 0
entry_count = 0
for note in feedback:
    clean_note = note.strip().lower()
    if '!' in note:
        intensity = 1.5
    else:
        intensity = 1.0
    temp_score = analyze_sentiment(clean_note) * intensity
    sentiment_tally += temp_score
    entry_count += 1

average_sentiment = sentiment_tally / entry_count if entry_count > 0 else 0

# Misleading intermediate calculation (distractor)
dummy_scaling = base_metrics['scaling_factor'] ** 2 * 10
buffer_zone = base_metrics['tolerance'] * 3.5

# Simulate conditional override that doesn't trigger
critical_override = False
if status_flags['maintenance'] and base_metrics['baseline'] < 90:
    critical_override = True

# Key logic chain with nesting and multiple concepts
def evaluate_performance(feedback_list, metrics):
    total_weight = 0
    compound_modifier = 1.0
    
    # Use of tuple unpacking and dictionary access
    factors = [(metrics['baseline'], 0.6), (metrics['tolerance'], 0.1), (aggregate, 0.3)]
    for value, weight in factors:
        total_weight += value * weight
    
    # Boolean logic with short-circuiting
    if average_sentiment > 0 and not (critical_override or status_flags['debug_mode']):
        compound_modifier += 0.2
    elif average_sentiment < -1:
        compound_modifier -= 0.15
    
    # String-based logic affecting numeric output
    positive_trigger = any('excellent' in f.lower() or 'great' in f.lower() for f in feedback_list)
    penalty_trigger = sum(1 for f in feedback_list if 'terrible' in f.lower()) >= 1
    
    if positive_trigger and not penalty_trigger:
        compound_modifier += 0.1
    
    intermediate_result = total_weight * compound_modifier
    
    # Final adjustment using string method to count occurrences
    exclamation_count = sum(note.count('!') for note in feedback_list)
    bonus_per_exclamation = 1.2
    final_adjustment = intermediate_result + (exclamation_count * bonus_per_exclamation)
    
    return int(final_adjustment)

# Execution point of interest
final_score = evaluate_performance(feedback, base_metrics)

# Print required result
print(f"Result: {final_score}")