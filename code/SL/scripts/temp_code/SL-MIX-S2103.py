import re
from functools import reduce

def dna_hash(sequence):
    return sum(ord(nucleotide) * (3 ** i) for i, nucleotide in enumerate(sequence))

class PalindromeAnalyzer:
    def __init__(self):
        self.palindromes_found = []
    
    def find_palindromes(self, seq):
        palindromes = []
        for i in range(len(seq)):
            for j in range(i+4, min(len(seq)+1, i+12)):  # Minimum length 4, max 11
                substring = seq[i:j]
                if substring == substring[::-1] and re.match(r'^[ATGC]+$', substring):
                    palindromes.append(substring)
        return list(set(palindromes))  # Remove duplicates
    
    @staticmethod
    def calculate_stability(sequence):
        gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence)
        return round(gc_content * len(sequence) * 2.5)

# DNA sequence from a regulatory region
chromosome_segment = "ATGCCGCAATCGGCTAGCTAGCCGATTACGGCCGTAGCTAGCTAG"

analyzer = PalindromeAnalyzer()
palindrome_list = analyzer.find_palindromes(chromosome_segment)

# Filter palindromes with high stability (>7) and length (>5)
stable_palindromes = [
    p for p in palindrome_list 
    if analyzer.calculate_stability(p) > 7 and len(p) > 5
]

# Calculate hash scores for stable palindromes
hash_scores = list(map(dna_hash, stable_palindromes))

# Apply greedy selection: pick palindromes with highest scores until total length <= 20
selected_indices = []
total_length = 0
sorted_indices = sorted(range(len(hash_scores)), key=lambda i: hash_scores[i], reverse=True)

for idx in sorted_indices:
    if total_length + len(stable_palindromes[idx]) <= 20:
        selected_indices.append(idx)
        total_length += len(stable_palindromes[idx])

# Compute final regulatory score using logical operations and ternary operators
base_score = reduce(lambda x, y: x ^ y, [hash_scores[i] for i in selected_indices], 0) if selected_indices else 0
length_bonus = 10 if total_length >= 15 else (5 if total_length >= 10 else 0)
penalty = 3 if any(len(p) % 2 != 0 for p in [stable_palindromes[i] for i in selected_indices]) else 0

regulatory_score = (base_score & 0xFF) | (length_bonus << 8) ^ penalty

print(f"Result: {regulatory_score}")