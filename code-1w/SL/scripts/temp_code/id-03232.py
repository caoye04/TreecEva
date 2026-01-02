def calculate_final_score(records, importance_weights):
    base_scores = [len(record['name']) * record['level'] for record in records]
    
    # Irrelevant computation: track max name length (not used in final score)
    max_name_length = max([len(r['name']) for r in records])
    temp_debug_info = {r['name']: len(r['name']) for r in records}

    # Semi-relevant transformation: normalize weights
    total_weight = sum(importance_weights.values())
    normalized_weights = {k: v / total_weight for k, v in importance_weights.items()}

    # Core logic: compute weighted contribution from level and active status
    level_sum = sum(r['level'] for r in records)
    active_bonus = sum(1 for r in records if r['active']) * 10
    
    # Distractor: unused complexity with zip and enumerate
    indexed_offsets = [i + len(name) for i, name in enumerate([r['name'] for r in records])]
    dummy_pairs = list(zip(base_scores, indexed_offsets))

    # Actual scoring using lambda to combine level sum and active bonus
    multiplier = (lambda x, y: x * 1.5 + y * 0.7)(level_sum, active_bonus)
    
    # Final score calculation
    final_score = int(multiplier + normalized_weights['bonus'])
    return final_score

# Data setup
data = [
    {'name': 'Alice', 'level': 5, 'active': True},
    {'name': 'Bob', 'level': 3, 'active': False},
    {'name': 'Charlie', 'level': 7, 'active': True},
    {'name': 'Diana', 'level': 4, 'active': True}
]

weights = {
    'bonus': 6.0,
    'penalty': 2.0,
    'extra': 1.0
}

# Execute main logic
final_score = calculate_final_score(data, weights)
print(f"Target result: {final_score}")