def calculate_final_score(data):
    # Preprocessing: extract ranks and normalize
    normalized_ranks = [max(0, min(x, 100)) for x in data if isinstance(x, int)]
    
    # Irrelevant transformation: reverse and scale (not used in final logic)
    reversed_scaled = [round((100 - x) * 1.5) for x in normalized_ranks]
    temp_result = sum(reversed_scaled) // len(reversed_scaled) if reversed_scaled else 0

    # Core logic begins
    filtered_ranks = list(filter(lambda x: x > 50, normalized_ranks))
    if not filtered_ranks:
        return -1
    
    # Compute weighted contributions
    weights = [i + 1 for i in range(len(filtered_ranks))]
    weighted_sum = sum(w * r for w, r in zip(weights, filtered_ranks))
    total_weight = sum(weights)
    
    # Secondary adjustment based on count
    adjustment_factor = len(filtered_ranks) ** 0.5
    raw_score = weighted_sum / total_weight if total_weight else 0
    
    # Distractor: complex string operation with no impact
    status_msg = "Processing complete".upper().replace(" ", "_")
    log_entry = f"[LOG] {status_msg}: {len(normalized_ranks)} entries"
    debug_flag = len(log_entry) > 20

    # Final computation
    final_score = int(raw_score + adjustment_factor) * (2 if debug_flag else 1)
    return final_score

# Input data with mixed types and outliers
data_input = [75, 88, 'N/A', 42, 91, 67, None, 58, 95]

# Key execution point
rank_data = [x if isinstance(x, int) else 0 for x in data_input]
final_score = calculate_final_score(rank_data)
print(f"Result: {final_score}")