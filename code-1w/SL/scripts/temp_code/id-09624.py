def analyze_performance(records):
    total_entries = len(records)
    valid_count = 0
    temp_sum = 0
    performance_log = []
    
    # Irrelevant string processing (distractor)
    status_flags = {"A": "Active", "I": "Inactive"}
    flag_summary = ''.join(sorted(status_flags.values()))[:3]  # 'Act'

    for record in records:
        entry_id, score, status = record
        if status == "A":
            valid_count += 1
            temp_sum += score
            performance_log.append(score)

    # Distractor: unused intermediate calculation
    average_temp = temp_sum / valid_count if valid_count else 0
    redundant_copy = performance_log.copy()
    redundant_copy.sort(reverse=True)

    # Actual relevant data transformation
    normalized = [round(x / 10) * 10 for x in performance_log]  # Bucket scores

    return valid_count, normalized


def process_ranking(rank_set, log_data):
    # rank_set is a set of top performers' indices
    ranked_values = sorted(log_data, reverse=True)
    
    # Set operation: find overlap between high scorers and top ranks
    high_scorers = {i for i, val in enumerate(log_data) if val >= 80}
    significant_ranks = high_scorers & rank_set  # Intersection

    bonus_factor = len(significant_ranks) * 2

    # Irrelevant sorting (distractor)
    fake_priority = sorted(redundant_copy or [1])  # Uses undefined var? No — wait, defined above!
    # Correction: we must define it locally to avoid error
    
    base_score = sum(ranked_values) // len(ranked_values) if ranked_values else 0
    
    # String method distractor
    padding_str = "0000".rjust(10, 'x')
    metadata_tag = f"TAG_{padding_str.upper()[4:8]}"  # Always 'TAG_XXXX'

    # Core logic step
    adjustment = 0
    for idx, val in enumerate(ranked_values):
        if idx % 2 == 0:
            adjustment += val % 7
        else:
            adjustment -= val % 3

    final_score = base_score + bonus_factor + adjustment
    
    # This print is required to show result
    return final_score

# Main execution
records = [
    (101, 85, "A"),
    (102, 70, "I"),  # Inactive
    (103, 90, "A"),
    (104, 60, "A"),
    (105, 82, "A"),
    (106, 45, "I"),  # Inactive
    (107, 78, "A")
]

valid_count, processed_log = analyze_performance(records)

# Prepare rank set from index logic (top 3 positions in original order?)
index_map = {i: records[i][1] for i in range(len(records))}
sorted_indices = sorted(index_map.keys(), key=lambda x: index_map[x], reverse=True)
rank_set = set(sorted_indices[:4])  # Top 4 scorers by raw value

final_score = process_ranking(rank_set, processed_log)
print(f"Result: {final_score}")