def evaluate_performance(log, thresh):
    total_entries = len(log)
    valid_count = 0
    temp_sum = 0.0
    outlier_count = 0
    normalized_scores = []

    for entry in log:
        stripped_entry = entry.strip()
        if not stripped_entry.isdigit():
            continue
        
        raw_value = int(stripped_entry)
        if raw_value < 0 or raw_value > 100:
            outlier_count += 1
            continue
            
        temp_sum += raw_value ** 0.5  # Distraction: not used later
        normalized_scores.append(raw_value / 100)
        
        if raw_value >= thresh:
            valid_count += 1

    # Irrelevant transformation
    adjusted_ratios = [round(x * x, 3) for x in normalized_scores if x > 0.5]
    adjustment_factor = sum(adjusted_ratios) if adjusted_ratios else 1.0

    # Dead computation path (no impact)
    hypothetical_max = 0
    for i in range(len(normalized_scores)):
        if i % 2 == 0:
            hypothetical_max += normalized_scores[i] * 2
        else:
            hypothetical_max += normalized_scores[i]

    # Actual logic branch: compute ratio of valid entries
    validity_ratio = valid_count / total_entries if total_entries > 0 else 0

    # Secondary metric (unused red herring)
    average_normalized = sum(normalized_scores) / len(normalized_scores) if normalized_scores else 0

    # Core result based on conditional logic
    if validity_ratio >= 0.6:
        base_score = 85
    elif validity_ratio >= 0.4:
        base_score = 65
    else:
        base_score = 40

    # Apply bonus only if certain conditions met
    bonus = 15 if len(adjusted_ratios) > 2 and adjustment_factor > 1.5 else 5
    
    # Final score calculation — this is the key output
    final_score = base_score + bonus

    return int(final_score)

# Simulated input data with noise
accuracy_log = ['92', ' 87 ', 'abc', '76', '105', '88', '73', '90', '!!', '85']
threshold = 75

# Execution point of interest
temp_sum = 0
for item in accuracy_log:
    if item.strip().isdigit():
        temp_sum += int(item.strip()) % 10

final_score = evaluate_performance(accuracy_log, threshold)
print(f"Result: {final_score}")