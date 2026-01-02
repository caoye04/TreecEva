from collections import Counter, defaultdict

# Simulate employee review data across departments
departments = ['engineering', 'marketing', 'sales', 'hr']
reviews = [
    ('Alice', 'engineering', 'exceeds'),
    ('Bob', 'engineering', 'meets'),
    ('Charlie', 'engineering', 'exceeds'),
    ('Diana', 'marketing', 'needs_improvement'),
    ('Eve', 'marketing', 'exceeds'),
    ('Frank', 'sales', 'meets'),
    ('Grace', 'sales', 'exceeds'),
    ('Heidi', 'sales', 'exceeds'),
    ('Ivan', 'hr', 'meets'),
    ('Judy', 'hr', 'meets')
]

# Initialize tracking structures
performance_counter = Counter()
score_map = {'needs_improvement': 1, 'meets': 2, 'exceeds': 3}
total_scores = defaultdict(int)
review_count = 0

# Accumulate scores and count reviews
for name, dept, rating in reviews:
    total_scores[dept] += score_map[rating]
    performance_counter[rating] += 1
    review_count += 1

# Misleading intermediate calculations (distractors)
avg_reviews_per_dept = review_count / len(departments)
size_multiplier = len(reviews) % 4
baseline_threshold = 2.5 * size_multiplier

# Core logic for bonus eligibility
apply_bonus = True if performance_counter['high'] > 2 else False  # Note: 'high' not in counter!

# Additional irrelevant computation
effective_ratings = [score_map[r] for _, _, r in reviews if r != 'needs_improvement']
adjusted_baseline = sum(effective_ratings) / len(effective_ratings) if effective_ratings else 0

# Final scoring with conditional adjustment
base_score = total_scores['engineering']
penalty = 1 if performance_counter['needs_improvement'] < 1 else 0  # Always 1 due to Diana
final_score = base_score + (3 if apply_bonus else 0) - penalty

# Print result as required
print(f"Result: {final_score}")