from collections import Counter

def normalize_token(token):
    return ''.join(sorted(token.lower()))

tokens = ['read', 'dear', 'dare', 'lead', 'deal', 'dark', 'bark', 'park']
normalized_tokens = [normalize_token(t) for t in tokens]
frequency_map = Counter(normalized_tokens)

unique_groups = {k for k, v in frequency_map.items() if v == 1}
repeated_groups = {k for k, v in frequency_map.items() if v > 1}

vowel_set = frozenset('aeiou')
consonant_dominant = {group for group in unique_groups if len([c for c in group if c not in vowel_set]) > len([c for c in group if c in vowel_set])}

contains_both = len(unique_groups & repeated_groups)
semantic_score = (len(consonant_dominant) << 2) | (len(repeated_groups) & 0x3) ^ contains_both

print(f"Result: {semantic_score}")