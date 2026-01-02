def analyze_sentiment(text_blocks):
    sentiment_scores = []
    for block in text_blocks:
        score = 0
        for word in block.split():
            if word.lower() in ['good', 'excellent', 'great']:
                score += 2
            elif word.lower() in ['bad', 'poor', 'terrible']:
                score -= 2
        sentiment_scores.append(score)
    return sentiment_scores

# Irrelevant helper function (distractor)
def compute_text_entropy(text_list):
    import math
    entropy = 0.0
    total_chars = sum(len(t) for t in text_list)
    if total_chars == 0:
        return 0.0
    for t in text_list:
        p = len(t) / total_chars
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

# Another misleading computation (dead path)
def calculate_redundancy_index(seq):
    seen = {}
    duplicates = 0
    for i, item in enumerate(seq):
        if item in seen:
            duplicates += abs(i - seen[item])
        seen[item] = i
    return duplicates // 2 if duplicates else 0

# Core logic with distractors embedded
def preprocess_feedback(raw_feedback):
    cleaned = []
    noise_counter = 0
    for entry in raw_feedback:
        if not isinstance(entry, str):
            noise_counter += 1
            continue
        stripped = entry.strip().lower()
        if stripped.startswith('ignore'):
            noise_counter += 1
            continue
        cleaned.append(stripped)
    # Distractor: unused transformation
    reversed_chunks = [c[::-1] for c in cleaned]
    return cleaned

# Main processing chain
def evaluate_performance(feedback_log, initial_rating):
    # Step 1: Clean data
    processed = preprocess_feedback(feedback_log)
    
    # Step 2: Compute sentiment (relevant)
    sentiments = analyze_sentiment(processed)
    
    # Step 3: Aggregate using weighted rolling window (key part)
    cumulative = initial_rating
    weights = [0.5, 0.8, 1.0][:len(sentiments)] if len(sentiments) < 4 else [0.3, 0.6, 0.8, 1.0]
    
    # Use enumerate and slicing together (required feature)
    for idx, (sent, weight) in enumerate(zip(sentiments, weights)):
        adjustment = sent * weight
        cumulative += adjustment
    
    # Step 4: Apply decay if long sequence (red herring)
    if len(processed) > 5:
        cumulative *= 0.95
    
    # Step 5: Bitwise tamper check (distractor)
    checksum = 0
    for s in sentiments:
        checksum ^= int(abs(s))
    if checksum & 1:
        cumulative -= 0.5
    
    # Final nonlinear mapping (relevant final step)
    final_value = int(cumulative ** 2 + 0.5) if cumulative >= 0 else -int(cumulative ** 2 + 0.5)
    return final_value

# Input data
user_reviews = [
    'Great product overall',
    'Excellent service and good experience',
    'Bad interface but great speed',
    'Poor design choices',
    'This should be ignored because it is invalid',
    'Good improvement over last version'
]

base_rating = 10

# Misleading intermediate calculations
entropy_metric = compute_text_entropy(user_reviews)
sentiment_trace = analyze_sentiment(user_reviews)
redundancy_flag = calculate_redundancy_index(user_reviews)

# Key execution point
cleaned_data = preprocess_feedback(user_reviews)
final_score = evaluate_performance(user_reviews, base_rating)

# Output result
print(f"Result: {final_score}")