from dataclasses import dataclass
from typing import List

dna_weights = {'A': 3, 'T': 2, 'G': 5, 'C': 4}
segments = ['ATGCG', 'TGCAT', 'GCATG', 'CATGC']
scores_cache = {}

@dataclass
class GeneSegment:
    sequence: str
    score: int = 0
    
    def calculate_score(self):
        if self.sequence in scores_cache:
            self.score = scores_cache[self.sequence]
            return self.score
        total = sum(dna_weights[nucleotide] for nucleotide in self.sequence)
        hashed_val = hash(self.sequence) % 100
        adjusted_score = total + (hashed_val // 10) - (len(self.sequence) * 2)
        scores_cache[self.sequence] = adjusted_score
        self.score = adjusted_score
        return self.score

segment_objects = [GeneSegment(seq) for seq in segments]
processed_scores = []

for segment in segment_objects:
    base_score = segment.calculate_score()
    if base_score > 15:
        bonus = (base_score * 2) // 3
        final_score = base_score + bonus
    else:
        penalty = base_score // 4
        final_score = base_score - penalty
    processed_scores.append(final_score)

# Greedy selection of non-overlapping segments
selected_indices = set()
index_pairs = [(i, processed_scores[i]) for i in range(len(processed_scores))]
index_pairs.sort(key=lambda x: x[1], reverse=True)

max_score = 0
for idx, score in index_pairs:
    if not selected_indices or all(abs(idx - sel_idx) > 1 for sel_idx in selected_indices):
        selected_indices.add(idx)
        max_score += score

print(f'Result: {max_score}')