import hashlib
import statistics

def calculate_syllable_weights(phoneme_sequence):
    dp_table = [0] * (len(phoneme_sequence) + 1)
    dp_table[0] = 1
    
    for idx in range(1, len(phoneme_sequence) + 1):
        current_phoneme_hash = int(hashlib.md5(phoneme_sequence[idx-1].encode()).hexdigest(), 16) % 1000
        dp_table[idx] = dp_table[idx-1] + (current_phoneme_hash * idx)
        if idx >= 2:
            dp_table[idx] = max(dp_table[idx], dp_table[idx-2] + (current_phoneme_hash * idx * 2))
    
    return dp_table[len(phoneme_sequence)]

conlang_phonemes = ['p', 't', 'k', 'b', 'd', 'g', 'm', 'n', 'l', 'r']
phoneme_frequency_map = {phoneme: calculate_syllable_weights([phoneme] * (i+1)) for i, phoneme in enumerate(conlang_phonemes)}
syllable_structure_scores = list(phoneme_frequency_map.values())

vowel_harmonization_set = frozenset(['a', 'e', 'i', 'o', 'u'])
consonant_inventory_set = frozenset(conlang_phonemes)
intersection_cardinality = len(vowel_harmonization_set & consonant_inventory_set)

if intersection_cardinality == 0:
    adjusted_scores = [score * 1.5 for score in syllable_structure_scores]
else:
    adjusted_scores = syllable_structure_scores

final_entropy_score = round(statistics.variance(adjusted_scores) * 1000)
print(f"Result: {final_entropy_score}")