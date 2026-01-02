import math

# Simulated bioinformatics data analysis pipeline with irrelevant transformations
def preprocess_genomic_data(raw_data):
    normalized = [x / max(raw_data) for x in raw_data]
    z_scores = [(x - sum(normalized)/len(normalized)) for x in normalized]
    filtered = [x for x in z_scores if x > 0.1]  # Irrelevant filtering
    return [math.log(x + 1e-5) for x in filtered]

# Distractor function - never called
def analyze_mutation_rate(sequence):
    mutations = 0
    for i in range(len(sequence) - 1):
        if sequence[i] != sequence[i+1]:
            mutations += 0.3
    return mutations * 1.7

# Real computation chain disguised among red herrings
def transform_expression_levels(expr_data):
    base_adjusted = [x + 2.0 for x in expr_data]
    powered = [math.pow(x, 1.5) for x in base_adjusted]
    capped = [min(x, 25.0) for x in powered]
    return capped

# Decoy statistical model
def fit_gaussian_model(samples):
    mean = sum(samples) / len(samples)
    variance = sum((x - mean)**2 for x in samples) / len(samples)
    return (mean, math.sqrt(variance))

# Core weighting logic buried in complexity
def apply_weight_scheme(values, weight_vector):
    weighted_vals = []
    temp_accum = 0.0
    
    for i in range(len(values)):
        if i % 2 == 0:
            temp_accum += values[i] * weight_vector[i % len(weight_vector)]
        else:
            temp_accum -= values[i] * 0.1
        
        if temp_accum > 10:  # Early reset - misleading path
            temp_accum = 5
    
        weighted_vals.append(temp_accum)
    
    # Final transformation only used here
    return [x * 1.1 for x in weighted_vals]

# Set operations used meaningfully but with distraction
def integrate_pathway_data(gene_sets):
    union_all = set().union(*gene_sets)
    intersections = []
    for i in range(len(gene_sets)-1):
        inter = set(gene_sets[i]) & set(gene_sets[i+1])
        intersections.append(inter)
    
    # Irrelevant diagnostic output
    sizes = [len(s) for s in intersections]
    avg_size = sum(sizes) / len(sizes) if sizes else 0
    
    # Only this line matters
    return len(union_all)

# Main scoring logic with multiple layers
def calculate_final_score(dataset, weights):
    # Step 1: Transform data through multiple irrelevant stages
    processed = transform_expression_levels(dataset)
    
    # Step 2: Apply weights with side effects
    applied = apply_weight_scheme(processed, weights)
    
    # Step 3: Use set logic on derived indices (distractor)
    high_indices = {i for i, v in enumerate(applied) if v > 8.0}
    mid_indices = {i for i, v in enumerate(applied) if 4.0 <= v <= 8.0}
    low_indices = {i for i, v in enumerate(applied) if v < 4.0}
    
    # Step 4: Compute score using only specific subset
    focus_group = high_indices | mid_indices  # Union
    focus_values = [applied[i] for i in sorted(focus_group)]
    
    # Step 5: Final calculation
    base_score = sum(focus_values)
    penalty = len(low_indices) * 1.5
    bonus = math.sqrt(len(high_indices)) if high_indices else 0
    
    # The actual answer
    final = base_score - penalty + bonus
    
    # Dead code path - never reached
    if final < 0:
        final = abs(final)
    
    return final

# Simulated input data
if __name__ == "__main__":
    # Primary dataset
    data_set = [1.2, 3.4, 2.1, 5.6, 4.3, 3.9]
    
    # Weight vector
    weights = [0.8, 1.2, 0.9]
    
    # Irrelevant genomic sequences
    genome_seq_1 = [0.1, 0.3, 0.4, 0.3, 0.1]
    genome_seq_2 = [0.2, 0.2, 0.5, 0.6, 0.1]
    
    # Unused intermediate variables (red herrings)
    norm_seq_1 = preprocess_genomic_data(genome_seq_1)
    norm_seq_2 = preprocess_genomic_data(genome_seq_2)
    fit_result = fit_gaussian_model(norm_seq_1)
    
    # Gene sets for pathway analysis (partially distracting)
    pathways = [
        ['geneA', 'geneB', 'geneC'],
        ['geneB', 'geneD', 'geneE'],
        ['geneC', 'geneE', 'geneF']
    ]
    
    # This call drives the real computation
    final_score = calculate_final_score(data_set, weights)
    
    # Output result as required
    print(f"Result: {final_score}")