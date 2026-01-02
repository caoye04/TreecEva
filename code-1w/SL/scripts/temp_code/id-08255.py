import itertools

def analyze_flow_components(matrix):
    # Irrelevant helper: computes submatrix sums (not used in final result)
    sub_sums = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i + j < 3:
                sub_sums.append(matrix[i][j] * 0.1)
    return [round(s, 3) for s in sub_sums]

def validate_thresholds(threshold_list):
    # Semi-relevant: checks validity but only returns a boolean used in conditional
    if not threshold_list:
        return False
    return all(0 <= t <= 100 for t in threshold_list)

def calculate_equilibrium(flow_data, limits):
    total_flux = 0
    adjustment_factor = 1.5
    decay_rate = 0.9
    temp_buffer = []

    # Simulate multi-step state evolution with filtering
    for row_idx, row in enumerate(flow_data):
        cumulative_row = 0
        for col_idx, val in enumerate(row):
            if row_idx == col_idx:
                cumulative_row += val ** 0.5
            elif val > limits[min(col_idx, len(limits) - 1)]:
                cumulative_row += val * 0.2
        total_flux += cumulative_row * decay_rate
        temp_buffer.append(cumulative_row)

    # Introduce auxiliary transformation (partially distractive)
    transformed = [x * adjustment_factor for x in temp_buffer if x > 5]
    secondary_sum = sum(transformed) / (len(transformed) or 1)

    # Core logic: count significant transitions across filtered combinations
    significant_pairs = 0
    for combo in itertools.combinations_with_replacement(range(len(flow_data)), 2):
        i, j = combo
        if i != j and abs(flow_data[i][j] - flow_data[j][i]) > limits[0]:
            significant_pairs += 1

    # Final score derived from both flux and symmetry analysis
    equilibrium_score = int(total_flux) + int(secondary_sum) - significant_pairs

    # Dead code path - never reached due to logic above
    if len(temp_buffer) > 100:
        equilibrium_score *= 2

    return equilibrium_score

# Main execution block
if __name__ == "__main__":
    # Input data
    flow_matrix = [
        [16, 20, 8],
        [12, 25, 30],
        [7, 18, 49]
    ]
    thresholds = [10, 20, 15]

    # Auxiliary computation - irrelevant to final answer
    component_analysis = analyze_flow_components(flow_matrix)
    is_valid = validate_thresholds(thresholds)

    # Key computational step
    equilibrium_score = calculate_equilibrium(flow_matrix, thresholds)

    # Print result as required
    print(f"Result: {equilibrium_score}")