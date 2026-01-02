def analyze_sentiment(text):
    positive_words = ['great', 'excellent', 'good', 'outstanding']
    negative_words = ['poor', 'bad', 'terrible', 'awful']
    words = text.lower().split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    return (pos_count - neg_count) * 10


def extract_codes(data_string):
    segments = data_string.split('-')
    code_values = []
    for segment in segments:
        if segment.isnumeric():
            code_values.append(int(segment))
    return code_values

# Irrelevant helper function (dead path)
def unused_utility(x):
    return x ** 2 + 3 * x - 7

# Main processing pipeline
raw_feedback = "The service was excellent but response time was poor and support was bad"
base_rating = 75
adjustment_factor = 1.2

sentiment_shift = analyze_sentiment(raw_feedback)

# Simulate parsing of embedded codes (mostly irrelevant)
tracking_data = "LOG-45-ERR-0-CODE-88"
code_parts = extract_codes(tracking_data)
summed_codes = sum(code_parts)  # Distractor computation
average_code = summed_codes / len(code_parts) if code_parts else 0

# Real metric transformation
interim_score = base_rating + sentiment_shift

# Conditional adjustment based on hidden rule
if interim_score >= 70:
    multiplier = 1.1
else:
    multiplier = 0.9

boosted_score = interim_score * multiplier

# Secondary adjustment using string slicing
feedback_slice = raw_feedback[15:25]  # 'excellent b'
extra_weight = len(feedback_slice.replace(' ', ''))  # 10 characters minus space → 9

# Another distractor: dictionary counting unrelated chars
distraction_counter = {}
for char in feedback_slice:
    if char not in 'aeiou':
        distraction_counter[char] = distraction_counter.get(char, 0) + 1
char_complexity = sum(distraction_counter.values())  # equals 5 (non-vowels)

# Final evaluation logic
base_metrics = {
    'score': boosted_score,
    'penalty': abs(sentiment_shift),
    'bonus': extra_weight
}

feedback_str = raw_feedback.upper()[::-1]  # Reversed uppercase string

def evaluate_performance(feedback_msg, metrics):
    length_indicator = len(feedback_msg) % 11  # cyclic effect
    base_val = metrics['score']
    penalty_adj = metrics['penalty'] // 10
    bonus_applied = metrics['bonus'] * 2 if 'EXCELLENT' in feedback_msg else 0
    
    # Core formula
    result = base_val - penalty_adj + bonus_applied
    
    # Red herring: complex slicing and character check
    mid_part = feedback_msg[10:30]
    vowel_count = sum(1 for c in mid_part if c.lower() in 'aeiou')
    if vowel_count > 3:
        result -= 5  # minor penalty
    
    return int(result)

final_score = evaluate_performance(feedback_str, base_metrics)
print(f"Target result: {final_score}")