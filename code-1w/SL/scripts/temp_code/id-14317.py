import math

# Irrelevant helper function (decoy)
def calculate_entropy(sequence):
    freq_map = {}
    for c in sequence:
        freq_map[c] = freq_map.get(c, 0) + 1
    entropy = 0.0
    total = len(sequence)
    for count in freq_map.values():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

# Unused transformation map (red herring)
nucleotide_weights = {'A': 1.0, 'T': 1.2, 'G': 1.5, 'C': 1.7, 'N': 0.0}

# Distractor: complex but unused scoring matrix
codon_matrix = [[(i * j + 1) % 7 for j in range(5)] for i in range(5)]

# Real processing begins here
patterns = ['ATG', 'TAA', 'TAG', 'TGA']
raw_data = 'GGCATGTTAAGCTAGCCCGATCGATGACGTAG'

# Misleading pre-scan with early break (dead path)
def preliminary_scan(seq, stops):
    count = 0
    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon in stops:
            if count > 2:
                return True
            break  # Early break makes rest of loop irrelevant
        count += 1
    return False

# Heavily distractor-laden but correct processing function
def process_biosequence(seq, stop_codons):
    length = len(seq)
    reverse_seq = seq[::-1]
    
    # Distractor: unused palindrome check
    is_palindrome = seq == reverse_seq
    
    # Irrelevant statistical measures
    base_count = {b: seq.count(b) for b in 'ATGC'}
    gc_content = (base_count['G'] + base_count['C']) / length
    
    # Real logic starts: find all stop codon positions
    stop_indices = []
    for i in range(len(seq) - 2):
        triplet = seq[i:i+3]
        if triplet in stop_codons:
            stop_indices.append(i)
    
    # Distractor: lambda that's referenced but not impactful
    adjust_score = lambda x, m: x * 1.1 if m > 0.5 else x * 0.9
    
    # Real scoring logic
    raw_score = 0
    for idx in stop_indices:
        # Weight by position: earlier stops penalized more
        positional_weight = 1 - (idx / length)
        raw_score += int(100 * positional_weight)
    
    # Distractor: conditional expression with no effect
    status_flag = 'valid' if len(stop_indices) >= 3 else 'review'
    status_flag = 'final' if gc_content > 0.4 else status_flag  # Overwritten
    
    # Key computation hidden among noise
    filter_threshold = 50
    adjustment_factor = 0.85
    
    # Critical statement with actual answer derivation
    filtration_score = int(raw_score * adjustment_factor)  # <-- Target variable
    
    # Dead code path (never reached due to unconditional prior assignment)
    if filtration_score < 0:
        fallback_map = {k: v**2 for k, v in base_count.items()}
        filtration_score = sum(fallback_map.values())
    
    return filtration_score

# Execution point of interest
filtration_score = process_biosequence(raw_data, patterns)

# Print result as required
print(f"Result: {filtration_score}")