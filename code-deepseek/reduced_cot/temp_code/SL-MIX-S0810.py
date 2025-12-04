def analyze_network_connections(nodes):
    connection_matrix = [[i * j for j in range(1, 4)] for i in range(1, nodes + 1)]
    
    # Calculate potential connections (distractor)
    potential_links = sum(len(row) for row in connection_matrix)
    
    # Find valid bidirectional pairs using slicing
    valid_pairs = []
    for i in range(len(connection_matrix)):
        for j in range(i + 1, min(i + 3, len(connection_matrix))):
            if connection_matrix[i][0] + connection_matrix[j][-1] > 5:
                valid_pairs.append(connection_matrix[i][1] + connection_matrix[j][1])
    
    # Calculate adjustment factor (partially relevant)
    adjustment_factor = len([x for x in valid_pairs if x % 2 == 0])
    
    # Redundant computation that doesn't affect final result
    total_weight = sum(valid_pairs) * 0.5
    
    # Final computation
    final_count = valid_pairs[-1] + adjustment_factor
    
    print(f"Result: {final_count}")
    return final_count

# Execute with specific input
result = analyze_network_connections(4)