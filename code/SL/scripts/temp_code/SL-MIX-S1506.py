import re
from collections import Counter
from functools import reduce
from dataclasses import dataclass

text_fragment = "AEIOUaeiouBCDFGbcdfg!!!???***"

vowel_pattern = re.compile(r'[AEIOUaeiou]')
consonant_pattern = re.compile(r'[BCDFGbcdfg]')
special_pattern = re.compile(r'[!@#$%^&*?]+')

vowels_found = vowel_pattern.findall(text_fragment)
consonants_found = consonant_pattern.findall(text_fragment)
special_symbols = special_pattern.findall(text_fragment)

char_frequency = Counter(text_fragment)
unique_chars = len(char_frequency)

vowel_count = len(vowels_found)
consonant_count = len(consonants_found)
special_count = len(special_symbols)

frequency_weights = {char: count for char, count in char_frequency.items() if count > 1}
weighted_sum = sum(count * ord(char) for char, count in frequency_weights.items())

base_ratio = vowel_count / max(consonant_count, 1)
adjusted_ratio = base_ratio * len([c for c in text_fragment if c.isupper()])

symbol_modifier = 1
if special_count > 0:
    symbol_modifier = reduce(lambda x, y: x * y, [len(group) for group in special_symbols], 1)

final_evaluation_score = int((weighted_sum + adjusted_ratio) * symbol_modifier / max(unique_chars, 1))

print(f"Result: {final_evaluation_score}")