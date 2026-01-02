def analyze_sentiment(texts):
    # Irrelevant function - decoy
    sentiment_totals = {}
    for t in texts:
        clean = t.lower().replace('.', '').strip()
        words = clean.split()
        score = 0
        for w in words:
            if w in ['good', 'excellent', 'great']:
                score += 2
            elif w in ['bad', 'poor']:
                score -= 2
        sentiment_totals[t[:10]] = score
    return sentiment_totals

def validate_input(data):
    # Dead code path - never used
    if not isinstance(data, list):
        return False
    for item in data:
        if not isinstance(item, str) or len(item) == 0:
            return False
    return True

def transform_ratings(ratings):
    # Distractor: transforms ratings but not used in final computation
    adjusted = []
    for r in ratings:
        if r < 1:
            r = 1
        elif r > 5:
            r = 5
        adjusted.append(round((r ** 0.5) * 2, 3))
    return adjusted

def calculate_composite(magnitude, signal, mode='advanced'):
    # Misleading intermediate result
    if mode == 'basic':
        return magnitude + signal
    else:
        return (magnitude * 1.5) + (signal * 0.8) - 2

def decode_key(s):
    # Bit manipulation red herring
    val = 0
    for c in s:
        val ^= ord(c)
        val = (val << 1) & 0xFF
    return val % 7

def process_feedback(reviews, weights):
    # Core logic with distractors embedded
    base_scores = []
    char_count_map = {}

    # Real logic begins
    for review in reviews:
        stripped = review.strip().upper()
        length = len(stripped)
        vowel_count = sum(1 for c in stripped if c in 'AEIOU')
        # Key relevant transformation
        normalized = vowel_count / length if length > 0 else 0
        base_scores.append(normalized * 100)

        # Distractor: tracking unused character frequency
        for c in stripped:
            if c.isalpha():
                char_count_map[c] = char_count_map.get(c, 0) + 1

    # Real accumulation
    weighted_sum = 0.0
    total_weight = 0.0

    for i, weight in enumerate(weights):
        if i >= len(base_scores):
            break
        weighted_sum += base_scores[i] * weight
        total_weight += weight

    average_score = weighted_sum / total_weight if total_weight > 0 else 0

    # Redundant transformation on correct value
    temp_result = average_score * 1.1
    final_adjustment = temp_result - (temp_result * 0.1)  # Cancels out

    # Final answer computation
    final_score = int(round(final_adjustment))

    # Decoy usage of other functions
    _ = calculate_composite(len(reviews), len(weights), 'advanced')
    _ = decode_key('final')

    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    reviews = [
        "This product is excellent and works great.",
        "Poor quality and bad design.",
        "Excellent performance, absolutely great!",
        "Not good, very poor user experience."
    ]
    weights = [0.4, 0.8, 0.6, 0.9]

    # Unused variables - red herrings
    raw_analysis = analyze_sentiment(reviews)
    validated = validate_input(reviews)
    transformed = transform_ratings([3.2, 4.1, 2.8, 5.0])
    key_code = decode_key('secret')

    # Critical statement
    final_score = process_feedback(reviews, weights)

    print(f"Result: {final_score}")