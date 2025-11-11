from collections import defaultdict
import math

document = "The quick brown fox jumps over the lazy dog. The dog was really lazy and very sleepy. The fox was quick and brown."

# Tokenize into sentences
sentences = [s.strip() for s in document.split('.') if s.strip()]

# Initialize data structures
word_freq = defaultdict(int)
sentence_scores = []

# Process each sentence
for sentence in sentences:
    words = sentence.lower().split()
    # Update word frequencies
    for word in words:
        word_freq[word] += 1
    
    # Calculate sentence complexity: average word length * unique words
    unique_words = len(set(words))
    avg_length = sum(len(word) for word in words) / len(words) if words else 0
    sentence_score = avg_length * unique_words
    sentence_scores.append(sentence_score)

# Compute aggregate score
frequency_weights = {word: math.log(freq + 1) for word, freq in word_freq.items()}
weighted_sentence_scores = []

for i, sentence in enumerate(sentences):
    words = sentence.lower().split()
    weight_sum = sum(frequency_weights[word] for word in words)
    weighted_score = sentence_scores[i] * weight_sum
    weighted_sentence_scores.append(weighted_score)

# Final aggregation using a polynomial combination
aggregate_score = sum(weighted_sentence_scores) + math.sqrt(sum(sentence_scores))

print(f"Result: {round(aggregate_score, 2)}")