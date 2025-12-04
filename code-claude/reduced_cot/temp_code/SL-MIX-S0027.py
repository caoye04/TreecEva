import itertools

# DNA analysis for genetic research
def analyze_genetic_markers(sample_a, sample_b):
    # Extract genetic markers from samples
    markers_a = set(sample_a)
    markers_b = set(sample_b)
    
    # Calculate potential mutation sites
    potential_mutations = len(markers_a.symmetric_difference(markers_b))
    
    # Find common genetic markers
    common_genes = markers_a.intersection(markers_b)
    overlap_size = len(common_genes)
    
    # Calculate mutation ratio (not used in final result)
    mutation_ratio = potential_mutations / (len(markers_a) + len(markers_b)) if markers_a or markers_b else 0
    
    # Calculate stability score based on common genes
    stability_score = sum(ord(gene[0]) % 10 for gene in common_genes)
    
    # Record pairs of common genes for further analysis
    gene_pairs = list(itertools.combinations(sorted(common_genes), 2)) if len(common_genes) >= 2 else []
    gene_pair_count = len(gene_pairs)
    
    return overlap_size, stability_score, gene_pair_count

# Sample genetic markers
sample1 = ['ACT', 'GTC', 'CAG', 'TAC', 'AGG']
sample2 = ['GTC', 'CAG', 'ATC', 'GTA', 'ACT']

# Analyze control samples for baseline
control_overlap, control_stability, control_pairs = analyze_genetic_markers(['GTC', 'TAC'], ['GTC', 'CAG'])

# Process experimental samples
overlap_size, stability, pairs = analyze_genetic_markers(sample1, sample2)

# Calculate weighted genetic similarity index
weighted_index = overlap_size * 2 - control_overlap

print(f"Target result: {overlap_size}")