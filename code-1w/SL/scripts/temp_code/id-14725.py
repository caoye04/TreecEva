def calculate_final_score(records, importance_weights):
    base_scores = []
    temp_offsets = []
    for record in records:
        raw_value = sum(ord(c) for c in record['name']) % 100
        adjustment = len(record['tags']) * 3.5 if 'priority' in record['tags'] else 0
        base_scores.append(raw_value + adjustment)
        
        # Distractor: irrelevant computation with no effect on final result
        reverse_name = record['name'][::-1]
        vowel_count = sum(1 for c in reverse_name.lower() if c in 'aeiou')
        temp_offsets.append(vowel_count ** 2)

    weighted_sum = 0
    max_base = max(base_scores)
    normalized = [score / max_base for score in base_scores]

    # Another distractor: dead code path (never executed due to fixed condition)
    debug_mode = False
    if debug_mode:
        print('Debug info:', temp_offsets)

    # Real computation
    for i, norm_val in enumerate(normalized):
        weight = importance_weights[i] if i < len(importance_weights) else 1.0
        weighted_sum += norm_val * weight

    # Use of set operation (required python feature): count unique tag types
    all_tags = set()
    for record in records:
        all_tags.update(record['tags'])
    tag_diversity_bonus = len(all_tags) * 0.25

    # Final score calculation
    final_score = weighted_sum + tag_diversity_bonus

    # Additional distractor: meaningless string manipulation
    metadata_str = "Summary:" + ''.join(sorted(all_tags, key=str.lower))
    padded_result = f"{final_score:.4f}".ljust(10, '0')

    return final_score

# Main execution
data_set = [
    {'name': 'Alice', 'tags': ['staff', 'priority', 'active']},
    {'name': 'Bob', 'tags': ['contractor', 'inactive']},
    {'name': 'Charlie', 'tags': ['staff', 'active']},
    {'name': 'Diana', 'tags': ['priority', 'active']}
]
weights = [1.2, 0.8, 1.0, 1.5]

intermediate_total = sum(len(item['name']) for item in data_set)
dummy_list = [x for x in range(10) if x % 2 == 0]  # List comprehension (required feature)

final_score = calculate_final_score(data_set, weights)
print(f"Result: {final_score}")