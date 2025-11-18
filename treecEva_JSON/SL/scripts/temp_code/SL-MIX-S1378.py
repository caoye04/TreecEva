import re
from collections import Counter

def is_positive_word(word):
    positive_patterns = [r'^awesome$', r'^excellent$', r'^fantastic$', r'^love$', r'^amazing$']
    return any(re.match(pattern, word, re.IGNORECASE) for pattern in positive_patterns)

feedback_responses = [
    "I love this product, it's fantastic!",
    "It's okay, nothing special.",
    "Amazing quality and excellent service.",
    "Not bad but could be better.",
    "Awesome experience, truly love it!"
]

# Filter out neutral responses (those containing 'okay' or 'not bad')
filtered_responses = [resp for resp in feedback_responses if not re.search(r'\b(okay|not bad)\b', resp, re.IGNORECASE)]

# Extract all words and convert to lowercase
all_words = []
for response in filtered_responses:
    words = re.findall(r'\b\w+\b', response.lower())
    all_words.extend(words)

# Count positive words using the custom function
positive_word_counts = Counter(filter(is_positive_word, all_words))

# Calculate sentiment score as sum of positive word counts
sentiment_score = sum(positive_word_counts.values())

print(f"Result: {sentiment_score}")