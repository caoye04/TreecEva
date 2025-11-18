import itertools
import statistics

def calculate_hash_distance(word1, word2):
    return abs(hash(word1) - hash(word2)) % 1000

def compute_semantic_coherence(word_groups):
    total_distances = []
    for group in word_groups:
        pairwise_distances = []
        # Generate all 2-combinations within each group
        for combo in itertools.combinations(group, 2):
            dist = calculate_hash_distance(combo[0], combo[1])
            pairwise_distances.append(dist)
        if pairwise_distances:
            # Compute mean distance for the group
            mean_dist = statistics.mean(pairwise_distances)
            total_distances.append(mean_dist)
    
    if not total_distances:
        return 0
    # Return the variance of all group means
    return statistics.variance(total_distances) if len(total_distances) > 1 else 0

# Ancient text word groups
ancient_vocabulary = [
    ['solar', 'lunar', 'stellar'],
    ['river', 'mountain', 'forest', 'ocean'],
    ['scribe', 'papyrus', 'ink', 'tablet', 'glyph']
]

final_coherence_score = compute_semantic_coherence(ancient_vocabulary)
print(f"Result: {final_coherence_score}")