# Word scoring system for a text analysis tool

def calculate_text_metrics():
    # Dictionary of word values based on significance
    points = {
        'excellent': 5,
        'good': 3,
        'average': 1,
        'poor': -1,
        'terrible': -3
    }
    
    # Sample user input (normally would come from input())
    user_input = ['The', 'service', 'was', 'GOOD', 'but', 'the', 'food', 'was', 'EXCELLENT']
    
    # Track word frequencies for reporting
    word_count = {}
    for word in user_input:
        word_lower = word.lower()
        word_count[word_lower] = word_count.get(word_lower, 0) + 1
    
    # Calculate the sentiment score
    score = sum([points.get(word.lower(), 0) for word in user_input])
    
    # Alternative scoring method (not used in final calculation)
    alt_score = 0
    for i, word in enumerate(user_input):
        if i % 2 == 0:  # Only count even-positioned words
            alt_score += points.get(word.lower(), 0)
    
    print(f"Result: {score}")
    return score

calculate_text_metrics()