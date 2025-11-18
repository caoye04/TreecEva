from collections import defaultdict

def transform_word(word):
    return ''.join(chr(ord(c) + 1) for c in word)

def is_vowel_shifted(word):
    vowels = 'aeiou'
    transformed = ''.join(chr(ord(c) - 1) for c in word)
    return any(c in vowels for c in transformed.lower())

token_weights = {'amazing': 1.5, 'technology': 2.0, 'today': 1.2, 'incredible': 1.8, 'advances': 1.6}
sentence = "amazing technology today incredible advances"
tokens = sentence.split()

# Transformation layer 1: Apply character shifts
transformed_tokens = list(map(transform_word, tokens))

# Transformation layer 2: Filter tokens based on vowel check
valid_tokens = [t for t in transformed_tokens if is_vowel_shifted(t)]

# Transformation layer 3: Calculate weighted scores using dictionary comprehension
base_scores = {token: token_weights.get(''.join(chr(ord(c)-1) for c in token), 1.0) for token in valid_tokens}

# Transformation layer 4: Apply bonus multiplier using lambda
bonus_multiplier = lambda x: 1.2 if len(x) > 7 else 1.0
adjusted_scores = {k: v * bonus_multiplier(k) for k, v in base_scores.items()}

# Final aggregation step
final_coherence_score = sum(adjusted_scores.values())

print(f"Result: {final_coherence_score}")