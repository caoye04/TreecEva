from collections import defaultdict

def calculate_segment_scores(segment):
    nucleotide_weights = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    correction_factors = defaultdict(lambda: 1.0, {'AA': 1.5, 'TT': 1.2, 'GG': 1.3, 'CC': 1.4})
    
    if len(segment) == 0:
        return 0
    
    if len(segment) == 1:
        return nucleotide_weights.get(segment[0], 0)
    
    mid = len(segment) // 2
    left_score = calculate_segment_scores(segment[:mid])
    right_score = calculate_segment_scores(segment[mid:])
    
    # Correction for boundary
    boundary_pair = segment[mid-1:mid+1]
    correction = correction_factors[''.join(boundary_pair)] if len(boundary_pair) == 2 else 1.0
    
    total = (left_score + right_score) * correction
    return total

def adjust_for_anomalies(score_sequence):
    adjustments = []
    for i, s in enumerate(score_sequence):
        if i > 0 and s > score_sequence[i-1]:
            adjustments.append(s * 1.1)
        elif i > 0 and s <= score_sequence[i-1]:
            adjustments.append(s * 0.95)
        else:
            adjustments.append(s)
    return adjustments

# Main processing
sequences = ['ATGCTAGCTA', 'GCTAGCTAGC', 'TAGCTAGCT']
scores = []
for seq in sequences:
    raw_score = calculate_segment_scores(list(seq))
    scores.append(raw_score)

adjusted_scores = adjust_for_anomalies(scores)
final_stability_score = sum(adjusted_scores)
print(f"Result: {int(final_stability_score)}")