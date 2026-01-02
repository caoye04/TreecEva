import math

# Simulate a chemical equilibrium computation with red herrings
def main():
    # Initial concentration matrix for molecular species (relevant)
    concentration_matrix = [
        [1.0, 2.5, 3.0],
        [4.0, 5.2, 6.1],
        [7.3, 8.0, 9.5]
    ]

    # Irrelevant thermodynamic constants (distractor)
    thermodynamic_constants = {
        'R': 8.314,
        'T': 298.15,
        'F': 96485
    }

    # Misleading intermediate calculation (dead path)
    def compute_entropy(arr):
        return sum(math.log(x) if x > 0 else 0 for row in arr for x in row)

    entropy_value = compute_entropy(concentration_matrix)  # Computed but unused

    # Threshold function using lambda (required feature)
    threshold_func = lambda x: x > 5.0

    # Helper to normalize rows (semi-relevant preprocessing)
    def normalize_rows(matrix):
        return [[val / sum(row) for val in row] for row in matrix]

    normalized_concentrations = normalize_rows(concentration_matrix)

    # Dummy transformation on normalized data (distractor)
    amplified = [[val * 1.5 for val in row] for row in normalized_concentrations]
    clipped = [[min(val, 1.0) for val in row] for row in amplified]  # Not used later

    # Actual core logic disguised among noise
    def calculate_equilibrium(mat, thresh):
        # Extract diagonal elements using slicing (required feature)
        diagonals = [mat[i][i] for i in range(len(mat))]

        # Apply threshold filter via lambda
        active_diagonals = list(filter(thresh, diagonals))

        # Compute mean of active diagonal components
        mean_active = sum(active_diagonals) / len(active_diagonals) if active_diagonals else 0

        # Augment with set operation to remove duplicates (required feature)
        unique_off_diagonal = set()
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i != j:
                    rounded = round(mat[i][j], 1)
                    unique_off_diagonal.add(rounded)

        # Use set difference with irrelevant reference set (misdirection)
        reference_set = {1.0, 2.5, 3.0, 4.0, 5.2, 6.1, 7.3, 8.0}
        exclusive_vals = unique_off_diagonal - reference_set  # Computed but not used

        # Secondary distraction: count how many off-diagonal exceed mean diagonal
        above_mean_count = 0
        total_off_diag = 0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i != j:
                    total_off_diag += 1
                    if mat[i][j] > mean_active:
                        above_mean_count += 1

        # Final score combines active diagonal mean and structural factor
        structural_bias = len(diagonals) / (above_mean_count + 1)  # Dampened by count
        final_score = mean_active * structural_bias

        return final_score

    # Key statement
    equilibrium_score = calculate_equilibrium(concentration_matrix, threshold_func)

    # Print result as required
    print(f"Result: {equilibrium_score}")

if __name__ == "__main__":
    main()