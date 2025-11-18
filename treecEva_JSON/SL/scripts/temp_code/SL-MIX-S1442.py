import re
from functools import wraps
from collections import defaultdict
from itertools import permutations

def transformation_tracker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.call_count += 1
        return result
    wrapper.call_count = 0
    return wrapper

class LinguisticAnalyzer:
    def __init__(self):
        self.pattern_cache = {}
    
    @transformation_tracker
    def analyze_pattern(self, text_segment):
        # Count vowels and consonants
        vowels = len(re.findall(r'[aeiouAEIOU]', text_segment))
        consonants = len(re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text_segment))
        return vowels * 3 - consonants * 2
    
    @transformation_tracker
    def process_combinations(self, word_list):
        score = 0
        for perm in permutations(word_list, 2):
            combined = ''.join(perm)
            if combined not in self.pattern_cache:
                self.pattern_cache[combined] = self.analyze_pattern(combined)
            score += self.pattern_cache[combined]
        return score

# Initialize analyzer
analyzer = LinguisticAnalyzer()

# Ancient text fragments
fragments = ['arcane', 'mystic', 'glyph']

# Dynamic programming table for storing intermediate results
dp_table = defaultdict(int)
total_transformations = 0

# Process each fragment with different combination approaches
for i, fragment in enumerate(fragments):
    # Direct analysis
    dp_table[i] = analyzer.analyze_pattern(fragment)
    
    # Combination analysis with other fragments
    remaining = [f for j, f in enumerate(fragments) if j != i]
    combo_score = analyzer.process_combinations(remaining)
    dp_table[i] += combo_score
    
    total_transformations += analyzer.analyze_pattern.call_count + analyzer.process_combinations.call_count

# Calculate final weighted score
final_score = 0
for i in range(len(fragments)):
    weight = (i + 1) * 2
    adjustment = len(re.findall(r'[aeiou]', fragments[i]))  # Vowel count adjustment
    final_score += dp_table[i] * weight + adjustment

# Apply final transformation based on total transformations
if total_transformations % 2 == 0:
    final_score = final_score ^ 0xFF  # XOR with 255
else:
    final_score = final_score & 0x7F  # Bitwise AND with 127

print(f"Result: {final_score}")