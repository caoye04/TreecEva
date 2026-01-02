from collections import defaultdict
import math

# Simulate employee feedback analysis with distractor computations
def preprocess_entries(entries):
    cleaned = []
    for entry in entries:
        if 'rating' not in entry or entry['rating'] <= 0:
            continue
        # Irrelevant transformation
        processed_text = entry.get('comment', '').strip().lower()
        word_count = len(processed_text.split())
        if word_count > 2:
            cleaned.append({
                'rating': entry['rating'],
                'length': word_count,
                'sentiment': 1 if 'good' in processed_text or 'excellent' in processed_text else 0
            })
    return cleaned

# Distractor function: unused but plausible
def calculate_tenure_bonus(years):
    return int(50 * math.pow(1.1, years))

# Core logic disguised among noise
def evaluate_performance(log, importance_weights):
    score = 0.0
    bonus_tracker = defaultdict(lambda: 0)
    temp_multiplier = 1.0

    # Misleading loop: tracks sentiment but doesn't impact final score directly
    for record in log:
        if record['sentiment'] == 1:
            bonus_tracker['positive'] += 1
        else:
            bonus_tracker['negative'] += 1

    # Actual scoring logic
    raw_ratings = [r['rating'] for r in log]
    avg_rating = sum(raw_ratings) / len(raw_ratings) if raw_ratings else 0

    # Weight adjustment using lambda (plausible but partially irrelevant)
    adjuster = lambda x, w: x * w
    adjusted = adjuster(avg_rating, importance_weights['base'])

    # Secondary metric: length influence (minor effect)
    total_length = sum(r['length'] for r in log)
    length_factor = 1 + (min(total_length, 50) / 100)  # Max +0.5

    # Real computation
    score += adjusted * length_factor

    # Dead code path: never executed due to data constraints
    if len(bonus_tracker) > 100:
        temp_multiplier *= 1.2

    # Final adjustments
    penalty = 0
    for r in log:
        if r['rating'] == 1:
            penalty += 0.5  # Small penalty for lowest rating

    score -= penalty

    # Distractor variables
    projected_growth = sum([int(math.sqrt(calculate_tenure_bonus(i+1))) for i in range(3)])
    stability_index = len(log) / (penalty + 1) if penalty != -1 else 0  # Unused

    final_normalized = round(score * 1.07, 4)  # Apply minor multiplier and round
    return final_normalized

# Input data
feedback_log = [
    {'rating': 4, 'comment': 'Good effort overall'},
    {'rating': 5, 'comment': 'Excellent work this quarter'},
    {'rating': 3, 'comment': 'Satisfactory performance'},
    {'rating': 5, 'comment': 'good initiative and teamwork'},
    {'rating': 2, 'comment': 'Needs improvement in communication'},
    {'rating': 1, 'comment': 'Poor attendance and output'},
    {'rating': 4, 'comment': 'good progress recently'}
]

weights = {
    'base': 10.5,
    'seniority': 1.2  # Unused weight
}

# Preprocessing (has side effects on data shape)
processed_log = preprocess_entries(feedback_log)

# Critical statement
final_score = evaluate_performance(processed_log, weights)

print(f"Result: {final_score}")