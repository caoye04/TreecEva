def calculate_load_distribution():
    weights = [120, 150, 135, 160, 175, 142, 138, 168]
    categories = ['A', 'B', 'C', 'B', 'A', 'C', 'B', 'A']
    
    # Irrelevant metadata (distractor)
    metadata = {'version': '1.2', 'author': 'engineer_x'}
    temp_buffer = [0] * len(weights)
    
    # Compute average for threshold
    avg_weight = sum(weights) / len(weights)
    
    # Identify indices where category is 'B' and weight above average
    selected_indices = []
    for i, (w, c) in enumerate(zip(weights, categories)):
        if c == 'B' and w > avg_weight:
            selected_indices.append(i)
    
    # Extract weights using slicing and filtering
    candidate_weights = weights[1:7]  # Slice to limit scope
    filtered_weights = [weights[i] for i in selected_indices if i < len(weights)]
    
    # Final computation
    total_weight = sum(filtered_weights)
    print(f"Result: {total_weight}")

calculate_load_distribution()