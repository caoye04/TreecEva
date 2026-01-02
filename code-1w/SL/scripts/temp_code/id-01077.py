def calculate_final_score(entries, adj):
    base_total = 0
    bonus_points = 0
    penalty_count = 0
    temp_result = 0

    for entry in entries:
        stripped_entry = entry.strip().lower()
        if 'error' in stripped_entry:
            penalty_count += 1
            continue
        if 'critical' in stripped_entry:
            bonus_points += 5
        elif len(stripped_entry) > 10:
            bonus_points += 2
        
        digit_sum = sum(int(c) for c in stripped_entry if c.isdigit())
        base_total += digit_sum

    # Simulate some intermediate processing that doesn't affect final outcome
    outlier_buffer = []
    for i in range(3):
        outlier_buffer.append(penalty_count * (i + 1))

    # Irrelevant string transformation chain
    debug_info = "Processing complete"
    debug_info = debug_info.replace("complete", "finished")
    debug_info = debug_info.upper().split()[0]  # unused

    adjusted_total = base_total * adj
    if bonus_points > 10:
        adjusted_total += 10
    else:
        adjusted_total += bonus_points

    consistency_check = len(entries) - penalty_count
    if consistency_check < 3:
        adjusted_total -= 5

    final_score = int(adjusted_total)
    return final_score

# Main execution
raw_data = [' Entry1: 123 ', 'error_critical', 'Data45 with text', 'Simple7', 'Critical99']
adjustment_factor = 1.75

intermediate_stats = {}
intermediate_stats['count'] = len(raw_data)
intermediate_stats['avg_length'] = sum(len(s) for s in raw_data) / len(raw_data)

# Unused helper list
shadow_copy = [s[::-1] for s in raw_data]

final_score = calculate_final_score(raw_data, adjustment_factor)
print(f"Target result: {final_score}")