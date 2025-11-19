from itertools import permutations
from collections import defaultdict

def calculate_score(s):
    vowels = set('aeiouAEIOU')
    specials = set('!@#$%^&*()')
    score = 0
    for char in s:
        if char in vowels:
            score += 2
        elif char in specials:
            score += 3
        elif char.isalpha():
            score += 1
        # Numbers ignored
    return score

characters = ['a', 'B', '!', '3']
perms = permutations(characters)
scores = defaultdict(int)
max_score = 0

for p in perms:
    perm_str = ''.join(p)
    current_score = calculate_score(perm_str)
    scores[perm_str] = current_score
    if current_score > max_score:
        max_score = current_score

print(f"Result: {max_score}")