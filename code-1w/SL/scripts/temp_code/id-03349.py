def analyze_sentiment(texts):
    sentiment_scores = []
    for text in texts:
        words = text.lower().split()
        score = 0
        positive_words = ['good', 'excellent', 'great', 'outstanding']
        negative_words = ['poor', 'bad', 'terrible', 'awful']
        for word in words:
            if word in positive_words:
                score += 1
            elif word in negative_words:
                score -= 2
        sentiment_scores.append(score)
    return sentiment_scores

# Irrelevant helper function (distractor)
def calculate_average(nums):
    if len(nums) == 0:
        return 0
    total = sum(nums)
    avg = total / len(nums)
    return round(avg, 2)

# Simulate customer feedback processing
feedback_raw = [
    "The product was excellent and great!",
    "Poor quality and terrible service.",
    "It was good but could be better",
    "Outstanding overall experience"
]

# Extract key phrases (semi-relevant)
processed_feedback = [text.replace('!', '').replace('.', '') for text in feedback_raw]
word_count_summary = [len(text.split()) for text in processed_feedback]

# Core sentiment analysis (relevant)
sentiments = analyze_sentiment(processed_feedback)

# Base rating from external source (fixed)
base_rating = 75

# Auxiliary metric (distractor)
total_characters = sum(len(text) for text in processed_feedback)
compression_ratio = len(processed_feedback) / (total_characters if total_characters > 0 else 1)

# Feedback list includes both raw and analyzed data
feedback_list = []
for i, text in enumerate(processed_feedback):
    entry = {
        'index': i,
        'text': text,
        'sentiment': sentiments[i],
        'length': word_count_summary[i],
        'weight': compression_ratio  # Not actually used
    }
    feedback_list.append(entry)

# Secondary unused computation (dead code path)
if any(f['sentiment'] < 0 for f in feedback_list):
    adjustment_factor = -5
else:
    adjustment_factor = 10

# Key logic with moderate nesting and combined operations
def evaluate_performance(feedback_data, base):
    total_impact = 0
    scaling_factor = 1.5
    penalty_threshold = -1
    
    for item in feedback_data:
        raw_sentiment = item['sentiment']
        text_len = item['length']
        
        # Nested conditional logic (intermediate complexity)
        if raw_sentiment > 0:
            contribution = raw_sentiment * scaling_factor
            if text_len >= 5:
                contribution *= 1.2
        elif raw_sentiment == 0:
            contribution = 0.5
        else:  # Negative sentiment
            contribution = abs(raw_sentiment) * -1
            if raw_sentiment <= penalty_threshold:
                contribution -= 1  # Extra penalty
        
        # Accumulate impact
        total_impact += contribution
    
    # Combine with base using weighted formula
    performance_index = base + (total_impact * 2.5)
    
    # Normalization step (redundant but plausible)
    normalized = max(0, min(100, performance_index))
    
    # Final transformation (answer depends on this)
    final_score = int(round(normalized + 0.4))  # Ensure integer result
    
    return final_score

# Execute critical statement
target_result = evaluate_performance(feedback_list, base_rating)
print(f"Result: {target_result}")