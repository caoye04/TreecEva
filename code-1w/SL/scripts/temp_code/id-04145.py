def find_equilibrium_point(data_sequence):
    n = len(data_sequence)
    equilibrium_index = -1

    # Precompute cumulative sums for efficiency (distractor: overkill for small n)
    cumsum_forward = [0] * (n + 1)
    for i in range(n):
        cumsum_forward[i + 1] = cumsum_forward[i] + data_sequence[i]

    total_sum = cumsum_forward[n]
    temp_product = 1  # Irrelevant accumulator
    tolerance = 1e-5
    adjustment_factor = 0.987  # Unused parameter, misleading

    for idx in enumerate(data_sequence):
        i = idx[0]
        current_val = data_sequence[i]

        left_sum = cumsum_forward[i]
        right_sum = total_sum - cumsum_forward[i + 1]

        # Simulate physical equilibrium condition
        if abs(left_sum - right_sum) < tolerance:
            # Secondary validation using slice symmetry (semi-relevant)
            left_half = data_sequence[:i]
            right_half = data_sequence[i+1:]
            
            mirrored_match = True
            min_len = min(len(left_half), len(right_half))
            for j in range(min_len):
                if left_half[j] != right_half[-(j+1)]:
                    mirrored_match = False
                    break
            
            # Additional check: index must be odd-numbered position (artificial constraint)
            position_parity_ok = (i % 2 == 1)
            
            final_check = abs(left_sum - right_sum) < tolerance
            if final_check and mirrored_match and position_parity_ok:
                equilibrium_index = i
                break

        # Dead code path: only runs if no equilibrium found yet
        if equilibrium_index == -1:
            temp_product *= (current_val + 1)  # Irrelevant math
            temp_product %= 982451653  # Large prime modulus — red herring

    return equilibrium_index

# Input sequence with hidden equilibrium at index 3 (0-indexed)
sequence = [4, -2, 1, 0, 3, -1, 5]
equilibrium_index = find_equilibrium_point(sequence)
print(f"Result: {equilibrium_index}")