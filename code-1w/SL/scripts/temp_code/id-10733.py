import itertools

def transform_sequence(seq, factor):
    """Apply transformation with red herring operations."""
    shifted = [(x * factor + 2) % 100 for x in seq]
    inverted = [99 - x for x in shifted]  # Unused distraction
    return shifted  # Only shifted is used

def validate_thresholds(thresholds):
    """Check if thresholds are non-decreasing (distractor logic)."""
    for i in range(1, len(thresholds)):
        if thresholds[i] < thresholds[i-1]:
            return False
    return True  # Computed but not critical to final answer

def calculate_flow_contributions(matrix):
    """Calculate row-wise products as intermediate values."""
    contributions = []
    for row in matrix:
        product = 1
        for val in row:
            product *= max(val, 1)
        contributions.append(product)
    return contributions

def calculate_equilibrium(matrix, thresholds):
    """Compute equilibrium score based on threshold crossings and flow sums."""
    # Step 1: Compute sum of each row (relevant)
    row_sums = [sum(row) for row in matrix]
    
    # Step 2: Count how many elements exceed their corresponding threshold (semi-relevant)
    excess_count = 0
    for i, thresh in enumerate(thresholds):
        if i < len(matrix):
            excess_count += sum(1 for x in matrix[i] if x > thresh)
    
    # Step 3: Use itertools to generate index pairs for dummy correlation check
    indices = list(itertools.combinations(range(len(matrix)), 2))
    correlation_shadow = 0
    for i, j in indices:
        correlation_shadow += abs(row_sums[i] - row_sums[j])  # Distractor accumulation
    
    # Step 4: Actual logic - weighted combination of row sums and threshold excess
    base_score = sum(row_sums) // len(row_sums) if row_sums else 0
    adjustment = excess_count * 3
    
    # Step 5: Introduce case conversion via string op (seemingly out of place but deterministic)
    mode_flag = "ADAPTIVE" if adjustment > 10 else "STATIC"
    modifier = 1 if mode_flag.lower() == "adaptive" else -1
    
    # Final computation
    equilibrium_score = base_score + adjustment * modifier
    
    # Irrelevant debug print that doesn't affect result
    # print(f'Debug - shadow: {correlation_shadow}, valid: {validate_thresholds(thresholds)}')
    
    return equilibrium_score

# Main execution block
if __name__ == "__main__":
    # Input data
    raw_sequence = [7, 13, 21, 31]
    scaling_factor = 3
    processed_seq = transform_sequence(raw_sequence, scaling_factor)
    
    # Construct flow matrix using transformed sequence
    flow_matrix = [
        [processed_seq[0], 15, 8],
        [12, processed_seq[1], 25],
        [9, 18, processed_seq[2]],
        [processed_seq[3], 14, 20]
    ]
    
    # Thresholds for comparison
    thresholds = [20, 10, 25]
    
    # Validate thresholds (computation has no downstream effect)
    is_valid = validate_thresholds(thresholds)
    
    # Key statement
    equilibrium_score = calculate_equilibrium(flow_matrix, thresholds)
    
    # Print result
    print(f'Result: {equilibrium_score}')