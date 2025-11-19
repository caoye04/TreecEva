from collections import Counter

def tokenize(text):
    return text.lower().split()

feedback = "I absolutely love this product but it could be better"
tokens = tokenize(feedback)
token_counter = Counter(tokens)

positive_words = {'love', 'great', 'excellent'}
negative_words = {'hate', 'bad', 'worst'}

has_positive = any(word in positive_words for word in tokens)
has_negative = any(word in negative_words for word in tokens)

sentiment_score = 0
if has_positive and not has_negative:
    sentiment_score = token_counter['love'] * 10
elif has_negative and not has_positive:
    sentiment_score = token_counter['hate'] * -10
elif has_positive and has_negative:
    sentiment_score = 5  # Mixed sentiment
else:
    sentiment_score = 0  # Neutral sentiment

print(f"Result: {sentiment_score}")