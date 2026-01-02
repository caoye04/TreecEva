from collections import defaultdict

# Simulate student assessment results with category-based scoring
def process_results(data):
    category_totals = defaultdict(int)
    category_count = defaultdict(int)

    for entry in data:
        cat = entry['category']
        score = entry['score']
        category_totals[cat] += score
        category_count[cat] += 1

    # Calculate average per category, apply bonus if avg >= 85
    adjusted_averages = {}
    for cat in category_totals:
        avg = category_totals[cat] / category_count[cat]
        adjusted_averages[cat] = avg + (5 if avg >= 85 else 0)

    # Compute overall performance with weighted contribution
    weights = {'math': 0.4, 'science': 0.35, 'literature': 0.25}
    composite = sum(adjusted_averages[c] * weights[c] for c in adjusted_averages)

    # Final nonlinear adjustment based on performance threshold
    final = int(composite) if composite < 90 else int(composite * 1.1)

    # Irrelevant tracking variable (minimal interference)
    debug_log = f'Processed {len(category_totals)} categories'

    return final

# Input data
assessment_data = [
    {'category': 'math', 'score': 90},
    {'category': 'math', 'score': 87},
    {'category': 'science', 'score': 82},
    {'category': 'science', 'score': 88},
    {'category': 'literature', 'score': 95},
    {'category': 'literature', 'score': 89}
]

final_score = process_results(assessment_data)
print(f"Result: {final_score}")