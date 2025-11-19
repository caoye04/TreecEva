from functools import lru_cache

class DNAAnalyzer:
    def __init__(self):
        self.nucleotide_map = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        self.position_weights = {i: self.fibonacci(i+1) for i in range(10)}
    
    @staticmethod
    @lru_cache(maxsize=None)
    def fibonacci(n):
        if n <= 1:
            return n
        return DNAAnalyzer.fibonacci(n-1) + DNAAnalyzer.fibonacci(n-2)
    
    def encode_sequence(self, seq):
        return [self.nucleotide_map[n] for n in seq]
    
    def mutation_distance(self, seq1, seq2, pos=0):
        if pos >= len(seq1) or pos >= len(seq2):
            return 0
        
        base_diff = abs(seq1[pos] - seq2[pos])
        weight = self.position_weights.get(pos, 1)
        current_contribution = base_diff * weight
        
        if current_contribution > 5:
            # Backtrack adjustment - reduce contribution by 20%
            current_contribution = int(current_contribution * 0.8)
            return current_contribution + self.mutation_distance(seq1, seq2, pos+2)
        else:
            return current_contribution + self.mutation_distance(seq1, seq2, pos+1)

# Analysis execution
analyzer = DNAAnalyzer()
original_seq = analyzer.encode_sequence('ACGTACGT')
mutated_seq = analyzer.encode_sequence('TGCAATGC')

# Calculate distances with different positional offsets
initial_distance = analyzer.mutation_distance(original_seq, mutated_seq)
adjusted_sequences = {
    'original': [x+1 for x in original_seq],
    'mutated': [x-1 for x in mutated_seq]
}
adjusted_distance = analyzer.mutation_distance(adjusted_sequences['original'], adjusted_sequences['mutated'])

# Final calculation combines both measurements with set operations on position weights
weight_keys_original = set(analyzer.position_weights.keys())
active_positions = frozenset(range(min(len(original_seq), len(mutated_seq))))
intersection_weights = sum(analyzer.position_weights[k] for k in weight_keys_original & active_positions)

final_distance = (initial_distance + adjusted_distance) // intersection_weights
print(f'Result: {final_distance}')