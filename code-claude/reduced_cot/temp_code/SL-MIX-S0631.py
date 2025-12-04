# Function to find overlapping elements between two sequences
def analyze_datasets(primary, secondary):
    # Initialize counters
    match_count = 0
    position_sum = 0
    
    # Create a list to track overlap positions
    overlap_counts = []
    
    # Iterate through both sequences simultaneously with position tracking
    for i, (p_val, s_val) in enumerate(zip(primary, secondary)):
        # Check if elements match
        if p_val == s_val:
            match_count += 1
            # Store position where match occurred (1-indexed for domain convention)
            overlap_counts.append(i + 1)
    
    # Calculate sum of positions where overlaps occurred
    overlap_sum = sum(overlap_counts)
    
    # Calculate average position (not needed for final result)
    avg_position = overlap_sum / match_count if match_count > 0 else 0
    
    return overlap_sum, match_count, avg_position

# Sample datasets (DNA sequences represented as character lists)
primary_data = ['A', 'C', 'G', 'T', 'A', 'G', 'C', 'T']
secondary_data = ['A', 'T', 'G', 'T', 'C', 'G', 'C', 'A']

# Run analysis
overlap_sum, matches, avg_pos = analyze_datasets(primary_data, secondary_data)

print(f"Result: {overlap_sum}")