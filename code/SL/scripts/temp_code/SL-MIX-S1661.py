import re
from collections import Counter
from itertools import combinations

def calculate_symbolic_density(fragment, symbols):
    return sum(fragment.count(symbol) for symbol in symbols)

class TextFragment:
    def __init__(self, content):
        self.content = content
        self.vowels = re.findall(r'[aeiouAEIOU]', content)
        self.consonants = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', content)
        self.symbolic_chars = ['†', '‡', '¶', '§']
    
    def get_vowel_ratio(self):
        if len(self.content) == 0:
            return 0
        return len(self.vowels) / len(self.content)
    
    def get_consonant_clusters(self):
        clusters = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]{2,}', self.content)
        return len(clusters)
    
    def get_symbolic_score(self):
        return calculate_symbolic_density(self.content, self.symbolic_chars)

text_sample = "The†quick‡brown¶fox§jumps†over‡the¶lazy§dog"
fragment = TextFragment(text_sample)

vowel_scoring_function = lambda ratio: int(ratio * 100) if ratio > 0.3 else int(ratio * 50)
vowel_score = vowel_scoring_function(fragment.get_vowel_ratio())

consonant_cluster_count = fragment.get_consonant_clusters()
cluster_combinations = len(list(combinations(range(consonant_cluster_count), min(2, consonant_cluster_count))))
cluster_bonus = cluster_combinations * 3 if cluster_combinations > 0 else 0

symbolic_score = fragment.get_symbolic_score()
symbolic_modifier = 2 if symbolic_score >= 4 else 1

base_composite_score = vowel_score + (consonant_cluster_count * 5) + cluster_bonus
final_evaluation_score = base_composite_score * symbolic_modifier if symbolic_modifier > 1 else base_composite_score + symbolic_score

print(f"Result: {final_evaluation_score}")