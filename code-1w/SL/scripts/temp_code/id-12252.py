def calculate_final_score(scores, importance_weights):
    normalized = [score / 100 for score in scores]
    weighted_values = [n * w for n, w in zip(normalized, importance_weights)]
    return int(sum(weighted_values) * 100)

# Student performance data
categories = ('homework', 'quiz', 'exam', 'project')
raw_scores = [85, 76, 92, 88]
weights = (0.1, 0.2, 0.4, 0.3)

# Irrelevant utility function (minor distraction)
def format_category_name(cat):
    return cat.title().replace('_', ' ')

# Compute final composite score
final_score = calculate_final_score(raw_scores, weights)

# Output result
print(f"Target result: {final_score}")