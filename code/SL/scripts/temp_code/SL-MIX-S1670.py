from functools import reduce

def hash_codon(codon):
    return sum(ord(nucleotide) * (3 ** i) for i, nucleotide in enumerate(codon))

def get_codon_scores(dna_fragment):
    codon_scores = {}
    for i in range(len(dna_fragment) - 2):
        codon = dna_fragment[i:i+3]
        if codon not in codon_scores:
            codon_hash = hash_codon(codon)
            score = (codon_hash % 10) + 1
            codon_scores[codon] = score
    return codon_scores

def max_non_overlapping_score(dna_fragment, codon_scores):
    n = len(dna_fragment)
    if n < 3:
        return 0
    
    dp = [0] * (n + 1)
    for i in range(3, n + 1):
        codon = dna_fragment[i-3:i]
        score = codon_scores.get(codon, 0)
        dp[i] = max(dp[i-1], dp[i-3] + score if i >= 3 else 0)
    return dp[n]

def process_dna_fragments(fragments):
    results = {}
    for fragment_id, fragment in fragments.items():
        scores = get_codon_scores(fragment)
        max_score = max_non_overlapping_score(fragment, scores)
        results[fragment_id] = max_score
    return results

def main():
    dna_fragments = {
        "FRAG_ALPHA": "ATGCGTACGTAGCTAG",
        "FRAG_BETA": "TTGCTAGCTAGCTAGCTAG",
        "FRAG_GAMMA": "ATGATGATGATGATG"
    }
    
    # Process fragments and collect scores
    fragment_scores = process_dna_fragments(dna_fragments)
    
    # Find the highest score among all fragments using functional programming
    highest_score = reduce(lambda x, y: x if x > y else y, fragment_scores.values())
    
    # Filter fragments with scores above a threshold using another functional approach
    high_scoring_fragments = {k: v for k, v in fragment_scores.items() if v > 7}
    
    # Calculate a final metric based on high-scoring fragments
    total_high_score = sum(high_scoring_fragments.values())
    
    # Determine if the highest individual score is from a fragment with above-average performance
    avg_score = sum(fragment_scores.values()) / len(fragment_scores)
    top_fragment = max(fragment_scores, key=fragment_scores.get)
    is_top_above_avg = fragment_scores[top_fragment] > avg_score
    
    # Final calculation combining multiple logical conditions
    final_metric = total_high_score + (10 if is_top_above_avg and len(high_scoring_fragments) >= 2 else 0)
    
    print(f"Result: {final_metric}")

if __name__ == "__main__":
    main()
