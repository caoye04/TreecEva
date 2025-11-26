def process_network_data(primary_nodes, secondary_nodes, threshold):
    # Relevant logic: Count valid node pairs and calculate weighted sum
    valid_pairs = []
    for i, primary in enumerate(primary_nodes):
        for j, secondary in enumerate(secondary_nodes):
            if primary > secondary and (primary + secondary) % threshold == 0:
                valid_pairs.append((i, j, primary * secondary))
    
    # Distractor: Unused computation with misleading operations
    misleading_sum = sum(primary_nodes) * len(secondary_nodes) - threshold ** 2
    dead_code_path = misleading_sum // 3 if misleading_sum > 100 else misleading_sum * 2
    
    # Relevant: Calculate weighted sum of valid pairs
    weighted_sum = 0
    for idx, (p_idx, s_idx, product) in enumerate(valid_pairs):
        weight = (p_idx + s_idx) % 4
        weighted_sum += product * (weight + 1)
    
    # More distractors: Irrelevant operations on copied data
    temp_nodes = primary_nodes.copy()
    temp_nodes.reverse()
    irrelevant_max = max(temp_nodes) if temp_nodes else 0
    fake_accumulator = sum(x * 2 for x in temp_nodes[:3])
    
    # Final relevant computation
    final_value = weighted_sum - (len(valid_pairs) * threshold)
    return final_value

# Main execution with mixed relevant and irrelevant data
primary_nodes = [12, 8, 15, 6, 20]
secondary_nodes = [4, 10, 3, 9, 5]
threshold = 7

# Irrelevant variable assignments
backup_threshold = threshold + 5
redundant_nodes = [x + 2 for x in primary_nodes]
dummy_operation = backup_threshold * len(redundant_nodes) // 2

# Key computation
final_computation = process_network_data(primary_nodes, secondary_nodes, threshold)

# Final output
print(f"Result: {final_computation}")