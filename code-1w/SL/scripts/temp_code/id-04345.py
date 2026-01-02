def calculate_final_score(scores, importance_weights):
    normalized = [score / 100 for score in scores]
    weighted = [n * w for n, w in zip(normalized, importance_weights)]
    total_weight = sum(importance_weights)
    return round(sum(weighted) / total_weight * 100, 3)

# Student assessment data
categories = ['homework', 'quiz', 'exam', 'project']
raw_scores = [85, 76, 92, 88]
weights = [0.1, 0.2, 0.4, 0.3]

# Irrelevant string processing (minimal distraction)
display_labels = [cat.title() + ':' for cat in categories if len(cat) > 4]
label_str = ' | '.join(display_labels)

final_score = calculate_final_score(raw_scores, weights)
print(f"Result: {final_score}")