import re
from dataclasses import dataclass
from typing import FrozenSet

text_fragment = "AEIOUaeiouBCDFGbcdfg!@#$%123"
vowel_set = frozenset('AEIOUaeiou')
consonant_set = frozenset('BCDFGbcdfg')
symbol_set = frozenset('!@#$%')
digit_set = frozenset('123')

text_chars = frozenset(text_fragment)
vowels_found = text_chars & vowel_set
consonants_found = text_chars & consonant_set
symbols_found = text_chars & symbol_set
digits_found = text_chars & digit_set

vowel_weight = lambda n: n * 3 if n <= 5 else n * 2
consonant_bonus = lambda c: 10 if c >= 3 else 0
symbol_modifier = lambda s: s * -2 if s > 2 else -5

categorized_counts = {
    'vowels': len(vowels_found),
    'consonants': len(consonants_found),
    'symbols': len(symbols_found),
    'digits': len(digits_found)
}

score_components = []
for category, count in categorized_counts.items():
    if category == 'vowels':
        score_components.append(vowel_weight(count))
    elif category == 'consonants':
        score_components.append(consonant_bonus(count))
    elif category == 'symbols':
        score_components.append(symbol_modifier(count))
    else:
        score_components.append(count * 4)

has_balanced_structure = bool(re.match(r'^[A-Z]+[a-z]+[0-9]+[!@#$%]+$', text_fragment))
structure_bonus = 25 if has_balanced_structure else 0

intermediate_score = sum(score_components)
final_linguistic_score = intermediate_score + structure_bonus if intermediate_score > 20 else intermediate_score - structure_bonus

print(f"Result: {final_linguistic_score}")