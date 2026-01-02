def analyze_performance(records):
    # Irrelevant preprocessing: character frequency analysis in names
    char_freq = {}
    for record in records:
        for char in record['name']:
            char_freq[char] = char_freq.get(char, 0) + 1

    # Distractor: unused transformation of data
    transformed = list(map(lambda x: {**x, 'temp_id': ord(x['name'][0]) % 10}, records))

    # Relevant: extract scores and apply weighting logic
    raw_scores = []
    categories = []
    for idx, entry in enumerate(records):
        if entry['active']:
            raw_scores.append(entry['score'])
            categories.append(entry['category'])

    # Semi-relevant: count category occurrences (only one used later)
    category_count = {}
    for cat in categories:
        category_count[cat] = category_count.get(cat, 0) + 1
    primary_category_count = category_count.get('core', 0)  # Actually used

    # Distractor: complex but unused slicing pattern
    rolling_window = [raw_scores[i:i+3] for i in range(len(raw_scores)-2)]
    avg_windows = [sum(window)/3 for window in rolling_window]

    # Relevant: prepare totals using modular arithmetic on indices
    totals = []
    for i, s in enumerate(raw_scores):
        offset = (i * 7) % 5
        adjusted = s + offset
        totals.append(adjusted)

    # Relevant: weight based on position parity and magnitude
    weights = []
    for i, t in enumerate(totals):
        base_weight = 0.5 if i % 2 == 0 else 1.5
        bonus = 0.1 if t > 85 else 0.0
        weights.append(round(base_weight + bonus, 2))

    # Helper function defined inside (increases nesting)
    def compute_aggregate(values, wts):
        aggregate = 0.0
        for j, (v, w) in enumerate(zip(values, wts)):
            contribution = v * w
            # Misleading intermediate: cumulative product not used
            dummy_product = 1
            for k in range(1, j+2):
                dummy_product *= k
            aggregate += contribution
        return round(aggregate, 4)

    final_score = compute_aggregate(totals, weights)
    
    # Print result as required
    print(f"Result: {final_score}")
    
    # Return unused metrics to encourage distraction
    summary = {
        'char_freq': char_freq,
        'primary_category_count': primary_category_count,
        'window_averages': avg_windows
    }
    
    return final_score

# Input data
student_records = [
    {'name': 'Alice', 'score': 92, 'category': 'core', 'active': True},
    {'name': 'Bob', 'score': 78, 'category': 'elective', 'active': True},
    {'name': 'Charlie', 'score': 85, 'category': 'core', 'active': False},
    {'name': 'Diana', 'score': 96, 'category': 'core', 'active': True}
]

# Execute
analyze_performance(student_records)