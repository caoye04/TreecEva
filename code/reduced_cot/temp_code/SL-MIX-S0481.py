import itertools
import math

def process_protein_sequence():
    # Amino acid molecular weights (g/mol)
    amino_weights = {
        'A': 89.09, 'R': 174.20, 'N': 132.12, 'D': 133.10,
        'C': 121.16, 'E': 147.13, 'Q': 146.15, 'G': 75.07,
        'H': 155.16, 'I': 131.17, 'L': 131.17, 'K': 146.19,
        'M': 149.21, 'F': 165.19, 'P': 115.13, 'S': 105.09,
        'T': 119.12, 'W': 204.23, 'Y': 181.19, 'V': 117.15
    }
    
    # Marker sequence for analysis
    marker = "MKQH"
    
    # Process 1: Create encoded sequence with positional adjustments
    encoded_seq = {i: math.floor(amino_weights[aa] * (i+1) * 100) for i, aa in enumerate(marker)}
    
    # Process 2: Apply sliding window transformation
    window_sums = {}
    for i in range(len(encoded_seq)):
        window_sum = 0
        for j in range(i, min(i+3, len(encoded_seq))):
            window_sum += encoded_seq[j]
        window_sums[i] = window_sum
    
    # Process 3: Find maximum window and apply special encoding
    max_window_index = max(window_sums, key=window_sums.get)
    if window_sums[max_window_index] > 50000:
        special_factor = 1.5
    else:
        special_factor = 1.2
    
    # Process 4: Generate combinations and calculate marker value
    marker_combinations = list(itertools.combinations(marker, 2))
    combination_weights = []
    
    for combo in marker_combinations:
        combo_weight = 0
        for aa in combo:
            combo_weight += amino_weights[aa]
        combination_weights.append(math.floor(combo_weight * 100))
    
    # Process 5: Calculate final marker value
    base_value = sum(combination_weights)
    adjusted_value = math.floor(base_value * special_factor)
    
    # Process 6: Apply final transformation with early return logic
    if adjusted_value % 2 == 0:
        final_marker_value = adjusted_value + (adjusted_value // 10)
    else:
        final_marker_value = adjusted_value - (adjusted_value // 7)
    
    # Process 7: Apply encoding correction
    correction_factor = len(str(final_marker_value))
    final_marker_value = final_marker_value * correction_factor
    
    return final_marker_value

final_marker_value = process_protein_sequence()
print(f"Result: {final_marker_value}")