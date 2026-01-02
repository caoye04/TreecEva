def analyze_feedback(reviews):
    sentiment_scores = []
    total_chars = 0
    
    for review in reviews:
        stripped = review.strip().lower()
        word_count = len(stripped.split())
        char_count = len(stripped)
        total_chars += char_count
        
        if 'excellent' in stripped or 'great' in stripped:
            sentiment_scores.append(3)
        elif 'poor' in stripped or 'bad' in stripped:
            sentiment_scores.append(-2)
        elif 'average' in stripped or 'okay' in stripped:
            sentiment_scores.append(1)
        else:
            sentiment_scores.append(0)
    
    average_length = total_chars / len(reviews) if reviews else 0
    adjustment_factor = int(average_length // 10) * 0.1  # Minor influence
    return sentiment_scores, adjustment_factor


def calculate_consistency(scores):
    if len(scores) < 2:
        return 1.0
    
    diffs = [abs(scores[i] - scores[i+1]) for i in range(len(scores)-1)]
    max_diff = max(diffs) if diffs else 0
    return 0.5 if max_diff > 2 else 0.9

# Simulated preprocessing step (irrelevant but looks important)
def normalize_data(entries):
    normalized = []
    for e in entries:
        clean = e.replace('!', '').replace('?', '').strip()
        normalized.append(clean)
    return normalized

# Misleading auxiliary function that's called but doesn't impact final result
def compute_reputation(base, age):
    decay = 0.95 ** age
    return base * decay + 10

# Core logic function
def evaluate_performance(feedback, base):
    raw_scores, adj = analyze_feedback(feedback)
    
    # Dead code path - never reached due to prior logic, but looks active
    redundant_multiplier = 1.0
    if False:  # Simulate unreachable branch
        temp = sum([x**2 for x in raw_scores])
        redundant_multiplier = max(0.5, temp / 100)
    
    total_sentiment = sum(raw_scores)
    consistency = calculate_consistency(raw_scores)
    
    # Actual key computation
    preliminary = base + total_sentiment
    adjusted = preliminary * consistency
    final_score = round(adjusted + adj, 2)
    
    # Extra unused variables to increase cognitive load
    avg_per_review = total_sentiment / len(raw_scores) if raw_scores else 0
    outlier_count = sum(1 for s in raw_scores if abs(s) == 3)
    
    return final_score

# Input data with meaningful context
feedback_list = [
    "  This was excellent service! Very happy.  ",
    "Poor communication and delayed response.",
    "Average experience, nothing special.",
    "Great staff and excellent facilities!",
    "It was okay, could be better next time."
]

base_rating = 50
normal_feedback = normalize_data(feedback_list)
reputation = compute_reputation(base_rating, 3)
final_score = evaluate_performance(feedback_list, base_rating)
print(f"Result: {final_score}")