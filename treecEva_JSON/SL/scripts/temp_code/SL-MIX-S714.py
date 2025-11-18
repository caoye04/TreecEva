from math import log2, exp
from itertools import permutations
from functools import reduce

def sequence_analyzer(dna_seq):
    nucleotides = list(set(dna_seq))
    pattern_count = len(list(permutations(nucleotides, 2)))
    if pattern_count > 10:
        weight_factor = exp(log2(pattern_count))
    elif pattern_count > 5:
        weight_factor = exp(log2(pattern_count / 2))
    else:
        weight_factor = exp(log2(1))
    return int(weight_factor * len(dna_seq))

class GeneticSample:
    def __init__(self, sequence):
        self.sequence = sequence
        self.complexity_score = 0
    
    def calculate_score(self):
        match len(self.sequence):
            case n if n > 10:
                self.complexity_score = sequence_analyzer(self.sequence[:10])
            case n if n > 5:
                self.complexity_score = sequence_analyzer(self.sequence[:5])
            case _:
                self.complexity_score = sequence_analyzer(self.sequence)
        return self.complexity_score

dna_sample = GeneticSample("ATCGATCGATCG")
final_score = dna_sample.calculate_score()
print(f"Result: {final_score}")