def calculate_final_score(entries, importance_weights):
    total = 0
    bonus = 10
    penalty = 5
    temp_result = []
    
    # Preprocess entries by cleaning string data
    cleaned_entries = [entry.strip().lower() for entry in entries]
    
    # Misleading computation: this is never used
    avg_length = sum(len(e) for e in cleaned_entries) / len(cleaned_entries) if cleaned_entries else 0
    redundant_sum = sum([len(e) for e in cleaned_entries]) * 2  # Distractor
    
    # Extract numeric scores from strings like 'score: 85'
    raw_scores = []
    for item in cleaned_entries:
        if 'score:' in item:
            try:
                score_val = int(item.split('score:')[-1].strip())
                raw_scores.append(score_val)
            except ValueError:
                continue

    # Weighted accumulation with early termination condition
    weighted_sum = 0
    for i in range(min(len(raw_scores), len(importance_weights))):
        if raw_scores[i] < 50:  # Poor performance cutoff
            break
        weighted_sum += raw_scores[i] * importance_weights[i]
    
    # Secondary adjustment based on data characteristics
    if len(raw_scores) >= 3:
        adjustment = (raw_scores[0] + raw_scores[-1]) // 4
    else:
        adjustment = 0
    
    # Final aggregation
    total = weighted_sum + adjustment + bonus  # Penalty is defined but not used
    
    # Irrelevant string manipulation - red herring
    status_labels = ['pass', 'fail', 'retry']
    status_map = {i: label.upper() for i, label in enumerate(status_labels)}
    
    return total

# Input data
data = [
    "  Score: 90 ",
    "score: 85",
    "comment: excellent work", 
    "score: 74",
    "score: 45"  # This will cause loop break due to <50
]
weights = [0.5, 1.0, 1.5, 2.0]

# Execute calculation
final_score = calculate_final_score(data, weights)
print(f"Result: {final_score}")