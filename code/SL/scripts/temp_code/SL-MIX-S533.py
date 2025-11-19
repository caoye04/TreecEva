from itertools import permutations

def calculate_permutation_score(perm):
    score = 0
    for i, char in enumerate(perm):
        if i % 2 == 0 and char in 'aeiou':
            score += 3
        elif i % 2 == 1 and char not in 'aeiou':
            score += 2
        else:
            score -= 1
    return score

def generate_cryptographic_keys(charset, target_length, min_score=5):
    valid_keys = []
    for perm in permutations(charset, target_length):
        score = calculate_permutation_score(perm)
        if score >= min_score:
            valid_keys.append((perm, score))
    return valid_keys

# Cryptographic character set for key generation
alphabet_subset = frozenset(['a', 'b', 'c', 'd', 'e', 'f'])
key_components = list(alphabet_subset)

# Generate valid cryptographic keys
secure_keys = generate_cryptographic_keys(key_components, 4, 6)

# Calculate final security score
final_score = 0
for key, score in secure_keys:
    vowel_count = sum(1 for c in key if c in 'aeiou')
    if vowel_count >= 2 and score > final_score:
        final_score = score

print(f"Result: {final_score}")