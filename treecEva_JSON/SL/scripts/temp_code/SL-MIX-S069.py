import re
from collections import namedtuple
from itertools import combinations

def calculate_motif_score(motif, pwm):
    score = 1.0
    for i, base in enumerate(motif):
        if base in pwm[i]:
            score *= pwm[i][base]
        else:
            score *= 0.01  # Background frequency for unknown bases
    return score

def find_regulatory_motifs(sequence, motifs_db):
    PositionWeightMatrix = namedtuple('PWM', ['positions'])
    
    # Define position weight matrix for motif recognition
    pwm_data = [
        {'A': 0.7, 'C': 0.1, 'G': 0.1, 'T': 0.1},
        {'A': 0.1, 'C': 0.7, 'G': 0.1, 'T': 0.1},
        {'A': 0.1, 'C': 0.1, 'G': 0.7, 'T': 0.1},
        {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.7}
    ]
    
    pwm = PositionWeightMatrix(pwm_data)
    
    # Find potential binding sites using regex
    binding_sites = []
    for motif_pattern in motifs_db:
        matches = re.finditer(motif_pattern, sequence)
        for match in matches:
            binding_sites.append((match.start(), match.group()))
    
    # Score each binding site
    scored_sites = []
    for start_pos, motif_seq in binding_sites:
        score = calculate_motif_score(motif_seq, pwm.positions)
        scored_sites.append((start_pos, motif_seq, score))
    
    # Apply positional weighting (sites closer to transcription start site get higher weights)
    tss_position = 50  # Transcription start site
    weighted_scores = []
    for start_pos, motif_seq, raw_score in scored_sites:
        distance = abs(start_pos - tss_position)
        positional_weight = max(0.1, 1.0 - (distance / 100.0))
        weighted_score = raw_score * positional_weight
        weighted_scores.append(weighted_score)
    
    # Calculate final score using combinatorial approach for cooperative binding
    final_score = 0.0
    for combo_size in range(1, min(3, len(weighted_scores) + 1)):
        for combo in combinations(weighted_scores, combo_size):
            combo_product = 1.0
            for score in combo:
                combo_product *= score
            final_score += combo_product if combo_size == 1 else combo_product * 0.5
    
    return final_score

# Test sequence from a promoter region
promoter_sequence = "ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG"

# Motif database patterns
motif_patterns = [r'[ACGT]{4}']

final_score = find_regulatory_motifs(promoter_sequence, motif_patterns)
print(f"Target result: {final_score}")