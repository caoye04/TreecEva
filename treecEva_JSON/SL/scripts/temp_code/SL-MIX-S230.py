import re
import itertools
from math import gcd
from functools import reduce

def parse_syllables(text_fragment):
    # Tokenize into syllables based on vowel-consonant patterns
    syllables = re.findall(r'[aeiou]*[^aeiou]*[aeiou]*', text_fragment)
    # Filter out empty strings
    return [s for s in syllables if s]

def count_vowels(syllable):
    return len(re.findall(r'[aeiou]', syllable))

def count_consonants(syllable):
    return len(re.findall(r'[^aeiou]', syllable))

def syllable_features(syllable):
    vowels = count_vowels(syllable)
    consonants = count_consonants(syllable)
    return {
        'text': syllable,
        'vowels': vowels,
        'consonants': consonants,
        'length': len(syllable)
    }

text_fragment = "aebocidofugahibojekulim"
syllable_list = parse_syllables(text_fragment)
syllable_data = [syllable_features(s) for s in syllable_list]

# Calculate GCD of all syllable lengths
lengths = [s['length'] for s in syllable_data]
gcd_of_lengths = reduce(gcd, lengths)

# Find all permutations of 3 syllables
resonant_chain_count = 0
for perm in itertools.permutations(syllable_data, 3):
    s1, s2, s3 = perm
    # Check resonant condition: s1.consonants == s2.vowels and s2.consonants == s3.vowels
    if s1['consonants'] == s2['vowels'] and s2['consonants'] == s3['vowels']:
        # Check multiple of GCD condition
        total_chars = s1['length'] + s2['length'] + s3['length']
        if total_chars % gcd_of_lengths == 0:
            resonant_chain_count += 1

result = resonant_chain_count
print(f"Result: {result}")