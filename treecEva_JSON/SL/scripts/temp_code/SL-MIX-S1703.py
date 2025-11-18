import re

documents = [
    "The quick brown fox jumps over the lazy dog.",
    "Is this the real life?",
    "Python programming is powerful!",
    "Can you solve this complex challenge?",
    "Advanced algorithms drive innovation."
]

vowels = 'aeiou'
consonants = 'bcdfghjklmnpqrstvwxyz'

sentence_scores = {}
aggregate_score = 0

for idx, sentence in enumerate(documents):
    # Early return if sentence ends with a question mark
    if sentence.strip().endswith('?'):
        continue
    
    # Transform sentence: remove punctuation and convert to lowercase
    clean_sentence = re.sub(r'[^\w\s]', '', sentence).lower()
    words = clean_sentence.split()
    
    # Short-circuit evaluation: check if any word has length >= 5
    if not any(len(word) >= 5 for word in words):
        continue
    
    # Count vowels and consonants
    vowel_count = sum(1 for char in clean_sentence if char in vowels)
    consonant_count = sum(1 for char in clean_sentence if char in consonants)
    
    # Compute score
    score = vowel_count * consonant_count
    sentence_scores[idx] = score
    aggregate_score += score

print(f"Result: {aggregate_score}")