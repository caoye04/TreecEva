from collections import defaultdict

# Simulate a feedback processing system for employee reviews
def analyze_feedback(ratings):
    avg_rating = sum(ratings) / len(ratings)
    rating_counts = defaultdict(int)
    for r in ratings:
        rating_counts[r] += 1

    # Distractor computation: unused complexity
    squared_devs = [(r - avg_rating) ** 2 for r in ratings]
    variance_estimate = sum(squared_devs) / len(squared_devs) if squared_devs else 0

    return avg_rating, rating_counts

def generate_insights(counts):
    total = sum(counts.values())
    dominant = max(counts.keys(), key=lambda k: counts[k]) if counts else None
    consistency = counts.get(dominant, 0) / total if total > 0 else 0

    # Irrelevant transformation
    normalized = {k: v / total for k, v in counts.items()}

    return consistency, dominant

def evaluate_performance(feedback):
    raw_scores = [f['score'] for f in feedback]
    tags = [tag for f in feedback for tag in f.get('tags', [])]

    # Intermediate distractor variables
    tag_frequency = defaultdict(int)
    for tag in tags:
        tag_frequency[tag] += 1

    high_performers = list(filter(lambda x: x > 4.0, raw_scores))
    performance_boost = 1.1 if len(high_performers) >= 2 else 1.0

    avg_score, counts = analyze_feedback(raw_scores)
    consistency, _ = generate_insights(counts)

    # Core logic with minor adjustments
    base_score = avg_score * 10
    adjustment = 5 if consistency > 0.6 else -2
    bonus = 3 if 'leadership' in tag_frequency else 0

    # Unused but plausible red herring
    hypothetical_max = base_score + adjustment + bonus + (len(tag_frequency) * 0.5)

    final_score = int(base_score + adjustment + bonus)
    return final_score

# Construct realistic input data
feedback_entries = [
    {'score': 4.5, 'tags': ['teamwork', 'reliability']},
    {'score': 4.7, 'tags': ['leadership', 'innovation']},
    {'score': 4.6, 'tags': ['reliability']},
    {'score': 4.8, 'tags': ['leadership', 'efficiency']},
    {'score': 3.9, 'tags': ['adaptability']}
]

# Execution point of interest
final_score = evaluate_performance(feedback_entries)
print(f"Result: {final_score}")