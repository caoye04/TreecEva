def analyze_records(records):
    processed_data = []
    temp_sum = 0
    index_map = {}
    
    for i, record in enumerate(records):
        if len(record) < 3:
            continue
        
        value = record[1] * 2 + record[2]
        offset = record[0] % 4
        
        # Distractor: irrelevant computation
        dummy_calc = (value ** 2) % 17
        temp_sum += dummy_calc // 3
        
        if value > 50:
            processed_data.append(value - offset)
        else:
            processed_data.append(value + offset)
        
        index_map[i] = value

    # Another distractor: unused sorting
    sorted_indices = sorted(index_map.keys(), key=lambda x: index_map[x], reverse=True)
    fallback_list = [x for x in sorted_indices if index_map[x] > 30]

    return processed_data


def calculate_ranking(data):
    total = 0
    multiplier = 1
    intermediate_results = []
    
    for idx, val in enumerate(data):
        adjusted = val * (idx + 1)
        if adjusted > 100:
            adjusted = 100
        
        # Logical filtering with short-circuiting
        flag = (idx % 2 == 0) and (adjusted > 40 or val < 60)
        
        if flag:
            multiplier += 0.1
        
        intermediate_results.append(adjusted)

    # Use of zip: pair current with next
    paired_changes = []
    for curr, nxt in zip(intermediate_results, intermediate_results[1:]):
        change = nxt - curr
        if change > 0:
            paired_changes.append(change * multiplier)

    # Final accumulation
    base_score = sum(intermediate_results)
    bonus = sum(paired_changes)
    final_score = int(base_score + bonus - 45)  # deterministic rounding to integer
    
    # Dead code path - never executed due to logic above
    if len(paired_changes) > 100:
        final_score *= 2
        
    return final_score

# Main execution
records = [
    [1, 20, 15],
    [2, 30, 25],
    [5, 40, 30],
    [6, 55, 10],
    [9, 60, 20]
]

processed_data = analyze_records(records)
final_score = calculate_ranking(processed_data)
print(f"Target result: {final_score}")