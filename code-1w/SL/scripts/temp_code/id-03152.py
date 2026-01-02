def evaluate_performance(records):
    total_entries = len(records)
    valid_count = 0
    temp_sum = 0
    outlier_threshold = 100
    normalization_factor = 1.5
    
    # Irrelevant pre-processing: case conversion on string identifiers
    processed_ids = [record['id'].upper() for record in records if 'id' in record]
    id_lengths = [len(pid) for pid in processed_ids]
    avg_id_length = sum(id_lengths) / len(id_lengths) if id_lengths else 0
    
    # Actual logic begins: filter and compute score
    scores = []
    for record in records:
        value = record.get('value', 0)
        category = record.get('category', '')
        
        # Check for outliers
        if abs(value) > outlier_threshold:
            continue
            
        # Only process certain categories
        if category.lower() in ['critical', 'standard']:
            if value > 10:
                temp_sum += value * 0.8  # Weighted contribution
            else:
                temp_sum += value * 0.5
            valid_count += 1
            scores.append(value)
    
    # Secondary filtering: ignore bottom 20% of valid scores
    sorted_scores = sorted(scores)
    cutoff = max(1, int(0.2 * len(sorted_scores)))
    trimmed_scores = sorted_scores[cutoff:]
    
    # Distractor: unused helper computation
    def calculate_entropy(data):
        from math import log
        freq = {}
        for d in data:
            freq[d] = freq.get(d, 0) + 1
        entropy = 0
        for count in freq.values():
            p = count / len(data)
            entropy -= p * log(p)
        return entropy
    
    # Another distractor variable
    average_trimmed = sum(trimmed_scores) / len(trimmed_scores) if trimmed_scores else 0
    adjustment = len(processed_ids) * 0.1  # Unused adjustment factor
    
    # Final scoring with fixed formula
    base_score = sum(trimmed_scores)
    penalty = valid_count * 2
    final_score = (base_score - penalty) * normalization_factor
    
    return int(final_score)

# Input data
sample_data = [
    {'id': 'ax1', 'value': 15, 'category': 'critical'},
    {'id': 'by2', 'value': 5, 'category': 'standard'},
    {'id': 'cz3', 'value': 200, 'category': 'critical'},  # outlier
    {'id': 'dm4', 'value': 8, 'category': 'experimental'},  # wrong category
    {'id': 'er5', 'value': 12, 'category': 'standard'},
    {'id': 'ft6', 'value': 6, 'category': 'standard'}
]

result = evaluate_performance(sample_data)
print(f"Result: {result}")