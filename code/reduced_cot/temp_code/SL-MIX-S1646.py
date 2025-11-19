import re
from collections import defaultdict
from functools import reduce

def calculate_positional_weight(nucleotide_freq):
    weights = {'A': 1.2, 'T': 0.8, 'G': 1.5, 'C': 1.0}
    return sum(count * weights[nuc] for nuc, count in nucleotide_freq.items())

class SequenceAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
        self.nucleotide_count = defaultdict(int)
        self.metric_score = 0
    
    def process_sequence(self):
        # Step 1: Count nucleotides
        for nucleotide in self.sequence:
            if nucleotide in 'ATGC':
                self.nucleotide_count[nucleotide] += 1
        
        # Step 2: Pattern matching for special motifs
        motif_matches = len(re.findall(r'ATG(?:[ATGC]{3})+?(?=TAA|TAG|TGA)', self.sequence))
        
        # Step 3: Calculate base metric
        base_metric = calculate_positional_weight(self.nucleotide_count)
        
        # Step 4: Adjust for motifs
        if motif_matches > 0:
            self.metric_score = base_metric * (1 + motif_matches * 0.25)
        else:
            self.metric_score = base_metric
        
        # Step 5: Apply GC-content adjustment
        total_nucleotides = sum(self.nucleotide_count.values())
        gc_content = (self.nucleotide_count['G'] + self.nucleotide_count['C']) / total_nucleotides if total_nucleotides > 0 else 0
        
        if gc_content > 0.5:
            self.metric_score *= 1.3
        elif gc_content < 0.4:
            self.metric_score *= 0.85
        
        # Step 6: Final normalization
        self.metric_score = round(self.metric_score, 2)

# Initialize analyzer with sample DNA sequence
sample_dna = "ATGGCTAGCTAGCTAACGTACGTAGCTAGCTAATGACGTAGCTAGCTAA"
analyzer = SequenceAnalyzer(sample_dna)
analyzer.process_sequence()
print(f"Result: {analyzer.metric_score}")