import itertools
import re

def phonetic_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 1.5 if isinstance(result, (int, float)) else result
    return wrapper

@phonetic_decorator
def calculate_vowel_value(vowel_char):
    vowel_map = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    return vowel_map.get(vowel_char.lower(), 0)

consonant_values = {c: idx for idx, c in enumerate('bcdfghjklmnpqrstvwxyz', 1)}
vowel_weights = {v: calculate_vowel_value(v) for v in 'aeiou'}

transformation_rules = [
    "CVC_PATTERN: b->3, a->2, t->4",
    "VOWEL_SHIFT: e->3, i->4",
    "CONSONANT_BOOST: r->8, s->9, t->10"
]

token_sequences = ['bat', 'rate', 'site', 'bit']

processed_tokens = []
for token in token_sequences:
    chars = list(token)
    for rule in transformation_rules:
        if 'CVC_PATTERN' in rule and len(chars) == 3 and chars[1] in 'aeiou':
            chars[0] = '3' if chars[0] == 'b' else chars[0]
            chars[1] = '2' if chars[1] == 'a' else chars[1]
            chars[2] = '4' if chars[2] == 't' else chars[2]
        elif 'VOWEL_SHIFT' in rule:
            for i, char in enumerate(chars):
                if char == 'e':
                    chars[i] = '3'
                elif char == 'i':
                    chars[i] = '4'
        elif 'CONSONANT_BOOST' in rule:
            for i, char in enumerate(chars):
                if char == 'r':
                    chars[i] = '8'
                elif char == 's':
                    chars[i] = '9'
                elif char == 't':
                    chars[i] = '10'
    processed_tokens.append(''.join(chars))

semantic_weights = []
for token in processed_tokens:
    weight = 0
    for char in token:
        if char.isdigit():
            weight += int(char)
        elif char in consonant_values:
            weight += consonant_values[char]
        elif char in vowel_weights:
            weight += vowel_weights[char]
    semantic_weights.append(weight)

combinations = list(itertools.combinations(semantic_weights, 2))
aggregated_weight = sum(max(pair) for pair in combinations)

# Apply final transformation based on token characteristics
vowel_rich_count = 0
for token in token_sequences:
    vowel_count = sum(1 for c in token if c in 'aeiou')
    if vowel_count > 1:
        vowel_rich_count += 1

final_semantic_weight = aggregated_weight
if vowel_rich_count >= 2:
    final_semantic_weight *= 2
elif vowel_rich_count == 1:
    final_semantic_weight += 10
else:
    final_semantic_weight -= 5

print(f"Result: {final_semantic_weight}")