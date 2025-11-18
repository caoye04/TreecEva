from collections import defaultdict
import re

def calculate_motif_strength(fragment):
    weights = {'A': 2, 'T': 3, 'G': 1, 'C': 4}
    return sum(weights[nuc] for nuc in fragment if nuc in weights)

# DNA fragments under analysis
dna_fragments = ['ATGCATGC', 'GGCCTTAA', 'TACGTACG']

# Initialize scoring system
motif_scores = defaultdict(int)
fragment_enhancement = {}

# Process fragments with lambda-based modifier
enhance_score = lambda base_score, length: base_score * (1.5 if length > 6 else 1.0)

for fragment in dna_fragments:
    base_score = calculate_motif_strength(fragment)
    enhanced = enhance_score(base_score, len(fragment))
    motif_scores[fragment] = enhanced
    # Pattern matching for significant motifs
    matches = re.findall(r'(?:GC){2,}', fragment)
    fragment_enhancement[fragment] = len(matches) * 10

# Greedy selection of top fragments
sorted_fragments = sorted(motif_scores.items(), key=lambda x: x[1], reverse=True)[:2]
selected_scores = [score for _, score in sorted_fragments]

# Final calculation using ternary logic
has_high_enhancement = any(enh > 5 for enh in fragment_enhancement.values())
bonus = 25 if has_high_enhancement else 0

final_score = int(sum(selected_scores) + bonus)
print(f"Result: {final_score}")