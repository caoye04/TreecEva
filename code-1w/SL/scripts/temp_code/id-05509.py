def calculate_final_score(data, multiplier):
    base_scores = [d['rank'] ** 2 for d in data]
    offsets = [hash(d['name']) % 100 for d in data]  # Irrelevant distraction
    adjusted_scores = []
    total_offset = sum(offsets)  # Dead computation - not used later

    threshold = 50
    for score in base_scores:
        if score > threshold:
            adjusted_scores.append(score * 0.9)
        else:
            adjusted_scores.append(score * 1.1)

    # Semi-relevant transformation
    normalized = [s / max(adjusted_scores) * 100 for s in adjusted_scores]
    avg_normalized = sum(normalized) / len(normalized)

    # Actual key logic
    raw_sum = sum(adjusted_scores)
    final_score = int(raw_sum * multiplier)

    # Distractor variables
    temp_result = ''.join([d['name'][0] for d in data]).upper()
    validation_check = len(temp_result) > 3 and avg_normalized > 40

    return final_score

# Main execution
player_data = [
    {'name': 'Alice', 'rank': 7},
    {'name': 'Bob', 'rank': 5},
    {'name': 'Charlie', 'rank': 8}
]
bonus_multiplier = 1.25

# Unused helper function (dead code path)
def debug_print_structure(obj):
    for k, v in obj.items():
        print(f'{k}: {len(str(v))}')

# Unused variable
system_timestamp = hash('init_2024') % 10000

final_score = calculate_final_score(player_data, bonus_multiplier)
print(f'Result: {final_score}')