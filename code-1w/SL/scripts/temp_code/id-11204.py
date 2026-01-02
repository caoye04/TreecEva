def process_rankings(ranks, people):
    total = 0
    bonus_flag = False
    temp_values = []
    
    # Preprocessing names: case conversion and filtering
    processed_names = [name.upper().replace(' ', '_') for name in people if len(name) > 4]
    valid_count = len(processed_names)

    # Use of enumerate and zip to align indices and values
    for i, (name, rank) in enumerate(zip(processed_names, [ranks[p] for p in people if len(p) > 4])):
        if i % 2 == 0:
            adjusted_rank = (rank ** 2) // (i + 1)
        else:
            adjusted_rank = rank + i

        # Simulate some irrelevant intermediate computation
        noise = len(name) * 3.14
        normalized_noise = round(noise, 2)
        temp_values.append(normalized_noise)  # Dead-end list, never used again

        # Core scoring logic
        if rank < 5:
            total += adjusted_rank * 2
            if 'A' in name:
                bonus_flag = True
        else:
            total -= adjusted_rank // 3

    # Set operation: find unique characters across high-performing candidates
    relevant_names = [p.upper().replace(' ', '_') for p in people if ranks[p] < 5]
    unique_chars = set(char for name in relevant_names for char in name)
    distinct_letters = len(unique_chars)

    # Final score adjustment with red herring variables
    scaling_factor = 1.5  # Not actually used
    offset = sum(ord(c) for c in unique_chars) % 7  # Distractor

    final_score = total + distinct_letters
    
    # Print result as required
    print(f"Result: {final_score}")
    return final_score

# Input data
candidate_list = ['Alice Johnson', 'Bob Smith', 'Carla Mendez', 'Dan Lee', 'Eva Rodriguez']
rank_map = {
    'Alice Johnson': 3,
    'Bob Smith': 6,
    'Carla Mendez': 2,
    'Dan Lee': 7,
    'Eva Rodriguez': 4
}

# Execution point
final_score = process_rankings(rank_map, candidate_list)