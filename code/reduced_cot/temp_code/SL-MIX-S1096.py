import heapq
import re

def calculate_motif_score(fragment):
    # Position weights for motif scoring
    position_weights = [1.2, 0.8, 1.5, 0.9, 1.1, 1.3, 0.7, 1.0]
    
    # Nucleotide base scores
    base_scores = {'A': 2, 'C': 3, 'G': 4, 'T': 1}
    
    # Apply position-weighted scoring
    weighted_scores = [
        base_scores[fragment[i]] * position_weights[i] 
        for i in range(min(len(fragment), len(position_weights)))
    ]
    
    # Create max heap (using negative values)
    heap = [-score for score in weighted_scores]
    heapq.heapify(heap)
    
    # Extract top 3 scores
    top_scores = []
    for _ in range(3):
        if heap:
            top_scores.append(-heapq.heappop(heap))
    
    # Calculate final score with lambda transformation
    transform = lambda x, y, z: (x * y + z) / 2.0
    
    # Short-circuit evaluation for boundary check
    if len(top_scores) >= 3 and top_scores[0] > 5.0:
        final_score = transform(top_scores[0], top_scores[1], top_scores[2])
    else:
        final_score = sum(top_scores) / len(top_scores) if top_scores else 0
    
    return final_score

# Encoded DNA fragment
encoded_fragment = "TCAGCTAG"

# Decode fragment using pattern matching
pattern = re.compile(r'([ACGT])(?=([ACGT]))?')
decoded_nucleotides = ''.join(match.group(1) for match in pattern.finditer(encoded_fragment))

# Calculate motif score
motif_rating = calculate_motif_score(decoded_nucleotides[:8])

print(f"Result: {int(motif_rating * 100)}")