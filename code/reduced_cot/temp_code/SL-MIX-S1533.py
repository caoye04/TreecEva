import statistics

class DNATokenizer:
    def __init__(self, sequence):
        self.sequence = sequence
    
    def __enter__(self):
        self.codons = [self.sequence[i:i+3] for i in range(0, len(self.sequence), 3) if len(self.sequence[i:i+3]) == 3]
        return self.codons
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

def calculate_mutation_score(codon):
    # Convert each character to its ASCII value and XOR them
    ascii_values = [ord(c) for c in codon]
    xor_result = ascii_values[0]
    for val in ascii_values[1:]:
        xor_result ^= val
    return xor_result

# DNA sequence for analysis
sequence = "ATGCGTACGTAGCTAG"

# Process the sequence using context manager
with DNATokenizer(sequence) as codons:
    # Calculate mutation scores for each codon
    scores = [calculate_mutation_score(codon) for codon in codons]
    
    # Apply bitwise AND with mask 0xF0 to each score
    masked_scores = [score & 0xF0 for score in scores]
    
    # Compute mean of masked scores
    mean_masked = statistics.mean(masked_scores)
    
    # Find codons with scores above mean
    high_scores = [score for score in masked_scores if score > mean_masked]
    
    # Calculate final score: sum of high scores shifted right by 2 bits
    final_score = sum(high_scores) >> 2

print(f"Result: {final_score}")