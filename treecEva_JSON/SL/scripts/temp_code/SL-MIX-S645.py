import re
from functools import reduce

def tokenize_and_score(document):
    # Preprocessing: remove punctuation and convert to lowercase
    clean_text = re.sub(r'[^\w\s]', '', document).lower()
    tokens = clean_text.split()
    
    # Dynamic programming table for valid word formation counts
    dp = [0] * (len(tokens) + 1)
    dp[0] = 1  # Base case: empty sequence is valid
    
    # Valid words dictionary (simulating a small lexicon)
    valid_words = {'the': True, 'quick': True, 'brown': True, 'fox': True, 'jumps': True, 
                   'over': True, 'lazy': True, 'dog': True, 'a': True, 'an': True}
    
    # Lambda for checking if a token is a valid word
    is_valid_word = lambda word: valid_words.get(word, False)
    
    # Process tokens using dynamic programming
    for i in range(1, len(tokens) + 1):
        # Check single token
        if is_valid_word(tokens[i-1]):
            dp[i] += dp[i-1]
        # Check pairs of tokens
        if i >= 2:
            pair = ' '.join(tokens[i-2:i])
            if is_valid_word(pair):
                dp[i] += dp[i-2]
    
    # Calculate linguistic score using functional programming
    word_lengths = list(map(len, filter(is_valid_word, tokens)))
    linguistic_score = reduce(lambda x, y: x + y, word_lengths, 0) if word_lengths else 0
    
    return dp[len(tokens)], linguistic_score

# Document to analyze
document = "The quick brown fox jumps over the lazy dog"
valid_formations, linguistic_score = tokenize_and_score(document)
print(f"Result: {linguistic_score}")