import re

def process_phonemes(phoneme_corpus):
    base_sets = [frozenset(phoneme) for phoneme in phoneme_corpus]
    vowel_pattern = re.compile(r'[aeiou]')
    
    # Filter phoneme sets containing vowels using regex
    vowel_sets = [
        ph_set for ph_set in base_sets
        if any(vowel_pattern.match(char) for char in ph_set)
    ]
    
    # Lambda to compute cardinality product
    cardinality_product = lambda s1, s2: len(s1) * len(s2)
    
    # Short-circuit evaluation with set intersection check
    score = 0
    for i in range(len(vowel_sets)):
        for j in range(i+1, len(vowel_sets)):
            if vowel_sets[i] and vowel_sets[j] and (vowel_sets[i] & vowel_sets[j]):
                score += cardinality_product(vowel_sets[i], vowel_sets[j])
    return score

# Corpus data
phoneme_data = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'g'],
    ['h', 'i'],
    ['j', 'k', 'l', 'm', 'n'],
    ['o', 'p', 'q'],
    ['r', 's', 't', 'u']
]

metric_score = process_phonemes(phoneme_data)
print(f"Result: {metric_score}")