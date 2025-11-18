from collections import Counter

def transform_nucleotide(nuc):
    mapping = {'A': 1, 'G': 2, 'T': 3, 'C': 4}
    return mapping.get(nuc, 0)

genomic_sequence = 'AGTCGTAC'
scores = [transform_nucleotide(n) for n in genomic_sequence]
frequency_counter = Counter(scores)

weighted_sum = sum(score * freq for score, freq in frequency_counter.items())
total_unique_scores = len(frequency_counter)

final_score = weighted_sum if total_unique_scores > 3 else 0
print(f'Result: {final_score}')