def evaluate_performance(entries, threshold):
    # Initialize tracking variables
    valid_count = 0
    temp_sum = 0
    penalty_factor = 1.0
    intermediate_results = []
    
    # Misleading pre-processing: calculates average but not used in final logic
    total_entries = len(entries)
    dummy_avg = sum(e[1] for e in entries) / total_entries if total_entries else 0
    adjustment_offset = dummy_avg * 0.1
    
    # Real logic begins: filter and score based on dynamic conditions
    for i, (name, score, category) in enumerate(entries):
        if score < threshold:
            continue
            
        # Categorize performance level (irrelevant to final score but adds complexity)
        if score > 90:
            performance_level = 'Outstanding'
        elif score > 75:
            performance_level = 'Strong'
        else:
            performance_level = 'Adequate'
            
        # Track only relevant entries
        valid_count += 1
        temp_sum += score
        
        # Simulate complex state tracking with unused structure
        entry_data = {
            'idx': i,
            'name': name,
            'raw_score': score,
            'adjusted': score + adjustment_offset,
            'level': performance_level
        }
        intermediate_results.append(entry_data)

    # Secondary filtering using set operations (relevant step)
    top_names = {entry[0] for entry in entries if entry[1] >= threshold}
    bonus_names = {"Alice", "David", "Sophia"}
    eligible_for_bonus = top_names & bonus_names  # Intersection
    bonus_points = len(eligible_for_bonus) * 5

    # Use of zip to align indices with filtered data (meaningful usage)
    indexed_scores = [s[1] for s in entries if s[1] >= threshold]
    ranked_pairs = list(enumerate(zip(top_names, indexed_scores), start=1))
    
    # Final computation chain
    base_score = temp_sum + bonus_points
    decay_factor = 0.95 ** (valid_count - 1) if valid_count > 1 else 1.0
    final_score = int(base_score * decay_factor)  # Deterministic integer result

    # Dead code branch — never executed under current logic
    if False:
        debug_log = {'entries_processed': intermediate_results}
        send_alert(debug_log)

    return final_score

# Input data
rankings = [
    ("Alice", 88, "Engineering"),
    ("Bob", 70, "Marketing"), 
    ("Charlie", 92, "Engineering"),
    ("David", 85, "Sales"),
    ("Eve", 60, "Marketing"),
    ("Sophia", 78, "Engineering")
]
base_threshold = 75

# Key execution point
final_score = evaluate_performance(rankings, base_threshold)
print(f"Result: {final_score}")