from itertools import combinations

def process_genomic_data():
    dna_sequence = "ATGCGATCGTAGCTAG"
    nucleotide_weights = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    
    # Step 1: Compute base scores using list comprehension
    base_scores = [nucleotide_weights[nuc] for nuc in dna_sequence]
    
    # Step 2: Apply positional transformation using lambda
    transformed_scores = list(map(lambda x, i: x * (i % 3 + 1), base_scores, range(len(base_scores))))
    
    # Step 3: Filter scores based on a condition using short-circuit evaluation
    filtered_scores = [score for score in transformed_scores if score > 5 or (score <= 5 and score % 2 == 0)]
    
    # Step 4: Calculate pairwise products using itertools
    pairwise_products = [a * b for a, b in combinations(filtered_scores, 2)]
    
    # Step 5: String transformation to create metadata tag
    metadata_tag = ''.join([str(x) for x in filtered_scores[:3]])
    
    # Step 6: Final score calculation with conditional logic
    final_score = sum(pairwise_products)
    if len(metadata_tag) >= 6 and metadata_tag.startswith('6'):
        final_score += 100
    elif len(metadata_tag) < 6 or metadata_tag.endswith('4'):
        final_score -= 50
    
    return final_score

# Execution
final_score = process_genomic_data()
print(f"Result: {final_score}")