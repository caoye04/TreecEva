from collections import defaultdict, Counter

# Simulate student test responses and scoring logic
def analyze_responses(responses):
    correct_count = 0
    total_questions = len(responses)
    category_breakdown = defaultdict(int)
    temporal_trend = []

    # Irrelevant time tracking (distractor)
    for i, entry in enumerate(responses):
        category_breakdown[entry['category']] += 1
        temporal_trend.append((i, entry['score']))  # Not used later

    # Misleading complexity with unused intermediate
    avg_per_category = {cat: 0 for cat in category_breakdown}
    for cat in category_breakdown:
        total_cat_score = sum(e['score'] for e in responses if e['category'] == cat)
        avg_per_category[cat] = total_cat_score / category_breakdown[cat]

    # Core logic: count correct answers above threshold
    for response in responses:
        if response['score'] >= 0.7:  # Passing threshold
            correct_count += 1

    return correct_count, total_questions

def calculate_final_score(raw_data):
    processed = [{'category': d[0], 'score': d[1]} for d in raw_data]
    
    # Red herring: character analysis from labels (unused)
    char_freq = Counter()
    for item in raw_data:
        for char in item[0].lower():
            if char.isalpha():
                char_freq[char] += 1
    
    # Secondary distraction: sorting with no impact
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    top_char = sorted_chars[0] if sorted_chars else None
    
    # Actual scoring logic
    correct, total = analyze_responses(processed)
    base_score = (correct / total) * 100 if total > 0 else 0
    
    # Apply adjustment based on distribution even if not needed
    counts = list(Counter([r[0] for r in raw_data]).values())
    variance_penalty = 0
    if len(counts) > 1:
        mean = sum(counts) / len(counts)
        variance_penalty = sum((x - mean) ** 2 for x in counts) / len(counts)
    
    adjusted_score = base_score - (variance_penalty * 2)  # Minor adjustment
    final_score = int(round(adjusted_score))
    
    return final_score

# Input data: (category, score)
data = [
    ('Algebra', 0.8), ('Geometry', 0.6), ('Algebra', 0.9), ('Calculus', 0.4),
    ('Geometry', 0.75), ('Algebra', 0.68), ('Calculus', 0.85), ('Geometry', 0.55),
    ('Algebra', 0.92), ('Calculus', 0.3), ('Geometry', 0.88), ('Algebra', 0.71)
]

# Execution point
final_score = calculate_final_score(data)
print(f"Result: {final_score}")