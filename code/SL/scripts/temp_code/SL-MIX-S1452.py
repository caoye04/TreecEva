import re
from collections import defaultdict

def calculate_phonetic_base(word):
    vowels = frozenset('aeiou')
    consonants = frozenset('bcdfghjklmnpqrstvwxyz')
    vowel_count = sum(1 for c in word if c in vowels)
    consonant_count = sum(1 for c in word if c in consonants)
    return (vowel_count * 3) ^ (consonant_count * 2)

def get_historical_modifier(word):
    pattern = r'^[a-m]+[n-z]*$'
    if re.match(pattern, word):
        return len(word) * 2
    elif re.match(r'^[n-z]+[a-m]*$', word):
        return len(word) * -1
    else:
        return 0

def compute_word_distinctiveness(word, memo):
    if word in memo:
        return memo[word]
    if len(word) <= 1:
        memo[word] = ord(word) if word else 0
        return memo[word]
    
    base_score = calculate_phonetic_base(word)
    modifier = get_historical_modifier(word)
    subword_score = compute_word_distinctiveness(word[1:], memo) if word[1:] else 0
    
    result = (base_score + modifier) ^ subword_score
    memo[word] = result
    return result

def aggregate_text_score(words_list):
    dp = [0] * (len(words_list) + 1)
    memoization_cache = {}
    
    for i in range(1, len(words_list) + 1):
        current_word = words_list[i-1]
        word_score = compute_word_distinctiveness(current_word, memoization_cache)
        dp[i] = dp[i-1] + word_score if dp[i-1] > 0 or word_score > 0 else word_score
    
    return dp[len(words_list)]

manuscript_words = ['quintessential', 'xerophytic', 'juxtapose', 'azure', 'myriad']
final_distinctiveness_score = aggregate_text_score(manuscript_words)
print(f"Result: {final_distinctiveness_score}")