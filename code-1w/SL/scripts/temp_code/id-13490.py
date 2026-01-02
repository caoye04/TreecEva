def calculate_final_score(entries, multiplier):
    base_scores = []
    adjustments = []
    temp_sum = 0

    for i, (rank, name) in enumerate(zip(entries, ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'])):
        score = (5 - rank) * 10
        adjustment = len(name) % 3
        base_scores.append(score)
        adjustments.append(adjustment)
        temp_sum += score

    filtered_ranks = [r for r in entries if r < 4]
    offset = sum([1 for x in adjustments if x > 0])

    # Irrelevant string processing (distractor)
    status_labels = ['High' if r < 2 else 'Low' for r in entries]
    label_count = {lbl: status_labels.count(lbl) for lbl in set(status_labels)}
    total_chars = sum(len(lbl) for lbl in status_labels)

    # Semi-relevant transformation
    weighted_bases = [bs * (adj + 1) for bs, adj in zip(base_scores, adjustments)]
    raw_total = sum(weighted_bases[:len(weighted_bases)//2 + 1])

    # Key computation hidden among distractions
    anomaly_detected = any(entries[i] == entries[i+1] for i in range(len(entries)-1))
    correction_factor = 0.9 if anomaly_detected else 1.0

    intermediate = raw_total * correction_factor
    final_value = int(intermediate * multiplier + offset)

    return final_value

# Main execution
rank_data = [1, 3, 2, 4, 5]
bonus_multiplier = 2.5

# Dead code path (distractor)
if len(rank_data) > 10:
    buffer = [0] * 10
    for idx in range(len(buffer)):
        buffer[idx] = idx * 2

# Unused variable assignment (distractor)
placeholder_summary = f"Processing {len(rank_data)} records with multiplier {bonus_multiplier}"

# Actual target computation
final_score = calculate_final_score(rank_data, bonus_multiplier)

print(f"Result: {final_score}")