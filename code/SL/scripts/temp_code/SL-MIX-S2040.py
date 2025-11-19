import re
from functools import reduce

def transform_syllable_weight(syllable):
    vowel, consonant = syllable
    base_weight = ord(vowel) * ord(consonant)
    if re.match(r'[aeiou]', vowel, re.IGNORECASE) and consonant.isupper():
        return base_weight + 10
    elif not re.match(r'[aeiou]', vowel, re.IGNORECASE) and consonant.islower():
        return base_weight - 5
    else:
        return base_weight

def aggregate_weights(weight_list):
    sorted_weights = sorted(weight_list, reverse=True)
    top_three_sum = sum(sorted_weights[:3])
    adjustment = reduce(lambda x, y: x ^ y, sorted_weights[3:], 0) if len(sorted_weights) > 3 else 0
    return top_three_sum - adjustment

# Initial dataset of syllables represented as (vowel, consonant)
syllable_dataset = [
    ('a', 'B'),
    ('E', 'f'),
    ('i', 'G'),
    ('O', 'h'),
    ('u', 'J'),
    ('A', 'k')
]

# Apply transformation to get weights
transformed_weights = list(map(transform_syllable_weight, syllable_dataset))

# Aggregate to compute final score
final_score = aggregate_weights(transformed_weights)
print(f'Result: {final_score}')