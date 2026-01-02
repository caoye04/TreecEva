from collections import defaultdict

# Simulate user feedback analysis for a training module
module_ratings = [4.5, 3.2, 4.8, 4.1, 3.9, 4.3, 4.7, 3.6]
feedback = [
    "very good and informative",
    "not great, too slow",
    "excellent content and pacing",
    "good but could improve examples",
    "decent overall experience",
    "amazing clarity and structure",
    "outstanding delivery and depth",
    "average, needs refinement"
]

# Irrelevant aggregation (distractor)
total_chars = sum(len(review) for review in feedback)
word_count_map = defaultdict(int)
positive_terms = {'good', 'great', 'excellent', 'amazing', 'outstanding', 'very', 'clear', 'informative'}
negative_terms = {'not', 'too', 'needs', 'refinement', 'slow', 'average'}

for review in feedback:
    words = review.lower().split()
    for word in words:
        word_count_map[word] += 1

# Semi-relevant preprocessing: count sentiment hits
sentiment_score = 0
for review in feedback:
    words = review.lower().split()
    for term in positive_terms:
        if term in words:
            sentiment_score += 1
    for term in negative_terms:
        if term in words:
            sentiment_score -= 1

# Misleading transformation (distractor)
adjusted_length_metric = total_chars / (len(feedback) or 1)
smoothed_sentiment = max(sentiment_score, 0.5) * 1.2

# Base rating from numerical scores
base_rating = sum(module_ratings) / len(module_ratings)

# Auxiliary function that appears complex but uses only core logic
def analyze_feedback_depth(feedback_list):
    total_depth = 0
    for f in feedback_list:
        clauses = f.split(',') + f.split(' and ')
        total_depth += len(clauses)
    return total_depth / len(feedback_list)

# Another distraction: unused helper
def calculate_readability_score(text):
    words = text.split()
    long_words = sum(1 for w in words if len(w) > 6)
    return (long_words / len(words)) * 100 if words else 0

# Core evaluation logic
def evaluate_performance(feedback, base):
    # Step 1: Boost base rating by sentiment influence
    pos_neg_ratio = max(smoothed_sentiment / 5.0, 0.8)
    
    # Step 2: Use feedback structural depth as multiplier
    depth_factor = analyze_feedback_depth(feedback)
    
    # Step 3: Apply composite adjustment
    adjusted_base = base * pos_neg_ratio
    amplified_score = adjusted_base * (1 + (depth_factor / 10))
    
    # Step 4: Cap the score to realistic range
    capped_score = min(amplified_score, 5.0)
    
    # Step 5: Final minor penalty if average word length is low (proxy for simplicity)
    avg_word_len = sum(len(word) for rev in feedback for word in rev.split()) / sum(len(rev.split()) for rev in feedback)
    if avg_word_len < 4.2:
        capped_score -= 0.15
    
    return round(capped_score, 4)

# Execution point of interest
final_score = evaluate_performance(feedback, base_rating)

# Print result as required
print(f"Result: {final_score}")