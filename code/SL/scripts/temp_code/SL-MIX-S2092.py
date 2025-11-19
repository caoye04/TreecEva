import base64
from collections import namedtuple

def calculate_nucleotide_value(nucleotide, position):
    encoding_map = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    base_value = encoding_map.get(nucleotide, 0)
    return base_value * (position + 1)

def process_dna_sequence(sequence):
    total_score = 0
    codon_scores = {}
    
    for i in range(len(sequence)):
        nucleotide = sequence[i]
        value = calculate_nucleotide_value(nucleotide, i)
        
        # Short-circuit evaluation for stop codon detection
        if nucleotide == 'T' and i+1 < len(sequence) and sequence[i+1] == 'A' and i+2 < len(sequence) and sequence[i+2] == 'G':
            break
            
        total_score += value
        
        # Track codon scores
        codon_index = i // 3
        if codon_index not in codon_scores:
            codon_scores[codon_index] = 0
        codon_scores[codon_index] += value
    
    return total_score, codon_scores

def adjust_score_with_encoding(score_dict):
    adjustments = {}
    for codon_idx, score in score_dict.items():
        # Encoding transformation
        encoded = base64.b64encode(str(score).encode()).decode()
        # Decode and apply adjustment logic
        decoded = base64.b64decode(encoded).decode()
        adjustments[codon_idx] = int(decoded) * (-1 if codon_idx % 2 == 1 else 1)
    return adjustments

# Main execution
SequenceData = namedtuple('SequenceData', ['sequence', 'metadata'])
dna_data = SequenceData(
    sequence="ATGGCTAGTC",
    metadata={'source': 'human', 'length': 10}
)

total_score, codon_scores = process_dna_sequence(dna_data.sequence)
adjusted_scores = adjust_score_with_encoding(codon_scores)

final_score = total_score
for adj in adjusted_scores.values():
    final_score += adj

print(f"Result: {final_score}")